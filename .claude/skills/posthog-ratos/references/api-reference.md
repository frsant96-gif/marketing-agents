# PostHog API — Referência rápida

## Autenticação

Personal API Key enviada como Bearer token:

```
Authorization: Bearer <POSTHOG_API_KEY>
```

Gerar em: **PostHog → configurações da conta (avatar) → Personal API Keys → Create personal API key**.
Escopos mínimos recomendados: `project:read`, `insight:read`, `feature_flag:read`, `experiment:read`, `session_recording:read`, `query:read`.

## Hosts

| Região | Host |
|---|---|
| EU Cloud | `https://eu.posthog.com` |
| US Cloud | `https://app.posthog.com` (ou `https://us.posthog.com`) |
| Self-hosted | URL própria da instância |

## Endpoints usados pela skill

| Endpoint | Uso |
|---|---|
| `GET /api/organizations/` | Lista organizações acessíveis |
| `GET /api/projects/` | Lista projetos acessíveis |
| `GET /api/projects/{id}/` | Detalhes de um projeto (nome, timezone) |
| `POST /api/projects/{id}/query/` com `kind: HogQLQuery` | Query SQL-like sobre a tabela `events` — base do `overview`, `top-events`, `trend`, `custom` |
| `POST /api/projects/{id}/query/` com `kind: FunnelsQuery` | Cálculo de funil ordenado entre eventos |
| `POST /api/projects/{id}/query/` com `kind: HeatmapQuery` | Dados de heatmap (clique, rage click, scroll depth) por URL |
| `GET /api/projects/{id}/insights/` | Lista insights salvos no projeto |
| `GET /api/projects/{id}/feature_flags/` | Lista feature flags e status de rollout |
| `GET /api/projects/{id}/experiments/` | Lista experimentos (A/B tests) |
| `GET /api/projects/{id}/session_recordings/` | Lista gravações de sessão com filtros de data |

## HogQL — exemplos úteis

```sql
-- Eventos e usuários únicos por dia
SELECT toDate(timestamp) AS dia, count() AS eventos, count(DISTINCT distinct_id) AS usuarios
FROM events
WHERE timestamp >= now() - INTERVAL 30 DAY
GROUP BY dia ORDER BY dia

-- Top eventos no período
SELECT event, count() AS total
FROM events
WHERE timestamp >= now() - INTERVAL 30 DAY
GROUP BY event ORDER BY total DESC LIMIT 20

-- Eventos de um usuário específico (por email em pessoa)
SELECT event, timestamp, properties
FROM events
WHERE person.properties.email = 'exemplo@dominio.com'
ORDER BY timestamp DESC LIMIT 50
```

## Rate limits

PostHog aplica rate limiting por API key (varia por endpoint, tipicamente ~240 req/min nos endpoints de leitura e mais restritivo em `/query/`). Em erro 429, aguardar 60s antes de tentar novamente — os scripts já tratam esse caso.

## Notas de versão

O `FunnelsQuery` e `HeatmapQuery` fazem parte da Query API unificada do PostHog. Se a PostHog alterar o schema dessas queries em versões futuras, o erro retornado pela API deixa claro qual campo está incorreto — ajustar o corpo da requisição em `scripts/reports.py` (`cmd_funnel`) ou `scripts/recordings.py` (`cmd_heatmap`) conforme a mensagem de erro.

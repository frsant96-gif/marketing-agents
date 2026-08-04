---
name: posthog-ratos
description: Consulta dados do PostHog via API oficial (REST + HogQL). Le eventos, tendencias, funis de conversao, feature flags, experimentos (A/B tests), session recordings e heatmaps. Use quando o usuario mencionar posthog, product analytics, eventos de produto, funil de conversao no produto, feature flag, rollout, experimento, ab test, session recording, gravacao de sessao, heatmap, rage click, HogQL. Tambem dispara com /posthog-ratos setup.
---

# PostHog Ratos

Skill completa para consulta de dados de product analytics do PostHog via API oficial (REST + Query API/HogQL). Cobre eventos, tendencias, funis de conversao, feature flags, experimentos (A/B tests), session recordings e heatmaps.

**IMPORTANTE: Esta skill e somente leitura. NUNCA cria, edita ou deleta feature flags, experimentos ou qualquer objeto no PostHog.**

**IMPORTANTE: NUNCA usar MCPs de PostHog. Esta skill usa SOMENTE os scripts Python locais.**

## Setup (primeira vez)

Quando o usuario pedir para configurar, rodar setup, ou for a primeira vez usando a skill, o Claude deve guiar o setup interativo:

### 1. Verificar dependencias

```bash
pip3 install requests pyyaml
```

### 2. Verificar .env

Checar se existe `~/.claude/skills/posthog-ratos/.env`. Se NAO existir, criar com o template:

```
# PostHog Ratos — Configuracao
# Os scripts leem este arquivo automaticamente. NAO precisa adicionar ao ~/.zshrc.

# OBRIGATORIO: Personal API Key do PostHog
# Gerar em: PostHog > avatar (canto inferior esquerdo) > Personal API Keys > Create personal API key
# Escopos minimos: project:read, insight:read, feature_flag:read, experiment:read, session_recording:read, query:read
POSTHOG_API_KEY=""

# Host do PostHog (default: eu.posthog.com)
POSTHOG_HOST="https://eu.posthog.com"

# Project ID padrao (opcional se todo comando usar --project com nome cadastrado em contas.yaml)
POSTHOG_PROJECT_ID=""
```

Perguntar ao usuario onde gerar a API Key se ele nao souber: **PostHog → clicar no avatar (canto inferior esquerdo) → Personal API Keys → Create personal API key**. Pedir pra colar a key e o host (confirmar se e EU ou US cloud) e preencher o `.env`.

### 3. Testar conexao

Rodar `read.py projects` pra confirmar que a API key funciona e listar os projetos acessiveis.

### 4. Cadastro de projetos (contas.yaml) — SETUP CONVERSACIONAL

Depois que a conexao funcionar, o Claude DEVE proativamente guiar o cadastro:

1. Mostrar a lista de projetos retornada por `read.py projects`
2. Perguntar: "Qual desses e o projeto principal? (ex: SolveWatch)"
3. Para cada projeto que o usuario quiser cadastrar, perguntar:
   - Nome do produto/cliente
   - project_id (da lista retornada)
4. Preencher o `contas.yaml` automaticamente com as respostas
5. Perguntar: "Quer cadastrar mais algum projeto?"

## Cadastro de projetos (contas.yaml)

**Arquivo:** `.claude/skills/posthog-ratos/contas.yaml`

Antes de executar qualquer operacao, o Claude DEVE ler este arquivo para resolver nomes de produtos/clientes para project IDs.
Quando o usuario disser "eventos do SolveWatch" ou "funil do SolveWatch", consultar o contas.yaml para obter o project_id.

Se o projeto nao estiver cadastrado, perguntar os dados e oferecer para adicionar ao arquivo.

## Como usar

Todos os scripts estao em `.claude/skills/posthog-ratos/scripts/`. O padrao e:

```
python3 <script>.py <subcomando> [argumentos]
```

O Claude deve interpretar o pedido do usuario e executar o script correto via Bash.

---

## Referencia rapida de operacoes

### Organizacoes e projetos (read.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `organizations` | Lista organizacoes acessiveis | `read.py organizations` |
| `projects` | Lista projetos acessiveis | `read.py projects` |
| `account` | Detalhes de um projeto | `read.py account --project SolveWatch` |

### Eventos, tendencias e funis (reports.py) — CORE DA SKILL

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `overview` | Eventos e usuarios unicos por dia | `reports.py overview --project SolveWatch --days 30` |
| `top-events` | Eventos mais frequentes no periodo | `reports.py top-events --project SolveWatch --days 30 --limit 20` |
| `trend` | Serie diaria de um evento especifico | `reports.py trend --project SolveWatch --event "purchase" --days 30` |
| `funnel` | Funil de conversao entre eventos, em ordem | `reports.py funnel --project SolveWatch --steps "pageview,signup,purchase" --days 30` |
| `insights` | Lista insights salvos no projeto | `reports.py insights --project SolveWatch` |
| `custom` | Query HogQL livre | `reports.py custom --project SolveWatch --query "SELECT event, count() FROM events GROUP BY event"` |

Parametros comuns:

| Parametro | O que faz | Exemplo |
|---|---|---|
| `--project` | Nome cadastrado em contas.yaml ou project_id direto | `SolveWatch` |
| `--days` | Janela de dias pra tras (default 30) | `7`, `30`, `90` |
| `--limit` | Limite de linhas | `20` |

### Feature flags e experimentos (flags.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `list` | Lista feature flags e status de rollout | `flags.py list --project SolveWatch --resumo` |
| `experiments` | Lista experimentos (A/B tests) | `flags.py experiments --project SolveWatch --resumo` |

### Session recordings e heatmaps (recordings.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `list` | Lista gravacoes de sessao no periodo | `recordings.py list --project SolveWatch --date-from 2026-07-01 --resumo` |
| `heatmap` | Dados de heatmap (clique, rage click, scroll) por URL | `recordings.py heatmap --project SolveWatch --url "https://solveplan.com.br/*" --tipo click` |

---

## Regras de seguranca

O Claude DEVE seguir estas regras ao executar operacoes:

1. **Somente leitura** — PostHog Ratos e uma skill de consulta, NUNCA cria, edita ou deleta nada no PostHog
2. **Nunca hardcodar API keys ou project IDs** — sempre usar env vars ou contas.yaml
3. **Respeitar rate limits** — se receber erro 429, aguardar 60 segundos antes de tentar novamente
4. **Nunca assumir origem de dados** — ao mostrar metricas, SEMPRE especificar o periodo e o projeto consultado
5. **NUNCA usar MCPs** — esta skill usa SOMENTE os scripts Python locais

## Fluxos comuns

### Visao geral do produto

1. `reports.py overview --project SolveWatch --days 30` — eventos e usuarios ativos
2. `reports.py top-events --project SolveWatch --days 30` — o que os usuarios mais fazem
3. `flags.py list --project SolveWatch --resumo` — quais features estao ativas

### Funil de conversao (ex: onboarding)

1. Perguntar ao usuario a sequencia de eventos que define o funil (ex: `signup`, `activation`, `first_use`)
2. `reports.py funnel --project SolveWatch --steps "signup,activation,first_use" --days 30`
3. Identificar a maior queda entre etapas e cruzar com `recordings.py list` do mesmo periodo pra entender o motivo

### Diagnostico de experimento (A/B test)

1. `flags.py experiments --project SolveWatch --resumo` — status e datas do experimento
2. `reports.py trend --project SolveWatch --event "<evento de conversao>" --days <duracao do teste>` — evolucao da metrica de conversao

### Investigar friccao numa pagina

1. `recordings.py heatmap --project SolveWatch --url "<url>" --tipo rageclick` — onde o usuario clica com frustracao
2. `recordings.py list --project SolveWatch --resumo --limit 10` — assistir gravacoes reais da mesma pagina/periodo

---

## Diagnostico com recomendacoes priorizadas

Quando o usuario pedir um "diagnostico", "analise com recomendacoes" ou "o que fazer com esses dados" (em vez de so puxar numeros crus), o Claude deve rodar o fluxo de leitura relevante e depois estruturar o output como uma tabela de recomendacoes — nao so listar metricas.

### Formato do output

1. **Resumo do periodo** — periodo consultado, projeto, e 2-3 linhas com o cenario geral (tendencia de alta/queda vs periodo anterior)
2. **Achados** — o que os dados mostram, com o numero que sustenta cada achado
3. **Recomendacoes priorizadas** — tabela:

| Prioridade | Achado | Recomendacao | Impacto esperado |
|---|---|---|---|
| Alta | [ex: queda de 60% entre "signup" e "activation" no funil] | [ex: revisar onboarding, simplificar primeiro passo] | [ex: aumentar taxa de ativacao] |
| Media | ... | ... | ... |
| Baixa | ... | ... | ... |

### Criterio de priorizacao

- **Alta** — etapa de funil com maior queda percentual E ligada a ativacao/conversao/receita
- **Media** — desvio relevante mas em evento secundario, ou afeta engajamento sem bloquear conversao
- **Baixa** — variacao dentro do esperado ou dado informativo sem acao clara associada

### Regra

Nunca recomendar sem citar o dado que sustenta — toda linha da tabela precisa apontar pra uma metrica especifica do relatorio rodado. Se o dado nao for suficiente pra afirmar causa, dizer isso explicitamente em vez de especular.

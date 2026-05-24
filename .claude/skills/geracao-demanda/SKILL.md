---
name: geracao-demanda
description: Perfilamento e enriquecimento de dados de empresas recebidas da SAP. Busca e prioriza contatos de TI e Finanças (gerentes, diretores e C-levels) a partir de uma lista de empresas em CSV/Excel. Calcula score de conta (pain + fit + expansion), classifica como HOT/WARM/COLD, filtra cargos por hierarquia P1–P8 e gera mensagem de outreach personalizada por IA. Use quando receber lista de empresas da SAP para prospecção, perfilamento de contas, enriquecimento de contatos ou preparação de listas de outreach.
---

# Geração de Demanda — Perfilamento e Enriquecimento de Contas SAP

## Objetivo
Transformar uma lista crua de empresas recebidas da SAP em uma lista qualificada com score de prioridade, os contatos certos (TI e Finanças) e mensagens de outreach prontas para uso.

---

## Passo 1 — Receber e entender a lista de entrada

Pedir ao usuário que cole ou faça upload do CSV/Excel com as empresas. Verificar quais colunas estão disponíveis:
- Nome da empresa
- CNPJ (se houver)
- Setor / segmento
- Tamanho (faturamento, nº de funcionários)
- Produto SAP em uso ou interesse
- Responsável comercial / SDR da Solveplan

Se faltar informação crítica (pelo menos nome + setor), perguntar antes de continuar.

---

## Passo 2 — Calcular score e classificar a conta (Account Scoring)

Para cada empresa, calcular um **score composto** com três dimensões inspiradas no modelo pain + fit + expansion:

### Dimensão 1 — Pain (0–4 pontos)
Sinais de que a empresa sente a dor que o SAP BDC resolve:

| Sinal | Pontos |
|-------|--------|
| Usa SAP ECC ou S/4HANA (dado direto da SAP) | +2 |
| Setor com demanda por consolidação/analytics: Manufatura, Agro, Varejo, Serviços Financeiros, Saúde, Logística | +1 |
| Empresa com multi-subsidiárias ou operações internacionais | +1 |

### Dimensão 2 — Fit (0–3 pontos)
Tamanho e maturidade da conta para receber BDC:

| Critério | Pontos |
|----------|--------|
| Faturamento acima de R$1B | +2 |
| Faturamento entre R$300M e R$1B | +1 |
| Mais de 500 funcionários | +1 |

### Dimensão 3 — Expansion (0–3 pontos)
Oportunidade de expansão / adoção de módulos adicionais:

| Sinal | Pontos |
|-------|--------|
| Não usa SAP Analytics Cloud (SAC) | +1 |
| Não usa SAP Datasphere | +1 |
| Usa Power BI ou Tableau (potencial migração) | +1 |

### Score final e classificação

```
SCORE = (pain × 3) + (fit × 2) + (expansion × 1)
```

| Score | Label | Significado |
|-------|-------|-------------|
| ≥ 15 | **HOT** 🔥 | Prioridade máxima — mobilizar SDR + AE imediatamente |
| 9–14 | **WARM** ⚡ | Boa oportunidade — incluir em campanha ABM |
| < 9 | **COLD** ❄️ | Baixo potencial imediato — nurturing de longo prazo |

Gerar colunas `SCORE_PAIN`, `SCORE_FIT`, `SCORE_EXPANSION`, `SCORE_TOTAL` e `LABEL` para cada empresa.

---

## Passo 3 — Buscar contatos por empresa

Para cada empresa (priorizar HOT primeiro), buscar contatos seguindo a hierarquia P1–P8 definida em `references/grupos-contato.md`.

**Regra de prioridade:**
- Sempre tentar P1 primeiro (CFO). Se não encontrar, descer para P2, P3...
- Meta: mínimo **2 contatos por empresa** — 1 do pilar Financeiro (P1–P5) + 1 do pilar TI/Sistemas (P3–P8)
- Nunca incluir contatos com termos ruins (ver `references/grupos-contato.md`)

**Fontes para busca (processo híbrido):**
1. **LinkedIn Sales Navigator** — buscar pelo nome da empresa + título do cargo. Filtrar por Brasil, cargo atual
2. **Apollo.io** — enriquecer com email profissional e telefone quando disponível
3. **Site da empresa** — aba "Sobre", "Equipe" ou "Liderança" para C-levels
4. **Google** — `"nome da empresa" + "CFO" OR "Diretor Financeiro" site:linkedin.com`

---

## Passo 4 — Validar e filtrar contatos

Para cada contato encontrado:

1. Verificar se o título está na lista de cargos prioritários (grupos P1–P8)
2. Verificar se NÃO contém nenhum termo da lista de termos ruins
3. Confirmar que o cargo é **atual** (não ex-, não antigo)
4. Classificar confiança do dado:

| Status | Critério |
|--------|----------|
| `verified` | Email profissional confirmado + cargo atual no LinkedIn |
| `partial` | Contato encontrado mas sem email ou cargo não confirmado |
| `low_confidence` | Cargo ambíguo, informação desatualizada ou fonte não confiável |

**Campos a coletar por contato:**
| Campo | Descrição |
|-------|-----------|
| `EMPRESA` | Nome da empresa |
| `LABEL_CONTA` | HOT / WARM / COLD |
| `SCORE_CONTA` | Score numérico da conta |
| `NOME_CONTATO` | Nome completo |
| `CARGO` | Título exato do LinkedIn/fonte |
| `AREA` | Financeiro / TI / Sistemas/ERP |
| `PRIORIDADE_CONTATO` | P1 a P8 conforme tabela |
| `EMAIL` | Email profissional (se disponível) |
| `LINKEDIN_URL` | URL do perfil |
| `FONTE` | LinkedIn / Apollo / Site / Google |
| `STATUS_CONTATO` | verified / partial / low_confidence |
| `OUTREACH` | Mensagem personalizada (ver Passo 5) |

---

## Passo 5 — Gerar mensagem de outreach personalizada por IA

Para cada conta HOT e WARM com ao menos 1 contato verified, gerar uma mensagem de primeiro contato personalizada.

**Lógica de personalização:**
- Se a empresa usa SAP ECC/S/4HANA → ângulo de modernização e BDC como evolução natural
- Se usa Power BI/Tableau → ângulo de consolidação e visão única vs. ferramentas fragmentadas
- Se é multi-subsidiária → ângulo de consolidação financeira intercompany
- Se setor é Manufatura/Agro → ângulo de planejamento de demanda e S&OP
- Se setor é Serviços Financeiros → ângulo de compliance e close financeiro

**Formato da mensagem (LinkedIn InMail ou email — máx 5 linhas):**
```
Linha 1: Gancho específico da empresa (sinal identificado)
Linha 2: Dor que o contato provavelmente sente no cargo dele
Linha 3: Como a Solveplan/SAP BDC resolve (sem jargão genérico)
Linha 4: Prova social rápida (ex: "já fizemos isso com [setor similar]")
Linha 5: CTA simples (15 min de conversa, não "demo" ou "apresentação")
```

Tom: direto, orientado a negócio, sem hype. Evitar: "transformação digital", "solução inovadora", "líder de mercado".

---

## Passo 6 — Montar o CSV de saída

Gerar um CSV com todas as colunas acima, ordenado por:
1. `LABEL_CONTA` (HOT → WARM → COLD)
2. `SCORE_CONTA` (maior primeiro dentro de cada grupo)
3. `PRIORIDADE_CONTATO` (P1 primeiro dentro de cada conta)

Salvar em `dados/enriquecimento/[nome-do-lote]-enriquecido-[data].csv`

---

## Passo 7 — Gerar resumo executivo

Entregar um resumo com:

**Funil de contas:**
- Total processado / HOT / WARM / COLD
- Top 5 contas por score (com motivo em 1 linha)

**Cobertura de contatos:**
- Total de contatos encontrados
- Breakdown por prioridade (P1–P8) e área (Financeiro / TI / Sistemas)
- % de contas com contato verified
- Empresas sem contato → lista para revisão manual

**Próximos passos:**
- HOT: acionar SDR + AE para sequência de outreach imediata
- WARM: incluir em campanha ABM ou nurturing LinkedIn
- COLD: manter em lista para requalificação em 90 dias

---

## Regras gerais

- Nunca incluir contatos com cargos operacionais, analistas, estagiários ou áreas não relacionadas
- Status `low_confidence` sempre sinaliza para revisão humana antes de contatar
- Não inventar emails — deixar em branco com `FONTE: pendente` se não encontrar
- Sempre registrar de onde veio cada informação na coluna `FONTE`
- Mensagem de outreach só para contas HOT e WARM com contato verified — não desperdiçar esforço em COLD sem email confirmado

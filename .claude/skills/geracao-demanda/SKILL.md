---
name: geracao-demanda
description: Perfilamento e enriquecimento de dados de empresas recebidas da SAP. Busca CNPJ via web e prioriza contatos de TI e Finanças via Apollo.io. Filtra cargos por hierarquia P1–P8 e gera mensagem de outreach personalizada por IA. Use quando receber lista de empresas da SAP para prospecção, perfilamento de contas, enriquecimento de contatos ou preparação de listas de outreach.
---

# Geração de Demanda — Perfilamento e Enriquecimento de Contas SAP

## Objetivo
Transformar uma lista crua de empresas recebidas da SAP em uma lista qualificada com CNPJ, os contatos certos (TI e Finanças) via Apollo.io e mensagens de outreach prontas para uso.

---

## Passo 1 — Receber e entender a lista de entrada

Pedir ao usuário que cole ou faça upload do CSV/Excel com as empresas. Verificar quais colunas estão disponíveis:
- Nome da empresa
- Razão social
- Estado / Município
- Segmento
- Porte
- Faturamento
- Website

Se faltar o nome da empresa, perguntar antes de continuar.

---

## Passo 2 — Buscar CNPJ por nome via web

Para cada empresa, buscar o CNPJ usando o script `scripts/buscar_cnpj.py` (roda localmente, gratuito).

**Fontes usadas pelo script (nesta ordem):**
1. `https://www.cnpj.biz/pesquisar.php?q=NOME` — busca por razão social
2. `https://brasilapi.com.br/api/cnpj/v1/{cnpj}` — validação e enriquecimento após encontrar o CNPJ

**Como rodar:**
```bash
python scripts/buscar_cnpj.py dados/Empresas_Kevin_Enriquecido_v2_2026-05-24.xlsx
```

O script adiciona a coluna `CNPJ` no Excel e salva uma nova versão com sufixo `_cnpj.xlsx`.

**Status possíveis na coluna CNPJ:**
| Status | Significado |
|--------|-------------|
| `00.000.000/0001-00` | CNPJ encontrado e válido |
| `pendente` | Não encontrado — revisar manualmente |
| `ambíguo` | Mais de um resultado — revisar manualmente |

---

## Passo 3 — Buscar contatos via Apollo.io

O Apollo.io está disponível em outra máquina com API key. Usar o script `scripts/apollo_enriquecimento.py`.

**Como rodar na máquina com API key:**
```bash
python scripts/apollo_enriquecimento.py dados/Empresas_Kevin_cnpj.xlsx
```

O script:
1. Lê a lista de empresas do Excel
2. Para cada empresa, busca na API do Apollo por domínio (website) ou nome
3. Filtra contatos seguindo a hierarquia P1–P8 (ver `references/grupos-contato.md`)
4. Descarta automaticamente contatos com termos ruins (analista, estagiário, SDR, etc.)
5. Meta: mínimo **2 contatos por empresa** — 1 do pilar Financeiro + 1 do pilar TI/Sistemas
6. Gera arquivo de saída com aba de contatos separada

**Campos retornados por contato:**
| Campo | Descrição |
|-------|-----------|
| `EMPRESA` | Nome da empresa |
| `CNPJ` | CNPJ da empresa |
| `NOME_CONTATO` | Nome completo |
| `CARGO` | Título exato do Apollo |
| `AREA` | Financeiro / TI / Sistemas/ERP |
| `PRIORIDADE_CONTATO` | P1 a P8 conforme tabela |
| `EMAIL` | Email profissional (se disponível) |
| `LINKEDIN_URL` | URL do perfil |
| `TELEFONE` | Telefone direto (se disponível) |
| `FONTE` | Apollo |
| `STATUS_CONTATO` | verified / partial / low_confidence |

---

## Passo 4 — Gerar mensagem de outreach personalizada por IA

Para cada empresa com ao menos 1 contato verified, gerar uma mensagem de primeiro contato personalizada.

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

## Passo 5 — Montar o Excel de saída

Gerar um Excel com duas abas:

**Aba 1 — Empresas:**
`EMPRESA | RAZAO SOCIAL | CNPJ | ESTADO | MUNICIPIO | SEGMENTO | PORTE | FATURAMENTO | WEBSITE`

**Aba 2 — Contatos:**
`EMPRESA | CNPJ | NOME_CONTATO | CARGO | AREA | PRIORIDADE_CONTATO | EMAIL | LINKEDIN_URL | TELEFONE | FONTE | STATUS_CONTATO | OUTREACH`

Salvar em `dados/enriquecimento/[nome-do-lote]-final-[data].xlsx`

---

## Passo 6 — Gerar resumo executivo

Entregar um resumo com:

**Cobertura:**
- Total de empresas processadas
- Empresas com CNPJ encontrado / pendente
- Total de contatos encontrados
- Breakdown por prioridade (P1–P8) e área (Financeiro / TI / Sistemas)
- % de contatos com email verified
- Empresas sem contato → lista para revisão manual

**Próximos passos:**
- Contatos verified com email → sequência de outreach imediata
- Contatos partial → validar manualmente antes de contatar
- Empresas sem contato → busca manual no LinkedIn Sales Navigator

---

## Regras gerais

- Nunca incluir contatos com cargos operacionais, analistas, estagiários ou áreas não relacionadas
- Status `low_confidence` sempre sinaliza para revisão humana antes de contatar
- Não inventar emails — deixar em branco com `FONTE: pendente` se não encontrar
- Sempre registrar de onde veio cada informação na coluna `FONTE`

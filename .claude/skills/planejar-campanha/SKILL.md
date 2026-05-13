---
name: planejar-campanha
description: Planeja campanhas de marketing completas — institucional, evento ou produto. Gera documento com objetivo, público, mensagem, canais, cronograma, budget e KPIs.
---

# /planejar-campanha

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md` e `_contexto/estrategia.md`.

## Passo 1 — Briefing rápido

Fazer as perguntas abaixo, uma por vez:

1. "Qual o nome da campanha?"
2. "Qual o tipo?" — opções: Institucional / Evento (presencial ou online) / Produto/solução
3. "Qual o objetivo principal?" — opções: Geração de leads / Geração de reuniões / Awareness de marca / Lançamento de solução / Ativação de base / Apoio a vendas
4. "Qual o produto ou tema central?" — se produto, qual solução SAP; se evento, qual o formato
5. "Qual o público-alvo?" — cargo, segmento, tipo de empresa
6. "Qual o período da campanha? (data de início e fim)"
7. "Qual o budget disponível?" — se não souber, responder "a definir"
8. "Qual o resultado esperado?" — ex: X leads, Y reuniões, Z de pipeline

Se o usuário já informou algum desses dados, não perguntar de novo.

## Passo 2 — Sugerir metas

Com base no tipo de campanha e resultado esperado, sugerir metas realistas:

| Indicador | Meta sugerida |
|-----------|---------------|
| Alcance (impressões) | [calcular com base no budget e canais] |
| Leads esperados | [meta] |
| Leads qualificados | [meta] |
| Reuniões | [meta] |
| Oportunidades abertas | [meta] |
| Pipeline gerado | [valor estimado] |

Confirmar com o usuário antes de prosseguir.

## Passo 3 — Gerar o plano

Ler o template em `.claude/skills/planejar-campanha/template.md` e substituir as variáveis `{{...}}` com as informações coletadas.

## Passo 4 — Salvar

Criar pasta `marketing/campanhas/[nome-da-campanha-em-slug]/` e salvar como `plano.md`.

Nomear com o nome da campanha em minúsculas, sem acentos, com hífens.

## Passo 5 — Confirmar e orientar

Informar onde foi salvo e quais seções ficaram em aberto, e perguntar:

> "Quer que eu ajude a detalhar alguma seção agora? Posso criar o calendário de conteúdo, o briefing de peças ou o roteiro de emails."

## Regras

- Adaptar o plano ao tipo de campanha: institucional é mais awareness, produto é mais conversão, evento tem pré/durante/pós
- Sempre conectar ao foco atual (SAP BDC) quando o tema permitir
- Para campanhas de produto, sugerir `material-campanha` para gerar as peças
- Para campanhas de evento, sugerir `planejar-evento` para o planejamento operacional
- Não gerar as peças criativas dentro dessa skill — isso é tarefa de `post-social`, `material-campanha` ou `artigo-blog`

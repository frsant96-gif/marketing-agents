---
name: planejar-evento
description: Planeja um evento do zero usando o framework de 26 passos. Faz o briefing, gera o documento completo e salva em eventos/[nome-do-evento]/plano.md
---

# /planejar-evento

## O que essa skill faz

Guia o planejamento completo de um evento usando o framework de 26 passos. A partir de um briefing rápido, gera o documento de planejamento preenchido e salva em `eventos/[nome-do-evento]/plano.md`.

## Antes de começar

Ler `_contexto/empresa.md` e `_contexto/preferencias.md` se existirem, pra calibrar o tom e o contexto.

## Passo 1 — Briefing rápido

Perguntar as informações essenciais, uma por vez:

1. "Qual o nome do evento ou ação?"
2. "Qual a data e o local (ou é online)?"
3. "Qual o objetivo principal?" — oferecer as opções: Geração de leads / Relacionamento / Fortalecimento de marca / Geração de reuniões / Apoio a vendas / Lançamento de solução
4. "Quem é o público-alvo? (cargo, segmento, tipo de empresa)"
5. "Qual solução ou produto é o foco?"
6. "Qual o orçamento disponível?"
7. "Qual resultado você espera? (ex: X leads, Y reuniões, Z de pipeline)"

Se o usuário já tiver passado essas informações antes de rodar a skill, não perguntar de novo — usar o que já foi dito.

## Passo 2 — Metas de sucesso

Com base no resultado esperado informado, sugerir metas realistas para:
- Nº de leads esperados
- Nº de leads qualificados
- Nº de reuniões
- Nº de oportunidades
- Valor de pipeline esperado

Confirmar com o usuário antes de prosseguir.

## Passo 3 — Gerar o documento

Ler o template em `.claude/skills/planejar-evento/template.md`.

Substituir todas as variáveis `{{...}}` com as informações coletadas:

| Variável | Valor |
|----------|-------|
| `{{NOME_EVENTO}}` | Nome do evento |
| `{{DATA}}` | Data informada |
| `{{LOCAL}}` | Local ou formato |
| `{{RESPONSAVEL}}` | Responsável principal |
| `{{OBJETIVO}}` | Objetivo escolhido |
| `{{PUBLICO}}` | Público-alvo |
| `{{SOLUCAO}}` | Solução foco |
| `{{ORCAMENTO}}` | Orçamento disponível |
| `{{RESULTADO_ESPERADO}}` | Resultado esperado |
| `{{META_LEADS}}` | Meta de leads |
| `{{META_LEADS_QUALIFICADOS}}` | Meta de leads qualificados |
| `{{META_REUNIOES}}` | Meta de reuniões |
| `{{META_OPORTUNIDADES}}` | Meta de oportunidades |
| `{{META_PIPELINE}}` | Valor de pipeline esperado |
| `{{PERFIL_CARGO}}` | Cargo/área do público |
| `{{SEGMENTO}}` | Segmento de mercado |
| `{{TIPO_EMPRESA}}` | Tipo de empresa |
| `{{CLIENTE_PROSPECT}}` | Cliente ou prospect |
| `{{DOR}}` | Dor principal a provocar |
| `{{FORMATO}}` | Formato do evento |
| `{{PIPELINE_CRM}}` | Pipeline no CRM |
| `{{SLA_CONTATO}}` | SLA de contato pós-evento |
| `{{NOTAS_TREINAMENTO}}` | Notas de treinamento (deixar em branco se não informado) |
| `{{DATA_CRIACAO}}` | Data de hoje |

Para variáveis não informadas no briefing, deixar em branco ou marcar como `A definir`.

## Passo 4 — Salvar o arquivo

Criar a pasta `eventos/[nome-do-evento]/` e salvar o documento como `plano.md`.

Nomear a pasta usando o nome do evento em minúsculas, sem acentos, com hífens no lugar de espaços.
Exemplo: "Summit Vendas 2025" → `eventos/summit-vendas-2025/plano.md`

## Passo 5 — Confirmar e orientar

Depois de salvar, informar:

> "Plano salvo em `eventos/[nome]/plano.md`.
>
> Os campos de orçamento, cronograma e responsáveis ainda estão em branco — você preenche à medida que for definindo. Quer que eu ajude com alguma seção agora?"

## Regras

- Não gerar conteúdo criativo por conta própria (ex: copys de convite, posts) — isso é tarefa de outras skills
- Se o usuário perguntar sobre comunicação do evento, sugerir `/roteiro-post` ou `/email-profissional`
- Se o usuário quiser publicar a landing page, sugerir `/publicar-site`
- Uma pergunta por vez durante o briefing
- Se o usuário já informou os dados antes de rodar a skill, pular direto pro Passo 3

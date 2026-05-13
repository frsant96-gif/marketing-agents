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

## Passo 3 — Validação crítica das suposições

Antes de gerar o plano, desafiar as suposições centrais da campanha com 3-5 perguntas diretas:

> "Antes de montar o plano, deixa eu testar algumas suposições pra garantir que a campanha está bem fundamentada."

Perguntar, uma por vez, só as mais relevantes ao contexto:

**Sobre o público:**
- "Por que esse público específico vai se importar com esse tema agora? O que está acontecendo no mercado deles que cria urgência?"
- "Esse público já conhece a Solveplan ou vai ser o primeiro contato? A campanha está calibrada pra esse nível de awareness?"

**Sobre o canal:**
- "Por que esses canais e não outros? Tem dado anterior que mostra que esse público converte nesses canais?"
- "Se o canal principal não performar, qual é o plano B?"

**Sobre a mensagem:**
- "Qual é a suposição central da mensagem? O público realmente tem essa dor ou estamos supondo?"
- "O que diferencia essa campanha de tudo que a Solveplan já fez antes? Por que alguém vai parar pra prestar atenção?"

**Sobre o resultado esperado:**
- "Com base em campanhas anteriores, essa meta de leads/reuniões é realista pro budget disponível?"
- "Se a campanha atingir a meta de leads mas não de reuniões, o que vai estar errado?"

Registrar as respostas e ajustar o briefing se necessário antes de gerar o plano.

*Se o usuário não quiser passar pela validação, pular e ir direto pro Passo 4.*

## Passo 4 — Gerar o plano

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

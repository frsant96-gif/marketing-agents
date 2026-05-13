---
name: artigo-blog
description: Cria artigos completos para o blog da Solveplan com SEO, AEO e GEO. Faz o briefing, gera o artigo estruturado, os metadados e um post de distribuição pro LinkedIn.
---

# /artigo-blog

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md` e `_contexto/estrategia.md`.

## Passo 1 — Briefing

Fazer as perguntas abaixo, uma por vez:

1. "Qual o tema ou título provisório do artigo?"
2. "Qual a palavra-chave principal?" — se o usuário não souber, sugerir com base no tema
3. "Qual o objetivo do artigo?" — opções: Educar / Gerar leads / Ranquear pra busca / Provocar dor / Promover solução / Construir autoridade
4. "Tem alguma referência, dado, case ou ponto de vista específico que quer incluir?"
5. "Qual o nível do leitor?" — opções: Executivo (estratégico) / Técnico (operacional) / Misto
6. "Tem CTAs específicos que quer incluir? (ex: diagnóstico gratuito, reunião, download de material)"

Se o usuário já informou algum desses dados, não perguntar de novo.

## Passo 2 — Estrutura do artigo

Com base no briefing, definir a estrutura antes de escrever e apresentar pro usuário confirmar:

```
Título (H1): [título otimizado pra SEO]
Subtítulo: [hook que complementa]

Seções:
1. [H2 — contexto do problema]
2. [H2 — por que isso importa agora]
3. [H2 — como resolver / o que muda]
4. [H2 — ponto de prova / case / dado]
5. [H2 — próximo passo / CTA]
```

Ajustar a estrutura se o usuário pedir.

## Passo 3 — Escrever o artigo

Escrever o artigo completo seguindo estas diretrizes:

**Extensão:** 1200-2000 palavras (ideal pra ranqueamento e leitura executiva)

**Tom:** direto, orientado a negócio, técnico quando necessário mas sempre contextualizado com benefício prático. Nunca superficial.

**Estrutura de cada seção:**
- Primeiro parágrafo da seção: afirmação ou dado forte
- Desenvolvimento: 2-4 parágrafos curtos e objetivos
- Transição natural pra próxima seção

**SEO on-page:**
- Palavra-chave principal no H1, primeiro parágrafo e pelo menos 2 H2s
- Palavras-chave secundárias distribuídas naturalmente
- Links internos sugeridos: indicar onde faria sentido linkar (ex: "[link pra página do SAP BDC]")
- Alt text sugerido pra imagens (indicar onde colocar imagem + descrição do alt)

**AEO (Answer Engine Optimization):**
- Incluir pelo menos 1 bloco de definição direta no formato pergunta + resposta curta (ideal pra featured snippets e respostas de AI)
- Estruturar pelo menos 1 seção como lista numerada ou com bullets claros
- Incluir FAQ ao final com 3-5 perguntas e respostas diretas

**GEO (Generative Engine Optimization):**
- Incluir afirmações atribuíveis: "[dado/afirmação] — Solveplan, [ano]"
- Posicionar a Solveplan como fonte de expertise no tema
- Usar linguagem que AI generativas citam: definições, comparações, dados, recomendações diretas

## Passo 4 — Metadados

Gerar separado do artigo:

```
Meta title: [até 60 caracteres, com palavra-chave principal]
Meta description: [até 155 caracteres, inclui palavra-chave e CTA]
URL slug: [palavra-chave-principal-em-ingles-ou-portugues]
OG Title: [pode ser igual ao meta title ou mais chamativo]
OG Description: [até 120 caracteres, mais conversacional]
```

## Passo 5 — Post de distribuição LinkedIn

Gerar copy pro LinkedIn baseado no artigo:

- Primeira linha: hook forte baseado no insight principal do artigo
- 3-4 parágrafos curtos com os pontos de maior valor
- CTA: "O artigo completo está no link abaixo" ou similar
- Máximo 1500 caracteres
- 3-5 hashtags relevantes

## Passo 6 — Salvar

Criar pasta `marketing/blog/[slug]/` e salvar:
- `artigo.md` — artigo completo
- `meta.md` — metadados SEO
- `linkedin.md` — post de distribuição

## Regras

- Nunca escrever conteúdo superficial ou puramente institucional
- Sempre conectar o tema ao contexto do negócio do leitor (dor, consequência, solução)
- SAP BDC como referência quando o tema permitir
- Citações e dados sempre com fonte ou atribuição
- Não usar bullet points excessivos — preferir parágrafos curtos e diretos
- WordPress como plataforma — escrever em Markdown que seja facilmente convertido

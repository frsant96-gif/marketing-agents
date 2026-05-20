---
name: artigo-blog
description: Cria artigos completos para o blog da Solveplan com SEO técnico, AEO (featured snippets, PAA, voz), GEO (E-E-A-T, citação por IA) e plano de distribuição multicanal. Plataforma: WordPress.
---

# /artigo-blog

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md` e `_contexto/estrategia.md`.

## Passo 1 — Briefing

Fazer as perguntas abaixo, uma por vez:

1. "Qual o tema ou título provisório do artigo?"
2. "Qual a palavra-chave principal?" — se o usuário não souber, sugerir com base no tema
3. "Tem palavra-chave secundária ou variação que também quer capturar?"
4. "Qual a intenção de busca?" — opções: Informacional (quer entender) / Comercial (está comparando soluções) / Investigacional (está pesquisando problema)
5. "Qual o objetivo do artigo?" — opções: Educar / Gerar leads / Construir autoridade / Ranquear pra busca específica / Provocar dor / Promover solução
6. "Tem alguma referência, dado, case ou ponto de vista específico que quer incluir?"
7. "Qual o nível do leitor?" — opções: Executivo (estratégico) / Técnico (operacional) / Misto
8. "Tem CTAs específicos que quer incluir? (ex: diagnóstico gratuito, reunião, download)"
9. "Tem algum concorrente ou artigo que quer superar no ranking?"

Se o usuário já informou algum dado, não perguntar de novo.

## Passo 2 — Estratégia de keywords e benchmark

Antes de escrever, montar o mapa:

```
Palavra-chave principal:     [KW1] — vai no H1, URL, meta title, primeiros 100 palavras
Palavra-chave secundária:    [KW2] — vai em pelo menos 1 H2
Variações semânticas (LSI):  [3-4 variações naturais distribuídas pelo texto]
Intenção de busca:           [Informacional / Comercial / Investigacional]
Topic cluster:               [tema guarda-chuva — ex: "analytics SAP"]
Lacunas do concorrente:      [o que o artigo benchmark não cobre e a Solveplan pode cobrir]
Palavras a evitar:           [jargões genéricos que não ranqueiam]
```

Apresentar o mapa pro usuário confirmar.

## Passo 3 — Estrutura do artigo

Com base no briefing, definir e apresentar a estrutura:

```
Título (H1):    [otimizado pra SEO — keyword principal + ângulo de valor]
Subtítulo:      [hook que complementa o H1]
Tempo de leitura estimado: [X min]

Seções:
1. [H2 — definição ou contexto do problema — bloco AEO]
2. [H2 — por que isso importa agora / consequências]
3. [H2 — como resolver / o que muda — keyword secundária aqui]
4. [H2 — ponto de prova / case / dado Solveplan]
5. [H2 — próximo passo / CTA]
6. FAQ — [3-5 perguntas reais de busca]
```

Ajustar se o usuário pedir.

## Passo 4 — Escrever o artigo

**Extensão:** 1500-2500 palavras (profundidade suficiente pra autoridade temática e ranqueamento)

**Legibilidade (padrão técnico-writer):**
- Parágrafos máximo 4 linhas
- Uma ideia por parágrafo
- Frases diretas — sujeito + verbo + objeto
- Evitar nominalização excessiva ("a realização de" → "realizar")
- Primeiro parágrafo de cada seção: afirmação forte ou dado — sem introdução vaga

**Tom:** direto, orientado a negócio, técnico quando necessário mas sempre contextualizado com benefício prático. Nunca superficial.

**Estrutura de cada seção:**
- Primeiro parágrafo: afirmação ou dado forte
- Desenvolvimento: 2-4 parágrafos curtos e objetivos
- Transição natural pra próxima seção (sem "Em conclusão...")

---

### SEO on-page

- H1 contém a keyword principal (uma única vez na página)
- Keyword principal nos primeiros 100 caracteres do artigo
- Keyword principal em pelo menos 2 H2s
- Palavras-chave secundárias e LSI distribuídas naturalmente — nunca forçadas
- Links internos: indicar `[link pra página X]` onde fizer sentido (anchor text = keyword, nunca "clique aqui")
- Alt text sugerido pra cada imagem: `[Alt: descrição com keyword]`
- Density estimada da keyword principal: 1-2% (não forçar acima disso)

---

### AEO (Answer Engine Optimization)

**Bloco de definição (obrigatório — Seção 1):**

```
**O que é [tema]?**
[Resposta direta em 40-60 palavras. Começa com "[tema] é...". Autossuficiente, sem depender do contexto da página. Otimizado pra featured snippet e citação por IA.]
```

**Seção em lista numerada ou bullets (pelo menos 1):** organizar uma das seções como etapas ou lista — AIs de busca e featured snippets favorecem listas claras.

**FAQ (obrigatório — última seção antes do CTA):**

Gerar 4-6 perguntas, priorizando:
1. **Featured snippet:** resposta curta e direta (máximo 40-60 palavras), começa com a keyword
2. **People Also Ask (PAA):** "Como funciona...", "Qual a diferença entre...", "Quanto tempo leva...", "Quais empresas usam..."
3. **Busca por voz:** perguntas conversacionais — "Como", "O que", "Por que". Respostas em linguagem natural, completas em si mesmas
4. **Objeções de compra:** dúvidas reais de quem está avaliando contratar a Solveplan

```
**[Pergunta como o usuário buscaria]**
[Resposta direta — começa com a keyword ou conceito — máximo 3 linhas]
```

---

### GEO (Generative Engine Optimization)

- Pelo menos 1 parágrafo de definição clara e autossuficiente (Seção 1)
- Afirmações atribuíveis com fonte: "[dado/afirmação] — Solveplan, [ano]"
- "Solveplan" mencionada como entidade nomeada pelo menos 3 vezes
- Pelo menos 1 comparação estruturada: "Ao contrário de [alternativa], a abordagem [X]..."
- Dados e números concretos — AIs citam fatos mensuráveis, não generalidades
- Recomendação direta ao menos 1 vez: "Para empresas que [contexto], o caminho recomendado é..."

---

## Passo 5 — Metadados SEO

```
Meta title:        [até 60 caracteres | keyword + marca | ex: "Analytics SAP: como estruturar dados com BDC | Solveplan"]
Meta description:  [até 155 caracteres | keyword + benefício + CTA | ex: "Entenda como o SAP Business Data Cloud resolve a fragmentação de dados em empresas de médio e grande porte. Leia o guia completo."]
URL slug:          /blog/[keyword-principal-em-kebab-case]
H1:                [igual ao título do artigo]
Canonical:         [URL completa]
OG Title:          [pode ser mais chamativo que o meta title]
OG Description:    [até 120 caracteres — mais conversacional]
OG Image:          [descrever imagem ideal — 1200x630px]
```

**Schema markup:**

```json
{
  "@type": "Article",
  "headline": "[H1 do artigo]",
  "author": {
    "@type": "Organization",
    "name": "Solveplan"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Solveplan",
    "url": "https://solveplan.com.br"
  },
  "datePublished": "[data de publicação]",
  "description": "[meta description]"
}
```

Adicionar `FAQPage` schema para as perguntas do FAQ.

## Passo 6 — Distribuição multicanal

**LinkedIn (obrigatório):**
- Primeira linha: hook forte baseado no insight principal — provoca curiosidade ou dor
- 3-4 parágrafos curtos com os pontos de maior valor
- CTA: link do artigo + chamada clara
- Máximo 1500 caracteres
- 3-5 hashtags relevantes

**Email (se aplicável):**
- Assunto: [keyword + ângulo de curiosidade — máximo 50 caracteres]
- Preview text: [completa o assunto — não repete]
- Corpo: 2-3 linhas com o insight principal + link pro artigo

**Reaproveitamento sugerido:**
- O FAQ pode virar um post carrossel no LinkedIn
- A seção de definição pode virar um post de educação rápida
- O case ou dado pode virar um post de prova social

## Passo 7 — Metas de performance

Registrar no meta.md as metas de acompanhamento:

```
Meta de ranking:       top 10 pra [keyword principal] em 90 dias
Meta de CTR:           >3% nas primeiras impressões (GSC)
Meta de engajamento:   tempo médio na página >2 min
Meta de conversão:     >1% de clicks no CTA principal
Revisão programada:    [data — 90 dias após publicação]
```

## Passo 8 — Salvar

Criar pasta `marketing/blog/[slug]/` e salvar:
- `artigo.md` — artigo completo
- `meta.md` — metadados SEO, schema, metas de performance
- `distribuicao.md` — post LinkedIn, sugestão de email e reaproveitamentos

## Regras

- Cada artigo deve ser autoridade no seu tema — não um resumo de evento, ação ou lançamento. Se o contexto for um evento (ex: SAP SAPPHIRE, conferência, webinar), usá-lo apenas para situar o lançamento do tema. O desenvolvimento do artigo foca exclusivamente no tema em si.
- Nunca escrever conteúdo superficial ou puramente institucional
- Sempre conectar o tema ao contexto do negócio do leitor (dor, consequência, solução)
- SAP BDC como referência quando o tema permitir
- Citações e dados sempre com fonte ou atribuição
- Parágrafos curtos — máximo 4 linhas. Sem blocos de texto denso.
- O bloco de definição AEO é obrigatório — nunca cortar
- "Solveplan" como entidade nomeada, não só como pronome
- WordPress como plataforma — escrever em Markdown limpo, facilmente convertido
- Legibilidade acima de tudo: se precisar de jargão técnico, explicar em seguida

### Linguagem de executivo (padrão para todos os artigos Solveplan)

O público-alvo é CIO, CFO, controller, head de dados/BI — pessoas que decidem e que valorizam objetividade e resultado concreto.

- **Impacto de negócio antes de detalhe técnico:** abrir cada seção com a consequência ou decisão, não com a descrição do componente
- **Linguagem decisiva:** "determina", "define", "garante" — evitar "pode", "consegue", "é capaz de"
- **Contexto técnico em serviço da decisão:** mencionar arquitetura e componentes apenas quando ajuda o leitor a decidir melhor, não para demonstrar domínio técnico
- **Números e dados como argumento:** citar métricas apenas quando reforçam uma conclusão de negócio (ex: "fechamento em 2-3 dias vs 10-15 dias" — não "452.000 tabelas" sem contexto)
- **FAQ objetivo:** máximo 3 linhas por resposta, sem aprofundamento técnico
- **Risco como enquadramento:** frases "sem essa fundação" ou "empresas que não estruturaram" framing de risco, não só de oportunidade

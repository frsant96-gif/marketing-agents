---
name: pagina-solucao
description: Cria o copy completo de páginas de solução para o site da Solveplan. Estruturado por seção com SEO técnico, AEO (featured snippets, PAA, voz) e GEO (E-E-A-T, citações por IA generativa). Plataforma: WordPress.
---

# /pagina-solucao

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md` e `_contexto/estrategia.md`.

## Passo 1 — Briefing

Fazer as perguntas abaixo, uma por vez:

1. "Qual a solução ou serviço da página?" — ex: SAP BDC, SAP Analytics Cloud, FP&A, Consolidação, AMS
2. "Qual a palavra-chave principal que quer ranquear?" — ex: "SAP Business Data Cloud"
3. "Tem alguma palavra-chave secundária ou variação que também quer capturar?" — ex: "plataforma de dados SAP", "SAP BDC Brasil"
4. "Qual a intenção de busca de quem vai chegar nessa página?" — opções: Informacional (quer entender) / Comercial (está comparando) / Transacional (quer contratar)
5. "Qual a dor principal do público que essa solução resolve?"
6. "Tem algum case ou resultado concreto que pode incluir como prova?"
7. "Qual o CTA principal?" — opções: Agendar diagnóstico / Falar com especialista / Baixar material / Ver case
8. "Tem alguma página concorrente ou referência que quer superar ou se basear?"

Se o usuário já informou algum dado antes de rodar a skill, não perguntar de novo.

## Passo 2 — Pesquisa online e análise de concorrentes

Pesquisar online antes de escrever (usar Agent tool ou WebSearch/WebFetch) — nunca montar a análise de benchmark só com conhecimento prévio do modelo. Delegar a um agent (subagent_type general-purpose) quando envolver múltiplos concorrentes ou pesquisa ampla, pedindo um relatório estruturado com fontes citadas.

Se o usuário informou uma página concorrente no briefing (pergunta 8), pesquisar essa página (WebFetch) e analisar:

```
Concorrente analisado:    [URL]
Keywords que ele usa:     [listar KWs identificadas no título, H1, H2s]
Estrutura da página:      [seções que ele tem]
Lacunas (o que ele não cobre): [tópicos, ângulos, provas que faltam]
Ângulo diferenciador:     [o que a Solveplan pode fazer melhor ou diferente]
```

Se o usuário não informou concorrente, pesquisar quem rankeia hoje pra keyword principal (WebSearch) e quais documentações/fontes técnicas oficiais existem sobre o tema, e gerar a mesma análise com base no que foi encontrado de fato — nunca com tópicos genéricos inventados.

## Passo 3 — Definir estratégia de keywords

Antes de escrever qualquer seção, montar o mapa de keywords da página:

```
Palavra-chave principal:     [KW1] — vai no H1, URL, meta title, primeiros 100 palavras
Palavra-chave secundária:    [KW2] — vai em pelo menos 1 H2 e no corpo da seção de solução
Variações semânticas (LSI):  [3-4 variações naturais — distribuídas pelo texto]
Intenção de busca:           [Informacional / Comercial / Transacional]
Topic cluster:               [tema guarda-chuva — ex: "analytics SAP"]
Palavras a evitar:           [jargões genéricos que não ranqueiam — ex: "transformação digital"]
```

Apresentar o mapa pro usuário confirmar antes de continuar.

## Passo 4 — Confirmar estrutura

> "Vou estruturar a página assim:
>
> 1. Hero — H1 + subheadline + CTA principal
> 2. Definição clara — parágrafo de definição otimizado pra AEO e GEO
> 3. Dor — o problema que o público enfrenta hoje
> 4. Solução — o que é e como funciona
> 5. Benefícios — o que muda pra quem contrata
> 6. Diferenciais — por que a Solveplan
> 7. Cases / prova — resultado real
> 8. CTA final — chamada pra ação
> 9. FAQ — perguntas reais (AEO / featured snippets)
>
> Bora com essa estrutura?"

Ajustar se o usuário pedir.

## Passo 5 — Escrever a página

Escrever cada seção separada com marcação clara.

---

### Seção 1: Hero

**H1:** [frase com palavra-chave principal — máximo 8 palavras — captura a promessa ou o problema]

*Regra SEO: H1 deve conter a keyword principal exata ou variação próxima. Aparece uma única vez na página.*

**Subheadline:** [expande o H1 com benefício concreto e palavra-chave secundária — 1-2 linhas]

**CTA principal:** [texto do botão — verbo de ação + proposta de valor — ex: "Agendar diagnóstico gratuito"]

**Micro-copy de suporte:** [reduz fricção — ex: "Sem compromisso. Especialistas SAP Gold Partner."]

**Alt text da imagem hero:** [descrever a imagem + incluir keyword — ex: "Consultores Solveplan implementando SAP Business Data Cloud em empresa de manufatura"]

---

### Seção 2: Definição clara *(bloco AEO + GEO — não cortar nem encurtar)*

**H2:** O que é [nome da solução]?

**Parágrafo de definição (40-60 palavras):** [Definição direta, completa e autossuficiente. Começa com "[Nome da solução] é..." — otimizado pra featured snippet e citação por IA generativa. Inclui: o que é, para quem, qual problema resolve e qual resultado entrega.]

*Este parágrafo é o mais importante pra AEO e GEO: responde a pergunta completa nas primeiras linhas, sem depender do contexto da página.*

**Contexto adicional (1 parágrafo):** [Expande com cenário de mercado, evolução tecnológica ou posicionamento — ajuda na autoridade temática]

**Comparação estruturada (1 frase):** ["Ao contrário de [alternativa comum], [nome da solução] [diferencial central]."]

---

### Seção 3: Dor

**H2:** [problema do mercado — pode usar keyword secundária]

**Corpo:** [2-3 parágrafos descrevendo a situação atual do público, as consequências de não resolver, a urgência. Usar dados ou afirmações validáveis.]

**H3 (opcional):** [subproblema específico — oportunidade pra keyword LSI]

**Dado ou micro-copy de prova:** [estatística, dado de mercado ou afirmação que valida o problema]

---

### Seção 4: Solução

**H2:** [Como a Solveplan resolve + keyword secundária ou LSI]

**Corpo:** [Explicação clara do que é, como funciona e qual o mecanismo de transformação — sem jargão desnecessário. Incluir keyword principal e secundária de forma natural.]

**Como funciona — etapas (H3s):**

```
H3: [Etapa 1]
[1-2 linhas descrevendo a etapa]

H3: [Etapa 2]
[1-2 linhas descrevendo a etapa]

H3: [Etapa 3]
[1-2 linhas descrevendo a etapa]
```

*Cada H3 é oportunidade pra keyword LSI diferente.*

---

### Seção 5: Benefícios

**H2:** [foco em resultado, não em feature — ex: "O que muda pra sua operação"]

**Lista de benefícios (4-6 itens):**

```
**[Título do benefício — bold]:** [Descrição com resultado concreto — 1-2 linhas]
```

*Títulos dos benefícios em bold funcionam como âncoras de leitura rápida e são captados por AIs de busca como bullets estruturados.*

---

### Seção 6: Diferenciais Solveplan

**H2:** [por que a Solveplan — pode ser: "Por que a Solveplan para [solução]?"]

**Corpo:** [2-3 parágrafos ou lista destacando: expertise técnica, metodologia, resultados, Gold Partner SAP. Mencionar "Solveplan" como entidade nomeada pelo menos 2 vezes nessa seção.]

**Números de autoridade (E-E-A-T):**
- +90 clientes atendidos
- +200 soluções entregues
- +280.000 horas de projetos SAP
- Parceira SAP Gold na América Latina

*Números de prova são sinais de E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) — fundamentais pra GEO.*

---

### Seção 7: Cases / Prova

**H2:** [resultados reais — ex: "Empresas que já transformaram sua operação com a Solveplan"]

**Case 1:**
```
Segmento/porte: [ex: Indústria química, grande porte]
Desafio: [1 linha]
O que foi feito: [1-2 linhas]
Resultado: [dado concreto de impacto]
```

*(Se o nome do cliente for confidencial, usar segmento + porte)*

**Depoimento (se aplicável):**
> "[citação direta, entre aspas]" — [Nome], [Cargo], [Empresa]

*Depoimentos são sinais de E-E-A-T e aumentam credibilidade pra GEO.*

---

### Seção 8: CTA Final

**H2:** [urgência ou proposta de valor — ex: "Comece com um diagnóstico gratuito"]

**Corpo:** [1-2 linhas reforçando o benefício de dar o próximo passo — não repetir o que já foi dito antes]

**CTA:** [texto do botão]

**Micro-copy de redução de fricção:** [ex: "Sem compromisso. Resposta em até 24h."]

---

### Seção 9: FAQ

**H2:** Perguntas frequentes sobre [nome da solução]

Gerar 5-7 perguntas, priorizando:

1. **Featured snippet:** pergunta com resposta curta e direta (máximo 40-60 palavras). Resposta começa com a keyword. Ex: "O que é SAP Business Data Cloud? O SAP Business Data Cloud (BDC) é..."
2. **People Also Ask (PAA):** perguntas que aparecem no Google pra esse tema — formatos: "Como funciona...", "Qual a diferença entre...", "Quanto custa...", "Quais empresas usam..."
3. **Busca por voz:** perguntas conversacionais — começam com "Como", "O que", "Por que", "Quando". Respostas em linguagem natural, completas em si mesmas.
4. **Objeções comerciais:** perguntas que refletem dúvidas reais de quem está avaliando contratar — ex: "Quanto tempo leva uma implantação?", "Preciso migrar tudo de uma vez?"

**Formato de cada FAQ:**

```
**[Pergunta exatamente como o usuário buscaria]**
[Resposta direta — começa com a keyword ou conceito central — máximo 3 linhas]
```

*Não usar perguntas genéricas ou óbvias demais. Cada pergunta deve ter potencial real de ranqueamento ou de reduzir objeção de compra.*

---

## Passo 6 — Metadados SEO

```
Meta title:        [até 60 caracteres | keyword principal + marca | ex: "SAP Business Data Cloud | Solveplan"]
Meta description:  [até 155 caracteres | keyword + benefício + CTA | ex: "Implante SAP BDC com especialistas Gold Partner. Dados integrados, analytics em tempo real. Agende um diagnóstico gratuito."]
URL slug:          /solucoes/[keyword-principal-em-kebab-case]
H1:                [igual ao hero headline]
Canonical:         [URL completa da página]
```

**Schema markup recomendado:**

```json
{
  "@type": "Service",
  "name": "[nome da solução]",
  "description": "[parágrafo de definição da Seção 2]",
  "provider": {
    "@type": "Organization",
    "name": "Solveplan",
    "url": "https://solveplan.com.br"
  },
  "areaServed": "América Latina",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "[nome da solução]"
  }
}
```

Adicionar também `FAQPage` schema para as perguntas da Seção 9:

```json
{
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[pergunta 1]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[resposta 1]"
      }
    }
  ]
}
```

**Open Graph:**
```
OG Title:       [título pra compartilhamento — pode ser mais chamativo que o meta title]
OG Description: [versão mais comercial da meta description]
OG Image:       [descrever imagem ideal — 1200x630px — com texto da proposta de valor]
```

**Links internos sugeridos:**

Indicar 2-3 páginas do site da Solveplan que fazem sentido linkar nessa página (ex: página de outro serviço relacionado, blog post de caso de uso, página de contato). Usar anchor text com keyword, não "clique aqui".

---

## Passo 7 — Checklist GEO (Generative Engine Optimization)

Verificar antes de salvar:

- [ ] Parágrafo de definição (Seção 2) responde a pergunta completa em menos de 60 palavras, sem depender de contexto externo
- [ ] "Solveplan" aparece como entidade nomeada pelo menos 3 vezes no texto total
- [ ] Existe pelo menos 1 comparação estruturada ("Ao contrário de X, a abordagem Y...")
- [ ] Números de autoridade presentes (clientes, soluções, horas, Gold Partner)
- [ ] Depoimento ou case com resultado mensurável
- [ ] FAQ cobre perguntas reais de busca, não perguntas genéricas
- [ ] Nenhuma seção depende de outra pra fazer sentido isolada (AIs de busca citam trechos, não páginas inteiras)

---

## Passo 8 — Checklist técnico WordPress

Antes de salvar, gerar checklist de verificação técnica pra quando a página for publicada:

**Performance (Core Web Vitals):**
- [ ] Imagens em formato WebP ou AVIF
- [ ] Imagens com dimensões definidas (width + height no HTML) pra evitar layout shift (CLS)
- [ ] Imagem hero com `loading="eager"`, demais imagens com `loading="lazy"`
- [ ] Plugin de cache ativo (ex: WP Rocket, W3 Total Cache)
- [ ] Nenhum script de terceiro bloqueando o render (verificar via PageSpeed Insights)

**Mobile-first:**
- [ ] Página testada em viewport mobile (375px)
- [ ] Botões de CTA com tamanho mínimo de 44px altura pra toque
- [ ] Textos legíveis sem zoom (mínimo 16px)
- [ ] Nenhum elemento com overflow horizontal

**SEO técnico WordPress:**
- [ ] Yoast SEO ou Rank Math configurado com meta title e meta description da skill
- [ ] URL slug definido conforme indicado nos metadados
- [ ] Imagem OG adicionada (1200x630px)
- [ ] Schema markup inserido via plugin ou bloco de código no rodapé
- [ ] Canonical URL configurada pra evitar duplicidade
- [ ] Página incluída no sitemap XML
- [ ] Sem erros de crawl (verificar no Google Search Console após publicação)

**Acessibilidade:**
- [ ] Alt text em todas as imagens
- [ ] Hierarquia de headings correta (um H1, H2s para seções, H3s para subseções)
- [ ] Links com texto descritivo (sem "clique aqui")

## Passo 9 — Salvar

Criar pasta `marketing/paginas/[slug-da-solucao]/` e salvar:
- `copy.md` — copy completa da página (todas as seções)
- `meta.md` — metadados SEO, schemas JSON, OG e sugestões de links internos

## Passo 10 — Confirmar e monitorar

Informar onde foi salvo e entregar o plano de monitoramento pós-publicação:

> "Quer ajustar alguma seção, adicionar um case específico ou criar o material visual da página?"

**Plano de monitoramento (gerar junto com os arquivos):**

```
Monitoramento pós-publicação — [nome da página]

Semana 1-2 (após publicar):
- Verificar indexação: site:solveplan.com.br/[slug]
- Confirmar que Google Search Console não mostra erros de crawl
- Testar PageSpeed Insights (meta: >80 mobile, >90 desktop)
- Verificar rich results com Google Rich Results Test (schema)

Mês 1:
- GSC: página aparece em "Cobertura"? Está indexada?
- GSC: quais queries estão trazendo impressões?
- Ajustar meta description se CTR < 2%

Mês 2-3:
- GSC: rankings subindo para a keyword principal?
- Analytics: tempo na página > 2 min = bom sinal de relevância
- Analytics: taxa de conversão do CTA (meta: >2%)
- Atualizar com novo case ou dado se disponível

Revisão trimestral:
- A keyword principal está no top 10? Se não, revisar seções de dor e solução
- Adicionar links internos de artigos novos do blog para essa página
- Atualizar FAQ com novas perguntas identificadas via GSC
```

Salvar o plano de monitoramento em `marketing/paginas/[slug]/monitoramento.md`.

---

## Regras

- Nunca escrever copy genérica de "plataforma robusta" — sempre conectar com dor real e resultado concreto
- H1 contém a keyword principal. Só existe um H1 por página.
- H2s são as grandes seções. H3s são subtópicos dentro delas. Não pular níveis.
- Cada seção tem um trabalho específico — não misturar (hero não é lugar de FAQ, dor não é lugar de vender)
- O parágrafo de definição (Seção 2) é sagrado — não encurtar nem misturar com outra seção
- FAQ é estratégico pra AEO — priorizar perguntas com volume real de busca, não perguntas óbvias
- SAP BDC como referência quando a solução se conectar com analytics/dados/planejamento
- Alt text em todas as imagens — sempre com keyword e contexto
- Links internos com anchor text de keyword, nunca "clique aqui" ou "saiba mais"

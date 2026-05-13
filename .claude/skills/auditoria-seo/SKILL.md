---
name: auditoria-seo
description: Audita qualquer página do site Solveplan e entrega scorecard SEO/AEO/GEO com pontuação por item (0-100), diagnóstico do que está faltando e plano de ação com os ajustes exatos para chegar a 100%.
---

# /auditoria-seo

## Antes de começar

Ler `_contexto/empresa.md` e `_contexto/estrategia.md`.

## Como usar

> "Qual a URL da página que você quer auditar?"

Aceita qualquer página do site Solveplan: página de solução, artigo de blog, home, landing page, página de evento.

Se o usuário quiser auditar várias páginas de uma vez, processar uma por vez e gerar um scorecard separado para cada.

---

## Passo 1 — Buscar a página

Usar WebFetch na URL informada e capturar o HTML completo.

Se a página não carregar ou retornar erro, informar o usuário e pedir para verificar se a URL está correta e pública.

---

## Passo 2 — Coletar dados de performance

Tentar buscar PageSpeed Insights via API pública (sem autenticação, funciona para volume baixo):

```
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=[URL]&strategy=mobile
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=[URL]&strategy=desktop
```

Se a API não responder, informar:
> "Não consegui buscar o PageSpeed automaticamente. Cole aqui o score mobile e desktop de pagespeed.web.dev para incluir na auditoria."

---

## Passo 3 — Analisar e pontuar

Avaliar cada item abaixo e atribuir a pontuação correspondente.

---

### CATEGORIA 1 — SEO On-Page (40 pontos)

#### Title Tag (10 pts)
| Critério | Pontos |
|----------|--------|
| Title tag existe e não está vazia | 2 |
| Comprimento entre 50 e 60 caracteres | 3 |
| Keyword principal está no title | 5 |

**O que verificar no HTML:** `<title>...</title>`

---

#### Meta Description (10 pts)
| Critério | Pontos |
|----------|--------|
| Meta description existe | 2 |
| Comprimento entre 120 e 155 caracteres | 3 |
| Keyword principal está na meta description | 3 |
| Tem CTA implícito ou benefício claro | 2 |

**O que verificar no HTML:** `<meta name="description" content="...">`

---

#### Estrutura de Headings (10 pts)
| Critério | Pontos |
|----------|--------|
| Existe exatamente um H1 na página | 4 |
| H1 contém a keyword principal | 3 |
| H2s seguem hierarquia lógica (não pula de H1 pra H4) | 2 |
| H2s ou H3s contêm keywords secundárias ou variações | 1 |

---

#### URL, Imagens e Links (10 pts)
| Critério | Pontos |
|----------|--------|
| URL slug é curto (até 5 palavras), limpo e contém keyword | 3 |
| Página serve em HTTPS | 1 |
| Todas as imagens têm atributo `alt` preenchido (não vazio) | 3 |
| Há pelo menos 2 links internos para outras páginas do site | 3 |

---

### CATEGORIA 2 — Performance Técnica (20 pontos)

| Critério | Pontos |
|----------|--------|
| PageSpeed mobile ≥ 80 | 8 |
| PageSpeed mobile entre 60-79 | 4 |
| PageSpeed desktop ≥ 90 | 5 |
| PageSpeed desktop entre 70-89 | 2 |
| LCP (Largest Contentful Paint) ≤ 2,5s | 4 |
| CLS (Cumulative Layout Shift) ≤ 0,1 | 3 |

*Se PageSpeed não estiver disponível, atribuir 0 e marcar como "não verificado".*

---

### CATEGORIA 3 — AEO — Answer Engine Optimization (25 pontos)

#### Bloco de Featured Snippet (10 pts)
| Critério | Pontos |
|----------|--------|
| Existe um parágrafo direto de 40-60 palavras respondendo a pergunta principal da página | 6 |
| Esse parágrafo está logo abaixo de um H2 em formato de pergunta | 4 |

**Exemplo de estrutura ideal:**
```html
<h2>O que é SAP Business Data Cloud?</h2>
<p>SAP Business Data Cloud é uma plataforma de dados e analytics que unifica
dados financeiros, operacionais e de negócio em uma única camada semântica,
permitindo que empresas consolidem relatórios e planejem com dados em tempo real.</p>
```

---

#### FAQ (8 pts)
| Critério | Pontos |
|----------|--------|
| Existe seção de perguntas frequentes (FAQ) na página | 4 |
| O FAQ tem pelo menos 3 perguntas relevantes ao tema | 2 |
| As perguntas refletem o que o público realmente busca (People Also Ask) | 2 |

---

#### Perguntas nos Headings (7 pts)
| Critério | Pontos |
|----------|--------|
| Pelo menos 2 H2s ou H3s estão formulados como perguntas | 4 |
| As perguntas abordam as dúvidas reais da persona (não genéricas) | 3 |

---

### CATEGORIA 4 — GEO — Generative Engine Optimization (15 pontos)

#### Schema Markup (6 pts)
| Critério | Pontos |
|----------|--------|
| Existe schema JSON-LD na página | 2 |
| Schema é do tipo correto para o conteúdo (Article, Service, FAQPage, Organization) | 2 |
| FAQPage schema está presente se a página tem seção FAQ | 2 |

**O que verificar no HTML:** `<script type="application/ld+json">`

---

#### E-E-A-T — Experiência, Expertise, Autoridade, Confiança (5 pts)
| Critério | Pontos |
|----------|--------|
| Autor identificado (nome real) — para artigos/blog | 2 |
| Data de publicação ou atualização visível | 1 |
| Menção a credenciais, cases ou número de clientes como prova | 2 |

---

#### Entidades e Citações (4 pts)
| Critério | Pontos |
|----------|--------|
| Nome "Solveplan" aparece de forma natural no conteúdo | 1 |
| Produtos SAP mencionados pelo nome correto (SAP BDC, SAP Analytics Cloud, etc.) | 1 |
| Dados, pesquisas ou fontes externas são citados | 1 |
| Localização ou mercado (América Latina, Brasil) está presente | 1 |

---

## Passo 4 — Gerar o scorecard

Formato de entrega:

```
## Scorecard SEO/AEO/GEO — [URL]
*Auditoria em: [data]*

---

### Resultado Geral

[SCORE TOTAL]/100

| Categoria | Pontuação | Máximo | Status |
|-----------|-----------|--------|--------|
| SEO On-Page | X | 40 | 🔴/🟡/🟢 |
| Performance Técnica | X | 20 | 🔴/🟡/🟢 |
| AEO | X | 25 | 🔴/🟡/🟢 |
| GEO | X | 15 | 🔴/🟡/🟢 |
| **Total** | **X** | **100** | |

🔴 Abaixo de 50% da categoria | 🟡 Entre 50-79% | 🟢 80% ou mais
```

---

```
### Detalhamento — SEO On-Page

Title Tag: X/10
✅ [item ok]
❌ [item faltando] — O que fazer: [instrução exata]

Meta Description: X/10
✅ [item ok]
❌ [item faltando] — O que fazer: [instrução exata]

Estrutura de Headings: X/10
[...]

URL, Imagens e Links: X/10
[...]

---

### Detalhamento — Performance Técnica

PageSpeed mobile: [score ou "não verificado"] — X/8
PageSpeed desktop: [score ou "não verificado"] — X/5
LCP: [valor ou "não verificado"] — X/4
CLS: [valor ou "não verificado"] — X/3

---

### Detalhamento — AEO

Bloco Featured Snippet: X/10
[...]

FAQ: X/8
[...]

Perguntas nos Headings: X/7
[...]

---

### Detalhamento — GEO

Schema Markup: X/6
[...]

E-E-A-T: X/5
[...]

Entidades e Citações: X/4
[...]
```

---

```
### Plano de ação para 100%

Ordenado por impacto (maior ganho de pontos primeiro):

| Prioridade | O que corrigir | Pontos a ganhar | Dificuldade |
|------------|---------------|-----------------|-------------|
| 1 | [item] | +X pts | Fácil / Médio / Difícil |
| 2 | [item] | +X pts | Fácil / Médio / Difícil |
...

**Ganho potencial:** +X pontos → chega em Y/100
```

---

Para cada item no plano de ação, entregar o **ajuste exato**:

```
Item: [nome do item]
Problema: [o que está errado ou faltando]
Solução:
[texto exato, código HTML ou instrução de onde mudar no WordPress]
Onde mudar: [campo no Yoast/Rank Math / editor de página / Functions.php / etc.]
```

---

## Passo 5 — Gerar arquivo Excel (CSV)

Ao finalizar a análise, sempre gerar automaticamente um arquivo CSV da auditoria — sem precisar pedir.

Criar pasta `marketing/auditorias-seo/` e salvar dois arquivos:

**Arquivo 1 — Scorecard resumido:** `[slug-da-pagina]-[data]-score.csv`

```csv
Categoria,Item,Pontuação Obtida,Pontuação Máxima,Status,O que corrigir
SEO On-Page,Title Tag,X,10,OK / Parcial / Faltando,[instrução ou vazio se ok]
SEO On-Page,Meta Description,X,10,OK / Parcial / Faltando,[instrução]
SEO On-Page,Estrutura de Headings,X,10,OK / Parcial / Faltando,[instrução]
SEO On-Page,URL + Imagens + Links,X,10,OK / Parcial / Faltando,[instrução]
Performance Técnica,PageSpeed Mobile,X,8,OK / Parcial / Faltando,[instrução]
Performance Técnica,PageSpeed Desktop,X,5,OK / Parcial / Faltando,[instrução]
Performance Técnica,LCP,X,4,OK / Parcial / Faltando,[instrução]
Performance Técnica,CLS,X,3,OK / Parcial / Faltando,[instrução]
AEO,Bloco Featured Snippet,X,10,OK / Parcial / Faltando,[instrução]
AEO,FAQ,X,8,OK / Parcial / Faltando,[instrução]
AEO,Perguntas nos Headings,X,7,OK / Parcial / Faltando,[instrução]
GEO,Schema Markup,X,6,OK / Parcial / Faltando,[instrução]
GEO,E-E-A-T,X,5,OK / Parcial / Faltando,[instrução]
GEO,Entidades e Citações,X,4,OK / Parcial / Faltando,[instrução]
TOTAL,,X,100,,
```

**Arquivo 2 — Plano de ação:** `[slug-da-pagina]-[data]-plano-acao.csv`

```csv
Prioridade,Item,Pontos a Ganhar,Dificuldade,O que fazer,Onde mudar no WordPress
1,[item],+X,Fácil / Médio / Difícil,[instrução exata],[campo Yoast / editor de página / etc.]
2,[item],+X,Fácil / Médio / Difícil,[instrução exata],[onde mudar]
...
```

*O CSV abre diretamente no Excel com dois cliques. Para visualizar corretamente no Excel Brasil: ao abrir, selecionar "Delimitado" → separador "Vírgula".*

---

## Passo 6 — Salvar relatório completo (opcional)

Se o usuário quiser salvar o relatório narrativo além do CSV:

Criar na mesma pasta `marketing/auditorias-seo/` e salvar como `[slug-da-pagina]-[data].md`.

---

## Modo comparativo — auditar várias páginas

Se o usuário quiser comparar múltiplas páginas:

1. Auditar cada uma separadamente e gerar os CSVs individuais de cada
2. Gerar tabela comparativa no final:

```
| Página | SEO | Performance | AEO | GEO | Total |
|--------|-----|-------------|-----|-----|-------|
| /solucoes/sap-bdc | 32/40 | 15/20 | 18/25 | 10/15 | 75/100 |
| /blog/artigo-x | 28/40 | 12/20 | 20/25 | 8/15 | 68/100 |
```

3. Gerar também um CSV consolidado `comparativo-[data].csv` com uma linha por página
4. Indicar qual página tem maior potencial de melhoria rápida

---

## Regras

- Nunca inventar dados — se não encontrou um elemento no HTML, marcar como ausente (0 pts) e não inferir
- Performance sem dado do PageSpeed = 0 pontos — informar o usuário e dar link direto: pagespeed.web.dev
- Sugestões de correção sempre em linguagem prática: o texto exato, não só "adicione uma meta description"
- Para páginas de blog: AEO tem peso maior — priorizá-lo no plano de ação
- Para páginas de solução/produto: SEO On-Page e GEO têm peso maior
- Ao identificar algo que funcionou bem (score alto em AEO, por exemplo), mencionar como modelo para outras páginas

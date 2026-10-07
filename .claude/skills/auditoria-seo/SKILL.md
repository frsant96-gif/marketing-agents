---
name: auditoria-seo
description: Audita qualquer página do site Solveplan e entrega scorecard SEO/AEO/GEO (0-100) com diagnóstico por item, cobertura de subperguntas (query fan-out), checagem do que robôs e IAs conseguem ler sem JavaScript, e plano de ação com os ajustes exatos para chegar a 100%. Opcionalmente faz diagnóstico de visibilidade (Google + IAs) e aplica as correções aprovadas no WordPress.
---

# /auditoria-seo

> **Versão 2 (out/2026).** A pontuação foi rebalanceada para incluir rastreabilidade por IA, conteúdo sem JavaScript e cobertura de subperguntas. Auditorias feitas antes de 07/10/2026 usam a v1: comparar a evolução **por item**, não só pelo total.

## Antes de começar

Ler `_contexto/empresa.md` e `_contexto/estrategia.md`.
Números oficiais para o site: 150+ empresas, 300+ projetos, 68+ especialistas, 13+ anos.

## Como usar

> "Qual a URL da página que você quer auditar?"

Aceita qualquer página do site Solveplan: página de solução, artigo de blog, home, landing page, página de evento.

Se o usuário quiser auditar várias páginas de uma vez, processar uma por vez e gerar um scorecard separado para cada.

**Fora do escopo** (não se aplica a uma consultoria B2B): SEO para e-commerce, Merchant Center, feeds de produto, SEO para notícias, SEO internacional. SEO local se resume a manter o Google Business Profile atualizado.

---

## Passo 1 — Buscar a página (HTML bruto)

Baixar o **HTML bruto** com `curl` (ou `Invoke-WebRequest`). Não usar WebFetch para pontuar: ele converte para texto e esconde tags, `alt`, schema e meta robots.

```bash
curl -sL -A "Mozilla/5.0" "[URL]?v=$RANDOM" -o pagina.html
```

O parâmetro `?v=` evita a cópia em cache do LiteSpeed.

O HTML bruto é **exatamente o que Google, GPTBot, ClaudeBot e PerplexityBot leem**. Tudo o que só aparece depois do JavaScript (contadores animados, abas, carrosséis) pode ser invisível para eles.

Buscar também:
- `https://solveplan.com/robots.txt`
- o sitemap (`/sitemap_index.xml`), para confirmar se a URL está listada

Se a página não carregar ou retornar erro, informar o usuário e pedir para verificar se a URL está correta e pública.

---

## Passo 2 — Coletar dados de performance

Tentar buscar PageSpeed Insights via API pública:

```
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=[URL]&strategy=mobile
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=[URL]&strategy=desktop
```

A cota gratuita costuma estar esgotada. Se a API não responder:
> "Não consegui buscar o PageSpeed automaticamente. Cole aqui o score mobile e desktop de pagespeed.web.dev para incluir na auditoria."

Registrar também, sem pontuar, o TTFB e o status do cache (`curl -w '%{time_starttransfer}'` e o header `X-LiteSpeed-Cache`).

---

## Passo 3 — Identificar a pergunta principal e as subperguntas

Antes de pontuar, definir:

1. **Keyword principal** da página (ex.: "consultoria SAP Business Data Cloud").
2. **Pergunta principal** que a página deve responder (ex.: "O que é SAP BDC e quem implementa?").
3. **6 subperguntas** que uma IA geraria ao "abrir" essa pergunta (query fan-out). Use a persona (CIO, CFO, controller, head de dados) e a jornada de compra:
   - O que é / como funciona
   - Diferença para a alternativa (ex.: BDC x Datasphere x BW)
   - Quanto tempo / quanto custa / o que é preciso ter antes
   - Riscos e erros comuns
   - Prova: quem já fez, com que resultado
   - Por que a Solveplan (diferencial, prêmio, parceria SAP)

Para cada subpergunta, marcar se a página **responde em texto visível** (✅), **responde parcialmente** (🟡) ou **não responde** (❌). Isso alimenta o critério de cobertura (AEO) e o FAQ sugerido.

---

## Passo 4 — Analisar e pontuar

Avaliar cada item abaixo e atribuir a pontuação correspondente.

---

### CATEGORIA 1 — SEO On-Page e Rastreabilidade (40 pontos)

#### Title Tag (8 pts)
| Critério | Pontos |
|----------|--------|
| Title tag existe e não está vazia | 2 |
| Comprimento entre 50 e 60 caracteres | 2 |
| Keyword principal está no title (de preferência no início) | 4 |

**O que verificar no HTML:** `<title>...</title>`

---

#### Meta Description (8 pts)
| Critério | Pontos |
|----------|--------|
| Meta description existe | 2 |
| Comprimento entre 120 e 155 caracteres | 2 |
| Keyword principal está na meta description | 2 |
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

*No Elementor, o título visual do topo costuma estar como H2. A correção é trocar a tag para H1, sem mudar o texto.*

---

#### URL, Imagens e Links internos (8 pts)
| Critério | Pontos |
|----------|--------|
| URL slug é curto (até 5 palavras), limpo e contém keyword | 2 |
| Página serve em HTTPS | 1 |
| Todas as imagens de conteúdo têm `alt` preenchido (ignorar pixels de rastreamento) | 2 |
| Há pelo menos 2 links internos **no corpo do texto** (não contam menu e rodapé) para páginas relacionadas | 3 |

---

#### Indexação e leitura por robôs e IAs (6 pts)
| Critério | Pontos |
|----------|--------|
| Página indexável e coerente: meta robots com `index`, canonical apontando para ela mesma e URL presente no sitemap | 2 |
| `robots.txt` não bloqueia Googlebot, Bingbot, GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot nem Google-Extended | 2 |
| Informação-chave está **no HTML bruto, em texto**: H1, parágrafo principal, números de prova (ex.: "150+ empresas") e CTA. Nada essencial só em imagem ou só via JavaScript | 2 |

**Como verificar o último item:** procurar no HTML bruto os números e frases-chave. Exemplo real (25/09/2026): os contadores da home apareciam como `0 +` no HTML porque o número só é preenchido pela animação. Para robôs e IAs, a Solveplan tinha "0+ empresas".

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

*Se PageSpeed não estiver disponível, atribuir 0, marcar como "não verificado" e mostrar também o **score sem performance (X/80)**, para dar para comparar páginas e datas.*

---

### CATEGORIA 3 — AEO — Answer Engine Optimization (25 pontos)

#### Bloco de resposta direta (8 pts)
| Critério | Pontos |
|----------|--------|
| Existe um parágrafo direto de 40-60 palavras respondendo a pergunta principal da página | 5 |
| Esse parágrafo está logo abaixo de um H2 em formato de pergunta | 3 |

**Exemplo de estrutura ideal:**
```html
<h2>O que é SAP Business Data Cloud?</h2>
<p>SAP Business Data Cloud é uma plataforma de dados e analytics que unifica
dados financeiros, operacionais e de negócio em uma única camada semântica,
permitindo que empresas consolidem relatórios e planejem com dados em tempo real.</p>
```

---

#### Cobertura de subperguntas — query fan-out (6 pts)
| Critério | Pontos |
|----------|--------|
| 5 ou 6 das 6 subperguntas do Passo 3 respondidas em texto visível | 6 |
| 3 ou 4 respondidas | 3 |
| 2 ou menos | 0 |

*As IAs montam a resposta juntando trechos que respondem às subperguntas. Página que só responde a pergunta principal perde citação para quem cobre o tema inteiro.*

---

#### FAQ (7 pts)
| Critério | Pontos |
|----------|--------|
| Existe seção de perguntas frequentes (FAQ) na página | 3 |
| O FAQ tem pelo menos 3 perguntas relevantes ao tema | 2 |
| As perguntas refletem o que o público realmente busca (People Also Ask, subperguntas do Passo 3) | 2 |

---

#### Perguntas nos Headings (4 pts)
| Critério | Pontos |
|----------|--------|
| Pelo menos 2 H2s ou H3s estão formulados como perguntas | 2 |
| As perguntas abordam as dúvidas reais da persona (não genéricas) | 2 |

---

### CATEGORIA 4 — GEO — Generative Engine Optimization (15 pontos)

#### Dados estruturados coerentes (6 pts)
| Critério | Pontos |
|----------|--------|
| Existe schema JSON-LD na página | 1 |
| O tipo corresponde ao conteúdo: página de solução = Service/WebPage; post = Article/BlogPosting; home = Organization + WebSite. **Página de solução marcada como BlogPosting = 0** | 2 |
| Os dados do schema batem com o visível (nome, endereço com `addressCountry: "BR"`, autor real, datas) | 1 |
| FAQPage schema está presente se a página tem seção FAQ | 2 |

**O que verificar no HTML:** `<script type="application/ld+json">`

---

#### E-E-A-T — Experiência, Expertise, Autoridade, Confiança (5 pts)
| Critério | Pontos |
|----------|--------|
| Autor identificado com nome real (para artigos/blog) **ou** responsável/time citado (para páginas de solução) | 2 |
| Data de publicação ou atualização visível | 1 |
| Prova concreta: case com número, prêmio (Melhor Parceiro SAP BDC 2026 LATAM), selo SAP Gold ou número de clientes | 2 |

---

#### Entidades, estatísticas e fontes (4 pts)
| Critério | Pontos |
|----------|--------|
| Nome "Solveplan" aparece de forma natural no conteúdo | 1 |
| Produtos SAP mencionados pelo nome correto (SAP Business Data Cloud, SAP Datasphere, SAP Analytics Cloud, SAP BW/4HANA) | 1 |
| Pelo menos uma estatística ou fonte externa citada (pesquisa, SAP, Gartner/IDC, dado de case) | 1 |
| Localização ou mercado (América Latina, Brasil) está presente | 1 |

---

## Passo 5 — Gerar o scorecard

Formato de entrega:

```
## Scorecard SEO/AEO/GEO — [URL]
*Auditoria em: [data] · versão 2 da skill*

---

### Resultado Geral

[SCORE TOTAL]/100   (sem performance: X/80)

| Categoria | Pontuação | Máximo | Status |
|-----------|-----------|--------|--------|
| SEO On-Page e Rastreabilidade | X | 40 | 🔴/🟡/🟢 |
| Performance Técnica | X | 20 | 🔴/🟡/🟢 |
| AEO | X | 25 | 🔴/🟡/🟢 |
| GEO | X | 15 | 🔴/🟡/🟢 |
| **Total** | **X** | **100** | |

🔴 Abaixo de 50% da categoria | 🟡 Entre 50-79% | 🟢 80% ou mais
```

---

```
### Pergunta principal e subperguntas

Pergunta principal: [pergunta]
| Subpergunta | Respondida? | Onde / o que falta |
|---|---|---|
| ... | ✅ / 🟡 / ❌ | ... |
```

---

```
### Detalhamento — SEO On-Page e Rastreabilidade

Title Tag: X/8
✅ [item ok]
❌ [item faltando] — O que fazer: [instrução exata]

Meta Description: X/8
Estrutura de Headings: X/10
URL, Imagens e Links internos: X/8
Indexação e leitura por robôs e IAs: X/6
[...]

---

### Detalhamento — Performance Técnica

PageSpeed mobile: [score ou "não verificado"] — X/8
PageSpeed desktop: [score ou "não verificado"] — X/5
LCP: [valor ou "não verificado"] — X/4
CLS: [valor ou "não verificado"] — X/3
TTFB / cache (referência): [valor]

---

### Detalhamento — AEO

Bloco de resposta direta: X/8
Cobertura de subperguntas: X/6
FAQ: X/7
Perguntas nos Headings: X/4

---

### Detalhamento — GEO

Dados estruturados coerentes: X/6
E-E-A-T: X/5
Entidades, estatísticas e fontes: X/4
```

---

```
### Plano de ação para 100%

Ordenado por impacto (maior ganho de pontos primeiro):

| Prioridade | O que corrigir | Pontos a ganhar | Dificuldade | Mexe no visual? |
|------------|---------------|-----------------|-------------|-----------------|
| 1 | [item] | +X pts | Fácil / Médio / Difícil | Não / Sim |
...

**Ganho potencial:** +X pontos → chega em Y/100
```

A coluna **"Mexe no visual?"** é obrigatória: title, description, schema e noindex não mexem; H1 (tag) praticamente não; texto novo, seções e cards mexem e devem ser feitos em rascunho.

Para cada item no plano de ação, entregar o **ajuste exato**:

```
Item: [nome do item]
Problema: [o que está errado ou faltando]
Solução:
[texto exato, código HTML ou instrução de onde mudar no WordPress]
Onde mudar: [Rank Math > Editar snippet / Elementor > widget X / Rank Math > Títulos e Meta / etc.]
```

Ao sugerir FAQ, usar as subperguntas ❌ e 🟡 do Passo 3 e entregar também o JSON-LD FAQPage pronto.

---

## Passo 6 — Gerar arquivo Excel (CSV)

Ao finalizar a análise, sempre gerar automaticamente os CSVs da auditoria, sem precisar pedir.

Salvar em `marketing/auditorias-seo/`. A pasta é sincronizada pelo OneDrive: gerar o arquivo no scratchpad e depois copiar, porque o OneDrive pode travar o arquivo enquanto sincroniza.

**Arquivo 1 — Scorecard resumido:** `[slug-da-pagina]-[data]-score.csv`

```csv
Categoria,Item,Pontuação Obtida,Pontuação Máxima,Status,O que corrigir
SEO On-Page,Title Tag,X,8,OK / Parcial / Faltando,[instrução ou vazio se ok]
SEO On-Page,Meta Description,X,8,OK / Parcial / Faltando,[instrução]
SEO On-Page,Estrutura de Headings,X,10,OK / Parcial / Faltando,[instrução]
SEO On-Page,URL + Imagens + Links internos,X,8,OK / Parcial / Faltando,[instrução]
SEO On-Page,Indexação e leitura por robôs e IAs,X,6,OK / Parcial / Faltando,[instrução]
Performance Técnica,PageSpeed Mobile,X,8,OK / Parcial / Faltando / Não verificado,[instrução]
Performance Técnica,PageSpeed Desktop,X,5,OK / Parcial / Faltando / Não verificado,[instrução]
Performance Técnica,LCP,X,4,OK / Parcial / Faltando / Não verificado,[instrução]
Performance Técnica,CLS,X,3,OK / Parcial / Faltando / Não verificado,[instrução]
AEO,Bloco de resposta direta,X,8,OK / Parcial / Faltando,[instrução]
AEO,Cobertura de subperguntas,X,6,OK / Parcial / Faltando,[subperguntas não respondidas]
AEO,FAQ,X,7,OK / Parcial / Faltando,[instrução]
AEO,Perguntas nos Headings,X,4,OK / Parcial / Faltando,[instrução]
GEO,Dados estruturados coerentes,X,6,OK / Parcial / Faltando,[instrução]
GEO,E-E-A-T,X,5,OK / Parcial / Faltando,[instrução]
GEO,Entidades + estatísticas + fontes,X,4,OK / Parcial / Faltando,[instrução]
TOTAL,,X,100,,
TOTAL SEM PERFORMANCE,,X,80,,
```

**Arquivo 2 — Plano de ação:** `[slug-da-pagina]-[data]-plano-acao.csv`

```csv
Prioridade,Item,Pontos a Ganhar,Dificuldade,Mexe no visual?,O que fazer,Onde mudar no WordPress
1,[item],+X,Fácil / Médio / Difícil,Não / Sim,[instrução exata],[onde mudar]
...
```

*Salvar com UTF-8 com BOM para os acentos abrirem certos no Excel.*

---

## Passo 7 — Salvar relatório completo (opcional)

Se o usuário quiser salvar o relatório narrativo além do CSV, criar na mesma pasta `marketing/auditorias-seo/` e salvar como `[slug-da-pagina]-[data].md`.

---

## Modo visibilidade — Google e IAs (opcional)

Usar quando o usuário perguntar "como estamos no Google/nas IAs" ou antes de planejar conteúdo. Não entra na nota da página.

1. **Posição no Google:** rodar `/search-console-ratos` para a URL (últimos 90 dias): queries, posição média, cliques, CTR. Destacar queries com posição entre 5 e 20 e CTR baixo, porque um title ou description melhor dá ganho rápido nelas.
2. **Presença nas IAs:** gerar uma lista de 8 a 10 perguntas reais da persona (ex.: "quem são os parceiros SAP Business Data Cloud no Brasil?", "como migrar do SAP BW para o Datasphere?"). Pedir ao usuário para testar no ChatGPT, Gemini, Perplexity e Copilot e anotar: a Solveplan aparece? É citada com link? Quais concorrentes aparecem? Entregar a planilha de teste pronta para preencher.
3. **Gap vs. concorrentes:** para as mesmas perguntas, listar quem aparece (Google e IAs) e qual página deles é citada. Comparar o que essa página tem que a da Solveplan não tem (FAQ, números, cases, comparativos).
4. **Tráfego vindo de IAs:** rodar `/ga4-ratos` filtrando origem por `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`, `claude.ai`. Registrar sessões e páginas de entrada.
5. **Copilot:** se houver Bing Webmaster Tools, verificar o relatório de citações em IA.

Salvar como `marketing/auditorias-seo/visibilidade-[data].xlsx`.

---

## Modo comparativo — auditar várias páginas

Se o usuário quiser comparar múltiplas páginas:

1. Auditar cada uma separadamente e gerar os CSVs individuais de cada
2. Gerar tabela comparativa no final:

```
| Página | SEO | Performance | AEO | GEO | Total | Sem perf. |
|--------|-----|-------------|-----|-----|-------|-----------|
| /sap-business-data-cloud/ | 32/40 | 15/20 | 18/25 | 10/15 | 75/100 | 60/80 |
```

3. Gerar também um CSV consolidado `comparativo-[data].csv` com uma linha por página
4. Indicar qual página tem maior potencial de melhoria rápida

Para varrer o site inteiro (sitemap), checar por URL: title, description, H1, meta robots e problemas. Ver `marketing/auditorias-seo/site-2026-09-25-varredura.csv` como modelo.

---

## Aplicar as correções no WordPress (só com aprovação)

Só aplicar o que o usuário aprovar **linha a linha** (planilha com coluna "Aprovado?" Sim/Não/Ajustar). Regras desta conta:

1. **Backup antes:** hPanel Hostinger → Sites → solveplan.com → Arquivos → Backups → Criar backup (1 manual a cada 24 h; o automático é diário).
2. **Acesso pela API:** as senhas de aplicativo ficam desativadas pelo Wordfence (Todas as opções → Proteção contra força bruta → Opções adicionais → "Desativar senhas da aplicação do WordPress"). Pedir para desmarcar só durante o trabalho e marcar de novo no fim.
3. **Rank Math via REST:** `POST /wp-json/rankmath/v1/updateMeta` com `{"objectID": ID, "objectType": "post", "meta": {...}}`. As chaves que funcionam são `rank_math_title`, `rank_math_description` e `rank_math_robots` (ex.: `["noindex","nofollow"]`). A chave `title` sozinha responde 200 mas **não grava**.
4. **Redirecionamentos:** criar pelo painel (Rank Math → Redirecionamentos). O endpoint `updateRedirection` responde "criado" sem gravar.
5. **noindex por tipo de conteúdo:** Rank Math → Títulos e Meta → aba do tipo (ex.: Banners) → Meta robots. **Nunca** na aba "Meta global", que vale para o site inteiro.
6. **Cache:** depois de alterar, conferir sem cache (`?v=`) e com cache. Se a home continuar antiga, fazer um "salvar" vazio (`POST /wp/v2/pages/7` com `{}`) para limpar o cache do LiteSpeed.
7. **Testar em 1 página antes de aplicar em massa.** Guardar os valores antigos num `rollback-[data].json` e, no fim, conferir cada URL no ar e confirmar que todas abrem com o visual do Elementor.
8. Mudanças que mexem no visual (texto novo, seções, cards) vão para **rascunho** para o usuário aprovar antes de publicar.

---

## Regras

- Nunca inventar dados: se não encontrou um elemento no HTML, marcar como ausente (0 pts) e não inferir
- Pontuar sempre pelo **HTML bruto**, não pelo que o navegador mostra depois do JavaScript
- Performance sem dado do PageSpeed = 0 pontos, informar o usuário, dar o link pagespeed.web.dev e mostrar o score sem performance (/80)
- Sugestões de correção sempre em linguagem prática: o texto exato, não só "adicione uma meta description"
- Para páginas de blog: AEO tem peso maior, priorizá-lo no plano de ação
- Para páginas de solução/produto: SEO On-Page e GEO têm peso maior, e a prova (prêmio BDC 2026, Gold, cases) deve aparecer em texto
- Conteúdo útil e original: sinalizar texto que parece copiado de material da SAP (genérico, sem "por que a Solveplan")
- Ao identificar algo que funcionou bem, mencionar como modelo para outras páginas (ex.: /sap-datasphere/ com H1 em pergunta e FAQ)

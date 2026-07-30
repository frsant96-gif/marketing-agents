## Scorecard SEO/AEO/GEO — https://solveplan.com/sap-datasphere/
*Auditoria em: 30/07/2026*

---

### Resultado Geral

**30/100**

| Categoria | Pontuação | Máximo | Status |
|-----------|-----------|--------|--------|
| SEO On-Page | 20 | 40 | 🔴 |
| Performance Técnica | 0 | 20 | 🔴 (não verificado) |
| AEO | 6 | 25 | 🔴 |
| GEO | 4 | 15 | 🔴 |
| **Total** | **30** | **100** | |

🔴 Abaixo de 50% da categoria | 🟡 Entre 50-79% | 🟢 80% ou mais

**Nota:** esta auditoria reflete o que está **ao vivo hoje** para o público e pro Google — o novo title/meta description que já aplicamos no banco de dados (via Rank Math API) ainda não apareceu porque a página está em cache LiteSpeed. Assim que você purgar o cache, title e meta description passam a valer o que está descrito no plano de ação abaixo.

---

### Detalhamento — SEO On-Page (20/40)

**Title Tag: 7/10**
✅ Title existe e não está vazio
❌ Comprimento fora da faixa 50-60 (tem 27 caracteres: "SAP DATASPHERE - Solveplan") — O que fazer: ampliar aproveitando o espaço, ex: "SAP Datasphere: o que é e como funciona | Solveplan" (já aplicado, falta purgar cache)
✅ Keyword principal ("SAP Datasphere") está no title

**Meta Description: 6/10**
✅ Meta description existe
❌ Tem ~156 caracteres e termina cortada no meio da frase ("...garantindo acesso") — O que fazer: reescrever fechando a ideia dentro de 120-155 caracteres (já aplicado, falta purgar cache)
✅ Keyword principal está na description
🟡 Tem benefício implícito mas nenhum CTA claro — O que fazer: fechar com CTA ("fale com a Solveplan", "agende uma conversa")

**Estrutura de Headings: 1/10**
❌ Não existe nenhum H1 na página — todos os títulos usam a tag H2 do widget "heading" do Elementor — O que fazer: trocar o primeiro H2 ("SAP DATASPHERE") para H1
❌ Consequentemente, não há H1 com a keyword — resolve junto com o item acima
❌ Sem H1, a hierarquia começa direto em H2 (pulo de nível) — O que fazer: definir 1 H1 e reorganizar os H2s como filhos
✅ Os H2s existentes trazem variações da keyword (SAP DWC, Data Warehouse Cloud, SAP DataSphere)

**URL, Imagens e Links: 6/10**
✅ URL curta, limpa e com keyword (/sap-datasphere/)
✅ HTTPS ativo
❌ Todas as imagens da página têm `alt=""` vazio (logo, imagens de conteúdo e carrossel de clientes) — O que fazer: preencher alt text descritivo em cada uma
🟡 Links internos existem só no rodapé (padrão de todas as páginas do site) — nenhum link contextual dentro do corpo do texto para outras páginas de solução (ex: SAP Analytics Cloud, Consolidação Contábil) — O que fazer: adicionar 2+ links dentro dos parágrafos

---

### Detalhamento — Performance Técnica (0/20 — não verificado)

A API pública do PageSpeed Insights retornou erro 429 (cota diária esgotada) no momento da auditoria. Não verificado:
- PageSpeed mobile
- PageSpeed desktop
- LCP (Largest Contentful Paint)
- CLS (Cumulative Layout Shift)

**Ação:** rodar manualmente em [pagespeed.web.dev](https://pagespeed.web.dev/analysis?url=https%3A%2F%2Fsolveplan.com%2Fsap-datasphere%2F) e me passar os números pra eu completar essa parte do scorecard.

---

### Detalhamento — AEO (6/25)

**Bloco de Featured Snippet: 6/10**
✅ Existe um parágrafo de ~44 palavras que define o SAP Datasphere de forma direta ("O SAP Datasphere transforma dados fragmentados em uma estrutura unificada e eficiente...")
❌ Esse parágrafo está sob o H2 "SAP DATASPHERE" (rótulo), não sob uma pergunta ("O que é o SAP Datasphere?") — O que fazer: só renomear o heading, o parágrafo já serve

**FAQ: 0/8**
❌ Não existe seção de FAQ na página — O que fazer: adicionar 4-5 perguntas reais, priorizando o que a busca orgânica já mostra que as pessoas perguntam (ver achado do GSC abaixo)

**Perguntas nos Headings: 0/7**
❌ Nenhum H2 é uma pergunta — todos são rótulos ("Antes do DataSphere", "A transição: SAP DWC", "O avanço: SAP DataSphere", "Dados que movem decisões") — O que fazer: reformular pelo menos 2 como pergunta

---

### Detalhamento — GEO (4/15)

**Schema Markup: 2/6**
✅ Existe schema JSON-LD (Organization, WebSite, WebPage, Person, BlogPosting)
❌ O tipo usado é `BlogPosting` — errado para uma página de solução/produto (deveria ser `Service` ou `WebPage`) — O que fazer: ajustar em Rank Math > Schema
❌ Sem `FAQPage` (porque não há FAQ ainda)

**E-E-A-T: 0/5**
❌ Autor no schema é `felippeemanoel` (slug técnico, não nome/cargo real) — pouco relevante pra uma página institucional de produto
❌ Data de publicação/atualização não aparece visível no conteúdo pro leitor
❌ Conteúdo não menciona nenhuma credencial da Solveplan (parceira SAP Gold, Melhor Parceiro SAP BDC 2026, 150+ empresas) — dado que isso é o principal diferencial competitivo da empresa hoje, é a maior lacuna da página

**Entidades e Citações: 2/4**
✅ "Solveplan" aparece naturalmente várias vezes
✅ Produtos SAP citados corretamente (SAP Datasphere, SAP BW, SAP BW/4HANA, SAP Data Warehouse Cloud)
❌ Nenhum dado, pesquisa ou fonte externa citada
❌ Não menciona atuação na América Latina/Brasil

---

### Plano de ação para 100%

Ordenado por impacto (maior ganho de pontos primeiro):

| Prioridade | O que corrigir | Pontos a ganhar | Dificuldade |
|------------|---------------|-----------------|-------------|
| 1 | Criar seção de FAQ com schema FAQPage | +10 | Médio |
| 2 | Adicionar H1 na página | +7 | Fácil |
| 3 | Reescrever pelo menos 2 headings como pergunta | +7 | Médio |
| 4 | Reformular o H2 de definição em pergunta (aproveita o parágrafo já existente) | +4 | Fácil |
| 5 | Preencher alt text em todas as imagens | +3 | Fácil |
| 6 | Corrigir tipo de schema (BlogPosting → Service/WebPage) | +2 | Médio |
| 7 | Adicionar prova social (SAP Gold, Melhor Parceiro BDC 2026, 150+ empresas) no texto | +2 | Fácil |
| 8 | Adicionar dado/fonte externa + menção América Latina | +2 | Fácil |
| 9 | Adicionar links internos contextuais no corpo do texto | +1 | Fácil |
| 10 | Rodar PageSpeed Insights e ajustar performance | até +20 | Fácil (medir) / varia (corrigir) |

**Ganho potencial:** +38 a +58 pontos → chega em 68-88/100 (o restante depende do resultado real do PageSpeed)

---

### Conexão com o achado do Search Console

O item de maior prioridade (FAQ) não é arbitrário: os dados do GSC mostram queries como **"o que é datasphere"** (14 impressões, posição 10, 0 cliques) e **"datasphere o que é"** (21 impressões, posição 9,2, 0 cliques) — a página tem impressão pra essa intenção mas nada na estrutura responde diretamente a ela hoje. FAQ + heading em formato de pergunta ataca esse gap direto.

---

### Arquivos gerados
- `sap-datasphere-2026-07-30-score.csv` — scorecard detalhado
- `sap-datasphere-2026-07-30-plano-acao.csv` — plano de ação priorizado

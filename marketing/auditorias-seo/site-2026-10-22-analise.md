# Análise do site solveplan.com — 22/10/2026
*Skill /auditoria-seo v2 · 108 URLs do sitemap varridas · comparação com 25/09/2026*

---

## Resumo

O que foi feito em 25/09 **continua no ar**: os 72 titles, descriptions e noindex aprovados estão todos ativos, nenhum se perdeu. O sitemap está limpo, o PaPM redireciona para /contato/ e o robots.txt deixa Google e IAs lerem o site.

Os problemas grandes **continuam os mesmos de 25/09**, porque eram as etapas deixadas para depois:

1. **26 das 30 páginas institucionais seguem sem H1**, incluindo a home e a BDC. Os textos já foram aprovados em 25/09.
2. **28 das 30 páginas usam o schema de post de blog (BlogPosting)**, e o endereço da empresa no schema está com país "55".
3. **A home e a página BDC não mudaram de conteúdo.** A home não fala de BDC nem do prêmio. A BDC tem 297 palavras genéricas, sem prova, sem link para os posts de BDC e sem citar a Solveplan no texto.
4. **Os contadores da home e da Sobre nós aparecem como "0 +"** para Google e IAs.

Dois pontos novos:

- **22 páginas de categoria do blog estão indexadas**, sem description e com 160 a 500 palavras (só listas de posts). Elas diluem o site no Google.
- **10 páginas têm FAQ no texto, mas sem o schema FAQPage**: 5 posts e os 5 cases, estes a confirmar.

| Página | Nota v2 | Sem performance |
|---|---|---|
| Home | **35/100** | 35/80 |
| /sap-business-data-cloud/ | **28/100** | 28/80 |

*A nota v2 não se compara com a de 25/09 (v1). Por item, o title e a description da home e da BDC saíram de 2 e 7 para 8/8 nos dois casos.*

---

## O que mudou desde 25/09

| Item | 25/09 | 22/10 |
|---|---|---|
| Titles e descriptions aprovados (72) | aplicados | ✅ todos no ar |
| Páginas de teste no Google | 5 indexadas | ✅ fora do índice e do sitemap |
| PaPM | publicada | ✅ rascunho + 301 para /contato/ |
| Case novo | — | ✅ SSA Alimentos + SAP Datasphere (com H1) |
| FAQPage schema | poucas páginas | ✅ 9 páginas (Datasphere, Solve Watch, 4 posts, 3 eventos) |
| Páginas sem H1 | 28 | ⚠️ 26 (só saíram as que viraram rascunho) |
| Schema BlogPosting em páginas | todas | ⚠️ 28 de 30 |
| Contadores "0 +" | home | ⚠️ home + Sobre nós |
| "Analitycs" no menu, "BLog", botão para /aceleradores/ | aberto | ⚠️ ainda aberto |
| Imagens sem alt | — | ⚠️ 530 de 719 |
| PageSpeed | não medido | ⚠️ não medido (cota da API esgotada) |

---

## Página BDC — o que as IAs não encontram nela

Pergunta principal: *"O que é o SAP Business Data Cloud e quem implementa?"*

| Subpergunta | Responde? | O que falta |
|---|---|---|
| O que é o BDC e o que inclui | ✅ | Ok, mas a definição tem ~30 palavras e fica sob "A Solução" |
| BDC x Datasphere x BW: preciso migrar? | 🟡 | Lista os componentes, mas não explica a diferença nem a migração |
| Quanto tempo leva / o que preciso ter antes | ❌ | Nada sobre prazo, pré-requisitos ou licença |
| Riscos e custos de consumo | ❌ | O blog tem o post "Gestão de consumo SAP BDC", mas a página não linka |
| Quem já implementou, com que resultado | ❌ | Nenhum case (Klabin, SSA Alimentos) |
| Por que a Solveplan | ❌ | Não cita o prêmio de Melhor Parceiro SAP BDC 2026 LATAM, o selo Gold nem a própria Solveplan |

**A página que recebe 65% do tráfego responde 1 de 6 perguntas.** A reescrita dela continua sendo a maior alavanca do site.

## Home — subperguntas

Pergunta principal: *"Qual consultoria SAP contratar para dados, analytics e BDC?"*

| Subpergunta | Responde? |
|---|---|
| O que a Solveplan faz | ✅ |
| Trabalha com BDC / Datasphere? | 🟡 só nos cards do blog |
| Para que empresas e setores | ❌ os logos estão em imagem |
| Como funciona o trabalho (diagnóstico → implantação → sustentação) | ❌ |
| Resultados comprovados | ✅ case Matrix Energia |
| Por que a Solveplan | 🟡 diz "principal parceiro SAP", sem prêmio nem Gold |

---

## Plano de ação

| # | O que fazer | Onde | Impacto | Mexe no visual? |
|---|---|---|---|---|
| 1 | **H1 nas 26 páginas.** Trocar a tag do título do topo de H2 para H1, com o texto aprovado em 25/09 | Elementor, widget Título > Tag HTML | +7 pts por página | Praticamente não (conferir o tamanho da fonte) |
| 2 | **Schema das páginas.** Tipo padrão das Páginas = Nenhum/WebPage; País = BR. Testar em 1 página antes, porque páginas antigas podem ter o "Artigo" gravado | Rank Math > Títulos e Meta > Páginas; > SEO local | +1 a 3 pts por página | Não |
| 3 | **Noindex nas 22 categorias do blog** (aba Categorias, **nunca** a "Meta global") | Rank Math > Títulos e Meta > Categorias > Meta robots | Tira páginas finas do Google | Não |
| 4 | **Contadores "0 +"** na home e na Sobre nós: número inicial = número final (150, 300, 68, 13) | Elementor, widget Contador | Prova legível para Google e IAs | Leve: some a animação de contagem |
| 5 | **FAQPage nos 5 posts com FAQ sem schema** (Gestão de ambientes Datasphere, Knowledge Graph, Business AI Platform, Joule Work, Governança BDC); conferir os cases | Widget HTML com JSON-LD | +2 pts por página | Não |
| 6 | **Alts:** começar pela BDC (6/6) e pela home (8/29) | Mídia > Biblioteca > Texto alternativo | +2 pts por página | Não |
| 7 | **Correções rápidas:** "Analitycs" > "Analytics" no menu; "BLog" > "Blog"; botão "Fale com nossos especialistas" > /contato/ | Aparência > Menus; Elementor | Credibilidade e conversão | Mínimo |
| 8 | **Reescrever a página BDC** em rascunho: definição de 40-60 palavras sob H2 em pergunta, as 5 subperguntas que faltam, prêmio + Gold, case, links para os posts de BDC, FAQ + FAQPage, CTA | `/pagina-solucao` > rascunho no WordPress | De 28 para ~75/80 | Sim (rascunho) |
| 9 | **Home nova** em rascunho: hero BDC + prêmio, bloco "O que a Solveplan faz?", setores em texto, FAQ | Elementor > cópia em rascunho | De 35 para ~70/80 | Sim (rascunho) |
| 10 | **PageSpeed:** medir home e BDC em pagespeed.web.dev e colar os scores | pagespeed.web.dev | Fecha a nota de performance | Não |

Os itens 1 a 7 não mudam o visual (ou mudam muito pouco) e levam cerca de 2 a 3 horas no painel. Os itens 8 e 9 são conteúdo novo e passam pela aprovação em rascunho.

**Antes de aplicar qualquer item:** backup manual na Hostinger e, se for pela API, desmarcar a opção do Wordfence só durante o trabalho. Desde 13/10, o firewall do Wordfence bloqueia o `rankmath/v1/updateMeta` (403), então os itens de Rank Math vão pelo painel ou exigem liberar essa regra antes.

---

## Arquivos

- `site-2026-10-22-varredura.csv` — as 108 URLs, com H1, title, description, schema, FAQPage, imagens sem alt e os problemas de cada uma
- `home-2026-10-22-score.csv` e `sap-business-data-cloud-2026-10-22-score.csv` — scorecards v2
- Base de comparação: `site-2026-09-25-varredura.csv` e `site-2026-09-25-analise.md`

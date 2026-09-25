# Análise do site solveplan.com
*25/09/2026. Fontes: HTML público, sitemap (91 URLs), REST API do WordPress (somente leitura) e comparação com a auditoria de 28/07/2026*

---

## Resumo executivo

O site tem boa base técnica: servidor rápido (TTFB de ~80 ms com cache LiteSpeed), Rank Math, sitemap e tags de rastreamento (GTM, HubSpot, LinkedIn Insight) instalados. O blog de BDC está forte. O problema está em duas frentes:

1. **Mensagem desalinhada com a estratégia.** A home não fala de SAP BDC nem do prêmio de Melhor Parceiro SAP BDC 2026 LATAM, que é o principal diferencial hoje. BDC aparece só no menu.
2. **A página que recebe 65% do tráfego (/sap-business-data-cloud/) é a mais fraca em conversão.** São 302 palavras de texto genérico, sem prova, sem case, sem FAQ e com um CTA só. Isso explica boa parte da rejeição de 78,8%.

Os problemas técnicos de SEO (sem H1, schema errado, alts vazios) **já tinham sido apontados em julho e continuam lá**. A /sap-datasphere/ foi corrigida e mostra que o modelo funciona.

**Score da home: 26/100** (SEO 19/40 · Performance não verificada · AEO 0/25 · GEO 7/15)

---

## 1. Mensagem e conversão (maior impacto em pipeline)

| # | Achado | Evidência | O que fazer |
|---|--------|-----------|-------------|
| 1 | Home não vende BDC | Hero: "Planejamento, Analytics e Consolidação". BDC só no menu e no rodapé | Hero com BDC + selo "Melhor Parceiro SAP BDC 2026 – América Latina" + CTA "Agende um diagnóstico BDC" |
| 2 | Prêmio e selo Gold invisíveis | "Gold" aparece só no schema; o prêmio não aparece na home nem na página BDC | Faixa de prova social logo abaixo do hero: prêmio 2026, prêmio 2025, SAP Gold e logos de clientes |
| 3 | Página BDC rasa | 302 palavras, texto de catálogo SAP ("solução SaaS abrangente…"), sem "por que a Solveplan" | Reescrever com `/pagina-solucao`: dor → abordagem Solveplan → case (Klabin/Datasphere) → FAQ → CTA |
| 4 | Números divergentes | Site: 150+ empresas / **300+** projetos / **68+** especialistas. Contexto interno: 150+ / **390+** / **60+** | Confirmar os números oficiais e atualizar os contadores |
| 5 | Contadores aparecem como "0+" para robôs | O HTML entrega "0 +" e o JavaScript anima depois. Google e IAs podem ler "0+ empresas" | Pôr o número real como texto (ou usar o valor inicial = valor final no widget Contador) |
| 6 | CTA quebrado | "Fale com nossos especialistas" na home leva para /aceleradores/, não para contato | Apontar para /contato/ ou para uma LP de diagnóstico |
| 7 | Página de contato fraca | 72 palavras, sem H1. Horário "8h–18h e 13h–18h30" é confuso | Corrigir o horário, dizer o que acontece depois do envio e incluir um agendamento direto (HubSpot Meetings) |
| 8 | Sem landing pages para mídia | Anúncios caem em páginas institucionais | Prioridade H2 já prevista: LP BDC dedicada para LinkedIn/Google Ads |

---

## 2. SEO técnico (site todo)

| Problema | Escala | Como corrigir |
|----------|--------|---------------|
| **Páginas sem H1** | 28 de 31 páginas institucionais (home, BDC, serviços, contato, sobre, todos os aceleradores) | No Elementor, trocar a Tag HTML do título principal de cada página para **H1** (template: /sap-datasphere/) |
| **Schema BlogPosting + Person em páginas** | Todas as páginas; o "autor" é o usuário `felippeemanoel` | Rank Math → Títulos e Meta → Páginas → Tipo de Schema: **Nenhum** (mantém WebPage) |
| addressCountry = "55" no schema Organization | Site todo | Rank Math → Títulos e Meta → Local SEO → País: **BR** |
| Lixo indexado no sitemap | /banner/banner-2, /banner/banner-3, /video-aceleradores/video-teste/, /midia-em-acelerador/analytics/, /cases-abertos/ | Rank Math → Títulos e Meta → cada tipo de post → **noindex** e remover do sitemap |
| Descriptions fracas ou duplicadas | Contato ("CONTATO"), Sobre ("Sobre Nós"), Analytics ("Analytics"), Blog (vazia). /servicos/ tem a mesma description da página BDC | Reescrever no Rank Math (120–155 caracteres) |
| Description copiada errada | Post "Clean Core" usa a description do post de agronegócio | Reescrever |
| Titles em CAIXA ALTA | SAP BUSINESS DATA CLOUD, FÁBRICA DE BI, CONSOLIDAÇÃO CONTÁBIL etc. | Caixa normal + keyword: "Consultoria SAP Business Data Cloud (BDC) \| Solveplan" |
| Titles longos (>65) | 41 URLs, quase todas do blog, por causa do sufixo " - Solveplan" | Tirar o sufixo nos posts ou encurtar os títulos SEO |
| Possível canibalização | `governanca-dados-financeiros-sap-bdc` × `sap-business-data-cloud-governanca-financeira`; slugs com "-2" (posts duplicados) | Fundir ou diferenciar e redirecionar (301) |
| Imagens sem alt | Página BDC: 8 de 8; home: 10 de 31 | Preencher na Biblioteca de Mídia |
| Sem WebP | 75 imagens na home, todas JPG/PNG (o plugin Image Optimization está ativo) | Ativar a conversão WebP no plugin |
| og:image pequena | 561×374, alt "Home" | Imagem 1200×630 com a marca e o selo do prêmio |
| Erros de digitação | Menu "Analitycs", rodapé "SAP DataSphere", "SolvePlan" × "Solveplan" nas notícias | Corrigir |

**Performance:** a cota da API do PageSpeed estava esgotada hoje, então esse item não foi verificado. O servidor responde bem, mas a home carrega 27 scripts e 26 folhas de estilo (Elementor + plugins). Rodar em pagespeed.web.dev.

---

## 3. Segurança (verificado com acesso de leitura)

| Risco | O que fazer |
|-------|-------------|
| **A Application Password foi compartilhada no chat** | Revogar agora: Usuários → administrador → Senhas de aplicativo → Revogar. Criar outra só quando precisar |
| `/wp-json/wp/v2/users` expõe publicamente os logins (`administrador`, `felippeemanoel`, `solveplan`) | Bloquear o endpoint de usuários para visitantes não logados (plugin de segurança ou regra no LiteSpeed) |
| `xmlrpc.php` aberto (responde 200) | Desativar, porque é vetor de força bruta |
| Nenhum plugin de segurança ou backup visível | Confirmar com a hospedagem se há backup diário. Se não houver, instalar UpdraftPlus + Wordfence (ver `/wordpress`) |

Plugins ativos (13) e atualizados: ACF Pro, Elementor/Pro 4.2, Rank Math, LiteSpeed Cache, Site Kit, HubSpot (leadin), Image Optimization, Insert Headers and Footers, Duplicate Page, Cookie Law Info, WP Consent API, Pojo Accessibility. WordPress 6.8.9.

---

## 4. O que está funcionando (usar como modelo)

- **/sap-datasphere/**: H1 em forma de pergunta ("O que é o SAP Datasphere?"), title de 60 caracteres e description de 157. É o padrão a replicar nas páginas de solução.
- **Blog BDC recente** (Knowledge Core, consumo BDC, Joule, SAP + Anthropic, SAPPHIRE 2026): temas atuais e títulos bons para busca e para IA.
- **Páginas de evento 2026**: titles curtos e descriptions com data e horário.
- **Cases com números** (Zilor 6 meses, M. Dias Branco −96%, Lins −90%): ótima prova, mas escondida. Merecem destaque na home e na página BDC.

---

## 5. Home: correções prontas

**Title (57):** `Consultoria SAP BDC, Analytics e Planejamento | Solveplan`

**Meta description (144):** `Parceira SAP Gold e Melhor Parceiro SAP Business Data Cloud 2026 na América Latina. Analytics, planejamento e consolidação com dados confiáveis.`

**H1 (hero, trocar a tag no Elementor):** `Consultoria SAP em dados, analytics, planejamento e consolidação`

**Bloco de snippet (H2 + 54 palavras):**
> **O que a Solveplan faz?**
> A Solveplan é uma consultoria SAP especializada em dados, analytics, planejamento financeiro e consolidação. Parceira SAP Gold e eleita Melhor Parceiro SAP Business Data Cloud 2026 na América Latina, já entregou mais de 390 projetos para mais de 150 empresas de médio e grande porte, com SAP BDC, SAP Datasphere e SAP Analytics Cloud.

*(confirmar 390 × 300 antes de publicar)*

**FAQ (widget Acordeão, perguntas em H3):**
1. **O que é SAP Business Data Cloud (BDC)?** Plataforma SaaS da SAP que unifica dados SAP e não-SAP (Datasphere, SAP Analytics Cloud, BW e SAP Databricks) numa camada governada para analytics, planejamento e IA.
2. **Qual a diferença entre SAP Datasphere e SAP BDC?** O Datasphere é a camada de dados. O BDC é o pacote que junta o Datasphere a SAC, BW, Databricks e aos data products gerenciados pela SAP.
3. **Quanto tempo leva um projeto de SAP Analytics Cloud?** Nos nossos cases, entre 3 e 10 meses: Matrix Energia em 3, Zilor em 6 e M. Dias Branco em 10.
4. **Como sair das planilhas no planejamento financeiro?** Levando o orçamento para o SAP Analytics Cloud Planning integrado ao ERP. A Zilor eliminou as planilhas em 6 meses.

**FAQPage JSON-LD** (widget HTML do Elementor, no fim da página):
```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"O que é SAP Business Data Cloud (BDC)?","acceptedAnswer":{"@type":"Answer","text":"Plataforma SaaS da SAP que unifica dados SAP e não-SAP (Datasphere, SAP Analytics Cloud, BW e SAP Databricks) numa camada governada para analytics, planejamento e IA."}},
{"@type":"Question","name":"Qual a diferença entre SAP Datasphere e SAP BDC?","acceptedAnswer":{"@type":"Answer","text":"O Datasphere é a camada de dados. O BDC é o pacote que junta o Datasphere a SAC, BW, Databricks e aos data products gerenciados pela SAP."}},
{"@type":"Question","name":"Quanto tempo leva um projeto de SAP Analytics Cloud?","acceptedAnswer":{"@type":"Answer","text":"Nos cases da Solveplan, entre 3 e 10 meses: Matrix Energia em 3, Zilor em 6 e M. Dias Branco em 10."}},
{"@type":"Question","name":"Como sair das planilhas no planejamento financeiro?","acceptedAnswer":{"@type":"Answer","text":"Levando o orçamento para o SAP Analytics Cloud Planning integrado ao ERP. A Zilor eliminou as planilhas em 6 meses."}}]}
</script>
```

**Ganho potencial na home:** +52 pontos sem performance (→ 78/100), ou até 98/100 se o PageSpeed estiver bom.

---

## Ordem sugerida de execução

| Semana | Ação | Por quê |
|--------|------|---------|
| Hoje | Revogar a Application Password; bloquear o endpoint de usuários e o xmlrpc | Risco de segurança aberto |
| 1 | H1 + schema + noindex do lixo + titles/descriptions (site todo) | ~2 h no painel e corrige 80% do SEO técnico |
| 1 | Home: hero BDC + prêmio + CTA certo + snippet + FAQ | Alinha a vitrine com a prioridade comercial |
| 2–3 | Reescrever a página BDC (`/pagina-solucao`) + LP para ads | 65% do tráfego com 78,8% de rejeição: maior alavanca de pipeline |
| 3 | WebP, og:image, alts, typos | Acabamento |
| Depois | Rodar `/auditoria-seo` de novo na BDC e na home | Medir a evolução |

Arquivos desta análise: `home-2026-09-25-score.csv`, `home-2026-09-25-plano-acao.csv`, `site-2026-09-25-varredura.csv` (91 URLs com os problemas de cada uma).

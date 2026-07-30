---
name: search-console-ratos
description: Consulta dados do Google Search Console via SDK oficial (google-api-python-client). Le sites, sitemaps, performance de busca organica (cliques, impressoes, CTR, posicao media) por query, pagina, pais, dispositivo e data. Inspeciona status de indexacao de URLs especificas (cobertura, canonical, mobile usability, rich results). Use quando o usuario mencionar search console, gsc, busca organica, indexacao, cobertura, posicao media no google, cliques organicos, impressoes organicas, ctr organico, sitemap, url inspection, rich results, core web vitals, paginas nao indexadas, erros de crawl. Tambem dispara com /search-console-ratos setup.
---

# Search Console Ratos

Skill completa para consulta de dados do Google Search Console (GSC) via SDK oficial (`google-api-python-client`, APIs `webmasters` v3 e `searchconsole` v1). Traz performance de busca organica (cliques, impressoes, CTR, posicao media) por query, pagina, pais, dispositivo e data, alem de inspecao de indexacao por URL.

**IMPORTANTE: Esta skill e o braco de execucao (leitura) do GSC. Para aplicar correcoes no site com base nos achados, usar em conjunto com a skill `wordpress` (edicao via REST API) — ver secao "Do diagnostico a correcao" abaixo.**

**IMPORTANTE: Esta skill e separada de `ga4-ratos` porque respondem perguntas diferentes: GA4 mostra o que o visitante fez depois de chegar no site; GSC mostra como o Google enxerga e posiciona o site na busca (antes do clique). Usar os dois juntos pra diagnostico completo de SEO.**

**IMPORTANTE: NUNCA usar MCPs. Esta skill usa SOMENTE os scripts Python locais.**

## Setup (primeira vez)

Quando o usuario pedir para configurar, rodar setup, ou for a primeira vez usando a skill, o Claude deve guiar o setup interativo:

### 1. Verificar dependencias

```bash
pip3 install google-api-python-client google-auth
```

### 2. Verificar .env

Checar se existe `~/.claude/skills/search-console-ratos/.env`. Se NAO existir, criar com o template:

```
# Search Console Ratos — Configuracao
# Os scripts leem este arquivo automaticamente. NAO precisa adicionar ao ~/.zshrc.

# OBRIGATORIO: Site URL cadastrada no GSC
# Formato "URL-prefix": "https://solveplan.com/" (com barra final)
# Formato "Dominio": "sc-domain:solveplan.com" (cobre http/https/www/subdominios)
GSC_SITE_URL=""

# AUTH — Escolha UM dos tres modos:

# MODO 1: Service Account (recomendado)
# Baixe o JSON da service account no Google Cloud Console
# e coloque o path completo aqui. IMPORTANTE: depois de criar a service account,
# adicione o email dela (algo@projeto.iam.gserviceaccount.com) como "Usuario"
# na propriedade dentro do Search Console (Configuracoes > Usuarios e permissoes > Adicionar usuario).
# Sem esse passo a API retorna 403 mesmo com credenciais validas.
GSC_CREDENTIALS_PATH=""

# MODO 2: OAuth2 proprio
# GSC_CLIENT_ID=""
# GSC_CLIENT_SECRET=""
# GSC_REFRESH_TOKEN=""

# MODO 3: Compartilhado — deixe em branco e o script busca automaticamente
# nas credenciais OAuth ja configuradas em ga4-ratos ou google-ads-ratos
# (a conta Google usada la precisa ter acesso a propriedade no GSC).
```

**Modo 1 (Service Account) — recomendado:** Cria uma service account no Google Cloud Console (mesmo projeto usado pra GA4/Google Ads, se houver), habilita a API "Google Search Console API", baixa o JSON, coloca o path em `GSC_CREDENTIALS_PATH` e **adiciona o email da service account como usuario na propriedade do Search Console** (isso e obrigatorio — diferente do GA4, o GSC nao usa IAM do GCP, usa a lista de usuarios do proprio Search Console).

**Modo 2/3 (OAuth2):** Se o usuario ja usa OAuth2 em `ga4-ratos` ou `google-ads-ratos` com a conta que tem acesso ao Search Console, os scripts reusam essas credenciais automaticamente. So funciona se a mesma conta Google tiver acesso a propriedade no GSC (verificar em Search Console > Configuracoes > Usuarios e permissoes).

### 3. Validar acesso

Rodar `read.py sites` para confirmar que a autenticacao funciona e listar as propriedades acessiveis.

### 4. Cadastro de sites (contas.yaml) — SETUP CONVERSACIONAL

Depois que o `.env` estiver preenchido e `read.py sites` funcionar, o Claude DEVE proativamente guiar o cadastro:

1. Mostrar a lista de sites retornada por `read.py sites`
2. Perguntar ao usuario: "Qual desses e o site principal? Quer que eu ja preencha o contas.yaml?"
3. Preencher o `contas.yaml` automaticamente com nome do cliente + site_url
4. Perguntar: "Quer cadastrar mais algum site?"

## Cadastro de sites (contas.yaml)

**Arquivo:** `~/.claude/skills/search-console-ratos/contas.yaml`

Antes de executar qualquer operacao, o Claude DEVE ler este arquivo para resolver nomes de clientes para site URLs.
Quando o usuario disser "search console da Solveplan" ou "posicao das paginas do site", consultar o contas.yaml
para obter a site_url do cliente.

Se o site nao estiver cadastrado, perguntar os dados e oferecer para adicionar ao arquivo.

## Como usar

Todos os scripts estao em `~/.claude/skills/search-console-ratos/scripts/`. O padrao e:

```
python3 <script>.py <subcomando> [argumentos]
```

O Claude deve interpretar o pedido do usuario e executar o script correto via Bash.

---

## Referencia rapida de operacoes

### Leitura (read.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `sites` | Lista sites/propriedades acessiveis | `read.py sites` |
| `sitemaps` | Lista sitemaps cadastrados, com erros/warnings | `read.py sitemaps --site https://solveplan.com/` |
| `sitemap-submit` | Envia/reenvia um sitemap pro Google reprocessar | `read.py sitemap-submit --feedpath sitemap_index.xml` |

### Relatorios (reports.py) — CORE DA SKILL

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `queries` | Termos de busca com clicks, impressions, CTR, posicao media | `reports.py queries --days 28 --limit 25` |
| `pages` | Paginas com clicks, impressions, CTR, posicao media | `reports.py pages --days 28 --limit 25` |
| `page-queries` | Queries que trazem trafego pra uma pagina especifica (diagnostico por pagina) | `reports.py page-queries --page https://solveplan.com/blog/artigo --days 90` |
| `countries` | Breakdown por pais | `reports.py countries --days 28` |
| `devices` | Breakdown por dispositivo (desktop, mobile, tablet) | `reports.py devices --days 28` |
| `dates` | Evolucao diaria de clicks/impressions/CTR/posicao | `reports.py dates --days 90` |
| `search-appearance` | Breakdown por tipo de aparencia na busca (rich results, etc) | `reports.py search-appearance --days 28` |
| `custom` | Query custom com dimensoes livres e filtro | `reports.py custom --dimensions query,page --filter-dimension page --filter-expression /blog/ --filter-operator contains` |
| `compare` | Compara periodo atual vs anterior (clicks, impressions, CTR, posicao) | `reports.py compare --days 28` |

Parametros comuns:

| Parametro | O que faz | Exemplo |
|---|---|---|
| `--site` | Site URL do GSC | `https://solveplan.com/` |
| `--days` | Quantidade de dias pra tras (a partir de hoje, com 2 dias de delay do GSC) | `28`, `90`, `365` |
| `--start-date` / `--end-date` | Periodo explicito (YYYY-MM-DD) | `2026-06-01` / `2026-06-30` |
| `--limit` | Limite de linhas | `50` |

### Inspecao de URL (inspect.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `url` | Status de indexacao, canonical, cobertura, mobile usability, rich results de uma URL | `inspect.py url --url https://solveplan.com/blog/artigo` |

---

## Regras de seguranca

O Claude DEVE seguir estas regras ao executar operacoes:

1. **Leitura por padrao** — os comandos de `reports.py`, `read.py sites/sitemaps` e `inspect.py` sao somente leitura. O unico comando que escreve algo no GSC e `read.py sitemap-submit` (reenvio de sitemap) — usar so quando o usuario pedir explicitamente
2. **Nunca hardcodar site URLs ou credenciais** — sempre usar env vars ou contas.yaml
3. **Respeitar rate limits** — se receber erro de quota, aguardar 60 segundos antes de tentar novamente
4. **Sempre especificar o periodo e o site** ao mostrar metricas — dados de GSC tem defasagem de ~2-3 dias
5. **NUNCA usar MCPs** — esta skill usa SOMENTE os scripts Python locais

---

## Do diagnostico a correcao — GSC + WordPress

Sim, da pra fechar o ciclo completo: **diagnosticar no Search Console e aplicar a correcao direto no WordPress**, sem precisar do usuario abrir o painel. O que pode ser feito direto por API e o que precisa de acao manual:

### O que dá pra corrigir direto via API (sem o usuario tocar no painel)

| Achado no GSC | Correcao aplicavel via API | Como |
|---|---|---|
| Titulo/meta description ruins (CTR baixo em pagina com posicao boa) | Reescrever SEO title e meta description | Endpoint Rank Math `POST /wp-json/rankmath/v1/updateMeta` — ver [[reference-wordpress-rankmath-api]] |
| Conteudo desatualizado ou raso numa pagina que rankeia mas nao converte | Editar o conteudo da pagina/post | `PATCH /wp-json/wp/v2/{posts\|pages\|CPT}/{id}` |
| Falta de link interno (pagina orfa, poucas queries variadas) | Adicionar links internos no corpo do conteudo | Editar `content.rendered`/`content` via `wp/v2` |
| Alt text ausente em imagens | Adicionar alt text | `wp/v2/media/{id}` (campo `alt_text`) |
| Sitemap com erro ou desatualizado | Reenviar sitemap | `read.py sitemap-submit` |

**Fluxo recomendado quando o usuario pedir "corrige com base no Search Console":**
1. Rodar `reports.py pages` e `reports.py queries` (ou `page-queries` pra uma URL especifica) pra achar o problema: posicao boa + CTR baixo = titulo/meta fraco; impressao alta + posicao ruim = conteudo fraco pra intencao de busca; `inspect.py url` pra confirmar que a pagina esta indexada e sem erro de cobertura
2. Propor a correcao especifica (novo title, nova meta description, novo trecho de conteudo, alt text) e mostrar pro usuario antes de aplicar
3. Aplicar via API do WordPress (usar as credenciais e endpoints documentados na skill `wordpress` e na memoria `reference-wordpress-rankmath-api`)
4. Sugerir reinspecionar a URL depois de 1-2 dias com `inspect.py url` pra ver se o status mudou

### O que NAO da pra corrigir via API — precisa de acao manual no painel/plugin

- **Performance/Core Web Vitals** (LCP, CLS, INP) — depende de plugin de cache, otimizacao de imagem, hospedagem. Ver skill `wordpress` secao 1
- **Erros de crawl/robots.txt/redirecionamento** — mudanca de configuracao de servidor ou plugin (Redirection), nao e um campo de post
- **Problemas de indexacao por bloqueio no `robots.txt` ou `noindex` de tema/plugin** — exige checar configuracao global, nao so o post
- **Mobile usability** — normalmente e o tema/CSS, nao o conteudo do post
- **Migracao de dominio/HTTPS/estrutura de URL** — mudanca estrutural, requer planejamento e redirecionamentos 301 em massa

Quando o achado cair nessa segunda lista, o Claude deve apontar o problema com os dados do GSC e direcionar pra skill `wordpress` (checklist correspondente) em vez de tentar aplicar via API.

## Fluxos comuns

### Diagnostico geral de SEO organico

1. `reports.py compare --days 28` — cresceu ou caiu nos ultimos 28 dias vs 28 anteriores?
2. `reports.py queries --days 28 --limit 30` — quais termos trazem trafego
3. `reports.py pages --days 28 --limit 20` — quais paginas performam melhor/pior
4. `read.py sitemaps` — sitemap sem erro?

### Pagina com trafego caindo

1. `reports.py page-queries --page <url> --days 90` — quais queries perderam posicao/impressao
2. `inspect.py url --url <url>` — ainda esta indexada? algum erro de cobertura?
3. Comparar com `ga4-ratos reports.py landing-pages` pra ver se o problema e so ranking ou tambem conversao

### Oportunidade de CTR (posicao boa, poucos cliques)

1. `reports.py queries --days 28 --limit 50` — filtrar mentalmente por posicao media baixa (boa) e CTR baixo
2. `reports.py custom --dimensions query,page --filter-dimension page --filter-expression <url> --filter-operator equals` — cruzar queries com a pagina certa
3. Propor novo title/meta description e aplicar via Rank Math API (ver secao acima)

### Antes de publicar conteudo novo

1. `reports.py queries --days 90` — ver quais termos ja trazem trafego pro tema, evitar canibalizacao
2. Depois de publicar: `read.py sitemap-submit` (se o sitemap nao atualizar sozinho) + `inspect.py url` pra acompanhar a indexacao

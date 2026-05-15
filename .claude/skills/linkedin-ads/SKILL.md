---
name: linkedin-ads
description: Gerencia campanhas LinkedIn Ads via Marketing API. Le contas, grupos de campanha, campanhas e criativos. Analisa performance (impressoes, cliques, CTR, CPL, leads). Cria, edita, pausa e arquiva objetos. Gera copy e briefing visual para anuncios. Planeja segmentacao por cargo, setor, empresa e Matched Audiences. Use quando o usuario mencionar linkedin ads, campanhas linkedin, sponsored content, message ads, lead gen linkedin, segmentacao linkedin, performance linkedin, criativos linkedin, budget linkedin, CPL linkedin. Tambem dispara com /linkedin-ads setup.
---

# LinkedIn Ads

Skill completa para gestao de LinkedIn Ads via Marketing API REST. Executa operacoes de leitura, analytics, criacao e edicao de campanhas. Tambem gera copy e planejamento de segmentacao sem precisar da API.

## Setup (primeira vez)

Quando o usuario pedir para configurar, rodar setup, ou for a primeira vez usando a skill:

### 1. Verificar dependencias

```bash
pip3 install requests python-dotenv
```

### 2. Criar o app LinkedIn

1. Acessar https://www.linkedin.com/developers/apps/new
2. Criar app associado a uma Company Page
3. Em "Products", solicitar acesso a **Marketing Developer Platform**
4. Em "Auth", copiar **Client ID** e **Client Secret**

### 3. Criar .env

Rodar o check para criar o template automaticamente:

```bash
python3 .claude/skills/linkedin-ads/scripts/setup.py check
```

Preencher `LINKEDIN_CLIENT_ID` e `LINKEDIN_CLIENT_SECRET` no arquivo gerado.

### 4. Gerar access token

```bash
python3 .claude/skills/linkedin-ads/scripts/setup.py oauth
```

Isso abre o browser, o usuario autoriza, e o token e salvo automaticamente.

### 5. Testar conexao

```bash
python3 .claude/skills/linkedin-ads/scripts/setup.py test
```

### Subcomandos do setup.py

| Subcomando | O que faz |
|---|---|
| `check` | Verifica dependencias e variaveis do .env |
| `oauth` | Gera access token via OAuth2 (abre browser) |
| `refresh` | Renova o access token usando o refresh token |
| `test` | Testa conexao listando contas acessiveis |

## Cadastro de contas (contas.yaml)

**Arquivo:** `.claude/skills/linkedin-ads/contas.yaml`

Antes de qualquer operacao, ler este arquivo para resolver nomes para IDs.
Se o cliente nao estiver cadastrado, perguntar os dados e oferecer para adicionar.

Apos setup bem-sucedido, guiar o cadastro conversacional:
1. Rodar `read.py accounts` para listar contas
2. Perguntar qual e a conta principal
3. Preencher o contas.yaml com nome e account_id

## Como usar

Todos os scripts estao em `.claude/skills/linkedin-ads/scripts/`. O padrao e:

```
python3 <script>.py <subcomando> [argumentos]
```

---

## Referencia rapida de operacoes

### Leitura (read.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `accounts` | Lista contas de anuncio | `read.py accounts` |
| `campaign-groups` | Grupos de campanha da conta | `read.py campaign-groups --account-id 123` |
| `campaigns` | Campanhas da conta ou grupo | `read.py campaigns --account-id 123` |
| `creatives` | Criativos de uma campanha | `read.py creatives --campaign-id 456` |
| `targeting` | Facetas de segmentacao | `read.py targeting --facet urn:li:adTargetingFacet:titles` |

### Insights (insights.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `account` | KPIs totais da conta | `insights.py account --account-id 123 --since 2026-04-01 --until 2026-04-30` |
| `campaign` | Metricas por campanha | `insights.py campaign --account-id 123` |
| `creative` | Metricas por criativo | `insights.py creative --campaign-id 456` |
| `daily` | Evolucao diaria | `insights.py daily --account-id 123 --since 2026-04-01 --until 2026-04-30` |

Parametros de data: `--since YYYY-MM-DD --until YYYY-MM-DD` (padrao: ultimos 30 dias)

### Criacao (create.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `campaign-group` | Cria grupo PAUSED | `create.py campaign-group --account-id 123 --name "BDC-Q2" --objective LEAD_GENERATION` |
| `campaign` | Cria campanha PAUSED | `create.py campaign --account-id 123 --group-id 456 --name "BDC-CIO" --type SPONSORED_UPDATES --format SINGLE_IMAGE --objective LEAD_GENERATION --budget 50 --bid 8` |
| `creative` | Associa post organico como criativo | `create.py creative --campaign-id 456 --post-urn urn:li:ugcPost:123` |

**IMPORTANTE:** Todos os objetos sao criados com status **PAUSED**. Ativar manualmente apos revisar.

### Edicao (update.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `campaign-group` | Status ou nome do grupo | `update.py campaign-group --group-id 123 --status ACTIVE` |
| `campaign` | Status, budget ou nome | `update.py campaign --campaign-id 456 --status ACTIVE --budget 80` |
| `creative` | Status do criativo | `update.py creative --creative-id 789 --status ACTIVE` |

### Arquivamento (delete.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `campaign` | Arquiva campanha | `delete.py campaign --campaign-id 456` |
| `campaign-group` | Arquiva grupo | `delete.py campaign-group --group-id 123` |
| `creative` | Arquiva criativo | `delete.py creative --creative-id 789` |

Nota: LinkedIn nao permite delecao fisica — objetos sao arquivados.

---

## Copy e briefing visual (sem API)

Quando o usuario pedir copy para LinkedIn Ads, gerar sem precisar da API:

### Formato Single Image Ad

```
HEADLINE (max 70 caracteres):
[headline]

TEXTO INTRODUTORIO (max 150 caracteres para preview, 600 total):
[corpo]

CTA: [Learn More | Download | Sign Up | Register | Contact Us | Apply Now]
URL de destino: [url]
```

### Criativo no Canva (via MCP)

Quando o usuario pedir para criar o design do anuncio, usar o Canva MCP diretamente:

1. Perguntar se quer usar brand kit Solveplan (sempre recomendar que sim)
2. Se sim, chamar `list-brand-kits` para listar e o usuario selecionar
3. Chamar `search-brand-templates` para ver se ha template de ad disponivel
4. Se houver template adequado → `create-design-from-brand-template`
5. Se nao houver → `generate-design` com os parametros abaixo:

```
design_type: "facebook_post" (1200x627 — Single Image Ad)
             "instagram_post" (1080x1080 — Square Ad)
query: "[headline do anuncio] — anuncio LinkedIn B2B [tema da campanha],
        fundo [cor Solveplan], logo no canto, texto destaque, visual executivo"
brand_kit_id: [ID do brand kit selecionado]
```

6. Mostrar as opcoes geradas e perguntar qual o usuario prefere
7. Confirmar com `create-design-from-candidate` para salvar no Canva do usuario

### Briefing visual (fallback sem Canva)

Se o usuario preferir criar manualmente:

```
Formato: 1200x627px (landscape) ou 1080x1080px (quadrado)
Fundo: [cor da paleta Solveplan]
Elemento visual principal: [imagem/icone/grafico]
Headline no criativo: [texto curto — max 40 caracteres]
Logo: canto inferior direito
CTA visual: botao destacado
```

### Variantes A/B

Sempre gerar 2 variantes:
- **Variante A** — foco na dor/problema do ICP
- **Variante B** — foco no resultado/beneficio

---

## Planejamento de segmentacao

Quando o usuario pedir segmentacao, sugerir sem API:

### ICP Solveplan (referencia)

- **Cargos:** CIO, CFO, Controller, Head de Dados, Head de BI, COO, CHRO
- **Senioridade:** Director, VP, C-Level
- **Setores:** Manufacturing, Financial Services, Retail, Healthcare, Technology
- **Tamanho:** 500-10.000 funcionarios (Mid-Market a Enterprise)
- **Localizacao:** Brasil

### Matched Audiences

- **Lista de contas:** upload de CSV com domínios das contas-alvo (ABM)
- **Website Retargeting:** Insight Tag no site para retargetar visitantes
- **Contact List:** upload de emails de leads do CRM

---

## Fluxos comuns

### Criar campanha de Lead Generation

1. `create.py campaign-group --objective LEAD_GENERATION`
2. `create.py campaign --type SPONSORED_UPDATES --format SINGLE_IMAGE --objective LEAD_GENERATION`
3. Gerar copy (2 variantes A/B) — ver secao Copy
4. **Criar criativo no Canva** — usar fluxo Canva MCP (ver secao acima)
5. Criar post organico no LinkedIn com a imagem exportada do Canva, copiar URN
6. `create.py creative --post-urn urn:li:ugcPost:XXX`
7. Validar: `read.py campaigns`, `read.py creatives`
8. `update.py campaign --status ACTIVE` (ativar grupo e campanha juntos)

### Auditoria de performance

1. `insights.py account --since YYYY-MM-DD --until YYYY-MM-DD`
2. `insights.py campaign` — comparar campanhas
3. `insights.py creative --campaign-id XXX` — identificar criativos que performam
4. `insights.py daily` — identificar tendencias

### Renovar token expirado

```bash
python3 .claude/skills/linkedin-ads/scripts/setup.py refresh
```

---

## Regras de seguranca

1. **Criar sempre PAUSED** — nunca criar com status ACTIVE diretamente
2. **Confirmar antes de arquivar** — perguntar ao usuario antes de executar delete.py
3. **Confirmar antes de ativar** — perguntar antes de mudar para ACTIVE
4. **Ativar todos os niveis** — ao ativar campanha, ativar tambem grupo e criativos
5. **Nunca hardcodar tokens** — sempre usar .env
6. **Token expirado** — se receber 401, orientar a rodar `setup.py refresh`
7. **MCPs permitidos somente para Canva** — design de criativos usa o Canva MCP; todo o resto usa scripts Python locais

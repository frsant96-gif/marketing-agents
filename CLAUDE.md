# CLAUDE.md

# Solveplan — Claude Code OS

## O que é esse workspace
Workspace de marketing e vendas da Solveplan — consultoria SAP especializada em dados, analytics, planejamento financeiro e consolidação. Usado por Fran (Francielle Beline) para criar conteúdo, propostas, materiais comerciais e planejar eventos e campanhas com foco em geração de pipeline para SAP Business Data Cloud (BDC).

**Estrutura de pastas:**
```
_contexto/          — contexto do negócio (lido no início de cada sessão)
marca/              — guia de identidade visual e logo
dados/              — drop zone pra arquivos pra análise (CSV, XLSX, PDF, TXT)
marketing/          — conteúdo, carrosséis, posts, artigos
comercial/          — propostas e materiais de vendas
eventos/            — planos de eventos e ações de marketing
templates/skills/   — templates base pra criar novas skills
templates/ferramentas/catalogo.md — APIs, CLIs e MCPs disponíveis
.claude/skills/     — skills personalizadas criadas pra esse negócio
```

## Sobre o negócio
A Solveplan ajuda empresas de médio e grande porte a transformar dados em ativos estratégicos, com soluções SAP para analytics, planejamento financeiro e consolidação. Parceira SAP Gold na América Latina, com +200 soluções entregues e +90 clientes atendidos. Foco atual: vender SAP Business Data Cloud (BDC).

## O que mais fazemos aqui
- Criação de conteúdo para LinkedIn e redes sociais (posts, carrosséis)
- Propostas comerciais e materiais de vendas
- Planejamento de eventos e ações de marketing (skill `/planejar-evento`)
- Emails profissionais para prospects e clientes
- Análise de dados de campanhas e resultados

## Clientes e contexto
Consultoria B2B. Atende CIOs, CFOs, controllers, heads de dados/BI, COO, CHRO em empresas de médio e grande porte.

## Tom de voz
Direto, orientado a negócio, técnico quando necessário mas sem jargão vazio. Posicionamento de autoridade sem hype. Sempre conectar com a dor real do cliente e gerar ação. Evitar: "transformação digital" genérico, promessas exageradas, conteúdo superficial.

## Ferramentas conectadas
SAP Datasphere, SAP Analytics Cloud, SAP BTP, SAP S/4HANA, Power BI, aceleradores próprios

---

## Skills personalizadas

| Skill | Descrição |
|-------|-----------|
| `/planejar-evento` | Planeja evento do zero com framework de 26 passos — gera plano completo em `eventos/` |
| `/post-social` | Cria copy por formato (post único, imagem, vídeo, carrossel) — salva em `marketing/posts/` |
| `/artigo-blog` | Briefing → artigo completo com SEO/AEO/GEO + metadados + post LinkedIn — salva em `marketing/blog/` |
| `/release-pr` | Briefing → release para imprensa + pitch para jornalistas — salva em `marketing/releases/` |
| `/planejar-campanha` | Briefing → plano de campanha completo (institucional/evento/produto) — salva em `marketing/campanhas/` |
| `/pagina-solucao` | Briefing → copy estruturada por seção + SEO/AEO/GEO — salva em `marketing/paginas/` |
| `/assinatura-email` | Dados pessoais → HTML de assinatura com identidade visual Solveplan |
| `/plano-marketing` | Perguntas estratégicas + funil → plano anual com calendário, budget e KPIs — salva em `marketing/planos/` |
| `/ebook` | Briefing → conteúdo completo + guia de layout pro Canva — salva em `marketing/ebooks/` |
| `/material-campanha` | Briefing → copy + briefing visual pra banners, LP, email, apresentação no Canva — salva em `marketing/materiais/` |
| `/anuncio` | Briefing → copy (2 variantes A/B) + briefing visual + configuração de campanha para LinkedIn Ads e Google Ads |
| `/abm` | Planejamento completo de campanha ABM — segmentação por tier, mensagens por vertical, Matched Audiences no LinkedIn, orquestração com vendas e framework de mensuração por conta |
| `/relatorio` | Analisa dados de marketing e gera relatório estruturado (executive summary, insights, recomendações, visualizações) — cobre campanhas, eventos, conteúdo, SEO, pipeline e ABM |
| `/atribuicao` | Analisa qual canal realmente gerou pipeline — modelos multi-touch (U-shaped, linear, first/last touch), UTM, CAC, ROAS e recomendações de realocação de budget |
| `/pesquisa-mercado` | Pesquisa de mercado estruturada — concorrentes, segmentos, tendências SAP/analytics na América Latina — com fontes verificadas e relatório executivo |
| `/video-editor` | Roteiro, briefing de edição e guia de publicação pra vídeos — talking head, Reels/conteúdo e clips de webinar — ferramentas: CapCut, Canva Video, Camtasia |
| `/clip-social` | Transforma gravações longas em clips otimizados por plataforma — identifica momentos, define cortes, gera legendas e calendário de publicação |

---

## Skills disponíveis

| Skill | Descrição |
|-------|-----------|
| `/setup` | Configura o sistema: entrevista o usuário e preenche `_contexto/` e `marca/` |
| `/iniciar` | Carrega o contexto do negócio no início de cada sessão |
| `/mapear` | Mapeia processos repetitivos e cria skills personalizadas |
| `/atualizar` | Varre o projeto e atualiza os arquivos de contexto desatualizados |
| `/syncar` | Commit + push pro GitHub (configura o remote na primeira vez) |
| `/novo-projeto` | Cria pasta de projeto com CLAUDE.md dedicado |
| `/carrossel` | Cria carrosséis pra Instagram/TikTok em HTML + PNG |
| `/proposta-comercial` | Gera proposta profissional em HTML com identidade visual |
| `/slide` | Cria slide/card visual em HTML + PNG |
| `/roteiro-post` | Transforma ideia em roteiro de post ou vídeo |
| `/email-profissional` | Rascunha email profissional a partir de contexto livre |
| `/analisar-dados` | Analisa arquivo em `dados/` e gera resumo com insights |
| `/publicar-site` | Publica HTML com link compartilhável via Cloudflare Pages |

Skills visuais (`/carrossel`, `/slide`, `/proposta-comercial`) requerem Playwright pra renderizar PNG:
```bash
npx playwright install chromium
```

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (se existirem e estiverem configurados):

1. `_contexto/empresa.md` — quem é o usuário, o que faz, como funciona o negócio
2. `_contexto/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_contexto/estrategia.md` — foco atual, prioridades, o que pode esperar

Usar essas informações como base pra qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considerar o foco atual descrito em `estrategia.md`.

Para qualquer tarefa visual (carrossel, proposta, slide, landing page), consultar `marca/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas usar o contexto naturalmente.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe uma skill relevante em `.claude/skills/` ou `.claude/commands/`.
Se encontrar, seguir as instruções da skill.
Se não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível (o usuário provavelmente vai pedir de novo no futuro), perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o padrão de repetição for claro.

---

## Aprender com correções

Quando o usuário corrigir algo, melhorar uma resposta ou dar uma instrução que parece permanente (frases como "na verdade é assim", "não faça mais isso", "prefiro assim", "sempre que...", "evita...", "da próxima vez..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde faz mais sentido salvar:

- **Sobre o negócio** (quem são os clientes, como funciona a empresa, serviços, mercado) → adicionar em `_contexto/empresa.md`
- **Sobre preferências e estilo** (tom de voz, formato de resposta, o que evitar, como estruturar textos) → adicionar em `_contexto/preferencias.md`
- **Sobre prioridades e foco atual** (projetos em andamento, metas do momento, prazos importantes, o que é prioridade agora) → adicionar em `_contexto/estrategia.md`
- **Regra de comportamento nessa pasta** (onde salvar arquivos, como nomear, fluxos específicos) → adicionar no próprio `CLAUDE.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro. Confirmar o que foi salvo mostrando a linha adicionada.

Não perguntar se a correção for óbvia de contexto imediato (ex: "na verdade o arquivo se chama X"). Só perguntar quando a informação tiver valor duradouro.

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante no projeto (novo cliente, nova skill, mudança de foco, novo processo, ferramenta instalada, estrutura de pastas alterada), perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize os arquivos de memória?"

Se sim, identificar o que precisa atualizar:

- **Novo cliente, serviço, ferramenta, equipe** → `_contexto/empresa.md`
- **Mudança de prioridade ou foco** → `_contexto/estrategia.md`
- **Correção de tom ou estilo** → `_contexto/preferencias.md`
- **Nova pasta, regra de organização, skill criada** → `CLAUDE.md`
- **Mudança visual (cores, fontes, logo)** → `marca/design-guide.md`

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo inteiro, só adicionar ou editar a linha relevante.

**Quando NÃO perguntar:**
- Tarefas pontuais que não mudam o contexto (ex: escrever um email, criar um post avulso)
- Perguntas simples ou conversas sem ação
- Mudanças que já foram salvas pelo bloco "Aprender com correções"

**Dica:** se não sabe se algo mudou, rode `/atualizar` pra uma varredura completa.

---

## Criação de skills

Quando o usuário pedir pra criar uma nova skill:

1. Verificar se existe um template relevante em `templates/skills/`. Se existir, usar como base e adaptar pro contexto do usuário
2. Perguntar: "Essa skill é específica pra esse projeto ou vai ser útil em qualquer projeto?"
   - Específica desse negócio → salvar em `.claude/skills/nome-da-skill/SKILL.md` (local)
   - Útil em qualquer projeto → salvar em `~/.claude/skills/nome-da-skill/SKILL.md` (global)
3. Ler `_contexto/empresa.md` e `_contexto/preferencias.md` pra calibrar o conteúdo da skill ao contexto do negócio
4. Se a skill precisar de arquivos de apoio (templates, referências, exemplos), criar dentro da pasta da skill
5. Seguir o fluxo da skill-creator nativa do Claude Code

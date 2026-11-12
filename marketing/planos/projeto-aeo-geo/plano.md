# Projeto AEO/GEO — 16/11/2026 a 15/01/2027

**Responsável:** Fran (sozinha) · **Apoio:** Claude escreve, prepara e confere; Fran revisa, aprova, publica e faz os cliques no painel.
**Ritmo:** cerca de **2h30 por semana**, em blocos curtos. A semana de 21/12 é mais leve (recesso).
**Base:** auditoria GEO de 12/11/2026 (`[GEO] audit_12.11.26.pdf`) e análise do site de 22/10/2026 (`marketing/auditorias-seo/site-2026-10-22-analise.md`).

---

## Por que este projeto

Na auditoria de 12/11, as IAs (ChatGPT, Gemini, Perplexity, Copilot) citaram a Solveplan em **3 de 10 respostas** (posição 14 de 45). Quando a citam, recomendam bem, mas **só nas perguntas de "qual consultoria contratar"**. Nas perguntas de problema, comparação e aprendizado, a Solveplan não aparece. As IAs também **não associam a Solveplan a SAP BDC nem a Group Reporting**, apesar do prêmio de Melhor Parceiro SAP BDC 2026 LATAM.

## Metas para 15/01/2027

| Meta | Hoje | Alvo |
|---|---|---|
| Citação nas mesmas 10 perguntas | 3 de 10 | **5 de 10** |
| Perguntas de problema/comparação/aprendizado em que a Solveplan aparece | 0 | **pelo menos 2** |
| IAs mencionam a Solveplan junto com SAP BDC | não | **sim** |
| Páginas-chave com H1, schema certo e FAQ | poucas | **home, BDC, Group Reporting e 2 artigos novos** |

## Regras de trabalho (combinadas)

- **Backup manual na Hostinger** antes de qualquer mudança no site.
- O que muda o visual vai antes para **rascunho**. Publicar só depois da aprovação da Fran.
- Mudanças no site **de segunda a quinta**, nunca na sexta.
- Para trabalhar pela API: desmarcar "Desativar senhas da aplicação" no Wordfence só durante o trabalho e marcar de novo no fim.
- Números oficiais: 150+ empresas, 300+ projetos, 68+ especialistas, 13+ anos.

---

## Cronograma

Formato de cada tarefa: `- [ ] Txx | quem | tempo da Fran | tarefa`. Quando terminar, a caixa vira `[x]`.

### Semana 1 — 16/11 a 19/11 · Fundação técnica (feriado em 20/11)
- [ ] T01 | Fran | 5 min | Backup manual no hPanel (Sites > solveplan.com > Arquivos > Backups > Criar backup)
- [ ] T02 | Claude escreve, Fran sobe | 30 min | Criar o **llms.txt** (resumo da Solveplan para as IAs) e subir na raiz do site (hPanel > Gerenciador de arquivos > public_html)
- [ ] T03 | Fran | 20 min | **Schema Organization** no Rank Math > Títulos e Meta > SEO Local: país BR, descrição nova com prêmio BDC 2026 e Gold, LinkedIn (texto pronto pelo Claude)
- [ ] T04 | Fran | 20 min | Padronizar **"Solveplan"** (hoje aparece "SolvePlan") nos títulos das notícias e cases
- [ ] T05 | Fran | 15 min | Correções rápidas: menu "Analitycs" > "Analytics"; "BLog" > "Blog"; botão "Fale com nossos especialistas" > /contato/
- [ ] T06 | Fran | 10 min | Medir o **PageSpeed** da home e da página BDC em pagespeed.web.dev e mandar os números ao Claude

### Semana 2 — 23/11 a 27/11 · Estrutura das páginas
- [ ] T07 | Fran | 2h | **H1 nas 26 páginas** (Elementor > título do topo > Tag HTML: H1), conferindo o visual. Lista pronta na planilha de 25/09
- [ ] T08 | Fran | 10 min | **Noindex nas 22 categorias** do blog (Rank Math > Títulos e Meta > aba Categorias; nunca a "Meta global")
- [ ] T09 | Fran | 20 min | Contadores **"0 +"** na home e na Sobre nós: número inicial = número final
- [ ] T10 | Fran | 20 min | **Schema das páginas**: Rank Math > Títulos e Meta > Páginas > Schema = Nenhum. Testar em 1 página e conferir com o Claude

### Semana 3 — 30/11 a 04/12 · Página BDC (texto)
- [ ] T11 | Claude | 0 | Escrever a **página BDC nova** (`/pagina-solucao`): definição direta, BDC x Datasphere x BW, prazos e pré-requisitos, riscos de consumo, case, prêmio, FAQ + schema
- [ ] T12 | Fran | 30 min | Conversa de 30 min com um consultor de BDC para validar prazos, pré-requisitos, riscos e o case (Klabin ou SSA Alimentos)
- [ ] T13 | Fran | 40 min | Revisar o texto da página BDC

### Semana 4 — 07/12 a 11/12 · BDC no ar + Group Reporting (texto)
- [ ] T14 | Fran (Claude ajuda) | 1h | Backup + montar a página BDC em **rascunho**, aprovar e publicar
- [ ] T15 | Claude escreve, Fran revisa | 1h | Página **Consolidação / SAP Group Reporting** no formato pergunta e resposta (inclui 20 min de validação com consultor)

### Semana 5 — 14/12 a 18/12 · Group Reporting no ar + autoridade fora do site
- [ ] T16 | Fran | 45 min | Publicar a página de Group Reporting (backup antes, rascunho primeiro)
- [ ] T17 | Claude escreve, Fran envia | 40 min | **Release do prêmio BDC 2026** (`/release-pr`) enviado a 3 portais (Baguete, TI Inside, IT Forum)
- [ ] T18 | Fran | 30 min | Atualizar o perfil no **SAP Partner Finder** (competências, descrição, cases)

### Semana 6 — 21/12 a 01/01 · Semana leve (recesso)
- [ ] T19 | Claude escreve, Fran revisa | 40 min | Artigo 1: **"Como migrar do SAP BPC para SAC Planning e Group Reporting"** (revisar quando puder)

### Semana 7 — 04/01 a 08/01 · Conteúdo de problema
- [ ] T20 | Fran | 30 min | Publicar o artigo 1 + post no LinkedIn (`/post-social`)
- [ ] T21 | Fran (Claude escreve) | 1h | **Case M. Dias Branco aprofundado**: 30 min de conversa com o consultor + 30 min de revisão
- [ ] T22 | Claude escreve, Fran revisa | 40 min | Artigo 2: **"Eliminações intercompany e fechamento no SAP Group Reporting"**

### Semana 8 — 11/01 a 15/01 · Fechamento e medição
- [ ] T23 | Fran | 45 min | Publicar o artigo 2 e o case M. Dias Branco + posts no LinkedIn
- [ ] T24 | Fran (Claude escreve) | 45 min | Home: bloco **"O que a Solveplan faz?"** + FAQ, em rascunho (publicar se aprovado)
- [ ] T25 | Fran + Claude | 30 min | **Repetir a auditoria GEO** com as mesmas 10 perguntas; o Claude compara com 12/11 e com o tráfego vindo de IAs no GA4

---

## Se sobrar tempo (próximo ciclo)

- Comparativo "Consultoria especialista x integradora global em SAC Planning e Group Reporting: quando escolher cada uma" (sem citar concorrentes)
- Guia "Lentidão em modelos de planejamento no SAC: causas e correções"
- Cases Zilor e Matrix Energia aprofundados
- Alts das imagens em massa (530 sem alt)
- Home nova completa com foco em BDC

## Fora deste projeto (de propósito)

- Página "Solveplan vs Deloitte" com nome de concorrente
- `ai-agents.json` (não é um padrão adotado pelas IAs)
- O robots.txt sugerido pela auditoria (ele bloquearia as páginas de solução para o ChatGPT e o Claude)

## Registro

| Data | O que aconteceu |
|---|---|
| 12/11/2026 | Plano criado a partir da auditoria GEO de 12/11 |
| 12/11/2026 | E-mail da Semana 1 enviado (pelo Outlook do computador). llms.txt e texto do schema Organization prontos |

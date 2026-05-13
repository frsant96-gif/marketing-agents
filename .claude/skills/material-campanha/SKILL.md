---
name: material-campanha
description: Cria copy e briefing visual para materiais de campanha da Solveplan — banners, landing pages, emails marketing e apresentações. Todos os visuais são produzidos no Canva.
---

# /material-campanha

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md`, `_contexto/estrategia.md` e `marca/design-guide.md`.

## Passo 1 — Briefing da campanha

Perguntar os dados abaixo, uma por vez:

1. "Qual o nome ou tema da campanha?"
2. "Qual o produto ou solução em foco?"
3. "Qual o objetivo do material?" — Gerar leads / Agendar reunião / Promover evento / Nutrir base / Lançamento
4. "Qual(is) material(is) você precisa?" — opções: Banner (redes sociais/anúncio) / Landing page / Email marketing / Apresentação / Todos
5. "Tem uma data ou prazo de veiculação?"

Se o usuário já passou algum dado antes de rodar a skill, não perguntar de novo.

## Passo 2 — Gerar por tipo de material

### Banner (redes sociais ou anúncio pago)

Para cada tamanho necessário, gerar:

**Copy do anúncio:**
- Headline: [máximo 7 palavras — foco no resultado ou na dor]
- Descrição: [máximo 2 linhas — benefício ou prova]
- CTA: [botão — ex: "Saiba mais", "Agendar diagnóstico", "Baixar agora"]

**Briefing visual pro Canva:**
- Formato e dimensões sugeridas: [ex: 1080x1080 feed, 1080x1920 stories, 1200x628 LinkedIn]
- Fundo: `#0A0E19` ou `#0A0837`
- Elemento visual: [foto corporativa / ícone / dado em destaque / mockup de interface]
- Cor de destaque: `#006AFF` no CTA ou elemento principal
- Logo: `logo-escuro.png.png`, canto inferior direito
- Overlay se usar foto: `#0A0E19` em 60% opacidade
- Fonte do título: Prompt ExtraBold
- Variante por formato: adaptar layout mantendo mensagem

---

### Landing page

**Copy completa da LP:**

**Headline (H1):** [promessa clara — máximo 8 palavras]
**Subheadline:** [expande a promessa — 1 linha]
**Corpo (acima da dobra):** [2-3 linhas com contexto e reforço da proposta]
**Benefícios:** [3-4 bullets com formato "verbo + resultado"]
**CTA principal:** [texto do botão]
**Micro-copy de redução de fricção:** [ex: "Sem compromisso. Resposta em até 24h."]
**Social proof:** [número de clientes, cases, ou selo SAP Gold Partner]

**Briefing visual pro Canva / desenvolvedor:**
- Layout sugerido: hero full-width com fundo escuro → seção de benefícios → formulário → social proof
- Formulário: nome, empresa, email, telefone, cargo
- Integração sugerida: [Mailchimp / HubSpot / formulário nativo conforme stack]

---

### Email marketing

**Assunto:** [máximo 50 caracteres — com curiosidade ou dado forte]
**Pré-header:** [máximo 80 caracteres — complementa o assunto]

**Estrutura do email:**

```
[Header com logo Solveplan]

[Headline — 1 linha em destaque]

[Corpo — 2-3 parágrafos curtos e diretos]
  - Parágrafo 1: contexto / dor
  - Parágrafo 2: solução / o que muda
  - Parágrafo 3: prova ou dado

[CTA — botão com fundo #006AFF]

[Texto abaixo do botão — ex: "Prefere responder esse email? Fala comigo diretamente."]

[Footer com logo, endereço, link de descadastro]
```

**Briefing visual pro Canva / template de email:**
- Largura: 600px
- Fundo do email: `#0A0E19` ou `#FFFFFF` dependendo do template
- Tipografia: Montserrat (ou Arial como fallback)
- Botão CTA: fundo `#006AFF`, texto `#FFFFFF`, border-radius 4px

---

### Apresentação (deck)

**Estrutura da apresentação:**
- Slide 1: Capa — nome da campanha/solução + logo Solveplan
- Slide 2: Agenda ou objetivo da apresentação
- Slide 3-4: Contexto do problema / mercado
- Slide 5-7: Solução e como funciona
- Slide 8-9: Benefícios e diferenciais
- Slide 10: Cases ou prova
- Slide 11: Próximos passos / CTA
- Slide 12: Contracapa com contato

**Copy de cada slide:** [título + tópicos principais — máximo 5 bullets ou 60 palavras por slide]

**Briefing visual pro Canva:**
- Formato: 1920x1080px (16:9)
- Paleta: fundo `#0A0E19`/`#0A0837`, destaque `#006AFF`, texto `#FFFFFF`
- Fonte: Prompt pra títulos | Montserrat pra corpo
- Logo: canto inferior direito em todos os slides
- Slide de dados: número grande em `#006AFF` ou `#94FF96`
- Slides de case: fundo alternativo mais claro ou borda lateral `#006AFF`

---

## Passo 3 — Salvar

Criar pasta `marketing/materiais/[nome-da-campanha-em-slug]/` e salvar:
- `copy.md` — toda a copy gerada, organizada por tipo de material
- `briefing-visual.md` — instruções de produção no Canva por peça

## Passo 4 — Confirmar

Informar onde foi salvo e perguntar:

> "Materiais salvos. Quer ajustar alguma copy, adaptar pra outro formato, ou criar o plano completo da campanha com `/planejar-campanha`?"

## Regras

- Copy de anúncio tem que ser testável: gerar 2 versões de headline quando possível (teste A/B)
- Email: assunto é o material mais importante — não tratar como genérico
- Apresentação: máximo 5 elementos por slide — slide cheio não convence executivo
- Landing page: um objetivo, um CTA — nunca duas chamadas pra ação concorrentes
- Sempre conectar ao SAP BDC quando o tema envolver dados/analytics/planejamento
- Nunca usar "transformação digital" sem contexto ou dado que sustente

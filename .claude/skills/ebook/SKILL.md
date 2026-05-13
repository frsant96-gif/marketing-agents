---
name: ebook
description: Cria o texto completo de e-books da Solveplan — briefing estratégico, estrutura por capítulo, copy de cada seção e guia de layout pro Canva. Formatos: landscape (apresentação) ou portrait (documento).
---

# /ebook

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md`, `_contexto/estrategia.md` e `marca/design-guide.md`.

## Passo 1 — Briefing

Fazer as perguntas abaixo, uma por vez:

1. "Qual o título ou tema do e-book?"
2. "Qual o objetivo?" — opções: Educar sobre problema / Apresentar solução / Gerar leads (topo de funil) / Habilitar vendas (meio de funil) / Demonstrar autoridade
3. "Pra qual persona é o foco?" — CIO, CFO, Controller, Head de dados/BI, COO, Misto
4. "Qual o nível de profundidade?" — Introdutório (overview) / Intermediário (conceitos + aplicação) / Avançado (técnico + operacional)
5. "Qual o formato?" — Landscape (estilo apresentação, 16:9) / Portrait (estilo documento, A4/vertical)
6. "Tem dados, cases ou referências que quer incluir?"
7. "Qual o CTA do e-book?" — ex: Agendar diagnóstico / Baixar outro material / Ver case completo

Se o usuário já informou algum dado antes de rodar a skill, não perguntar de novo.

## Passo 2 — Propor estrutura

Com base no briefing, sugerir a estrutura do e-book e confirmar antes de escrever:

**Estrutura padrão landscape (estilo Solveplan):**
```
Capa
Índice / sumário
Slide de contexto/problema (1-2 slides)
Slide de dados / evidências do problema (1 slide)
Conteúdo principal (3-6 slides/seções)
Slide de solução / posicionamento Solveplan
Case / prova (1-2 slides)
Slide de CTA / próximo passo
Contracapa com logo e contato
```

**Estrutura padrão portrait (estilo documento):**
```
Capa
Sumário
Introdução (1 página)
Capítulos (3-5, cada um com 1-2 páginas)
Conclusão / próximos passos
CTA
Sobre a Solveplan (boilerplate)
```

Adaptar a estrutura com base no tema e objetivo antes de confirmar.

## Passo 3 — Escrever o conteúdo

Escrever slide por slide (landscape) ou seção por seção (portrait) com marcação clara:

---

### Capa

**Título principal:** [título do e-book]
**Subtítulo:** [complemento — máximo 1 linha]
**Visual sugerido:** [descrever visual ideal pra capa — fundo escuro + elemento visual temático]
**Indicação tipográfica:** Prompt ExtraBold pra título, Montserrat Medium pra subtítulo

---

### [Número + Título de cada seção/slide]

**Headline/Título:** [H2 da seção]
**Corpo:** [texto — máximo 80 palavras por slide em landscape, 250 por página em portrait]
**Destaque visual sugerido:** [dado em destaque, ícone, gráfico, citação]
**Nota pra Canva:** [instrução específica de layout se necessário]

---

*(Repetir para cada seção)*

---

### CTA Final

**Título:** [chamada de ação]
**Corpo:** [1-2 linhas reforçando o próximo passo]
**CTA:** [texto do botão ou ação]
**Contato:** Solveplan | solveplan.com.br

---

### Sobre a Solveplan (boilerplate)

> A Solveplan é uma consultoria especializada em soluções SAP para dados, analytics, planejamento financeiro e consolidação. Parceira SAP Gold na América Latina com mais de 200 soluções entregues, 90 clientes atendidos e 280 mil horas de projetos.

---

## Passo 4 — Guia de layout pro Canva

Gerar um guia curto de produção:

**Formato:** {{FORMATO}} — [dimensões: 1920x1080px landscape / 794x1123px portrait A4]
**Paleta:** fundo `#0A0E19` ou `#0A0837`, destaque `#006AFF`, texto `#FFFFFF`, acento `#94FF96` com moderação
**Tipografia:** Prompt Bold/ExtraBold pra títulos e destaques | Montserrat Regular/Medium pra corpo
**Logo:** usar `logo-escuro.png.png` — posicionar no canto inferior direito ou no slide de CTA/capa
**Ícones:** estilo minimalista, stroke, arestas retas com cantos levemente curvos
**Imagens:** fotografia corporativa ou mockups de interface — sempre escurecer com overlay `#0A0E19` em ~60%
**Gráficos/dados:** usar `#006AFF` como cor primária, `#94FF96` como destaque

**Slides especiais:**
- Capa: tipografia grande, visual de impacto, logo em destaque
- Dados/evidência: número grande em `#006AFF` ou `#94FF96`, rótulo em branco pequeno
- CTA: fundo mais claro ou elemento que quebra o padrão — tem que se destacar

## Passo 5 — Salvar

Criar pasta `marketing/ebooks/[slug-do-tema]/` e salvar:
- `conteudo.md` — texto completo de todos os slides/seções
- `layout-guide.md` — guia de produção no Canva

Nomear a pasta com o tema em minúsculas, sem acentos, com hífens.

## Passo 6 — Confirmar

Informar onde foi salvo e perguntar:

> "Conteúdo e guia de layout salvos. Quer revisar alguma seção, adicionar um case específico, ou ajustar o CTA?"

## Regras

- Landscape: máximo 80 palavras por slide — e-book não é artigo, é apresentação visual
- Portrait: manter parágrafos curtos, hierarquia clara com H2/H3, leitura fácil no scroll
- SAP BDC como referência quando o tema envolver dados/analytics/planejamento
- Nunca usar "transformação digital" como headline — sem substância
- Dados e cases são o que vendem o e-book — priorizar onde colocar o conteúdo mais denso
- CTA tem que ser específico: "Agendar diagnóstico" > "Entre em contato"

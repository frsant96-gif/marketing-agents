---
name: post-social
description: Cria copy para posts de redes sociais da Solveplan. Briefing estratégico, geração por formato e plataforma (LinkedIn, Instagram, X/Twitter), e checklist de auto-verificação antes de entregar.
---

# /post-social

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md` e `_contexto/estrategia.md`.

## Passo 1 — Briefing

Fazer as perguntas abaixo, uma por vez:

1. "Qual o tema ou assunto do post?"
2. "Qual o objetivo?" — opções: Gerar awareness / Educar / Gerar leads / Provocar dor / Promover case / Anunciar solução / Engajamento / Autoridade executiva
3. "Qual o formato?" — opções: Post único (texto), Imagem estática, Carrossel (slides), Vídeo gravado, Motion / Reels com texto animado
4. "Pra qual plataforma?" — opções: LinkedIn / Instagram / X (Twitter) / Todas (gerar versão pra cada uma)
5. "Tem algum dado, case, ou referência que quer incluir?"
6. "Pra qual persona é o foco principal?" — opções: CIO, CFO, Controller, Head de dados/BI, COO, Geral

Se o usuário já informou algum desses dados antes de rodar a skill, não perguntar de novo.

## Passo 2 — Escolher rota por formato

### Formato: Carrossel

Delegar pra skill `/carrossel` com o briefing completo:

> "Vou criar esse como carrossel. Rodando `/carrossel` com as informações que você passou."

### Formato: Post único (texto) / Imagem / Motion

Seguir o Passo 3 com a plataforma escolhida.

### Formato: Vídeo gravado

Gerar roteiro completo:
- **Hook (0-3s):** frase de abertura que retém — vai aparecer em legenda ou dita pela câmera
- **Problema (3-15s):** contextualização da dor
- **Solução (15-45s):** como a Solveplan resolve, com ponto de prova
- **CTA (45-60s):** chamada pra ação clara
- **Indicações técnicas:** onde pausar, onde mostrar tela/slide, tom sugerido

---

## Passo 3 — Gerar por plataforma

### LinkedIn

**Tom:** profissional, direto, orientado a negócio, posicionamento de autoridade sem hype.

**Estrutura AIDA:**
- **Atenção (linha 1):** para o scroll — afirmação forte, dado surpreendente ou pergunta que provoca. Sem emojis, sem "Você sabia que".
- **Interesse (linhas 2-4):** contextualização do problema ou oportunidade
- **Desejo (linhas 5-8):** como a solução resolve / o que muda pra quem age
- **Ação (última linha):** CTA claro — reunião, diagnóstico, link, comentário

**Regras LinkedIn:**
- Máximo 1.300 caracteres (posts mais curtos têm mais alcance)
- Quebras de linha após cada 1-2 frases — LinkedIn não renderiza parágrafos densos
- 3-5 hashtags no final — específicas (#SAPAnalytics #DataCloud #FPandA), não genéricas (#inovação)
- Gerar 2 versões com abordagens diferentes

**Formatos especiais:**
- *Post de lista:* "X razões pelas quais..." ou "X sinais de que..." — bom pra salvar/compartilhar
- *Post de opinião:* começa com "Discordo de..." ou "A maioria faz X. Mas..." — bom pra engajamento
- *Post de case:* situação → desafio → solução → resultado — bom pra autoridade

---

### Instagram

**Tom:** mais visual e direto. Primeiras palavras têm que reter antes do "ver mais".

**Estrutura:**
- **Linha 1 (antes do corte):** frase de impacto — máximo 125 caracteres visíveis
- **Desenvolvimento:** 3-5 pontos curtos, cada um em linha própria
- **CTA:** link na bio / comentário / salvar o post

**Regras Instagram:**
- Máximo 2.200 caracteres (mas 300-500 funcionam melhor no feed)
- Emojis são aceitos aqui — usados com moderação (1-2 por parágrafo)
- 5-10 hashtags no final ou no primeiro comentário — misturar específicas e de nicho
- O visual carrega mais peso que o texto — indicar no briefing visual o que a imagem deve comunicar

**Briefing visual (se for imagem ou Reels):**
- Headline da imagem: máximo 6-8 palavras
- Dado ou frase de destaque: opcional
- Paleta: fundo `#0A0E19` ou `#0A0837`, destaque `#006AFF`, texto `#FFFFFF`
- Elemento visual sugerido (ícone, dado, mockup, foto)

---

### X (Twitter)

**Tom:** conversacional, direto, opinativo. Pensa em voz alta com autoridade.

**Formatos:**

*Tweet único:*
- Máximo 280 caracteres
- Hook na primeira frase — sem rodeio
- Terminar com pergunta ou afirmação que provoca resposta

*Thread (para temas mais complexos):*
- Tweet 1: afirmação forte que resume tudo (hook)
- Tweets 2-5: desenvolvimento com 1 ideia por tweet
- Tweet final: conclusão + CTA
- Máximo 280 caracteres por tweet
- Indicar numeração: 1/ 2/ 3/...

**Regras X:**
- Sem hashtags em excesso — máximo 2, só se realmente relevantes
- Linguagem mais informal que LinkedIn — pode usar contrações e frases curtas
- Dados e números funcionam muito bem como hook

---

## Passo 4 — Se "Todas as plataformas"

Gerar uma versão adaptada pra cada plataforma a partir do mesmo briefing. Mostrar as 3 versões lado a lado com nota de qual elemento mudou entre elas.

```
LinkedIn:
[copy LinkedIn]

Instagram:
[copy Instagram]

X:
[copy X]

O que mudou: [explicação rápida das adaptações]
```

---

## Passo 5 — Checklist de auto-verificação

Antes de entregar, verificar cada item:

**Hook:**
- [ ] A primeira linha para o scroll sem depender do contexto anterior?
- [ ] Evita "Você sabia que", "É com grande prazer" ou frases genéricas?
- [ ] Funciona lida sozinha, sem o restante do post?

**Conteúdo:**
- [ ] Tem um insight concreto — não só informação genérica?
- [ ] Conecta com uma dor real do público (CIO, CFO, Head de dados)?
- [ ] Menciona SAP BDC ou analytics de forma relevante (se o tema permitir)?
- [ ] Não usa "transformação digital" sem contexto?

**Posicionamento:**
- [ ] Posiciona a Solveplan como especialista, não como vendedor?
- [ ] Tem pelo menos 1 dado, caso ou afirmação verificável?

**Plataforma:**
- [ ] O comprimento respeita o limite da plataforma?
- [ ] As hashtags são específicas e relevantes (não genéricas)?
- [ ] O CTA é claro e proporcional ao estágio de relacionamento (awareness ≠ reunião)?

Se algum item falhar, reescrever antes de salvar.

---

## Passo 6 — Salvar

Criar pasta `marketing/posts/[tema-em-slug]/` e salvar como `copy.md`.

Incluir no arquivo: versões geradas + resultado do checklist.

## Passo 7 — Confirmar

> "Quer ajustar o tom, trocar de formato, gerar uma versão diferente ou adaptar pra outra plataforma?"

## Passo 8 — Gerar Excel do post

Após salvar o `copy.md`, sempre gerar um arquivo Excel com os dados do post.

Criar o arquivo `marketing/posts/[tema-em-slug]/post-dados.xlsx` usando Python + openpyxl com as seguintes colunas (exatamente nessa ordem e com esses nomes):

```
Data | Dia | Linha Editorial | Tema | Origem do Post | Título de Conteúdo |
Objetivo | Persona | Etapa do Funil | Copy LinkedIn | Copy Facebook |
Copy Instagram | Formato | Horário | Ref. Texto | Responsável | Status
```

**Preenchimento de cada coluna com base no briefing:**

| Coluna | Como preencher |
|--------|---------------|
| Data | Data de publicação informada, ou deixar em branco se não definida |
| Dia | Dia da semana da data de publicação |
| Linha Editorial | Pilar de conteúdo: Educação/Produto, Autoridade/Tendência, Case/Prova Social, Engagement, Artigo/Blog |
| Tema | Assunto principal do post (resumido em uma linha) |
| Origem do Post | Case de cliente / Artigo do blog / SAPPHIRE / Evento / Criação própria |
| Título de Conteúdo | Hook — primeira linha do post (a frase que para o scroll) |
| Objetivo | Awareness, Educação, Geração de pipeline, Engajamento, Autoridade, Credibilidade |
| Persona | Persona(s) alvo: CFO, Controller, CIO, Head de Dados, COO, Geral |
| Etapa do Funil | Topo, Meio ou Fundo |
| Copy LinkedIn | Texto completo do post LinkedIn gerado |
| Copy Facebook | Texto adaptado para Facebook |
| Copy Instagram | Caption para Instagram |
| Formato | Texto longo, Carrossel, Poll, Vídeo, Imagem estática |
| Horário | Deixar em branco — a ser definido na publicação |
| Ref. Texto | Caminho do arquivo: `marketing/posts/[tema-em-slug]/copy.md` |
| Responsável | "Fran" (padrão) |
| Status | "🟡 Criado" (padrão ao criar) |

**Formatação visual obrigatória:**
- Cabeçalho: fundo `#0A1A3C` (azul Solveplan), fonte branca, bold, tamanho 10
- Linhas alternadas: branco e `#EEF2F8`
- Status "✅ Pronto": fundo verde claro `#D6F5E8`, fonte verde `#1A7A4A`
- Status "🟡 Criado": fundo amarelo claro `#FFF9C4`, fonte `#7A5A00`
- `wrap_text=True` em todas as células, `vertical="top"`
- Congelar linha 1 (cabeçalho) e coluna A
- Filtro automático em todas as colunas
- Largura das colunas de Copy (LinkedIn/Facebook/Instagram): 65-70 caracteres

Após salvar o Excel, abrir automaticamente com `Start-Process` (Windows).

Confirmar com:
> "Excel salvo em `marketing/posts/[tema-em-slug]/post-dados.xlsx` e aberto automaticamente."

## Regras

- Nunca usar "transformação digital" como buzzword sem contexto
- Nunca prometer resultado sem base técnica
- Primeira linha tem que parar o scroll — testar internamente antes de entregar
- Quando o tema conectar com SAP BDC, conectar — é a prioridade atual
- Tom: autoridade sem hype, direto, focado em negócio
- LinkedIn é a plataforma prioritária da Solveplan — quando houver dúvida de formato, otimizar pra ela

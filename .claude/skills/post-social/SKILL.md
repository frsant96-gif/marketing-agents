---
name: post-social
description: Cria copy para posts de redes sociais da Solveplan. Faz briefing estratégico e gera o conteúdo no formato certo — post único, imagem, vídeo ou carrossel.
---

# /post-social

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md` e `_contexto/estrategia.md` pra calibrar tom, contexto e prioridade atual.

## Passo 1 — Briefing

Fazer as perguntas abaixo, uma por vez:

1. "Qual o tema ou assunto do post?"
2. "Qual o objetivo?" — opções: Gerar awareness / Educar o público / Gerar leads / Provocar dor / Promover case / Anunciar solução / Engajamento
3. "Qual o formato?" — opções: Post único (texto), Imagem estática, Carrossel (slides), Vídeo gravado, Motion / Reels com texto animado
4. "Tem algum dado, case, ou referência que quer incluir?"
5. "Pra qual persona é o foco principal?" — opções: CIO, CFO, Controller, Head de dados/BI, COO, Geral

Se o usuário já informou algum desses dados antes de rodar a skill, não perguntar de novo.

## Passo 2 — Escolher rota por formato

### Formato: Carrossel

Delegar pra skill `/carrossel` com o briefing completo. Informar:

> "Vou criar esse como carrossel. Rodando `/carrossel` com as informações que você passou."

### Formato: Post único (texto)

Gerar o copy seguindo estrutura AIDA:
- **Atenção:** primeira linha que para o scroll — afirmação forte, dado surpreendente, ou pergunta que provoca
- **Interesse:** contextualização do problema ou oportunidade (2-3 linhas)
- **Desejo:** como a solução resolve / o que muda pra quem resolve
- **Ação:** CTA claro — reunião, diagnóstico, link, comentário

**Regras do copy:**
- Máximo 1200 caracteres (LinkedIn)
- Primeira linha sem emojis e sem "Você sabia que"
- Tom direto, orientado a negócio, sem buzzwords
- SAP BDC como foco quando o tema permitir
- Hashtags: 3-5 no final, relevantes e específicas

Gerar 2 versões com abordagens diferentes.

### Formato: Imagem estática

Gerar:
1. **Copy do post** (legenda) — seguindo AIDA, máximo 800 caracteres
2. **Briefing visual pro Canva:**
   - Headline da imagem (máximo 8 palavras)
   - Subheadline ou dado de destaque (opcional)
   - Paleta sugerida: fundo `#0A0E19` ou `#0A0837`, destaque `#006AFF`, texto `#FFFFFF`
   - Elemento visual sugerido (ícone, dado, mockup, foto)
   - Template base sugerido (se o usuário tiver templates no Canva, indicar qual se encaixa)

### Formato: Vídeo gravado

Gerar roteiro completo:
- **Hook (0-3s):** frase de abertura que retém — vai aparecer em legenda ou dita pela câmera
- **Problema (3-15s):** contextualização da dor
- **Solução (15-45s):** como a Solveplan resolve, com ponto de prova
- **CTA (45-60s):** chamada pra ação clara
- **Indicações técnicas:** onde pausar, onde mostrar tela/slide, tom sugerido (direto, consultivo)

### Formato: Motion / Reels com texto animado

Gerar sequência de frames:
- Frame 1: Headline — frase de gancho (máximo 6 palavras)
- Frame 2-4: Pontos principais (máximo 2 linhas por frame)
- Frame final: CTA com identidade visual Solveplan

Para cada frame:
- Texto exato
- Cor de fundo sugerida (da paleta)
- Elemento visual sugerido

## Passo 3 — Salvar

Criar pasta `marketing/posts/[tema-em-slug]/` e salvar o output como `copy.md`.

Nomear a pasta com o tema em minúsculas, sem acentos, com hífens.
Exemplo: "Lançamento SAP BDC" → `marketing/posts/lancamento-sap-bdc/copy.md`

## Passo 4 — Confirmar

Informar onde foi salvo e perguntar:

> "Quer ajustar o tom, trocar de formato, ou gerar uma versão diferente?"

## Regras

- Nunca usar "transformação digital" como buzzword sem contexto
- Nunca prometer resultado sem base técnica
- Primeira linha sempre tem que parar o scroll — testar internamente antes de entregar
- Quando o tema conectar com SAP BDC, conectar — é a prioridade atual
- Tom: autoridade sem hype, direto, focado em negócio

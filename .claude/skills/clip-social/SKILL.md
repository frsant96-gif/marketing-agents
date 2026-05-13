---
name: clip-social
description: Transforma gravações longas (webinars, eventos, entrevistas) em clips otimizados por plataforma. Identifica os melhores momentos, define cortes, gera legenda de publicação e briefing de edição pra CapCut, Canva Video ou Camtasia.
---

# /clip-social

## Antes de começar

Ler `_contexto/empresa.md` e `_contexto/preferencias.md`.

## O que essa skill faz

Você tem uma gravação longa — webinar, evento, entrevista, live. Essa skill ajuda a:
1. Identificar os melhores momentos pra virar clip
2. Definir o corte certo pra cada plataforma
3. Gerar a legenda de publicação já pronta
4. Passar um briefing claro pra editar no CapCut ou Canva Video

## Passo 1 — Entender o material

Perguntar, um por vez:

1. "Qual é o vídeo original?" — webinar / evento presencial gravado / entrevista / live / call gravada
2. "Qual a duração total do vídeo?"
3. "Qual o tema central da gravação?"
4. "Você já tem em mente algum momento específico que foi impactante? (timestamp ou descrição)"
5. "Pra quais plataformas quer publicar?" — LinkedIn / Instagram / TikTok / Todas

Se o usuário não souber o momento ideal, executar o Passo 2A. Se souber, ir direto pro Passo 2B.

## Passo 2A — Identificar os melhores momentos

Guiar o usuário pra encontrar os clips sem precisar assistir tudo:

> "Pra encontrar os melhores clips rapidinho, responda:"

- "Teve algum dado ou estatística mencionada que causou reação?"
- "Teve uma pergunta da audiência que gerou uma resposta forte?"
- "Qual frase resumiria o evento em uma linha?"
- "Houve algum momento de tensão, surpresa ou discordância?"
- "O que você quer que as pessoas lembrem desse evento?"

Com base nas respostas, sugerir os tipos de clip a extrair:

```
Clip 1 — [tipo: Insight / Dado / Opinião / Resposta]
Onde procurar: [descrição do contexto pra localizar na timeline]
Por que funciona: [justificativa de por que esse clip vai performar]
Plataforma ideal: [LinkedIn / Instagram / TikTok]
Duração estimada: [Xs a Xs]

Clip 2 — [tipo]
...
```

## Passo 2B — Definir os cortes

Para cada clip identificado:

```
Clip: [nome / tema]
Arquivo fonte: [nome do arquivo de vídeo]
Timestamp de início: [hh:mm:ss]
Timestamp de fim: [hh:mm:ss]
Duração: [Xs]

O que é esse momento:
[1-2 frases descrevendo o que acontece no clip]

Por que funciona como clip:
[hook identificado / dado impactante / opinião forte / resposta surpreendente]

Adaptação necessária:
[contexto que falta / silêncio que deve ser cortado / identificação do palestrante]
```

## Passo 3 — Adaptar por plataforma

Para cada clip, gerar a versão adaptada por plataforma:

### LinkedIn

```
Formato: 1:1 (quadrado) para feed / 9:16 para stories/newsletter
Duração ideal: 45s a 3min
Recorte de câmera: centralizar no rosto do palestrante
Legenda de abertura (text overlay): "[Nome do Evento] — [Data]"
Identificação do palestrante: "[Nome], [Cargo] — Solveplan" (canto inferior esquerdo, aparece nos primeiros 5s)
Destaque de frase: a frase mais forte do clip em texto sobreposto
CTA no final: "Assista ao webinar completo" ou "Comenta o que achou"
```

### Instagram Reels

```
Formato: 9:16 obrigatório (1080x1920px)
Duração ideal: 30s a 60s — cortar sem piedade
Recorte: usar CapCut "Smart Crop" pra recortar 16:9 pra 9:16
Hook visual nos primeiros 2s: texto sobreposto com a frase mais impactante
Legenda automática: ativar no CapCut — revisar erros de transcrição
Música: instrumental leve (opcional) — Volume: 15-20%
CTA no frame final: "Siga pra mais conteúdo" / "Link na bio"
```

### TikTok

```
Formato: 9:16 obrigatório
Duração ideal: 30s a 60s
Tom: mais direto e rápido que LinkedIn — cortar toda hesitação
Hook nos primeiros 1s: não tem margem — a frase mais forte vai primeiro
Texto sobreposto: usar bastante — boa parte da audiência assiste sem som
CTA: direto — "Segue aqui pra mais SAP e dados"
Hashtags: 3-5 específicas (#SAPAnalytics #Dados #CFO #Analytics)
```

## Passo 4 — Briefing de edição

Perguntar: "Vai editar no CapCut, Canva Video ou Camtasia?"

Gerar um briefing passo a passo adaptado:

---

**CapCut (mobile ou desktop) — clips rápidos, Reels, TikTok:**

```
BRIEFING DE EDIÇÃO — [Nome do clip]
Ferramenta: CapCut

Passo 1 — Importar
Abrir CapCut → Novo projeto → Importar [nome do arquivo]

Passo 2 — Cortar
Arrastar timeline até [timestamp de início]
Marcar início do clip
Arrastar até [timestamp de fim]
Marcar fim do clip
Apagar o resto

Passo 3 — Formato
Clicar em "Proporção" → Selecionar [1:1 ou 9:16]
Se 9:16 e original era 16:9: ativar "Smart Crop" ou ajustar manualmente centralizando no rosto

Passo 4 — Legenda automática
Menu → "Legenda" → "Auto Legenda"
Idioma: Português (Brasil)
Revisar e corrigir erros
Fonte: negrito / tamanho: grande / posição: centro-inferior
Destaque: colorir a frase mais importante em #006AFF

Passo 5 — Texto sobreposto
Adicionar texto com nome do evento e data (início do clip)
Adicionar texto com nome e cargo do palestrante (primeiros 5s)
Adicionar CTA no último frame (2-3s)

Passo 6 — Áudio
Verificar se áudio original está limpo
Se quiser adicionar trilha: "Música" → Instrumental → Volume: 20%

Passo 7 — Revisar
[ ] Hook nos primeiros 3s
[ ] Palestrante identificado
[ ] Legenda cobre todo o áudio
[ ] CTA no final
[ ] Formato correto pra plataforma

Passo 8 — Exportar
Resolução: 1080p
Frame rate: 30fps
Salvar em: [pasta local ou Google Drive]
```

## Passo 5 — Gerar legenda de publicação

Para cada clip, gerar a legenda pronta pra publicar usando as regras do `/post-social`:

```
Plataforma: [LinkedIn / Instagram / TikTok]

LEGENDA:
[copy completa pronta pra copiar e colar]

Hashtags: [3-5 relevantes]

Melhor horário pra publicar: [sugestão baseada na plataforma]
- LinkedIn: terça a quinta, 7h-9h ou 12h-13h
- Instagram: terça a sexta, 11h-13h ou 19h-21h
- TikTok: qualquer dia, 19h-23h
```

## Passo 6 — Calendário de clips

Se o usuário tiver múltiplos clips do mesmo evento, sugerir um calendário de publicação:

```
Semana 1 — clip mais impactante (maior alcance)
Semana 2 — clip de insight técnico (autoridade)
Semana 3 — clip de Q&A / pergunta da audiência (engajamento)
Semana 4 — teaser ou "o que você perdeu" (FOMO)
```

## Passo 7 — Salvar

Criar pasta `marketing/videos/clips/[nome-do-evento]/` e salvar:
- `clips.md` — lista de todos os clips com timestamps e briefings
- `legendas.md` — legendas prontas pra cada plataforma
- `calendario.md` — sugestão de calendário de publicação (se múltiplos clips)

## Regras

- Legenda obrigatória em todos os clips — 85% dos vídeos são assistidos sem som
- Hook nos primeiros 3s é inegociável — se o clip não tem hook nos primeiros 3s, cortar ou adicionar texto de abertura
- Duração: cortar sem piedade — melhor 45s ótimos do que 3min mediocres
- 1 clip = 1 ideia — não tentar colocar tudo em um clip só
- Identificar o palestrante com texto na tela — não assumir que a audiência sabe quem é
- Cada plataforma tem seu formato — nunca publicar o mesmo arquivo sem adaptar

---
name: persona
description: Cria, atualiza e consulta personas de marketing da Solveplan. Usa framework Jobs to be Done (JTBD) e jornada do comprador. Salva as personas em _contexto/personas/ para uso em campanhas, conteúdo e abordagem comercial.
---

# /persona

## Antes de começar

Ler `_contexto/empresa.md` e `_contexto/estrategia.md`.

## Modos de uso

Perguntar:

> "O que você quer fazer com personas?"

1. **Criar persona nova** — a partir de informações que você tem sobre o público
2. **Atualizar persona existente** — adicionar dados novos (pesquisa, entrevista, feedback de vendas)
3. **Consultar persona** — "como o CFO pensa sobre esse problema?" pra usar em copy ou campanha
4. **Listar personas** — ver quais já existem em `_contexto/personas/`

---

## Modo 1 — Criar persona nova

### Passo 1 — Coletar informações

Perguntar, uma por vez, só o que o usuário não souber pular:

**Identidade:**
1. "Qual o cargo ou papel dessa persona?" — ex: CFO, CIO, Head de dados, Controller
2. "Em que tipo de empresa ela trabalha?" — segmento, porte, ERP atual
3. "Qual a faixa de senioridade?" — C-level / Diretoria / Gerência / Coordenação

**Contexto profissional:**
4. "Quais são as principais responsabilidades dela no dia a dia?"
5. "Quais métricas ou resultados ela é cobrada a entregar?"
6. "Quais ferramentas ela usa hoje?" — ex: SAP, Excel, Power BI, planilhas

**Jobs to be Done (o que ela está tentando resolver):**
7. "Qual o problema principal que essa persona enfrenta com dados/analytics hoje?"
8. "O que ela está tentando alcançar quando busca uma solução como a que a Solveplan oferece?"
   — *Não a feature, o resultado real: "quero ter visibilidade do resultado financeiro consolidado antes do fechamento"*
9. "O que ela já tentou antes que não funcionou?"
10. "O que impede ela de resolver sozinha?" — restrições: orçamento, tempo, falta de equipe técnica, política interna

**Comportamento de compra:**
11. "Ela é quem decide a compra, quem influencia ou quem usa?"
12. "O que ela precisa ver pra confiar numa consultoria? (prova, case, referência, demo, dado)"
13. "Quais são as objeções mais comuns dela?" — ex: "já tentamos isso e não funcionou", "não temos orçamento agora"

**Informações opcionais (preencher quando tiver):**
- Onde ela busca informação (LinkedIn, eventos SAP, Gartner, indicação)
- Tom de comunicação que ela responde melhor (técnico / executivo / pragmático)
- Frases reais que ela usa ao falar do problema (direto de entrevistas ou conversas)

Se o usuário não tiver todas as informações agora, preencher o que tiver e marcar o resto como `[a preencher]`.

### Passo 2 — Montar o documento da persona

```markdown
# Persona: [Nome fictício + Cargo]
*Atualizado em: [data]*

## Quem é
**Cargo:** [cargo]
**Empresa:** [segmento + porte típico]
**ERP / Ferramentas atuais:** [lista]
**Nível de maturidade analítica:** [básico / intermediário / avançado]

## Responsabilidades e pressões
[2-3 parágrafos sobre o dia a dia, o que ela entrega e pelo que é cobrada]

## Jobs to be Done
**O que ela está tentando fazer:**
> "[Frase em primeira pessoa — o resultado que ela quer, não a feature]"
> Exemplo: "Quero fechar o mês sem passar 3 semanas consolidando planilhas de 12 subsidiárias."

**Contexto que cria urgência:**
[O que está acontecendo no mercado, na empresa ou no setor que torna esse problema urgente agora]

**O que ela já tentou:**
- [tentativa 1] — por que não funcionou
- [tentativa 2] — por que não funcionou

**O que a impede de resolver sozinha:**
- [barreira 1]
- [barreira 2]

## Jornada do comprador

| Fase | O que ela pensa | O que ela faz | O que ela sente |
|------|-----------------|---------------|-----------------|
| **Awareness** — percebe o problema | [pensamento] | [busca info, conversa com pares] | [frustração, pressão] |
| **Consideração** — avalia soluções | [compara opções, pede referência] | [assiste demo, lê case] | [ceticismo, esperança] |
| **Decisão** — escolhe fornecedor | [o que precisa pra confiar] | [envolve outros decisores, negocia] | [cautela, responsabilidade] |
| **Pós-venda** — usa a solução | [o que espera ver acontecer] | [acompanha entrega, reporta resultado] | [alívio ou decepção] |

## Comportamento de compra
**Papel na decisão:** [Decisor / Influenciador / Usuário final]
**O que ela precisa ver pra confiar:** [prova, dado, referência, demo, case do setor]
**Com quem ela consulta antes de decidir:** [CIO, equipe financeira, diretoria]

## Objeções comuns
| Objeção | Como a Solveplan responde |
|---------|--------------------------|
| "[objeção 1]" | [resposta] |
| "[objeção 2]" | [resposta] |
| "[objeção 3]" | [resposta] |

## Como se comunicar com ela
**Tom:** [técnico / executivo / pragmático / consultivo]
**Canais que ela usa:** [LinkedIn / eventos SAP / Gartner / indicação]
**Frases que ela usa** (quando disponível):
- "[frase real 1]"
- "[frase real 2]"

**O que NÃO falar com ela:**
- [o que gera rejeição imediata — ex: "transformação digital", promessas sem dado]

## Implicações pra marketing
**Mensagem principal:** [a frase que mais vai ressoar com essa persona]
**Formato de conteúdo que funciona:** [case / dado / comparação / guia prático / webinar]
**CTA ideal pra ela:** [diagnóstico gratuito / demo / conversa com especialista / material técnico]
**Onde abordá-la:** [LinkedIn / evento / indicação / email]
```

### Passo 3 — Salvar

Criar pasta `_contexto/personas/` se não existir e salvar como `[cargo-em-slug].md`.

Exemplos: `cfo.md`, `cio.md`, `head-dados.md`, `controller.md`

---

## Modo 2 — Atualizar persona existente

Perguntar:
> "Qual persona você quer atualizar e o que mudou?"

Ler o arquivo existente em `_contexto/personas/`, aplicar as novas informações e registrar a data de atualização no topo.

Exemplos de atualizações comuns:
- "Vendas me disse que o CFO está sempre preocupado com prazo de ROI" → adicionar em Objeções e Comportamento de compra
- "Fizemos uma entrevista com um cliente CIO e ele falou X" → adicionar em Frases reais e JTBD
- "Percebemos que o Controller não decide, só influencia" → atualizar Papel na decisão

---

## Modo 3 — Consultar persona

Perguntar:
> "Qual persona e o que você quer saber?"

Exemplos de consultas:
- "Como o CFO pensa sobre consolidação?" → responder com base no arquivo da persona
- "Quais objeções o CIO tem?" → listar as objeções registradas
- "Que tipo de conteúdo funciona pro Head de dados?" → recomendar formato e mensagem
- "Qual CTA usar pro Controller numa campanha de ABM?" → responder com base no perfil

Sempre indicar se a informação vem do arquivo salvo ou é inferência baseada no perfil.

---

## Modo 4 — Listar personas

Listar os arquivos existentes em `_contexto/personas/` com nome, cargo e data de última atualização.

---

## Conexão com outras skills

Quando uma persona está bem preenchida, referenciar em:
- `/planejar-campanha` — "pra qual persona é essa campanha?" → carregar o arquivo e calibrar mensagem
- `/post-social` — "pra qual persona é esse post?" → ajustar tom e hook
- `/artigo-blog` — "nível do leitor" → usar o perfil pra calibrar profundidade técnica
- `/abm` — "segmentação por vertical" → cruzar com contas-alvo por segmento
- `/pesquisa-mercado` — "quem é o comprador nesse segmento?" → usar persona como base de pesquisa

---

## Regras

- Persona é documento vivo — atualizar sempre que surgir dado novo (entrevista, feedback de vendas, pesquisa)
- JTBD em primeira pessoa e focado em resultado, não em feature: "quero X" não "preciso de uma plataforma que faça Y"
- Objeções reais têm mais valor que objeções imaginadas — priorizar o que vendas ouve de verdade
- Se uma informação não está confirmada, marcar como `[hipótese — validar]`
- Nunca deletar versão anterior — ao atualizar, registrar o que mudou e por quê

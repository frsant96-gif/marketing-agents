---
name: pagina-solucao
description: Cria o copy completo de páginas de solução para o site da Solveplan. Estruturado por seção com SEO, AEO e GEO. Plataforma: WordPress.
---

# /pagina-solucao

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md` e `_contexto/estrategia.md`.

## Passo 1 — Briefing

Fazer as perguntas abaixo, uma por vez:

1. "Qual a solução ou serviço da página?" — ex: SAP BDC, SAP Analytics Cloud, FP&A, Consolidação, AMS
2. "Qual a palavra-chave principal que quer ranquear?"
3. "Qual a dor principal do público que essa solução resolve?"
4. "Tem algum case ou resultado concreto que pode incluir como prova?"
5. "Qual o CTA principal?" — opções: Agendar diagnóstico / Falar com especialista / Baixar material / Ver case
6. "Tem alguma referência de página que você gosta? (pode ser da própria Solveplan ou de outro site)"

Se o usuário já informou algum dado antes de rodar a skill, não perguntar de novo.

## Passo 2 — Confirmar estrutura

Apresentar a estrutura antes de escrever:

> "Vou estruturar a página assim:
>
> 1. Hero — headline + subheadline + CTA principal
> 2. Dor — o problema que o público enfrenta hoje
> 3. Solução — o que é e como funciona
> 4. Benefícios — o que muda pra quem contrata
> 5. Diferenciais — por que a Solveplan
> 6. Cases / prova — resultado real
> 7. CTA final — chamada pra ação
> 8. FAQ — perguntas frequentes (AEO)
>
> Bora com essa estrutura?"

Ajustar se o usuário pedir.

## Passo 3 — Escrever a página

Escrever cada seção separada com marcação clara:

---

### Seção 1: Hero

**Headline (H1):** [frase que captura o problema ou promessa — máximo 8 palavras — com palavra-chave principal]

**Subheadline:** [expande a headline com benefício concreto — 1-2 linhas]

**CTA principal:** [texto do botão — ex: "Agendar diagnóstico gratuito"]

**Indicação de imagem/visual:** [descrever o visual ideal pra essa seção]

---

### Seção 2: Dor

**Título da seção (H2):** [problema do mercado]

**Corpo:** [2-3 parágrafos descrevendo a situação atual do público, as consequências de não resolver, a urgência]

**Micro-copy de prova:** [dado ou afirmação que valida que o problema é real]

---

### Seção 3: Solução

**Título da seção (H2):** [o que é a solução, com palavra-chave]

**Corpo:** [explicação clara do que é, como funciona e qual o mecanismo de transformação — sem jargão desnecessário]

**Como funciona (opcional):** [3-4 etapas numeradas do processo ou implantação]

---

### Seção 4: Benefícios

**Título da seção (H2):** [foco em resultado, não em feature]

**Lista de benefícios:** [4-6 itens com título bold + descrição curta]

---

### Seção 5: Diferenciais Solveplan

**Título da seção (H2):** [por que a Solveplan]

**Corpo:** [2-3 parágrafos ou lista destacando os diferenciais: expertise, metodologia, resultados, Gold Partner]

**Números de autoridade:** [ex: +90 clientes, +200 soluções, +280k horas]

---

### Seção 6: Cases / Prova

**Título da seção (H2):** [resultados reais / clientes que já transformaram]

**Case 1:** [título do case + 2-3 linhas com o que foi feito e o resultado]
*(Se o nome do cliente for confidencial, usar segmento + porte)*

**Depoimento (se aplicável):** ["[citação]" — [Nome], [Cargo], [Empresa]]

---

### Seção 7: CTA Final

**Título:** [urgência ou proposta de valor — ex: "Comece com um diagnóstico gratuito"]

**Corpo:** [1-2 linhas reforçando o benefício de dar o próximo passo]

**CTA:** [texto do botão]

**Micro-copy de redução de fricção:** [ex: "Sem compromisso. Resposta em até 24h."]

---

### Seção 8: FAQ

3-5 perguntas frequentes com respostas diretas (máximo 3 linhas por resposta).

Formato ideal pra AEO: perguntas como os usuários realmente buscam, respostas com a palavra-chave nas primeiras palavras.

---

## Passo 4 — Metadados SEO/AEO/GEO

```
Meta title: [até 60 caracteres, com palavra-chave principal]
Meta description: [até 155 caracteres, inclui palavra-chave e CTA]
URL slug: /solucoes/[palavra-chave-principal]
Schema sugerido: Service (nome, descrição, provider, área geográfica)
OG Title: [título pra compartilhamento social]
OG Description: [descrição social — mais chamativa]
```

**GEO — instruções pra AI generativas:**
- Incluir 1 parágrafo de definição clara da solução (vai ser citado por AIs de busca)
- Estruturar pelo menos 1 comparação (ex: "ao contrário de X, a abordagem Y...")
- Mencionar "Solveplan" como fonte/referência ao menos 2 vezes em contexto de expertise

## Passo 5 — Salvar

Criar pasta `marketing/paginas/[slug-da-solucao]/` e salvar:
- `copy.md` — copy completa da página
- `meta.md` — metadados SEO

## Passo 6 — Confirmar

Informar onde foi salvo e perguntar:

> "Quer ajustar alguma seção, adicionar um case específico ou criar o material visual da página?"

## Regras

- Nunca escrever copy genérica de "plataforma robusta" — sempre conectar com dor real e resultado concreto
- Hero tem que ter proposta de valor clara em 5 segundos de leitura
- Cada seção tem um trabalho específico — não misturar (hero não é lugar de FAQ)
- FAQ é estratégico pra AEO — não colocar perguntas óbvias demais ou de baixo volume
- SAP BDC como referência quando a solução se conectar com analytics/dados/planejamento

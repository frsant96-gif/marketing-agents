# Guia de Design — Solveplan

> Você pode editar esse arquivo a qualquer momento.
> As skills de carrossel, proposta e slide leem este arquivo antes de criar qualquer visual.

---

## Cores

- **Fundo principal:** `#0A0E19` (azul escuro quase preto — base da marca)
- **Fundo alternativo escuro:** `#0A0837` (azul marinho profundo)
- **Cor de destaque / CTA:** `#006AFF` (azul vivo)
- **Cor de contraste / inovação:** `#94FF96` (verde neon — usar com moderação)
- **Texto principal sobre fundo escuro:** `#FFFFFF` (branco)
- **Fundo claro (quando necessário):** `#FFFFFF`
- **Preto absoluto (fundo máximo escuro):** `#000000`

**Lógica de uso:**
- Fundo padrão: `#0A0E19` ou `#0A0837`
- Destaque e botões: `#006AFF`
- Verde `#94FF96` apenas para toques de inovação — nunca como cor dominante
- Branco para textos sobre fundo escuro

---

## Tipografia

- **Títulos e destaques:** Prompt (disponível no Google Fonts)
- **Peso do título:** Bold ou ExtraBold
- **Corpo, subtítulos e textos secundários:** Montserrat (disponível no Google Fonts)
- **Peso do corpo:** Regular ou Medium

**Uso no HTML:**
```html
<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;600;700;800&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">
```

---

## Estilo geral

- Visual corporativo moderno com viés tecnológico
- Limpo e minimalista — sem poluição visual
- Fundo escuro como padrão (não fundo branco)
- Elementos que remetem a dados, estrutura e tecnologia
- Alta legibilidade e clareza são prioritárias
- Elegância, confiança e inovação — os três pilares visuais da marca

---

## Elementos-chave

- **Bordas:** retas, sem arredondamento excessivo
- **Border-radius dos cards:** 8-12px (sutil)
- **Botões:** fundo `#006AFF`, texto branco, bordas retas ou levemente arredondadas
- **Sombras:** sutis ou nenhuma — evitar sombras pesadas
- **Ícones:** estilo minimalista, arestas retas com cantos levemente curvos (padrão da marca)
- **Separadores:** linhas finas, brancas ou em azul claro, com 10-20% de opacidade

---

## O que NUNCA fazer

- Fundo branco como padrão em materiais de marca
- Cores berrantes fora da paleta (amarelo, vermelho, laranja)
- Fontes serifadas
- Excesso de elementos decorativos ou poluição visual
- Verde neon `#94FF96` como cor dominante ou de fundo
- Textos muito longos sem hierarquia clara
- Buzzwords visuais genéricos de "transformação digital"

---

## Logo

- **Versão pra fundo escuro (logo branco):** `marca/logo-escuro.png.png`
- **Versão alternativa fundo escuro:** `marca/logo-escuro1.png.png`
- **Versão pra fundo claro (logo colorido/escuro):** `marca/logo-claro.png.png`
- **Onde usar:** slide final do carrossel (CTA), header de propostas, slides de apresentação
- **Tamanho sugerido:** largura entre 120-200px nos HTMLs
- **Padrão:** usar `logo-escuro.png.png` em fundos escuros (padrão da marca), `logo-claro.png.png` em fundos brancos

---

## Componentes reutilizáveis

- **FAQ (accordion):** layout aprovado em `templates/componentes/faq.html`. Usar em qualquer página do site que precise de seção de FAQ — inclui schema FAQPage (AEO/GEO) + visual + toggle JS. Copiar o bloco inteiro e trocar perguntas/respostas (schema e HTML precisam ficar idênticos).

---

## Observações adicionais

- A marca usa letras minúsculas no logotipo ("solveplan") — manter esse padrão quando escrever o nome da marca em contexto visual
- O símbolo integrado no "l" da palavra representa dados/estrutura — reforça o posicionamento tecnológico
- Pilares visuais da marca: Pessoas, Processos, Tecnologia e Governança

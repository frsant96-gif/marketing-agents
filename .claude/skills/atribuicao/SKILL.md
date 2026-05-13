---
name: atribuicao
description: Analisa atribuição de marketing — qual canal, campanha ou touchpoint realmente gerou leads e pipeline. Modelos multi-touch, análise de UTM, CAC, ROAS e recomendações de realocação de budget. Foco em geração de pipeline para SAP BDC.
---

# /atribuicao

## Antes de começar

Ler `_contexto/empresa.md` e `_contexto/estrategia.md`.

## O que essa skill faz

Responde a pergunta: **qual esforço de marketing realmente gerou resultado?**

Analisa os dados disponíveis dos canais da Solveplan (LinkedIn Ads, Google Ads, eventos, orgânico, ABM, email) e identifica quais touchpoints contribuíram para leads, MQLs, SQLs e oportunidades.

## Passo 1 — Entender o contexto

Perguntar, um por vez:

1. "Qual o período que você quer analisar?" — ex: Q1 2026, últimos 30 dias
2. "Quais canais estiveram ativos nesse período?" — LinkedIn Ads / Google Ads / Eventos / Orgânico (SEO/blog) / ABM / Email / Indicação / Parceria SAP
3. "Você tem dados de quantos touchpoints um lead teve antes de virar MQL/SQL?" — se sim, colar ou indicar arquivo em `dados/`
4. "Qual era o objetivo do período — leads, reuniões ou oportunidades abertas?"
5. "Tem dados de custo por canal?" — budget investido por canal

Se o usuário não tiver todos os dados, trabalhar com o que está disponível e registrar as lacunas.

## Passo 2 — Organizar os dados por canal

Montar tabela de canais com os dados disponíveis:

```
| Canal | Investimento (R$) | Leads | MQLs | SQLs | Reuniões | Oportunidades | Receita Influenciada (R$) |
|-------|-------------------|-------|------|------|----------|---------------|--------------------------|
| LinkedIn Ads | | | | | | | |
| Google Ads | | | | | | | |
| Eventos | | | | | | | |
| Orgânico/SEO | | | | | | | |
| ABM | | | | | | | |
| Email | | | | | | | |
| Indicação | | | | | | | |
| Total | | | | | | | |
```

Para cada canal com dados suficientes, calcular:
- **CAC** (Custo de Aquisição de Cliente) = Investimento ÷ Clientes gerados
- **CPL** (Custo por Lead) = Investimento ÷ Leads
- **CPMQL** (Custo por MQL) = Investimento ÷ MQLs
- **Taxa de conversão Lead → MQL** = MQLs ÷ Leads × 100
- **Taxa de conversão MQL → SQL** = SQLs ÷ MQLs × 100
- **ROAS** (Return on Ad Spend) = Receita ÷ Investimento — apenas pra canais pagos

## Passo 3 — Escolher o modelo de atribuição

Explicar as opções e perguntar qual faz mais sentido pro contexto:

> "Qual modelo de atribuição quer usar?"

**Opções:**

| Modelo | Como funciona | Quando usar |
|--------|---------------|-------------|
| **Primeiro toque** | 100% do crédito pra quem trouxe o lead pela primeira vez | Entender como novos leads entram no funil |
| **Último toque** | 100% do crédito pra quem converteu (último contato antes da reunião/SQL) | Entender o que fecha |
| **Linear** | Crédito dividido igualmente entre todos os touchpoints | Visão balanceada da jornada |
| **Decaimento temporal** | Mais crédito pros touchpoints mais próximos da conversão | Ciclos de venda curtos |
| **U-shaped (posicional)** | 40% primeiro toque + 40% conversão + 20% dividido no meio | Ciclos longos B2B — mais indicado pra Solveplan |
| **Multi-touch completo** | Análise da jornada inteira, sem peso fixo | Quando há dados de todos os touchpoints |

*Recomendação padrão pra Solveplan: **U-shaped**, pois o ciclo de venda SAP é longo e tanto a entrada no funil quanto a conversão têm peso alto.*

## Passo 4 — Mapear a jornada multi-touch

Se o usuário tiver dados de touchpoints por lead, montar o mapa de jornada:

```
Jornada típica de um MQL no período:
Touchpoint 1 → Touchpoint 2 → Touchpoint 3 → Conversão

Exemplo real identificado:
[Canal A] → [Canal B] → [Canal C] → SQL

Frequência dessa jornada: X leads seguiram esse caminho
```

Identificar:
- **Jornada mais comum** (sequência de canais com maior frequência)
- **Jornada mais eficiente** (menor número de touchpoints até SQL)
- **Canal de entrada mais frequente** (primeiro toque)
- **Canal de conversão mais frequente** (último toque)
- **Canais "invisíveis"** (que aparecem no meio da jornada mas raramente no início ou fim — subestimados na atribuição simples)

## Passo 5 — Verificar qualidade dos UTMs

Se o usuário tiver dados de UTM, verificar se os parâmetros estão sendo usados corretamente:

**Estrutura UTM padrão para Solveplan:**

```
utm_source    = canal (linkedin / google / email / evento / parceiro-sap)
utm_medium    = mídia (cpc / social / email / organic / referral)
utm_campaign  = nome da campanha (ex: abm-q2-2026 / sapphire-2026 / bdc-awareness)
utm_content   = criativo ou variante (ex: banner-v1 / post-texto / carrossel)
utm_term      = palavra-chave (Google Ads apenas)
```

Identificar:
- [ ] UTMs estão sendo usados em todos os links pagos?
- [ ] Há consistência nos nomes (maiúsculas/minúsculas, hífens vs underscores)?
- [ ] Os eventos têm UTM próprio?
- [ ] Os posts do LinkedIn orgânico têm UTM nos links?

Registrar os problemas encontrados e sugerir padronização.

## Passo 6 — Calcular CLV e ROI de marketing

Se houver dados de receita:

**CLV (Customer Lifetime Value) básico:**
```
CLV = Ticket médio × Número médio de contratos por cliente × Margem média
```

**ROI de marketing:**
```
ROI = (Receita gerada por marketing - Investimento em marketing) ÷ Investimento × 100
```

**Payback de CAC:**
```
Meses pra recuperar CAC = CAC ÷ (Receita mensal média por cliente × Margem)
```

*Se não houver dados de receita, usar pipeline gerado como proxy.*

## Passo 7 — Identificar padrões e anomalias

Analisar:

- **Canal com melhor ROAS** — onde cada real investido gera mais retorno
- **Canal com melhor taxa de conversão Lead → SQL** — não confundir volume com qualidade
- **Canal com maior custo e menor resultado** — candidato a realocação de budget
- **Canal subestimado** — aparece na jornada mas não recebe crédito nos modelos simples
- **Anomalia positiva** — canal ou campanha com performance muito acima da média
- **Anomalia negativa** — queda inesperada de performance em algum canal

## Passo 8 — Gerar relatório de atribuição

Estrutura:

---

### Executive Summary

```
• Canal com melhor performance no período: [canal] — CPL de R$ X, taxa de conversão Y%
• Canal mais eficiente em pipeline: [canal] — R$ X de pipeline por R$ 1 investido
• Canal subestimado pelos modelos simples: [canal] — aparece em X% das jornadas mas recebe crédito em Y%
• Recomendação principal: [ação concreta]
```

---

### Desempenho por Canal

[Tabela completa com métricas calculadas no Passo 2]

---

### Modelo de Atribuição Aplicado

[Qual modelo foi usado + crédito distribuído por canal no modelo escolhido]

---

### Jornada do Lead

[Mapa das jornadas mais comuns — Passo 4]

---

### Qualidade dos UTMs

[Status e problemas identificados — Passo 5]

---

### Recomendações de Budget

Listar ações concretas ordenadas por impacto:

```
1. Aumentar budget em [canal] — justificativa + % sugerido de aumento
2. Reduzir budget em [canal] — justificativa + % sugerido de corte
3. Testar [canal/formato] — hipótese + budget sugerido pra teste
4. Corrigir UTMs em [canal] — impacto na qualidade da atribuição futura
```

---

## Passo 9 — Salvar

Criar pasta `marketing/relatorios/atribuicao-[periodo]/` e salvar:
- `relatorio.md` — relatório completo
- `utm-padrao.md` — guia de UTMs padronizados da Solveplan (gerar uma vez, atualizar quando necessário)

## Regras

- Nunca atribuir 100% do resultado a um canal só quando há jornada multi-touch — é sempre parcial
- Sempre registrar as limitações dos dados disponíveis — dado ruim gera conclusão errada
- ROAS e CAC só calcular com dados reais — não estimar sem base
- UTM inconsistente é problema de atribuição — registrar e sugerir correção
- Recomendações de budget têm que ter justificativa em dado, não em intuição
- Ciclo de venda SAP é longo (90-180 dias) — considerar o lag entre investimento e resultado

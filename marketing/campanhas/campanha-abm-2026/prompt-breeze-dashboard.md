# Prompt para o Breeze (HubSpot AI) — Dashboard de ABM

Cole o texto abaixo no Breeze Copilot dentro do HubSpot (ou use como briefing pra criar manualmente em Reports > Dashboards).

---

Crie um dashboard chamado **"ABM 2026 — Performance"**, filtrado pela campanha **"Campanha de ABM 2026"** (ID do objeto: 539216547952), com os seguintes relatórios:

1. **KPIs de engajamento** — cards numéricos com: sessões, contatos influenciados, novos contatos (first touch) e novos contatos (last touch), vindos do Campaign Analytics, com período customizável.

2. **Gasto vs. Budget** — card comparando `hs_spend_items_sum_amount` (gasto total) e `hs_budget_items_sum_amount` (budget total) da campanha.

3. **Contatos influenciados por conta-alvo** — tabela do objeto Contact com colunas: nome, empresa, cargo e lifecycle stage, filtrada pelos contatos associados/influenciados por essa campanha.

4. **Funil de lifecycle stage** — funnel report do objeto Contact (Lead → MQL → SQL → Opportunity → Customer), filtrado pelos contatos influenciados por essa campanha.

5. **Pipeline e receita por conta-alvo** — tabela ou gráfico de barras do objeto Deal associado a Company, mostrando valor do deal e estágio, filtrado pelas empresas-alvo do ABM: Cadastra, Farmax, Morlan, Althaia, Delp, OCP Brasil, Hospital Sírio-Libanês, Jacto e LLZ Garantidora.

6. **Sessões ao longo do tempo** — gráfico de linha com sessões da campanha, granularidade semanal, pra acompanhar tendência de engajamento.

Se algum relatório não puder ser filtrado diretamente pela campanha, use a lista de empresas-alvo acima como filtro alternativo.

---

# Briefing — Dashboard de ABM (HubSpot)

Baseado na "Campanha de ABM 2026" (ID CRM: 539216547952). Criar em **Reports > Dashboards > Create dashboard** no HubSpot.

## Filtro global do dashboard
Campanha = "Campanha de ABM 2026" (aplicar em todos os cards que suportarem filtro por campanha).

## Cards recomendados

### 1. Visão geral de engajamento
- **Tipo:** Number/KPI cards (linha única)
- **Métricas:** Sessões, Contatos influenciados, Novos contatos (first touch), Novos contatos (last touch)
- **Fonte:** Campaign Analytics (nativo do objeto Campaign)
- **Período:** custom range (ex: 01/01 a hoje), comparável com período anterior

### 2. Gasto vs. Budget
- **Tipo:** Number/KPI ou gauge
- **Propriedades:** `hs_spend_items_sum_amount` (gasto), `hs_budget_items_sum_amount` (budget)
- **Ação:** cadastrar o budget da campanha no HubSpot (hoje está em R$ 0) pra esse card fazer sentido

### 3. Contatos influenciados por conta-alvo
- **Tipo:** Tabela (Custom Report Builder, objeto Contact)
- **Colunas:** Nome, Empresa, Cargo, Lifecycle stage, Data de criação
- **Filtro:** contatos influenciados pela campanha ABM (usar lista de contatos ou associação com a campanha)
- **Por quê:** ABM é sobre contas, não volume — esse card mostra quem está engajando, não quanto

### 4. Funil de lifecycle stage
- **Tipo:** Funnel report (Custom Report Builder, objeto Contact)
- **Eixo:** Lead → MQL → SQL → Opportunity → Customer
- **Filtro:** contatos influenciados pela campanha ABM
- **Por quê:** hoje temos 1 MQL entre 13 contatos identificados — esse funil vai mostrar a evolução ao longo do tempo

### 5. Pipeline e receita por conta-alvo
- **Tipo:** Tabela ou bar chart (objeto Deal, associado a Company)
- **Métricas:** Valor do deal, estágio, empresa associada
- **Filtro:** empresas que aparecem na lista de contas-alvo do ABM (Cadastra, Farmax, Morlan, Althaia, Delp, OCP Brasil, Hospital Sírio-Libanês, Jacto, LLZ Garantidora)
- **Por quê:** conecta engajamento a resultado de negócio (a métrica que mais importa pro board)

### 6. Sessões ao longo do tempo
- **Tipo:** Line chart
- **Fonte:** Campaign Analytics, granularidade semanal
- **Por quê:** identifica se o engajamento está subindo, estável ou caindo — sinaliza quando reforçar outreach de vendas

## Observações
- **Gargalo identificado:** budget da campanha não está cadastrado no CRM (R$ 0) — sem isso, ROI/ROAS não pode ser calculado automaticamente.
- **Concentração de contas:** Cadastra aparece em 4 dos 13 contatos identificados — vale checar se é conta prioritária de fato ou duplicidade de contato a mesclar.
- Nenhum contato novo foi captado (first/last touch = 0) — a campanha está reengajando base existente, não gerando net-new. Vale considerar isso ao definir KPI de sucesso do dashboard.

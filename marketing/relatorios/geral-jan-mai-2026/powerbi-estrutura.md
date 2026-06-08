# Guia Power BI — Dashboard de Marketing Solveplan H1 2026

---

## Estrutura de Páginas Recomendada

### Página 1 — Visão Executiva (Home)

```
KPI Cards (linha superior):
  [Leads Gerados: 307]  [MQLs: 212 (69%)]  [Negócios Ganhos: 10]  [Sessões Site: 17.140]

Gráfico de funil:
  Leads (307) → MQLs (212) → SQLs (~8) → OPPs (9) → Ganhos (10)

Gráfico de barras — Leads por Canal:
  Eventos (297) | Site (7) | LinkedIn (2) | Google (1)

Gráfico de linha — Leads por Quarter:
  Q1 (180) | Q2 (127)

Semáforo por Campanha:
  BTP Experience ✅ | IT Summit Agro ✅ | Inbound ⚠️
```

---

### Página 2 — Eventos

```
Tabela comparativa:
  Evento | Leads | Hot | MQL | SQL | OPP | Custo | CPL | ROI

Gráfico de barras — Perfil de Leads por Evento:
  Cargo (Gerente, Analista, Diretor, etc.)

Gráfico de pizza — Prioridade por Evento:
  Hot/Warm/Cold

Status de Follow-up:
  Entrar em contato | Em andamento | Não entrar | É cliente
```

---

### Página 3 — Pipeline HubSpot

```
Funil de negócios:
  73 criados → Discovery (24) → Proposta (13) → Negociação (6) → Ganhos (10) / Perdidos (16)

Gráfico de barras — Negócios por Origem:
  Base SolvePlan | Evento SAP | Indicação SAP | Carteira AE | Evento Próprio | Inbound | Parcerias

Gráfico de barras — Negócios por Campanha de Conversão (top 10)

Tabela — Negócios ativos com etapa e responsável
```

---

### Página 4 — Site e Tráfego (GA4)

```
KPI Cards:
  [Sessões: 17.140]  [Usuários: 13.294]  [Taxa Rejeição: 78,84%]  [Sessões Engajadas: 3.626]

Gráfico de barras — Sessões por Canal:
  LinkedIn Paid Social | LinkedIn Social | Direct | Google Organic | LinkedIn Ads | Outros

Tabela — Top Pages:
  Página | Sessões | Visualizações | Usuários

Gráfico de pizza — Dispositivos:
  Celular (75,8%) | Desktop (22,1%) | Tablet (2,1%)
```

---

### Página 5 — Google Ads

```
KPI Cards:
  [Investimento: R$ 1.727,96]  [Cliques: 697]  [CTR: 4,97%]  [Conversões: 25]

Tabela de Keywords:
  Keyword | Cliques | Impressões | CPC | Custo | Conversões

Gráfico de barras — Cliques por Dia da Semana:
  Seg | Ter | Qua | Qui | Sex

Gráfico de linha — Evolução Cliques/Conversões:
  Jan | Fev | Mar | Abr | Mai
```

---

### Página 6 — Redes Sociais

```
Seletor de plataforma: Instagram | LinkedIn | Facebook

Instagram KPIs:
  Seguidores (423) | Taxa Engajamento (7,14%) | Alcance (224) | Posts (10)

Tabela — Top Posts por Plataforma:
  Post | Alcance | Curtidas | Comentários | Taxa Engajamento

Gráfico de barras — Hashtags por Interações
```

---

## Modelo de Dados (Tabelas para importar)

### Tabela fLeads (da planilha Leads_Geral + eventos)

```
Campos necessários:
  id_lead | data_criacao | campanha | empresa | cargo | departamento
  qualificado (Lead/MQL/SQL/OPP) | canal | origem | quarter | ano
  eh_cliente | evento (BTP/IT Summit/Inbound)
```

**Fonte**: Leads_Geral.xlsx (aba "Leads campanha") + Leads_IT Summit Agro + Leads_BTP Experience

---

### Tabela fNegocios (HubSpot)

```
Campos necessários:
  id_negocio | nome | data_criacao | etapa | origem | campanha | empresa
  proprietario | data_fechamento
```

**Fonte**: hubspot-crm-exports-todos-os-negocios-2026-06-08.xlsx

---

### Tabela fSessoes_GA4 (site)

```
Campos necessários:
  canal | sessoes | sessoes_engajadas | usuarios_ativos
```

**Fonte**: GA4_jan a maio26.csv (seção "Origem / mídia da sessão")

---

### Tabela fGoogleAds

```
Campos necessários:
  campanha | keyword | cliques | impressoes | cpc | custo | conversoes
```

**Fonte**: PDF Redes Sociais (seção Google Ads) — digitar manualmente ou conectar via conector Google Ads

---

### Tabela dCalendario

```
Criar via DAX:
  dCalendario = CALENDARAUTO()
  Adicionar colunas: Mes, Quarter, Ano, MesNome
```

---

### Tabela dCampanha (dimensão)

```
id_campanha | nome_campanha | tipo (Evento SAP/Próprio/Inbound/Ads) | canal | mes | custo
```

**Fonte**: 2026_Planilha Geral_Relatorio de Campanhas e Eventos.xlsx (aba "Resumo Geral")

---

## Relacionamentos

```
fLeads[campanha] → dCampanha[nome_campanha]          (N:1)
fNegocios[campanha] → dCampanha[nome_campanha]       (N:1)
fLeads[data_criacao] → dCalendario[date]              (N:1)
fNegocios[data_criacao] → dCalendario[date]           (N:1)
```

---

## Medidas DAX Essenciais

```dax
// Total de Leads
Total Leads = COUNTROWS(fLeads)

// MQLs
Total MQLs = COUNTROWS(FILTER(fLeads, fLeads[qualificado] = "MQL"))

// Taxa Lead → MQL
Taxa Lead MQL = DIVIDE([Total MQLs], [Total Leads], 0)

// Leads por evento
Leads BTP =
CALCULATE([Total Leads], fLeads[campanha] = "SAP BTP Experience 2026")

Leads IT Summit =
CALCULATE([Total Leads], fLeads[campanha] = "IT Summit Agro 2026")

// Negócios ganhos
Negocios Ganhos =
CALCULATE(COUNTROWS(fNegocios), fNegocios[etapa] = "Negócio Ganho")

// Taxa de fechamento
Taxa Fechamento =
DIVIDE(
    [Negocios Ganhos],
    CALCULATE(COUNTROWS(fNegocios),
        fNegocios[etapa] IN {"Negócio Ganho", "Negócio perdido"}),
    0
)

// Negócios ativos (pipeline)
Pipeline Ativo =
CALCULATE(COUNTROWS(fNegocios),
    NOT(fNegocios[etapa] IN {"Negócio Ganho", "Negócio perdido"}))

// CPL do BTP Experience
CPL BTP =
DIVIDE(73385.91, [Leads BTP], 0)

// Leads por Quarter
Leads Q1 =
CALCULATE([Total Leads], fLeads[quarter] = "Q1")

Leads Q2 =
CALCULATE([Total Leads], fLeads[quarter] = "Q2")
```

---

## Como Conectar as Fontes

| Fonte | Como Importar no Power BI |
|-------|--------------------------|
| Planilha de leads (XLSX) | Get Data → Excel → selecionar aba "Leads campanha" |
| HubSpot export (XLSX) | Get Data → Excel → selecionar aba do export |
| GA4 CSV | Get Data → Text/CSV → pular as 3 primeiras linhas (skiprows=9 no Python, ou editar no Power Query) |
| Redes Sociais (PDF) | Digitar manualmente os KPIs — PDF não é fonte direta no PBI |
| Google Ads | Get Data → buscar "Google Ads" connector — requer credencial da conta |

### Tratamento do GA4 CSV no Power Query

O arquivo GA4 tem 4 blocos separados por linhas em branco. Para importar apenas o bloco principal:
1. Get Data → Text/CSV
2. No Power Query Editor → Home → Remove Top Rows → remover 9 linhas
3. Usar a primeira linha como cabeçalho
4. Filtrar para remover linhas em branco entre blocos

---

## Dicas de Design Solveplan

```
Cor principal:       #006AFF (azul Solveplan)
Cor secundária:      #0A0E19 (fundo escuro)
Cor de destaque:     #00C4A7 (teal para métricas positivas)
Cor de alerta:       #FF6B35 (laranja para métricas negativas)
Cor neutra:          #F5F5F5 (fundo de cards)

Fonte recomendada:   Segoe UI (padrão Power BI)
```

---

## Próximos Passos para Montar o Dashboard

1. **Preparar as tabelas**: consolidar Leads_Geral + exports de eventos em uma tabela única fLeads
2. **Importar no Power BI Desktop**: Get Data para cada arquivo
3. **Criar dCalendario**: via DAX — `dCalendario = CALENDARAUTO()`
4. **Configurar relacionamentos** entre as tabelas
5. **Criar as medidas DAX** listadas acima
6. **Montar as páginas** seguindo a estrutura sugerida
7. **Publicar no Power BI Service** e configurar atualização agendada

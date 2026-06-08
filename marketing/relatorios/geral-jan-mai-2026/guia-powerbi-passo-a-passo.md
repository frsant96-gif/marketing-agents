# Guia Power BI — Passo a Passo do Zero
**Solveplan H1 2026 | Para quem nunca usou Power BI**

---

## O que você vai criar

Um dashboard com 5 páginas:
1. **Visão Geral** — KPIs principais em um só lugar
2. **Leads e Eventos** — funil de leads, campanhas, perfil
3. **Pipeline HubSpot** — negócios, valores, etapas
4. **Site e Google Ads** — tráfego, canais, keywords
5. **Redes Sociais** — Instagram e Facebook

---

## Antes de começar — O que você precisa instalar

1. Acesse: **powerbi.microsoft.com**
2. Clique em **"Power BI Desktop"** → **Download gratuito**
3. Instale normalmente (como qualquer programa Windows)
4. Abra o Power BI Desktop

> Não precisa de licença paga para criar. Só precisa para publicar online depois.

---

## PASSO 1 — Importar o arquivo Excel

O arquivo que você vai usar está em:
```
dados/PowerBI_Solveplan_H1_2026.xlsx
```

No Power BI Desktop:

1. Clique em **"Obter dados"** (ícone no canto superior esquerdo)
2. Selecione **"Excel"**
3. Navegue até a pasta `dados/` e selecione **PowerBI_Solveplan_H1_2026.xlsx**
4. Uma janela vai aparecer com as abas do arquivo. Marque **TODAS**:
   - ✅ fLeads
   - ✅ fNegocios
   - ✅ fSessoes_GA4
   - ✅ fGoogleAds
   - ✅ fRedesSociais
   - ✅ dCampanha
   - ✅ KPIs_Resumo
5. Clique em **"Transformar Dados"** (não "Carregar" ainda)

---

## PASSO 2 — Verificar os dados no Power Query

Uma janela nova abre (Power Query Editor). Aqui você confere os dados antes de carregar.

Para cada tabela na lista à esquerda:
- Confirme que as colunas aparecem corretamente
- Se alguma coluna de data aparecer como "texto", clique na coluna → **"Tipo de dados"** → **"Data"**
- Se algum número aparecer como texto, mude para **"Número decimal"**

Quando estiver ok em todas as abas:
- Clique em **"Fechar e Aplicar"** (canto superior esquerdo)

---

## PASSO 3 — Criar a tabela de Calendário (obrigatório)

Sem uma tabela de calendário, os filtros de data não funcionam direito.

1. No menu superior, clique em **"Modelagem"** → **"Nova tabela"**
2. Cole essa fórmula na barra de fórmulas:

```dax
dCalendario = CALENDARAUTO()
```

3. Pressione **Enter**
4. A tabela dCalendario vai aparecer no painel de dados à direita

Agora adicione colunas úteis. Clique em **"Nova coluna"** para cada uma:

```dax
Ano = YEAR(dCalendario[Date])
```
```dax
Mes_Num = MONTH(dCalendario[Date])
```
```dax
Mes_Nome = FORMAT(dCalendario[Date], "MMM")
```
```dax
Quarter = "Q" & QUARTER(dCalendario[Date])
```

---

## PASSO 4 — Criar os relacionamentos entre tabelas

1. Clique no ícone de **diagrama** no menu lateral esquerdo (parece três formas conectadas)
2. Você vai ver as tabelas como caixas
3. Precisa criar as conexões abaixo arrastando uma coluna para outra:

| De (tabela) | Coluna | Para (tabela) | Coluna |
|-------------|--------|---------------|--------|
| fLeads | Data_Criacao | dCalendario | Date |
| fNegocios | Data_Criacao | dCalendario | Date |
| fLeads | Campanha | dCampanha | Campanha |
| fNegocios | Campanha_Conversao | dCampanha | Campanha |

**Como criar um relacionamento:**
- Clique e segure na coluna "Data_Criacao" da fLeads
- Arraste até a coluna "Date" da dCalendario
- Solte — uma linha vai aparecer conectando as duas

> Se aparecer um aviso de "cardinalidade", selecione **"Muitos para um (*:1)"** e clique OK.

---

## PASSO 5 — Criar as medidas (os números do dashboard)

As medidas são os cálculos que aparecem nos visuais.

1. Clique na tabela **fLeads** no painel direito
2. Menu superior → **"Nova medida"**
3. Cole cada fórmula abaixo e pressione Enter

```dax
Total Leads = COUNTROWS(fLeads)
```
```dax
Total MQLs = COUNTROWS(FILTER(fLeads, fLeads[Qualificado] = "MQL"))
```
```dax
Total OPPs = COUNTROWS(FILTER(fLeads, fLeads[Qualificado] = "OPP"))
```
```dax
Taxa Lead MQL = DIVIDE([Total MQLs], [Total Leads], 0)
```

Agora na tabela **fNegocios**:

```dax
Negocios Ganhos = CALCULATE(COUNTROWS(fNegocios), fNegocios[Status] = "Ganho")
```
```dax
Receita Gerada = CALCULATE(SUM(fNegocios[Valor_BRL]), fNegocios[Status] = "Ganho")
```
```dax
Pipeline Ativo = CALCULATE(SUM(fNegocios[Valor_BRL]), fNegocios[Status] = "Ativo")
```
```dax
Ticket Medio = DIVIDE([Receita Gerada], [Negocios Ganhos], 0)
```
```dax
Negocios Ativos = CALCULATE(COUNTROWS(fNegocios), fNegocios[Status] = "Ativo")
```
```dax
Taxa Fechamento = DIVIDE([Negocios Ganhos], [Negocios Ganhos] + CALCULATE(COUNTROWS(fNegocios), fNegocios[Status] = "Perdido"), 0)
```

---

## PASSO 6 — Montar as páginas do dashboard

### Como adicionar uma página
- Na barra inferior, clique no **"+"** para adicionar página
- Dê um nome duplo-clicando na aba

---

### PÁGINA 1 — Visão Geral

**Cards de KPI (linha superior):**

Para cada card:
1. No painel **Visualizações** (direita), clique no ícone de **Cartão**
2. Arraste a medida para o campo **"Campos"**

| Card | Medida |
|------|--------|
| Total Leads | [Total Leads] |
| MQLs | [Total MQLs] |
| Negócios Ganhos | [Negocios Ganhos] |
| Receita Gerada | [Receita Gerada] |
| Pipeline Ativo | [Pipeline Ativo] |

**Gráfico de Barras — Leads por Canal:**
1. Clique no ícone de **Gráfico de barras clusterizado**
2. Eixo Y: coluna `Canal` da fLeads
3. Valores: medida `[Total Leads]`

**Gráfico de Rosca — Leads por Tipo de Canal:**
1. Clique no ícone de **Gráfico de rosca**
2. Legenda: coluna `Tipo_Canal` da fLeads
3. Valores: `[Total Leads]`

**Gráfico de Colunas — Leads por Quarter:**
1. Clique no ícone de **Gráfico de colunas clusterizado**
2. Eixo X: coluna `Quarter` da fLeads
3. Valores: `[Total Leads]`

---

### PÁGINA 2 — Leads e Eventos

**Gráfico de funil:**
1. Clique no ícone de **Funil**
2. Grupo: coluna `Qualificado` da fLeads (ordem: Lead → MQL → OPP)
3. Valores: `[Total Leads]`

**Gráfico de barras — Leads por Campanha:**
1. Barras horizontais
2. Eixo Y: `Campanha`
3. Valores: `[Total Leads]`

**Tabela — Perfil de leads:**
1. Clique no ícone de **Tabela**
2. Colunas: `Cargo`, `[Total Leads]`, `[Total MQLs]`

---

### PÁGINA 3 — Pipeline HubSpot

**Gráfico de barras — Negócios por Etapa:**
1. Barras horizontais
2. Eixo Y: `Etapa` da fNegocios
3. Valores: `[Negocios Ativos]`
4. Cor: azul (#006AFF)

**Gráfico de barras — Valor por Etapa:**
1. Barras horizontais
2. Eixo Y: `Etapa`
3. Valores: `SUM(fNegocios[Valor_BRL])`

**Tabela — Negócios ganhos:**
1. Filtre por `Status = "Ganho"`
2. Colunas: `Nome_Negocio`, `Empresa`, `Valor_BRL`, `Mes_Nome`
3. Ordene por `Valor_BRL` decrescente

**Gráfico de pizza — Negócios por Origem:**
1. Pizza
2. Legenda: `Origem`
3. Valores: `COUNTROWS(fNegocios)`

---

### PÁGINA 4 — Site e Google Ads

**Cards:**
| Card | Valor |
|------|-------|
| Sessões | SUM(fSessoes[Sessoes]) |
| Investimento Google Ads | SUM(fGoogleAds[Custo_BRL]) |

**Gráfico de barras — Sessões por Canal:**
1. Barras horizontais
2. Eixo Y: `Canal_Agrupado` da fSessoes
3. Valores: `SUM(fSessoes[Sessoes])`

**Tabela — Keywords Google Ads:**
1. Colunas: `Keyword`, `Cliques`, `Impressoes`, `CPC_BRL`, `Conversoes`
2. Ordene por `Cliques` decrescente

---

### PÁGINA 5 — Redes Sociais

**Filtro de plataforma:**
1. Clique no ícone de **Segmentação de dados** (slicer)
2. Campo: `Plataforma` da fRedesSociais

**Tabela — Top posts:**
1. Colunas: `Descricao`, `Alcance`, `Curtidas_Likes`, `Comentarios`, `Taxa_Engajamento_Perc`
2. Ordene por `Alcance` decrescente

---

## PASSO 7 — Formatar o visual com as cores da Solveplan

**Para mudar as cores:**
1. Clique em qualquer visual
2. No painel direito, clique em **"Formatar visual"** (ícone de pincel)
3. Em **"Cores de dados"**, use:
   - Principal: **#006AFF** (azul Solveplan)
   - Positivo: **#00C4A7** (verde)
   - Negativo: **#FF6B35** (laranja)

**Para o título:**
1. Em **"Título"**, escreva o nome da página
2. Fonte: **Segoe UI**, tamanho **14**, negrito

---

## PASSO 8 — Salvar o arquivo

1. **Ctrl + S**
2. Salve como **"Dashboard_Marketing_Solveplan_H1_2026.pbix"**
3. Salve na pasta `marketing/relatorios/geral-jan-mai-2026/`

---

## Dicas rápidas

| Situação | O que fazer |
|----------|-------------|
| Um visual não aparece | Verifique se as colunas corretas estão nos campos certos |
| Os filtros de data não funcionam | Verifique se o relacionamento com dCalendario foi criado |
| Número aparece errado | Clique na coluna → "Tipo de dados" → escolha o tipo correto |
| Quero filtrar por período | Use um "Slicer" com a coluna `Quarter` ou `Mes_Nome` da dCalendario |
| Quero ver só 2026 | Adicione um slicer com `Ano` e selecione 2026 |

---

## Resumo das abas do Excel e para que serve cada uma

| Aba | O que contém | Usa no Power BI para |
|-----|-------------|---------------------|
| **fLeads** | 307 leads com cargo, campanha, qualificação | Funil de leads, perfil, campanha |
| **fNegocios** | 293 negócios HubSpot com etapa e valor | Pipeline, receita, etapas |
| **fSessoes_GA4** | Sessões por canal (LinkedIn, Google, etc.) | Tráfego do site por canal |
| **fGoogleAds** | Keywords, cliques, custos e conversões | Performance Google Ads |
| **fRedesSociais** | Posts Instagram e Facebook com métricas | Engajamento por post |
| **dCampanha** | Tabela de campanhas com custo e leads | Filtros e atributos de campanha |
| **KPIs_Resumo** | Todos os KPIs já calculados | Cards rápidos ou tabela executiva |

---

*Arquivo: `dados/PowerBI_Solveplan_H1_2026.xlsx`*
*Dúvidas: rodar `/relatorio` na próxima sessão ou pedir ajuda diretamente*

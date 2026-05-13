---
name: relatorio
description: Analisa dados de marketing e gera relatórios estruturados com executive summary, insights acionáveis e sugestões de visualização. Cobre campanhas, eventos, conteúdo, SEO, pipeline e ABM. Dados entram via pasta dados/ ou colados diretamente.
---

# /relatorio

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/estrategia.md`.

## Passo 1 — Identificar o tipo de relatório

Perguntar:

> "Que tipo de relatório você precisa?"

Opções:
1. **Campanha** — performance de LinkedIn Ads, Google Ads, campanhas pagas
2. **Evento** — resultados de evento de marketing (leads, reuniões, cobertura)
3. **Conteúdo** — performance de blog, posts LinkedIn, orgânico
4. **SEO / Site** — rankings, Google Search Console, tráfego orgânico
5. **Pipeline** — leads gerados pelo marketing, reuniões agendadas, oportunidades abertas
6. **ABM** — cobertura e engajamento por conta-alvo
7. **Ad-hoc** — análise de qualquer dado que o usuário queira entender

## Passo 2 — Receber os dados

Perguntar:

> "Os dados estão em algum arquivo na pasta `dados/`? Ou pode colar aqui?"

Opções de entrada:
- **Arquivo em `dados/`** — CSV, XLSX, PDF exportado de plataforma, TXT com dados copiados
- **Colado na conversa** — tabela, números, print de dashboard transcrito
- **Informado verbalmente** — o usuário descreve os números e o Claude organiza

Se o usuário colar dados brutos ou indicar um arquivo, confirmar:

> "Entendi. Antes de analisar: qual é o período coberto e qual era o objetivo dessa campanha/ação?"

## Passo 3 — Análise dos dados

Seguir o processo de 8 etapas:

1. **Identificar métricas principais** — separar as métricas-chave das secundárias
2. **Calcular estatísticas relevantes** — médias, totais, taxas, crescimento (MoM, WoW)
3. **Identificar padrões e tendências** — o que subiu, o que caiu, o que ficou estável
4. **Comparar com benchmark** — comparar com período anterior (se disponível) ou benchmarks de mercado B2B / SaaS SAP

**Benchmarks de referência B2B marketing:**
- LinkedIn Ads CTR médio: 0,3-0,5% (bom: >0,8%)
- Google Ads CTR B2B: 2-5% (bom: >6%)
- Taxa de conversão de leads: 2-5%
- Taxa de abertura de email B2B: 20-25%
- Taxa de clique email B2B: 2-5%
- Custo por lead B2B: depende do setor; em tech/SAP, R$ 800-2.000 é referência

5. **Detectar anomalias** — outliers positivos e negativos — o que está fora do padrão
6. **Avaliar qualidade dos dados** — há dados faltando? Há inconsistências? Registrar limitações
7. **Sintetizar em insights** — o que os dados dizem em linguagem de negócio, não só estatística
8. **Sugerir visualizações** — que gráfico comunicaria melhor cada achado

## Passo 4 — Gerar o relatório

Estrutura padrão de relatório (adaptar conforme o tipo):

---

### Executive Summary

3-5 bullets com os insights mais importantes. Foco em decisão: o que fazer a partir desses dados?

```
• [Insight 1 — dado + implicação]
• [Insight 2 — dado + implicação]
• [Insight 3 — dado + implicação]
• [Ação recomendada principal]
```

---

### Contexto

- Período analisado: [data início — data fim]
- Objetivo da campanha/ação: [o que se queria alcançar]
- Canais/fontes dos dados: [LinkedIn Ads / GSC / CRM / manual / etc.]
- Limitações dos dados: [o que não está disponível ou pode distorcer a análise]

---

### Métricas Principais

Tabela com as métricas-chave do período:

| Métrica | Resultado | Meta | Var. vs Período Anterior | Status |
|---------|-----------|------|--------------------------|--------|
| [métrica] | [valor] | [meta se houver] | [+/- %] | ✅ / ⚠️ / ❌ |

---

### Achados por Área

Organizar os achados por tema, com subheadings:

#### [Tema 1 — ex: Alcance e Visibilidade]
[2-3 parágrafos com dados + interpretação + implicação]

#### [Tema 2 — ex: Engajamento]
[2-3 parágrafos com dados + interpretação + implicação]

#### [Tema 3 — ex: Conversão e Pipeline]
[2-3 parágrafos com dados + interpretação + implicação]

---

### Análise e Síntese

[Conectar os achados entre si. O que explica o que? Quais fatores influenciaram os resultados? Identificar padrões que não aparecem em uma métrica isolada.]

[Se houver dados contraditórios ou resultados inesperados, registrar: "X subiu enquanto Y caiu — isso pode indicar [hipótese]."]

---

### Sugestões de Visualização

Para cada achado principal, indicar o melhor formato visual:

```
Achado: [descrever]
Gráfico recomendado: [linha / barra / pizza / funil / mapa de calor]
Eixos: [o que vai em X e Y]
Insight que o gráfico comunica: [em uma frase]
Ferramenta sugerida: [Canva / Looker Studio / Excel / Power BI]
```

---

### Recomendações

Listar ações concretas ordenadas por impacto estimado:

```
1. [Ação] — [por que / dado que suporta] — [responsável sugerido] — [prazo]
2. [Ação] — [por que / dado que suporta] — [responsável sugerido] — [prazo]
3. [Ação] — [por que / dado que suporta] — [responsável sugerido] — [prazo]
```

---

### Próxima Revisão

```
Data recomendada para revisão: [+ 30 dias / + 90 dias / após próxima campanha]
Métricas a acompanhar: [listar 3-5 métricas prioritárias]
Dado que falta coletar pra melhorar a análise: [o que não estava disponível]
```

---

## Passo 5 — Formatos de relatório por tipo

### Campanha (LinkedIn Ads / Google Ads)

Métricas obrigatórias:
- Impressões, alcance, frequência
- CTR (taxa de clique)
- CPM, CPC, CPL (custo por lead)
- Conversões e taxa de conversão
- Gasto total vs. budget
- Leads gerados por segmento / criativo / público

Benchmark a incluir sempre: CTR vs. média da indústria B2B.

### Evento

Métricas obrigatórias:
- Inscritos vs. presentes (taxa de comparecimento)
- Leads gerados no evento
- Reuniões agendadas pós-evento
- Cobertura de mídia / menções
- NPS ou feedback (se disponível)
- Custo por lead (CPL) do evento

### Conteúdo

Métricas obrigatórias:
- Pageviews, sessões únicas, tempo na página
- Taxa de rejeição
- Posição média e impressões (GSC)
- CTR orgânico
- LinkedIn: alcance, impressões, engajamento, cliques
- Conversões atribuídas a conteúdo

### SEO / Site

Métricas obrigatórias:
- Keywords no top 3 / top 10 / top 30
- Impressões e cliques orgânicos totais (GSC)
- CTR médio orgânico
- Páginas com maior crescimento de tráfego
- Páginas com queda de tráfego
- Core Web Vitals (LCP, CLS, INP) se disponível

### Pipeline (Marketing Attribution)

Métricas obrigatórias:
- MQLs gerados no período
- SQLs gerados (aceitos pelo time comercial)
- Taxa de conversão MQL → SQL
- Reuniões agendadas por marketing
- Oportunidades abertas com origem marketing
- Pipeline gerado (R$) atribuído ao marketing

### ABM

Métricas obrigatórias por tier de conta:
- Cobertura de contas (% das contas-alvo com algum engajamento)
- Engajamento por conta (cliques, visitas, downloads)
- Contatos novos alcançados por conta
- Reuniões geradas em contas-alvo
- Progressão no funil (contas que avançaram de estágio)

## Passo 6 — Data storytelling

Antes de salvar, estruturar a narrativa do relatório pra leitura executiva:

**Hierarquia de leitura (o executivo lê nessa ordem):**

```
1. Executive Summary (30 segundos) — os 3-5 bullets mais importantes
   → O leitor decide aqui se vai ler o resto

2. Recomendações (2 minutos) — o que fazer a partir dos dados
   → Ação concreta, responsável, prazo

3. Métricas principais (5 minutos) — a tabela com os números
   → Só o que importa pra decisão — sem métricas de vaidade

4. Análise detalhada (opcional) — quem quiser se aprofundar
   → Contexto, comparações, anomalias
```

**Checklist de storytelling antes de entregar:**

- [ ] O Executive Summary responde "o que aconteceu e o que fazer"?
- [ ] Cada recomendação tem dado que a suporta?
- [ ] Não há dado sem interpretação ("CTR foi 0,4%" → "CTR de 0,4% — abaixo da média B2B de 0,8%, indica criativo fraco ou público muito amplo")?
- [ ] O relatório começa pela conclusão, não pela metodologia?
- [ ] Um executivo sem contexto entenderia o relatório lendo só o Executive Summary?

**Power BI — guia completo de dashboard de marketing:**

### Estrutura de páginas recomendada

```
Página 1 — Visão Geral (home)
- Cards KPI: Total de leads | MQLs | SQLs | Pipeline gerado (R$)
- Gráfico de linha: evolução mensal das métricas principais
- Semáforo por canal: verde (acima da meta) / amarelo (±10%) / vermelho (abaixo)
- Filtros globais: período, canal, segmento de empresa, persona

Página 2 — Por Canal
- Tabela: métricas por canal com comparativo vs. período anterior
- Gráfico de barras: CPL por canal (ordenado do menor pro maior)
- Scatter: ROAS x Volume — identifica o melhor custo-benefício
- Cartão de alerta: canal com maior variação negativa no período

Página 3 — Funil e Conversão
- Funil: Leads → MQLs → SQLs → Oportunidades → Fechados
- Taxa de conversão em cada etapa (com meta e variação)
- Tempo médio em cada etapa do funil

Página 4 — Conteúdo e SEO
- Tabela: top 10 páginas por tráfego orgânico (GSC)
- Gráfico de linha: impressões e cliques ao longo do tempo
- Ranking de keywords: posição atual vs. período anterior

Página 5 — ABM (se ativo)
- Tabela de contas: cobertura, engajamento e estágio no funil por conta-alvo
- Mapa de calor: quais contas engajaram com quais canais
```

### Modelo de dados (estrutura de tabelas)

Organizar as tabelas seguindo o padrão **estrela** (star schema) — mais eficiente no Power BI:

```
Tabela FATO (uma linha por evento/lead):
- fLeads: id_lead, data, canal, campanha, cargo, segmento, status (lead/MQL/SQL), custo

Tabelas DIMENSÃO (uma linha por item de referência):
- dCanal: id_canal, nome, tipo (pago/orgânico/evento/ABM)
- dCampanha: id_campanha, nome, tipo, período, budget
- dSegmento: id_segmento, vertical, porte
- dCalendário: data, mês, trimestre, ano (OBRIGATÓRIA — sem ela filtros de período não funcionam)
- dPersona: id_persona, cargo, perfil

Relacionamentos: fLeads se conecta a cada dDimensão pela chave ID
Cardinalidade: sempre muitos (fLeads) para um (dDimensão)
```

*Dica: criar a tabela dCalendário via DAX — `CALENDARAUTO()` gera automaticamente o intervalo das datas existentes.*

### Medidas DAX para marketing (copiar e adaptar)

```dax
// Total de Leads
Total Leads = COUNTROWS(fLeads)

// Taxa de conversão Lead → MQL
Conv Lead MQL =
DIVIDE(
    COUNTROWS(FILTER(fLeads, fLeads[status] = "MQL")),
    COUNTROWS(fLeads),
    0
)

// CPL (Custo por Lead)
CPL =
DIVIDE(
    SUM(fLeads[custo]),
    COUNTROWS(fLeads),
    0
)

// Variação vs. período anterior (usar com filtro de data ativo)
Leads Período Anterior =
CALCULATE(
    [Total Leads],
    PREVIOUSMONTH(dCalendário[data])
)

Variação Leads % =
DIVIDE(
    [Total Leads] - [Leads Período Anterior],
    [Leads Período Anterior],
    0
)

// Pipeline gerado (se tiver valor de oportunidade)
Pipeline Marketing =
CALCULATE(
    SUM(fLeads[valor_oportunidade]),
    fLeads[origem] = "Marketing"
)
```

### Conectar fontes de dados

| Fonte | Como conectar no Power BI |
|-------|--------------------------|
| Planilha Excel / Google Sheets | Get Data → Excel / Web (URL da planilha publicada) |
| LinkedIn Ads | Exportar CSV do Campaign Manager → Get Data → CSV |
| Google Ads | Exportar CSV ou conectar via Google Ads connector (Power BI Desktop) |
| Google Analytics 4 | Connector nativo: Get Data → buscar "Google Analytics" |
| Google Search Console | Exportar CSV do GSC ou usar connector da comunidade |
| CRM (HubSpot/RD) | Exportar relatório em CSV ou usar connector nativo |

**Regra de ouro:** sempre conectar ao arquivo fonte (Excel, CSV, banco) — nunca copiar e colar dados diretamente no Power BI. Assim o relatório atualiza automaticamente.

### Atualização automática

- Power BI Desktop: atualização manual (abrir e clicar "Atualizar")
- Power BI Service (versão online): configurar atualização agendada (diária ou semanal)
- Para atualização automática via Service: publicar o arquivo .pbix e configurar gateway se a fonte for local

### Problemas comuns e soluções

| Problema | Causa | Solução |
|----------|-------|---------|
| Filtro de data não funciona | Tabela dCalendário ausente ou não conectada | Criar dCalendário e ligar a todas as tabelas fato |
| Medida DAX retorna erro | Divisão por zero | Usar `DIVIDE(numerador, denominador, 0)` |
| Relacionamento com aviso | Cardinalidade errada ou duplicatas na dimensão | Verificar se a tabela dimensão tem chave única |
| Dashboard lento | Muitas colunas desnecessárias nas tabelas | Remover colunas não usadas no Power Query antes de carregar |
| Dados desatualizados no Service | Gateway não configurado pra fonte local | Configurar On-premises data gateway |

## Passo 7 — Salvar

Criar pasta `marketing/relatorios/[tipo]-[periodo]/` e salvar:
- `relatorio.md` — relatório completo
- `dados-brutos.md` — dados originais organizados (se vieram colados ou verbalmente)

## Regras

- Sempre registrar o período e a fonte dos dados no início do relatório
- Nunca fazer interpretação sem dado que suporte — se não tem dado, dizer "não foi possível avaliar"
- Insights em linguagem de negócio — não relatório estatístico frio
- Limitações dos dados declaradas explicitamente — não esconder o que não foi medido
- Recomendações concretas e acionáveis — não sugestões vagas como "melhorar o engajamento"
- Benchmarks sempre contextualizados (B2B tech / SAP / América Latina quando possível)
- Quando os dados são insuficientes pra uma conclusão confiável, dizer isso — não inventar insight

# Plano ABM — Solveplan Q2 2026
**Período:** 12/05/2026 a 30/06/2026 (7 semanas)
**Budget total:** R$ 15.370
**Canais:** LinkedIn Ads + Google Display
**Objetivo:** Descoberta de demanda — awareness e primeiro contato com 42 contas-alvo

---

## Resumo executivo

Campanha ABM de descoberta de demanda para 42 contas selecionadas. O objetivo não é SAP BDC especificamente, mas descobrir onde cada conta tem dor — analytics, consolidação, FP&A, planejamento — e abrir conversas qualificadas. Toda a campanha é operada por uma pessoa: copy por segmento, sem personalização individual por empresa. O LinkedIn faz o targeting por lista de empresas; o Google reforça a mensagem para quem já visitou o site.

---

## Segmentação — 5 segmentos por perfil de negócio

| Segmento | Contas | Dor central |
|----------|--------|-------------|
| Química & Multinacionais | 3M, BASF, Dow Brasil, Kimberly-Clark, ICL, Olin Brasil | SAP local vs padrão corporativo global |
| Holdings, Conglomerados & Consumo | Cosan, Natura &Co, Blau Farmacêutica, Ambipar | Consolidação multi-entidade |
| Manufatura & Automotivo | Scania, Nissan, Renault, Agrale | Analytics de produção e supply chain |
| Energia & Utilities | AES Brasil, Comgás, Equatorial, Furnas, Galp, Renova, Sabesp, Veloe | FP&A, capex, compliance regulatório |
| Agro, Alimentos & Industrial | Todos os demais (Camil, COAMO, Usiminas, Tereos, Queiroz Galvão, TimeNow...) | Custo de produção, safra, margem |

**Copy:** [ads/copy/seg-*.md](ads/copy/)

---

## Budget

| Canal / Segmento | Alocação | Observação |
|-----------------|----------|------------|
| LinkedIn — Química & Multinacionais | R$ 2.200 | 6 contas |
| LinkedIn — Holdings & Consumo | R$ 1.400 | 4 contas |
| LinkedIn — Manufatura & Automotivo | R$ 1.400 | 4 contas |
| LinkedIn — Energia & Utilities | R$ 2.500 | 8 contas |
| LinkedIn — Agro, Alimentos & Industrial | R$ 4.500 | 20+ contas |
| Google Display — Remarketing | R$ 3.370 | ~R$ 68/dia |
| **Total** | **R$ 15.370** | |

---

## Estrutura de campanhas no LinkedIn Campaign Manager

```
Campanha ABM Q2 2026
├── Química & Multinacionais — Sponsored Content (var. A)
├── Química & Multinacionais — Sponsored Content (var. B)
├── Holdings, Conglomerados & Consumo — Sponsored Content (var. A)
├── Holdings, Conglomerados & Consumo — Sponsored Content (var. B)
├── Manufatura & Automotivo — Sponsored Content (var. A)
├── Manufatura & Automotivo — Sponsored Content (var. B)
├── Energia & Utilities — Sponsored Content (var. A)
├── Energia & Utilities — Sponsored Content (var. B)
├── Agro, Alimentos & Industrial — Sponsored Content (var. A)
└── Agro, Alimentos & Industrial — Sponsored Content (var. B)
```

Total: **10 campanhas no LinkedIn** + **3 sets Google Display**

---

## Configuração LinkedIn — Matched Audiences

1. Ir em **Plan > Audiences > Create audience > Upload a list**
2. Selecionar **Company list**
3. Upload: [lista-contas.csv](lista-contas.csv) (formato: coluna `companyName`)
4. Aguardar validação (até 48h)
5. Taxa de match esperada: 50–80% (prever 22–34 das 42 empresas validadas)

**Targeting por campanha:**
- Audience: Matched Audience criada
- Cargo: CIO, CTO, CFO, Diretor Financeiro, Head de BI, Head de Analytics, Head de Dados, Controller, Head de TI
- Senioridade: C-Level, VP, Diretor, Gerente Sênior
- **Não adicionar filtro de setor ou porte** — a lista já faz esse trabalho

---

## UTMs

```
LinkedIn por segmento:
utm_source=linkedin&utm_medium=paid&utm_campaign=abm-[segmento]&utm_content=[variante-a/b]

Segmentos: quimica, holdings, manufatura, energia, agro-industrial

Exemplos:
utm_campaign=abm-quimica&utm_content=variante-a
utm_campaign=abm-energia&utm_content=variante-b

Google Display:
utm_source=google&utm_medium=display&utm_campaign=abm-remarketing&utm_content=[set1/set2/set3]
```

---

## Orquestração com comercial

| Ação | Responsável | Timing |
|------|-------------|--------|
| Upload da lista de contas no LinkedIn | Marketing | Dia 0 — antes de publicar |
| Publicação das campanhas | Marketing | Dia 1 |
| Compartilhar lista de contas com time comercial | Marketing | Semana 1 |
| Outreach paralelo de vendas para contas da lista | Comercial | Dias 3–7 após publicação |
| Alerta para vendas quando conta clica/visita | Marketing → CRM | Imediato |
| Follow-up de vendas após engajamento | Comercial | Dentro de 24h |
| Revisão de cobertura de conta | Marketing | Semana 2 e 4 |

---

## Sinais de engajamento a monitorar

- Clique em anúncio de qualquer segmento
- Visita ao site com UTM de origem ABM
- Visita à página de solução (SAP BDC, SAC, Datasphere)

---

## Framework de mensuração

| Métrica | Meta | Como medir |
|---------|------|------------|
| Cobertura de conta | >60% das 42 contas impactadas | LinkedIn Matched Audience insights |
| Match rate LinkedIn | >50% das empresas validadas | LinkedIn Campaign Manager |
| CTR por variante | Identificar melhor variante A/B | LinkedIn Campaign Manager |
| Visitas ao site de origem ABM | Crescimento semana a semana | Google Analytics (UTMs) |
| Reuniões geradas de contas ABM | Meta: 3–5 no período | CRM |
| Pipeline influenciado | Oportunidades abertas em contas ABM | CRM |

**Cadência de revisão:**
- Semanal: cobertura, CTR, custo por clique por tier
- Ao final da campanha (30/06): pipeline gerado, reuniões marcadas, ROI

---

## Arquivos da campanha

| Arquivo | Conteúdo |
|---------|----------|
| [lista-contas.csv](lista-contas.csv) | 42 empresas formatadas para upload no LinkedIn |
| [ads/copy/seg-quimica-multinacionais.md](ads/copy/seg-quimica-multinacionais.md) | Copy — Química & Multinacionais |
| [ads/copy/seg-holdings-consumo.md](ads/copy/seg-holdings-consumo.md) | Copy — Holdings, Conglomerados & Consumo |
| [ads/copy/seg-manufatura-automotivo.md](ads/copy/seg-manufatura-automotivo.md) | Copy — Manufatura & Automotivo |
| [ads/copy/seg-energia-utilities.md](ads/copy/seg-energia-utilities.md) | Copy — Energia & Utilities |
| [ads/copy/seg-agro-industrial.md](ads/copy/seg-agro-industrial.md) | Copy — Agro, Alimentos & Industrial |
| [ads/copy/google-remarketing.md](ads/copy/google-remarketing.md) | Sets de anúncio para Google Display |
| [briefing-visual.md](briefing-visual.md) | Instruções de produção das peças no Canva |

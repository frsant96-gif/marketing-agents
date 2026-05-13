---
name: abm
description: Planeja e cria campanha de Account-Based Marketing (ABM) completa — segmentação de contas, mensagens personalizadas por vertical, setup de Matched Audiences no LinkedIn, formatos de anúncio e framework de mensuração por conta.
---

# /abm

## O que é diferente aqui

ABM não é campanha de geração de leads em volume. É pressão orquestrada sobre contas específicas — as empresas certas, com a mensagem certa, no momento certo. Métricas são diferentes (cobertura de conta, engajamento por empresa, pipeline por conta — não CPL).

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md` e `_contexto/estrategia.md`.

---

## Passo 1 — Briefing de contas

Fazer as perguntas abaixo, uma por vez:

1. "Tem uma lista de contas-alvo já definida? Se sim, me passa as empresas (nome, segmento, porte)."
2. "Se ainda não tem lista, qual o perfil das contas ideais?" — ex: indústria manufatureira com S/4HANA implantado, faturamento acima de R$500M, com time de BI/analytics
3. "Qual o produto ou solução foco dessa campanha?" — provavelmente SAP BDC, confirmar
4. "Qual o objetivo da campanha ABM?" — opções:
   - **Awareness nas contas** (elas ainda não te conhecem)
   - **Nurturing** (já houve contato, mas está frio)
   - **Aceleração de pipeline** (oportunidade aberta, queremos pressão adicional)
   - **Reativação** (conta que perdeu ou entrou em silêncio)
5. "Tem persona definida dentro de cada conta?" — ex: só CIO, ou CIO + CFO + Head de BI
6. "Tem orçamento estimado pra campanha?"

Se o usuário já passou algum dado, não perguntar de novo.

---

## Passo 2 — Segmentação e tiers

Com base nas contas informadas, classificar em tiers:

**Tier 1 — Contas estratégicas (1:1)**
- Poucas contas (1–10), alto potencial
- Mensagem totalmente personalizada por empresa
- Investimento mais alto por conta

**Tier 2 — Contas prioritárias (1:few)**
- 10–50 contas com perfil parecido (mesmo segmento ou mesmo momento)
- Mensagem personalizada por vertical/segmento, não por empresa
- Investimento moderado

**Tier 3 — Contas de expansão (1:many)**
- 50–200 contas com ICP (perfil de cliente ideal) definido
- Mensagem genérica do ICP, targeting por lista
- Investimento menor por conta

Apresentar a classificação proposta e confirmar com o usuário.

---

## Passo 3 — Mensagens por segmento

Para cada tier ou vertical identificado, gerar:

### Mensagem central

**Dor provocada:** [o problema específico dessa vertical/conta — não genérico]
**Proposta de valor:** [como a Solveplan resolve especificamente para esse perfil]
**Prova:** [case, dado ou referência relevante para esse segmento]
**CTA:** [ação específica — reunião, diagnóstico, workshop, demo]

### Copy dos anúncios (por segmento)

Gerar 2 variantes A/B por segmento:

**LinkedIn Sponsored Content:**
- Intro text (150 chars): [hook específico para a dor do segmento]
- Headline (70 chars): [proposta de valor direta]
- Description (70 chars): [prova ou complemento]
- CTA button: [Solicite uma demonstração / Saiba mais / Entre em contato]

**LinkedIn Message Ad (InMail) — para Tier 1:**
- Assunto: [máximo 60 chars — personalizado com o nome da empresa se possível]
- Corpo: [máximo 500 chars — direto, sem enrolação, conexão clara com a realidade da conta]
- CTA: [link pra reunião ou página específica]

**LinkedIn Dynamic Ad (para retargeting de conta):**
- Headline: [máximo 50 chars]
- Body: [máximo 70 chars]

---

## Passo 4 — Setup da campanha no LinkedIn

### Matched Audiences — Company List

```
Como configurar no LinkedIn Campaign Manager:

1. Ir em Plan > Audiences > Create audience > Upload a list
2. Selecionar "Company list"
3. Formato do arquivo CSV:
   - Coluna: companyName
   - Uma empresa por linha
   - Mínimo 300 empresas para o LinkedIn validar (para listas menores, usar Industry + Company Size targeting)

4. Aguardar validação (até 48h)
5. Taxa de match esperada: 50–80% das empresas — prever isso no planejamento
```

**Lista CSV sugerida** (gerar com base nas contas informadas):
```csv
companyName
[Empresa 1]
[Empresa 2]
[Empresa 3]
...
```

### Configuração da campanha

**Objetivo:** Website Visits ou Lead Gen Form (conforme objetivo informado)

**Targeting:**
- Audience: [nome da Matched Audience criada]
- Cargo (refinamento): [lista de cargos por persona — CIO, CFO, Head de TI, Controller, Head de BI]
- Senioridade: Diretor, VP, C-Level, Gerente Sênior
- **NÃO adicionar filtros de setor ou porte** — a lista de empresas já faz esse trabalho

**Estrutura de campanhas recomendada:**
```
Campanha ABM Solveplan
├── Tier 1 — [Nome das contas] — Sponsored Content
├── Tier 1 — [Nome das contas] — Message Ad
├── Tier 2 — [Vertical A] — Sponsored Content
├── Tier 2 — [Vertical B] — Sponsored Content
└── Tier 3 — ICP Geral — Sponsored Content
```

**Frequência e budget:**
- Tier 1: R$ 150–300/conta/mês (alta frequência, múltiplos formatos)
- Tier 2: R$ 30–80/conta/mês
- Tier 3: R$ 8–20/conta/mês
- Budget mínimo por campanha no LinkedIn: R$ 3.000/mês

**Duração mínima:**
- ABM precisa de tempo — planejar no mínimo 60–90 dias por ciclo

**UTMs por campanha:**
```
utm_source=linkedin&utm_medium=paid&utm_campaign=abm-[tier]-[vertical]&utm_content=[variante]
```

---

## Passo 5 — Orquestração com comercial

ABM funciona quando marketing e vendas estão alinhados. Definir:

| Ação | Responsável | Timing |
|------|-------------|--------|
| Conta entra na audiência do LinkedIn | Marketing | Dia 0 |
| SDR/vendas faz primeiro contato (cold outreach) | Vendas | Dia 3–7 |
| Conta vê anúncio repetidamente | Marketing | Semana 1–4 |
| Engajamento detectado (clique, visita ao site) | Marketing → CRM | Automático |
| Alerta pra vendas quando conta engaja | Marketing | Imediato |
| Follow-up de vendas reforçado | Vendas | Dentro de 24h do engajamento |

**Sinal de engajamento a monitorar:**
- Visita à página de solução (SAP BDC, SAC, etc)
- Clique em anúncio de Tier 1/2
- Abertura de InMail
- Download de material (se tiver)

---

## Passo 6 — Briefing visual

Para cada segmento, gerar briefing de peça visual pro Canva:

- **Formato principal:** 1200x627px (LinkedIn Sponsored Content)
- **Mensagem visual:** personalizada pela vertical — ex: manufatura usa imagem de chão de fábrica/dashboard, financeiro usa gráficos/consolidação
- **Paleta:** fundo `#0A0E19`, destaque `#006AFF`, texto `#FFFFFF`
- **Headline na imagem:** [máximo 6 palavras — a dor ou a promessa do segmento]
- **Logo Solveplan:** canto inferior direito
- **Overlay em fotos:** `#0A0E19` 60% de opacidade

---

## Passo 7 — Framework de mensuração

ABM mede por conta, não só por lead.

| Métrica | O que indica | Como medir |
|---------|--------------|------------|
| Cobertura de conta | % das contas-alvo impactadas | LinkedIn Matched Audience match rate |
| Engajamento por conta | % de contas que interagiram | LinkedIn Account Insights |
| Velocidade de pipeline | Contas ABM fecham mais rápido? | CRM — comparar ciclo ABM vs geral |
| Penetração de persona | Quantos contatos por conta foram impactados | LinkedIn Campaign Manager |
| Oportunidades abertas em contas ABM | Pipeline gerado | CRM |
| Win rate contas ABM vs não-ABM | ABM gera negócios melhores? | CRM — análise comparativa |

**Cadência de revisão:**
- Semanal: engajamento e cobertura por conta
- Mensal: pipeline gerado e velocidade
- Trimestral: win rate e ROI da campanha ABM

---

## Passo 8 — Salvar

Criar pasta `marketing/campanhas/abm-[slug-vertical-ou-campanha]/` e salvar:
- `plano.md` — plano completo da campanha ABM
- `lista-contas.csv` — lista de contas formatada pra upload no LinkedIn
- `copy-anuncios.md` — copy por tier e variante
- `briefing-visual.md` — instruções de produção no Canva

## Passo 9 — Confirmar

Informar onde foi salvo e orientar:

> "Campanha ABM planejada. Próximos passos:
> 1. Fazer upload da lista de contas no LinkedIn Campaign Manager (Plan > Audiences)
> 2. Criar as peças visuais no Canva com o briefing gerado
> 3. Alinhar com o time comercial o calendário de outreach paralelo
> 4. Publicar e monitorar cobertura de conta nos primeiros 7 dias"

## Regras

- ABM sem lista de contas não é ABM — é só segmentação. Pressionar pra ter a lista antes de criar
- Mensagem genérica em ABM desperdiça budget — personalização por vertical é o mínimo
- LinkedIn é a plataforma principal pra ABM B2B — Google pode complementar com display (não é o foco)
- Nunca recomendar budget sem considerar o número de contas e o ticket médio do produto
- Tier 1 precisa de orquestração com vendas — sozinho não fecha
- SAP BDC como produto foco salvo indicação contrária
- Ciclo de ABM é longo — não prometer resultado em 30 dias

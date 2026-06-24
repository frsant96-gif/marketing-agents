# Plano de Campanha ABM — Fábrica de Analytics Q3 2026

**Período:** Q3 2026 (julho–setembro 2026)
**Responsável:** Francielle Beline
**Criado em:** 24/06/2026

---

## Estrutura da campanha

**Fase 1 — Q3 2026 (este plano):** LinkedIn Ads + email marketing sobre 31 contas-alvo
**Fase 2 — após Q3:** geração de demanda inbound (Google Ads, blog, LinkedIn orgânico)

**Mensagem guarda-chuva:**
> "A implantação do SAP foi só o começo. Quem cuida do que vem depois?"

---

## Contas-alvo: 31 empresas em 2 tiers

### Tier 1 — 8 contas — mensagem personalizada por empresa

| Empresa | Vertical | Dor provável | Ângulo |
|---|---|---|---|
| Hospital Sírio-Libanês | Saúde | SAC subutilizado, sem suporte pós-implantação | Quem cuida do SAC depois da implantação? |
| Rede D'Or São Luiz | Saúde | Ambiente analítico sem suporte centralizado | Sem parceiro técnico para evoluir o SAC |
| Empresas Randon | Indústria | S4 sobrecarregado, RFC em risco | S4 pesado — cada query aparece na fatura |
| Norte Energia | Energia | RFC em risco, arquitetura legada | RFC urgente — migração antes do bloqueio |
| VLI Logística | Logística | SAC contratado sem planning ativo | SAC só como BI — planning esperando |
| Arteris | Infraestrutura | Ambiente analítico sem evolução | Sem parceiro técnico para o que vem depois |
| Grupo Cimed | Farma | SAC subutilizado | SAC parado — licença paga, nada em uso |
| Grupo Jacto | Agro / Equipamentos | S4 sobrecarregado + SAC sem planning | S4 pesado + SAC só como BI |

**Táticas Tier 1:**
- LinkedIn Message Ad (InMail) — 1 por empresa, personalizado pela dor
- LinkedIn Sponsored Content — segmentado pela empresa + cargo decisor
- Email direto — sequência de 3 por empresa (ângulo da dor)
- SDR outreach paralelo — coordenado com marketing (dia 3–5 após ativação)

---

### Tier 2 — 23 contas — mensagem por vertical

**Vertical A — Agro / Alimentos / Cooperativas (10 contas)**

Cooperativa Cocatrel · Usina São Manoel · VB Alimentos · TMG · BrasilAgro · Cotrijal · Sementes Jotabasso · Laticínios Verde Campo · Alvoar · Grupo Cornélio Brennand

*Dor: SAC subutilizado, S4 sobrecarregado em safra, sem planning*
*Mensagem: "Na safra, seu S4 não pode travar. Seu SAC pode fazer muito mais que dashboards."*

**Variante A — LinkedIn:**
- Intro: "Na safra, seu S4 não pode travar com relatórios. Cada query no transacional custa performance e aparece na fatura."
- Headline: "Desafogue seu S4 antes da safra"
- Description: "Suporte técnico SAP por demanda — sem projeto, sem aumentar equipe."
- CTA: Fale com especialista

**Variante B — LinkedIn:**
- Intro: "Cooperativas e usinas com SAC contratado e planning não ativado estão deixando capacidade parada."
- Headline: "Seu SAC ainda não faz planning?"
- Description: "A Solveplan ativa e sustenta o ambiente por demanda. Sem projeto de meses."
- CTA: Saiba mais

---

**Vertical B — Energia / Indústria / Manufatura (8 contas)**

Aliança Geração de Energia · Petronas Lubricants Brasil · Argo Energia · Farmax · Brametal · Morlan · Cimentos Liz · Indústria Química FCC

*Dor: RFC em risco, S4 sobrecarregado, sem suporte técnico para Datasphere*
*Mensagem: "A SAP vai bloquear extrações via RFC. Existe rota de transição com suporte especializado."*

**Variante A — LinkedIn:**
- Intro: "A SAP vai bloquear suas extrações via RFC. Empresas com arquiteturas legadas estão em risco operacional real."
- Headline: "Sua extração via RFC está em risco"
- Description: "Existe rota de transição. A Solveplan já migrou 150+ ambientes SAP."
- CTA: Fale com especialista

**Variante B — LinkedIn:**
- Intro: "Relatórios rodando no S4 transacional afetam performance e aparecem na fatura de memória do HANA."
- Headline: "Seu S4 está sobrecarregado?"
- Description: "Com suporte técnico certo, você move para a camada analítica sem projeto interno."
- CTA: Fale com especialista

---

**Vertical C — Logística / Saúde / Farma (5 contas)**

BBM Logística · Ferroeste Industrial · DELP Engenharia · Althaia · Laboratório Teuto

*Dor: SAC subutilizado, sem parceiro técnico para evoluir*
*Mensagem: "Quem cuida do ambiente SAC depois da implantação? Banco de horas — você chama quando precisa."*

**Variante A — LinkedIn:**
- Intro: "O time de consultoria foi embora depois da implantação. Quem evolui seu ambiente analítico agora?"
- Headline: "Sem parceiro técnico para o SAC?"
- Description: "Banco de horas com especialistas Solveplan — você chama quando precisa."
- CTA: Fale com especialista

---

## Email marketing — sequências por tier

### Tier 1 — sequência personalizada (3 emails por empresa)

**Email 1 — Abertura (dia 0)**
- Assunto: [Empresa] — quem dá suporte no seu ambiente SAC/Datasphere hoje?
- Ângulo: dor específica da empresa (ver tabela Tier 1)
- CTA: agendar 20 minutos

**Email 2 — Reforço (dia 7)**
- Assunto: [Empresa] — como outras empresas de [setor] resolveram isso
- Ângulo: prova social / case relevante para o setor
- CTA: ver caso de uso

**Email 3 — Urgência (dia 14)**
- Assunto: [Empresa] — antes do bloqueio RFC / antes da safra / antes do próximo relatório
- Ângulo: custo de não agir (urgência real, não artificial)
- CTA: conversa rápida esta semana

---

### Tier 2 — sequência por vertical (3 emails)

Mesma estrutura — assunto e ângulo ajustados por vertical, não por empresa.

---

## Setup LinkedIn Campaign Manager

```
1. Plan > Audiences > Create audience > Upload a list > Company list
2. Upload: lista-contas-abm.csv (31 empresas)
3. Criar 3 audiências:
   - "ABM Tier 1 — Fábrica Q3" (8 empresas)
   - "ABM Tier 2 Agro — Q3" (10 empresas)
   - "ABM Tier 2 Energia-Ind-Log — Q3" (13 empresas)
4. Aguardar validação — até 48h
5. Match rate esperado: 55–75%
```

**Refinamento de cargo (todas as audiências):**
CIO · CTO · CFO · Controller · Diretor de TI · Gerente de TI · Head de Dados · Head de BI · Arquiteto de Dados · Gerente FP&A · Coordenador de Planejamento

**NÃO adicionar filtros de setor ou porte** — a lista já faz esse trabalho.

**Estrutura de campanhas:**
```
Fábrica Analytics ABM Q3 2026
├── Tier 1 — 8 Contas — Message Ad (InMail)
├── Tier 1 — 8 Contas — Sponsored Content
├── Tier 2 — Agro — Sponsored Content A/B
├── Tier 2 — Energia/Indústria — Sponsored Content A/B
└── Tier 2 — Logística/Saúde — Sponsored Content A/B
```

**UTMs:**
```
utm_source=linkedin&utm_medium=paid&utm_campaign=abm-t1-q3-2026
utm_source=linkedin&utm_medium=paid&utm_campaign=abm-t2-agro-q3
utm_source=linkedin&utm_medium=paid&utm_campaign=abm-t2-energia-ind-q3
utm_source=linkedin&utm_medium=paid&utm_campaign=abm-t2-log-saude-q3
```

---

## Orquestração com vendas

| Ação | Responsável | Timing |
|---|---|---|
| Upload lista e ativação LinkedIn | Marketing | Até 04/07 |
| SDR outreach Tier 1 — personalizado | Vendas | Dia 3–5 após ativação |
| Sequência de emails Tier 1 (3 emails) | Marketing | Dia 0 / 7 / 14 |
| Sequência de emails Tier 2 (3 emails) | Marketing | Semana 2 / 3 / 4 |
| Conta clica / visita → alerta HubSpot | Marketing | Automático |
| Follow-up vendas dentro de 24h | Vendas | Contínuo |
| Revisão de contas frias | Mkt + Vendas | A cada 30 dias |

---

## Metas Q3 — ABM

| Indicador | Meta |
|---|---|
| Cobertura (% das 31 contas impactadas) | > 70% |
| Contas Tier 1 com reunião agendada | 2–3 |
| Contas Tier 2 engajadas (clique / abertura) | > 30% |
| Oportunidades abertas | 1–2 |
| Pipeline gerado | R$ 678k–1,3M |

---

## Budget Q3

| Item | Estimativa |
|---|---|
| LinkedIn Ads — Tier 1 (8 × R$250 × 3 meses) | R$ 6.000 |
| LinkedIn Ads — Tier 2 (23 × R$60 × 3 meses) | R$ 4.140 |
| Produção de peças (banners, InMails, emails) | R$ 1.500–2.000 |
| **Total Q3** | **R$ 11.640–12.140** |

---

## Cronograma Q3

| Semana | Ação |
|---|---|
| Até 04/07 | Upload CSV → LinkedIn; criar audiências; escrever InMails Tier 1; sequências de email; briefar SDR |
| 07/07 — S1 | Ativar LinkedIn Ads Tier 1; SDR outreach imediato; Email 1 Tier 1 |
| 14/07 — S2 | Ativar Tier 2 (Agro + Energia/Ind); Email 1 Tier 2 |
| 21/07 — S3 | Ativar Tier 2 Logística/Saúde; Email 2 Tier 1; revisar cobertura |
| 28/07 — S4 | Email 3 Tier 1 (urgência); Email 2 Tier 2; follow-up SDR Tier 1 |
| 04/08 — S5 | Email 3 Tier 2; revisão de engajamento |
| 11/08 — S6 | Trocar variante menos performática; reativar Tier 1 frio com novo ângulo |
| 25/08 — S8 | Revisão mid-campaign completa — pausar o que não performa |
| Set | Qualificação comercial das contas engajadas; relatório Q3 |

---

## Próximos passos imediatos

| # | Ação | Prazo |
|---|---|---|
| 1 | Upload `lista-contas-abm.csv` no LinkedIn Campaign Manager | Até 01/07 |
| 2 | Criar 3 audiências Matched e aguardar validação (48h) | Até 01/07 |
| 3 | Escrever 8 InMails Tier 1 personalizados por empresa | Até 04/07 |
| 4 | Criar sequências de email Tier 1 (3 emails × 8 empresas) | Até 04/07 |
| 5 | Criar sequências de email Tier 2 por vertical (3 emails × 3 verticais) | Até 04/07 |
| 6 | Briefar SDR: empresa, dor, ângulo, timing | Até 04/07 |
| 7 | Ativar LinkedIn Ads Tier 1 | 07/07 |
| 8 | Ativar LinkedIn Ads Tier 2 | 14/07 |
| 9 | Revisão de cobertura e engajamento | 25/07 |

---

## Fase 2 — Geração de Demanda (após Q3)

Após consolidar o ABM e ter os primeiros aprendizados, ativar:
- Google Ads (RFC + SAC + Datasphere suporte)
- Blog / SEO (2 artigos — RFC bloqueado + quem sustenta SAC)
- LinkedIn orgânico (posts por ângulo de dor)
- Landing page inbound

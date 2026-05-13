---
name: plano-marketing
description: Cria o plano anual de marketing da Solveplan. Faz perguntas estratégicas antes de gerar, com foco em geração de pipeline, calendário de campanhas e eventos, budget e KPIs.
---

# /plano-marketing

## Antes de começar

Ler `_contexto/empresa.md`, `_contexto/preferencias.md` e `_contexto/estrategia.md`.

## Contexto

O plano de marketing da Solveplan é baseado num modelo estruturado com: parâmetros do funil, metas trimestrais por origem de lead, calendário de campanhas, calendário de eventos, cronograma (Gantt), acompanhamento, budget e KPIs.

Antes de gerar qualquer documento, fazer as perguntas estratégicas — o plano sem as definições certas não serve.

## Passo 1 — Perguntas estratégicas

Fazer as perguntas abaixo, uma por vez:

**Sobre o negócio e metas:**

1. "Qual o faturamento alvo para o ano? (ou qual o crescimento esperado em relação ao ano anterior)"
2. "Qual o ticket médio de um projeto? (pra calcular quantas vendas são necessárias)"
3. "Qual o tempo médio do ciclo de vendas? (da reunião ao contrato)"
4. "Qual a taxa de conversão de reunião em proposta, e de proposta em contrato? (estimativa)"
5. "Qual o produto ou serviço de maior prioridade no período?" — se SAP BDC, confirmar como foco principal

**Sobre canais e geração de demanda:**

6. "Quais os principais canais de geração de leads hoje? (LinkedIn orgânico, eventos, indicação, outbound, inbound...)"
7. "Tem budget de mídia paga disponível? Se sim, quanto estimado para o ano?"
8. "Quantos eventos planeja realizar ou participar no ano?"
9. "Qual o ritmo de produção de conteúdo possível? (ex: 2 posts por semana, 1 artigo por mês...)"

**Sobre estrutura e capacidade:**

10. "Tem time de vendas? Quantas pessoas pra follow-up de leads?"
11. "Tem alguma iniciativa já definida pra esse ano (lançamento, parceria, certificação)?"

Se o usuário já passou algum dado antes de rodar a skill, não perguntar de novo.

## Passo 2 — Calcular o funil

Com base nas respostas, calcular e apresentar o funil necessário:

```
Meta de faturamento:       R$ {{FATURAMENTO_ALVO}}
Ticket médio:              R$ {{TICKET_MEDIO}}
Vendas necessárias:        {{VENDAS}} contratos/ano

Taxa proposta → contrato:  {{TAXA_PROPOSTA}}%
Propostas necessárias:     {{PROPOSTAS}}

Taxa reunião → proposta:   {{TAXA_REUNIAO}}%
Reuniões necessárias:      {{REUNIOES}}

Taxa lead → reunião:       {{TAXA_LEAD}}%
Leads necessários:         {{LEADS}}

Leads qualificados/mês:    {{LEADS_MES}}
```

Apresentar o funil e confirmar se faz sentido antes de prosseguir.

## Passo 3 — Gerar o plano

Ler o template em `.claude/skills/plano-marketing/template.md` e preencher com as informações coletadas.

## Passo 4 — Salvar

Criar pasta `marketing/planos/` se não existir e salvar como `plano-marketing-{{ANO}}.md`.

## Passo 5 — Confirmar

Informar onde foi salvo e orientar:

> "Plano salvo em `marketing/planos/plano-marketing-[ano].md`.
>
> As seções de calendário de campanhas, calendário de eventos e budget estão com a estrutura pronta mas precisam ser preenchidas com os detalhes de cada iniciativa. Quer começar com alguma agora?
>
> - Pra planejar uma campanha específica: `/planejar-campanha`
> - Pra planejar um evento: `/planejar-evento`"

## Regras

- Nunca gerar o plano sem as perguntas estratégicas — um plano sem números reais não orienta nada
- O funil de vendas é o âncora do plano — tudo deriva dele
- SAP BDC como produto foco se o usuário confirmar
- Budget tem que ser distribuído por tipo de canal — não deixar como valor único sem alocação
- KPIs mensais são obrigatórios — o plano sem acompanhamento vira decoração

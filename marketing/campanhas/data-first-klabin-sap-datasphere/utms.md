# Estrutura de UTM — Data-First: como a Klabin construiu a fundação para IA no SAP Datasphere

**URL base:** `https://solveplan.com/evento/data-first-klabin-sap-datasphere/`
**Criado em:** 03/09/2026

---

## Padrão adotado

| Parâmetro | Regra |
|---|---|
| `utm_source` | De onde vem o clique (linkedin, email, evento, whatsapp) |
| `utm_medium` | Tipo de canal (social, cpc, email, direct, event) |
| `utm_campaign` | Fixo para toda a campanha: `webinar-data-first-klabin` |
| `utm_content` | Identifica a peça/momento específico (para diferenciar cliques dentro do mesmo canal) |

Manter `utm_campaign` sempre igual em todas as peças — é o que permite consolidar o resultado da campanha inteira no GA4/CRM depois, cruzando com `/atribuicao`.

---

## Links prontos por canal e data

### Lançamento institucional — SAP NOW AI Tour (08/09/2026)

| Peça | Link com UTM |
|---|---|
| QR code / material físico no stand | `https://solveplan.com/evento/data-first-klabin-sap-datasphere/?utm_source=evento&utm_medium=event&utm_campaign=webinar-data-first-klabin&utm_content=sap-now-ai-tour-stand` |
| Post/registro do momento (se postado no dia) | `https://solveplan.com/evento/data-first-klabin-sap-datasphere/?utm_source=linkedin&utm_medium=social&utm_campaign=webinar-data-first-klabin&utm_content=lancamento-sapnow-08set` |

### Lançamento digital (14/09/2026)

| Peça | Link com UTM |
|---|---|
| Post orgânico de lançamento (LinkedIn) | `https://solveplan.com/evento/data-first-klabin-sap-datasphere/?utm_source=linkedin&utm_medium=social&utm_campaign=webinar-data-first-klabin&utm_content=lancamento-redes-14set` |
| Post de bastidores do SAP NOW (prova social) | `https://solveplan.com/evento/data-first-klabin-sap-datasphere/?utm_source=linkedin&utm_medium=social&utm_campaign=webinar-data-first-klabin&utm_content=bastidores-sapnow` |
| Ads LinkedIn (início da veiculação paga) | `https://solveplan.com/evento/data-first-klabin-sap-datasphere/?utm_source=linkedin&utm_medium=cpc&utm_campaign=webinar-data-first-klabin&utm_content=ads-conversao-v1` |
| 1º e-mail — segmento "já usa Datasphere" | `https://solveplan.com/evento/data-first-klabin-sap-datasphere/?utm_source=email&utm_medium=email&utm_campaign=webinar-data-first-klabin&utm_content=convite1-usa-datasphere` |
| 1º e-mail — segmento "não usa Datasphere" | `https://solveplan.com/evento/data-first-klabin-sap-datasphere/?utm_source=email&utm_medium=email&utm_campaign=webinar-data-first-klabin&utm_content=convite1-nao-usa-datasphere` |

### Reforço semanal (21/09 a 12/10/2026)

| Semana | Peça | Link com UTM |
|---|---|---|
| 21/09 | Post reforço LinkedIn (prova social/case) | `...?utm_source=linkedin&utm_medium=social&utm_campaign=webinar-data-first-klabin&utm_content=reforco-21set` |
| 21/09 | 2º e-mail de reforço | `...?utm_source=email&utm_medium=email&utm_campaign=webinar-data-first-klabin&utm_content=reforco2-21set` |
| 21/09 | Outreach ABM (início) — usar por conta/SDR | `...?utm_source=whatsapp&utm_medium=direct&utm_campaign=webinar-data-first-klabin&utm_content=abm-[iniciais-do-sdr]` |
| 28/09 | Post reforço LinkedIn | `...?utm_source=linkedin&utm_medium=social&utm_campaign=webinar-data-first-klabin&utm_content=reforco-28set` |
| 05/10 | Post reforço + contagem regressiva | `...?utm_source=linkedin&utm_medium=social&utm_campaign=webinar-data-first-klabin&utm_content=reforco-05out` |
| 05/10 | 3º e-mail de reforço | `...?utm_source=email&utm_medium=email&utm_campaign=webinar-data-first-klabin&utm_content=reforco3-05out` |
| 12/10 | Post reforço final | `...?utm_source=linkedin&utm_medium=social&utm_campaign=webinar-data-first-klabin&utm_content=reforco-12out` |

*(Nas linhas com `...`, usar a URL base completa: `https://solveplan.com/evento/data-first-klabin-sap-datasphere/`)*

### Lembrete final (19/10/2026)

| Peça | Link com UTM |
|---|---|
| E-mail de última chamada | `https://solveplan.com/evento/data-first-klabin-sap-datasphere/?utm_source=email&utm_medium=email&utm_campaign=webinar-data-first-klabin&utm_content=lembrete-final` |
| Post LinkedIn de última chamada | `https://solveplan.com/evento/data-first-klabin-sap-datasphere/?utm_source=linkedin&utm_medium=social&utm_campaign=webinar-data-first-klabin&utm_content=lembrete-final-post` |

---

## Regra para o outreach ABM (contas estratégicas)

Como o outreach é feito individualmente por SDR/CS, usar sempre o mesmo padrão trocando só o identificador do responsável, pra saber depois quem gerou o quê:

```
https://solveplan.com/evento/data-first-klabin-sap-datasphere/?utm_source=whatsapp&utm_medium=direct&utm_campaign=webinar-data-first-klabin&utm_content=abm-[iniciais-do-sdr]
```

Trocar `whatsapp` por `linkedin-dm` ou `email-direto` conforme o canal usado em cada abordagem.

---

## Como isso será lido depois

- No GA4 (`/ga4-ratos`): todos os cliques com `utm_campaign=webinar-data-first-klabin` aparecem agrupados, permitindo comparar `utm_source`/`utm_medium` entre si (LinkedIn orgânico vs. pago vs. e-mail vs. ABM).
- Na análise de atribuição (`/atribuicao`): usar o `utm_content` pra identificar qual peça específica (post, e-mail, SDR) gerou os leads que viraram reunião/oportunidade — essencial já que o budget de ads é baixo e a maior parte do resultado deve vir de e-mail/ABM (ver observação estratégica no `plano.md` da campanha).
- **Antes de disparar qualquer peça, gerar o link final substituindo `[iniciais-do-sdr]` e conferir que não sobrou nenhum placeholder.**

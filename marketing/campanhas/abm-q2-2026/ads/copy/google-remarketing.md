# Google Display — Remarketing ABM
## Campanha ABM Q2 2026 | Retargeting de contas impactadas no LinkedIn

**Estratégia:** Google Display como camada de retargeting — reforçar a mensagem da Solveplan para visitantes do site que chegaram pelas campanhas LinkedIn ABM. Não é a camada principal de ABM (LinkedIn faz o targeting por empresa), mas aumenta a frequência de exposição para quem já demonstrou interesse.

**Público:** Visitantes do site vindos das UTMs das campanhas ABM (utm_campaign=abm*)

---

## Set 1 — Consolidação e FP&A

**Responsive Display Ad:**
- Headline 1: Dados SAP virando decisão
- Headline 2: Conheça nosso portfólio
- Headline 3: Parceiro SAP Gold
- Description 1: Transforme seu ambiente SAP em analytics estratégico. Mais de 200 projetos entregues na América Latina.
- Description 2: Planejamento financeiro, consolidação e analytics sobre SAP. Agende uma conversa.

---

## Set 2 — Eficiência operacional

**Responsive Display Ad:**
- Headline 1: Fechamento mais rápido
- Headline 2: Analytics sobre SAP
- Headline 3: Solveplan | Parceiro SAP Gold
- Description 1: Elimine o Excel do fechamento. SAP Analytics e Datasphere com quem entende do negócio.
- Description 2: FP&A, consolidação e analytics integrados ao seu SAP. Agende um diagnóstico.

---

## Set 3 — Retargeting direto (visitou página de solução)

**Responsive Display Ad — tom mais direto, já conhecem a marca:**
- Headline 1: Ainda avaliando o SAP BDC?
- Headline 2: 30 min de diagnóstico gratuito
- Headline 3: Veja como outras empresas fizeram
- Description 1: Mostramos como empresas do seu setor já usam SAP de forma mais estratégica. Sem compromisso.
- Description 2: Parceiro SAP Gold com +200 projetos. Agende uma conversa.

---

## Configuração técnica

**Audiência:** Remarketing — visitantes das páginas do site com tag de origem ABM
- Criar segmento: visitou qualquer página com `utm_campaign` contendo "abm"
- Adicionar segmento: visitou páginas de solução (SAP BDC, SAC, Datasphere)
- Excluir: clientes atuais (fazer upload de lista de exclusão por email)

**UTMs para Google:**
```
utm_source=google&utm_medium=display&utm_campaign=abm-remarketing&utm_content=[set1/set2/set3]
```

**Formatos de imagem recomendados:**
- 300x250 (retângulo médio — maior alcance)
- 728x90 (leaderboard)
- 160x600 (arranha-céu largo)
- 320x50 (banner mobile)

**Budget alocado:** ~R$ 3.370 do total da campanha
- Duração: 12/05 a 30/06 (7 semanas)
- Budget diário: ~R$ 68/dia
- Bid strategy: Target CPA ou Maximize Clicks (avaliar na primeira semana)

**Nota:** Google Display não faz targeting por empresa como o LinkedIn. O remarketing por URL/UTM é a forma mais próxima de ABM no Google para esse orçamento. Para targeting por empresa no Google, seria necessário Customer Match (lista de emails corporativos dos contatos).

# Posts — Semana 3 (15 a 19 de junho de 2026)

---

## 15/06 (Seg) — Reforma tributária 2026 + dados SAP

**Pilar:** Autoridade / Tendência
**Formato:** Post texto longo
**Gap explorado:** DIFERENCIADOR ÚNICO — nenhum concorrente conectou a reforma tributária à necessidade de arquitetura de dados SAP. Gatilho de urgência real para 2026.

---

### LinkedIn (copy completa)

A reforma tributária de 2026 não é um problema de contabilidade.
É um problema de arquitetura de dados.

Em 2026, as obrigações fiscais no Brasil mudaram de estrutura. Você já sabe.
O que talvez não esteja no seu radar é o que isso exige tecnicamente de quem opera em SAP.

Regimes tributários diferentes por tipo de operação.
Novas frequências de apuração.
Obrigações acessórias que exigem rastreabilidade completa — origem do dado, lançamento, alçada de aprovação.

Tudo isso pressiona a mesma coisa: a qualidade dos dados na fonte.

Não dá para cumprir as obrigações de 2026 com a arquitetura de dados de 2019.

O que as empresas que estão se antecipando estão fazendo:

→ Revisando o dado mestre — cliente, fornecedor, material, estrutura societária. Inconsistência no cadastro tem custo fiscal.
→ Garantindo rastreabilidade de ponta a ponta nas transações. Toda obrigação acessória começa num lançamento dentro do SAP.
→ Avaliando como as fontes não-SAP que alimentam o processo fiscal estão integradas. Excel como sistema intermediário não tem trilha de auditoria.
→ Mapeando quais regras de processo precisam estar refletidas no ambiente de dados — não só nos relatórios.

A reforma tributária é o gatilho de urgência mais concreto de 2026 para estruturar o ambiente de dados agora.

Não porque é obrigatório. Porque quem não estrutura vai cumprir as obrigações manualmente, caro e tarde — e vai ser auditado sobre dados que não tem como rastrear.

Se você está nesse processo de adequação com SAP, fala comigo.

#ReformaTributaria #SAP #DadosFiscais #Governança #SAPBusinessDataCloud #Solveplan

---

### Instagram / Facebook (caption adaptada)

A reforma tributária de 2026 não é problema de contabilidade. É problema de arquitetura de dados.

Novas regras = nova exigência de rastreabilidade. E rastreabilidade começa no dado na fonte — dentro do SAP.

O que as empresas que estão se antecipando estão fazendo:
→ Revisando dado mestre (cliente, fornecedor, estrutura societária)
→ Garantindo trilha de auditoria em transações fiscais
→ Integrando fontes não-SAP que alimentam o fiscal

Quem não estrutura vai cumprir manualmente, caro e tarde.

#ReformaTributaria #SAP #Governança #Dados #Solveplan

---

## 16/06 (Ter) — Promo artigo: SAP Knowledge Graph

**Pilar:** Artigo / Autoridade
**Formato:** Post texto longo
**Artigo:** `marketing/blog/sap-knowledge-graph/artigo.md`
**Gap explorado:** Parceiros falam de Joule como "copilot". Solveplan explica por que o dado de base define o teto de qualquer agente.

---

### LinkedIn (copy completa)

Há uma diferença entre uma IA que sabe o que é reconciliação financeira e uma que sabe como ela funciona na sua empresa.

Essa diferença tem nome: SAP Knowledge Graph.

Um modelo de linguagem genérico sabe o que é fechamento financeiro. Não sabe que na sua empresa ele acontece no dia 5, que o centro de custo 1200 é alçada do controller regional e que qualquer variação acima de R$ 50k exige aprovação antes do lançamento.

Quando um agente sem esse contexto executa algo dentro do ERP, opera sobre estruturas que não entende.

O SAP chama isso de alucinação empresarial: respostas tecnicamente coerentes, erradas no contexto real da operação. Em processos críticos — fechamento, ordem de compra, conformidade — esse tipo de erro não é aceitável.

O SAP Knowledge Graph resolve pelo mapeamento de 452.000 tabelas do S/4HANA com relações semânticas, processos e políticas — para que os agentes naveguem no mapa do negócio, não no texto.

E tem uma implicação direta para quem cuida de dados: o Knowledge Graph sabe como o ERP funciona em geral. O SAP BDC é o que faz ele saber como o seu ERP funciona especificamente.

Essa distinção — entre contexto genérico e contexto real — define o teto de precisão de qualquer agente no seu ambiente SAP.

Escrevemos um artigo explicando o funcionamento e o que isso muda para empresas que estão avaliando agentes SAP.

→ Link no primeiro comentário.

#SAPKnowledgeGraph #IA #SAP #SAPBusinessDataCloud #Agentes #FP&A #Solveplan

---

### Instagram / Facebook (caption adaptada)

IA sem contexto do negócio erra com precisão.

O SAP chama isso de alucinação empresarial: resposta tecnicamente coerente, errada no contexto real da sua operação.

O SAP Knowledge Graph resolve: 452.000 tabelas do S/4HANA mapeadas com relações semânticas, processos e políticas.

E o SAP BDC é o que faz esse mapa genérico virar o mapa da sua empresa.

📎 Artigo completo: link na bio.

#SAPKnowledgeGraph #IA #SAP #Dados #Solveplan

---

## 17/06 (Qua) — Carrossel: 5 dores de dados que travam o FP&A

**Pilar:** Educação / Dor
**Formato:** Carrossel (7 slides)
**Gap explorado:** Nenhum concorrente monta esse tipo de conteúdo com angulação FP&A + BDC específica para o público controller/CFO.

---

### Script dos slides

**SLIDE 1 — CAPA**
5 dores de dados que travam o FP&A
(e o que o SAP BDC faz por cada uma)

Visual: Fundo #0A0837, título em branco, subtítulo em #5de6c8.

---

**SLIDE 2 — Dor 1**
O ciclo de fechamento é longo demais

O que acontece: Semanas consolidando dados de múltiplas fontes. Cada área tem uma versão diferente do mesmo número. O relatório sai quando a janela de decisão já fechou.

O que o BDC faz: Integra todas as fontes com semântica unificada. O fechamento começa com o dado já consolidado — não com reconciliação.

Visual: ícone de calendário com X, seta para ícone de dados integrados.

---

**SLIDE 3 — Dor 2**
Planejamento vive em Excel

O que acontece: Modelos que quebram quando alguém abre errado. Versões em pastas diferentes, sem controle. Ninguém sabe qual planilha é a oficial.

O que o BDC faz: Substitui a planilha como sistema de planejamento por um ambiente governado, com trilha de auditoria e versão única da verdade.

Visual: ícone de planilha → ícone de ambiente integrado.

---

**SLIDE 4 — Dor 3**
Dado que existe mas ninguém confia

O que acontece: Divergências entre o que o ERP mostra e o que as áreas reportam. Mesmo cliente cadastrado de formas diferentes. Ninguém sabe qual número é o certo.

O que o BDC faz: Master Data Governance integrado — dado mestre unificado, validado, com política de qualidade centralizada e rastreável.

Visual: dois ícones de dado conflitante → um ícone de dado certificado.

---

**SLIDE 5 — Dor 4**
Sem visibilidade de custos de plataforma

O que acontece: A empresa usa SAP Datasphere mas não sabe onde está consumindo recursos. Cargas que custam mais do que deveriam. Nenhuma previsibilidade antes do invoice.

O que o BDC faz: Visibilidade nativa de consumo de Capacity Units — com histórico e projeção de custo.

Visual: gráfico de consumo, ícone de alerta de custo.

---

**SLIDE 6 — Dor 5**
IA sem fundação de dados pronta

O que acontece: A empresa quer agentes SAP, mas os dados não estão preparados. IA sobre dado fragmentado consolida erros mais rápido do que qualquer time consegue corrigir.

O que o BDC faz: É a camada de dados governados e contextualizados que transforma automação genérica em automação confiável.

Visual: ícone de agente IA + dado fragmentado → ícone de dado governado + agente confiável.

---

**SLIDE 7 — CTA**
Qual dessas dores está travando o seu FP&A hoje?

A Solveplan implementa SAP BDC e SAP Datasphere na América Latina.
+90 clientes. +390 projetos entregues. Parceiro SAP Gold.

Se quiser entender como resolver no seu ambiente — fala comigo.

Visual: logo Solveplan, credenciais SAP Gold, CTA em #5de6c8.

---

### Legenda LinkedIn
5 dores de dados que travam o FP&A — e o que o SAP BDC faz por cada uma.

Desliza para ver as 5.

Qual delas está mais presente no seu dia a dia? Comenta abaixo.

#FP&A #SAPBusinessDataCloud #Dados #Planejamento #Analytics #SAP #Solveplan

---

### Instagram / Facebook (caption)
5 dores que travam o FP&A — e o que o SAP BDC faz por cada uma.

Desliza 👆 e me conta qual é a sua.

#FP&A #SAPBusinessDataCloud #Dados #Planejamento #SAP

---

## 18/06 (Qui) — Governança de dados é responsabilidade do CFO, não de TI

**Pilar:** Autoridade / Reframe
**Formato:** Post texto longo
**Gap explorado:** Delaware publica para CIO e TI. Solveplan posiciona governança de dados como decisão executiva de finanças — diferenciação clara de audiência.

---

### LinkedIn (copy completa)

Governança de dados não é um projeto de TI.
É uma decisão estratégica do CFO.

Ainda existe uma divisão equivocada nas empresas: TI cuida dos dados, financeiro cuida dos números.

O problema é que os números saem dos dados. E quando os dados não têm governança, o financeiro passa o dia reconciliando inconsistências — não tomando decisões.

O que governança de dados significa na prática para finanças:

→ Saber qual é a versão correta de um número — e quem é o responsável por ele
→ Ter rastreabilidade de onde aquele número veio, quando foi gerado e o que foi aplicado
→ Garantir que o dado de planejamento e o de fechamento vêm da mesma fonte
→ Ter segurança de que o número apresentado ao board não vai ser questionado no slide 3

Empresas que têm governança de dados gastam menos tempo em reuniões de "por que o número é diferente" e mais tempo analisando o que ele diz.

Isso não é um argumento para investir em tecnologia.
É um argumento para que o CFO lidere a decisão de dados — não apenas aprove o budget de TI.

A SAP Business Data Cloud é a plataforma onde esse argumento se torna implementação. Mas a decisão de priorizar governança precisa vir de quem entende o custo real da falta dela.

E esse custo não aparece em uma linha do P&L. Aparece no retrabalho, na decisão errada e na auditoria que encontra o que o relatório não mostrou.

#Governança #FP&A #CFO #Dados #SAP #SAPBusinessDataCloud #Solveplan

---

### Instagram / Facebook (caption adaptada)

Governança de dados não é projeto de TI.
É decisão estratégica do CFO.

TI cuida dos dados, financeiro cuida dos números — essa divisão tem custo.

Quando o dado não tem governança, o financeiro passa o dia reconciliando, não decidindo.

O custo disso não aparece no P&L. Aparece no retrabalho, na decisão errada e na auditoria.

#Governança #FP&A #CFO #Dados #SAP #Solveplan

---

## 19/06 (Sex) — O que os melhores CFOs fazem diferente com dados em 2026

**Pilar:** Autoridade / Tendência
**Formato:** Post texto longo
**Gap explorado:** Conteúdo executivo com padrão de comportamento observado — não genérico de tendências. Nenhum concorrente está publicando nessa voz.

---

### LinkedIn (copy completa)

Os CFOs que mais avançam em 2026 não têm as melhores planilhas.
Têm os melhores dados.

Existe um padrão que observamos nos clientes que mais evoluíram nos últimos dois anos.

Não é sobre ter mais relatórios. É sobre ter menos perguntas sem resposta no momento em que a decisão precisa ser tomada.

O que esses CFOs fazem diferente:

**1. Tratam dado mestre como ativo financeiro**
Inconsistência no cadastro de fornecedor, cliente ou centro de custo tem custo — de reconciliação, de retrabalho, de decisão errada. Eles alocam budget para manter o dado limpo, não só para limpar quando o problema aparece.

**2. Fecham o mês com dado — não com dado que vai ser ajustado depois**
Processo de fechamento que começa com inconsistência termina com ajuste manual. Eles estruturaram o ambiente para que o dado chegue validado no fechamento — não para validar durante.

**3. Simulam antes de comprometer**
Cenários de budget não são uma última versão enviada para aprovação. São análises de sensibilidade feitas com o dado real, no sistema, antes da reunião — não na véspera, em Excel.

**4. Sabem onde está o risco antes do conselho perguntar**
Variação acima do threshold? O sistema notifica. Não esperam o relatório mensal para descobrir que houve um desvio três semanas atrás.

**5. Tratam a plataforma de dados como responsabilidade de finanças, não de TI**
Participam da definição do que é um dado confiável. Cobram qualidade de dado como cobrariam qualquer outra entrega financeira.

Esses comportamentos não surgem do nada. Surgem quando o ambiente técnico suporta — e quando o líder de finanças decide que dado é responsabilidade sua.

#CFO #FP&A #Dados #Analytics #Planejamento #SAP #Solveplan

---

### Instagram / Facebook (caption adaptada)

O que os CFOs que mais avançam em 2026 têm em comum?

Não têm as melhores planilhas.
Têm os melhores dados.

5 comportamentos que observamos nos clientes que mais evoluíram:

1. Tratam dado mestre como ativo financeiro
2. Fecham o mês com dado validado, não com dado que vai ser ajustado
3. Simulam cenários antes de comprometer
4. Sabem onde está o risco antes do conselho perguntar
5. Tratam dados como responsabilidade de finanças — não de TI

Cada um desses comportamentos depende de um ambiente técnico que suporte. 📎 Detalhes no link da bio.

#CFO #FP&A #Dados #Analytics #SAP #Solveplan

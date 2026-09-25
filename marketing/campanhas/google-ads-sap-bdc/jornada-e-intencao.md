# Google Ads SAP BDC — Jornada do lead e intenção de busca

**Data:** 25/09/2026 · **Responsável:** Fran · **Status:** planejamento (antes da copy)
**Arquivo de apoio:** `mapa-keywords.csv` (grupos de anúncio, keywords com volume real, match type, negativas)
**Fontes:** Keyword Planner (Brasil, pt e en, consulta de 25/09/2026) e termos de pesquisa reais da conta SVPL (jun/2025 a set/2026)

---

## 1. O que os dados mostram

### A demanda por BDC no Google é pequena e está concentrada em poucos termos

| Termo | Buscas/mês (BR) | Lance topo de página (R$) |
|---|---|---|
| consultoria sap | 1.000 | 2,00 a 25,59 |
| sap bdc | 390 | 1,44 a 33,30 |
| sap analytics cloud | 390 | 2,45 a 25,59 |
| solveplan | 390 | — |
| sap joule | 390 | 4,20 a 22,94 |
| sap datasphere | 320 | 4,88 a 41,58 |
| sac sap | 210 | 2,91 a 18,03 |
| analytics sap | 110 | 4,38 a 21,15 |
| sap business data cloud | 90 | 6,09 a 53,18 |
| parceiro sap | 70 | 3,99 a 26,18 |
| sap databricks | 50 | 8,82 a 37,87 |
| sap group reporting | 50 | 3,26 a 21,32 |
| sap bw 4hana | 30 | 3,36 a 10,23 |

Somando o núcleo BDC (bdc, business data cloud, datasphere, SAC, databricks, BW/4HANA), são **cerca de 1.500 buscas por mês no Brasil**. A concorrência no leilão é baixa em quase todos (índice entre 12 e 31 de 100).

Os termos de fundo de funil que a gente imaginaria, como "consultoria sap bdc", "implementação sap datasphere", "migração sap bw", "sap bw fim de suporte" e "dados sap para ia", **aparecem com volume zero** (menos de 10 buscas/mês). Em inglês o cenário é o mesmo. Na prática, o avaliador busca pelo nome do produto e decide pelo que encontra na página, não por uma busca do tipo "quero contratar consultoria de BDC".

### A conta nunca disputou esses termos de verdade

| Período jun/2025 a set/2026 | Cliques | Investimento | Conversões |
|---|---|---|---|
| Todas as campanhas | 2.883 | R$ 3.962 | 7 |
| Só termos ligados a BDC/SAP analytics/consolidação | 30 | R$ 117 (3%) | 0 |

A campanha "[Leads] Search - download e-book SAP BDC" gastou R$ 893 em 563 cliques. Os termos que mais trouxeram clique foram "análise de dados", "lasy ai", "perplexity" e "inteligência artificial". **"sap bdc" teve 11 impressões em 15 meses.** Nas outras campanhas o padrão se repete: "treinamento orçamento empresarial", "gestão de custos nas micro e pequenas empresas", "planilha de controle financeiro feminino".

Isso muda a leitura do H1. O CPC de R$ 2,48 e o CTR de 4,97% que estão em `estrategia.md` como sinal de que "escala bem" vieram de tráfego barato e fora do público. O motivo mais provável é correspondência ampla sem negativas suficientes. Não era um canal pronto para escalar. Era um canal que ainda não foi testado com o público certo.

### Conclusões para o planejamento

1. **Busca não consegue absorver muita verba em BDC.** Com cerca de 1.500 buscas/mês no núcleo, uma campanha bem feita gasta algo entre R$ 1.500 e R$ 3.000/mês antes de saturar. Colocar mais dinheiro em busca só vai empurrar o anúncio para termo errado de novo.
2. **Quem busca não é quem assina.** Quem digita "sap datasphere" é head de dados, arquiteto SAP ou gerente de TI. CFO e CIO não buscam BDC. O anúncio e a página precisam dar a esse avaliador **argumento para levar o assunto para cima**: custo, prazo, risco, case.
3. **O resto da verba (inclusive a da SAP) tem que ir para alcance qualificado:** Demand Gen/YouTube com público de quem buscou esses termos, remarketing e reforço no LinkedIn. Detalhes na seção 5.

---

## 2. Os gatilhos: o que faz alguém começar a buscar

Nenhuma empresa acorda querendo uma plataforma de dados. Alguma coisa acontece antes. Como os gatilhos quase não viram busca literal, eles entram na **mensagem** e na **segmentação de Demand Gen**, não como keyword:

| Gatilho | O que a pessoa sente | Onde usar |
|---|---|---|
| **Fim da manutenção do SAP BW** (BW 7.5 em 2027) | "Tenho que decidir para onde vai meu BW e não sei qual é o caminho" | Anúncios de "sap bw 4hana" e "sap datasphere", LP de migração |
| **S/4HANA implantado, analytics não** | "Migramos o ERP e os relatórios continuam no Excel" | Anúncios de SAC |
| **Projeto de IA parado** | "A IA não entrega porque o dado está bagunçado" | Anúncios de "sap joule" e "sap business ai" ("antes da IA, vem dados") |
| **Dados SAP e não SAP separados** | "Tenho SAP, Databricks e ninguém cruza nada" | Anúncios de "sap databricks" |
| **Custo e governança do Datasphere** | "O consumo está subindo e não sei onde" | Anúncios de Datasphere, Solve Watch |
| **Conversa de RISE / renovação com a SAP** | "A SAP falou de BDC e preciso entender antes de negociar" | Anúncios de "sap bdc" e "sap business data cloud" |

Para o Q4, os dois mais fortes são **BW 2027** (tem prazo, obriga decisão) e **IA parada** (está no discurso de todo C-level e conversa com o posicionamento "antes da IA, vem dados").

---

## 3. A jornada em cinco estágios

### Estágio 1 — Dor (ainda não sabe que o BDC é resposta)

- **Quem:** head de dados, coordenador de BI, arquiteto SAP.
- **Comportamento:** não busca "BDC". Busca o problema de forma genérica, e esses termos ("análise de dados", "inteligência artificial") foram exatamente os que queimaram verba no H1.
- **Como alcançar:** **não por busca.** Demand Gen/YouTube com segmento personalizado (quem buscou termos SAP de dados e visitou páginas de BDC/Datasphere), LinkedIn e conteúdo orgânico.
- **Oferta:** conteúdo que resolve parte da dúvida (guia de decisão BW, case Klabin, webinar).

### Estágio 2 — Exploração (conhece o BDC e quer entender)

- **Quem:** o mesmo avaliador, agora com o nome do produto na cabeça (ouviu da SAP, viu no SAP NOW, leu no LinkedIn).
- **O que busca:** "sap bdc", "sap business data cloud", "sap datasphere", "sap analytics cloud", "sap databricks", "sap bw 4hana". **É aqui que está quase todo o volume de busca.**
- **O que precisa ouvir:** o que é na prática, o que muda para quem já tem Datasphere/BW, por onde começar. Resposta direta, sem folder de produto.
- **Oferta:** página que explica o BDC com clareza e dois CTAs: material (lead morno) e conversa com especialista (lead quente).
- **Peso no budget de busca:** o maior. Aqui o prêmio de **Melhor Parceiro SAP BDC 2026 LATAM** pesa mais: a pessoa está formando opinião sobre com quem aprender.

### Estágio 3 — Avaliação de parceiro (fundo de funil)

- **Quem:** avaliador com projeto aprovado ou em aprovação.
- **O que busca:** "consultoria sap" (1.000/mês, genérico) e "parceiro sap" (70/mês). Os termos específicos ("consultoria sap bdc") não têm volume.
- **Como tratar:** "consultoria sap" só entra combinado com termo de dados (frase exata "consultoria sap analytics", "consultoria sap datasphere") ou com público de remarketing. Sozinho traz busca de SAP Business One, ABAP, vaga.
- **Oferta:** **diagnóstico/assessment BDC** com reunião agendada.

### Estágio 4 — Validação (já escolheu, está conferindo)

- **Quem:** o comprador ou o comitê, depois de conhecer a Solveplan (evento, indicação, ABM, LinkedIn).
- **O que busca:** "solveplan" (390/mês). É muito volume de marca para o tamanho da empresa, sinal de que eventos e LinkedIn estão gerando curiosidade.
- **Oferta:** cases, prêmio, contato direto.
- **Peso no budget:** mínimo. Campanha de marca é barata e evita que concorrente apareça em cima do nosso nome. Hoje não existe.

### Estágio 5 — Reengajamento (já entrou e parou)

- **Quem:** os 95 leads hot/warm dos eventos do H1 e quem visitou a página BDC sem converter (a página recebe 65% do tráfego do site).
- **Mecânica:** listas de remarketing aplicadas à busca (RLSA), Demand Gen para visitantes e, se a conta for elegível, Customer Match com a lista do HubSpot.

---

## 4. Estrutura de campanhas

Com pouco volume, dividir busca em muitas campanhas só fragmenta dados e o Smart Bidding não aprende. A proposta é **uma campanha de busca BDC com grupos por produto**, uma de marca, e o alcance em Demand Gen.

| Campanha | Grupos de anúncio | Keywords-âncora (volume/mês) | LP | Verba/mês |
|---|---|---|---|---|
| **Search BDC** | SAP BDC | sap bdc (390), sap business data cloud (90), business data cloud (30) | /sap-business-data-cloud/ com CRO | R$ 1.500 a 3.000 (teto natural da demanda) |
| | Datasphere | sap datasphere (320) | /sap-datasphere/ | |
| | SAC | sap analytics cloud (390), sac sap (210), analytics sap (110) | Página SAC / cases SAC | |
| | BDC + Databricks | sap databricks (50), sap bdc databricks (10) | /sap-business-data-cloud/ (seção Databricks) | |
| | BW e migração | sap bw 4hana (30), sap bw 7.5 (10) | LP de migração BW (a criar) | |
| | Consultoria SAP dados | "consultoria sap analytics", "consultoria sap datasphere", parceiro sap (70) | LP de diagnóstico BDC (a criar) | |
| **Marca** | Solveplan | solveplan (390) | Home / cases | R$ 200 a 400 |
| **Demand Gen BDC** | Segmento de busca SAP dados · Remarketing BDC · Lista HubSpot | Público, não keyword (seção 5) | LP de diagnóstico / webinar / e-book | O restante, incluindo verba SAP |

**Configuração da busca:**
- Correspondência **exata e de frase apenas**. Nada de ampla até ter conversões qualificadas registradas. Foi a ampla que levou 97% da verba do H1 para termo errado.
- Somente rede de pesquisa. Sem parceiros de pesquisa, sem Display.
- Localização: Brasil, "presença" (pessoas no local).
- Idioma: português e inglês.
- Horário: seg a sex, 7h às 20h.
- Lance: Maximizar Cliques com teto de CPC (R$ 15 a 20) nas primeiras 3 semanas. Depois Maximizar Conversões, e tCPA quando houver 15 a 30 conversões por mês.
- **Pausar ou limpar as campanhas atuais** antes de subir a nova. A "[Leads] Search - download e-book SAP BDC" está ativa e competindo pelo mesmo orçamento com tráfego errado.

**"sap joule" (390/mês):** tem volume, mas é interesse em IA da SAP, não em dados. Vale testar num grupo à parte com o ângulo "Joule só funciona com dado organizado", com verba limitada e mensagem honesta de que a conversa é sobre a base de dados.

---

## 5. Verba da SAP: onde ela rende mais

Como a busca satura em R$ 1.500 a 3.000/mês, a verba da SAP (fundos de marketing de parceiro) deve ir para onde tem escala e ainda fala com o público certo:

| Onde | Por que | Ideia de uso |
|---|---|---|
| **Demand Gen / YouTube** | Alcança o avaliador antes de ele buscar. Permite segmento personalizado com as keywords da seção 1 e URLs de BDC/Datasphere/Databricks | Vídeo curto do case Klabin ou "BW 2027: 3 caminhos", CTA para diagnóstico |
| **Remarketing** | 65% do tráfego do site já cai na página BDC, com 78,8% de rejeição. É público quente sendo desperdiçado | Sequência: prova social → material → diagnóstico |
| **LinkedIn Ads** | Único canal que segmenta por cargo e empresa. Complementa o Google com CFO/CIO, que não buscam | Contas ABM do plano Q3 |
| **Busca** | Só até o teto de demanda | Garante presença em 100% das buscas de sap bdc / datasphere |

**Pontos para confirmar com a SAP antes de investir** (as regras variam por programa e trimestre, por isso vale checar no portal de parceiro ou com o gerente de canal):
- Valor disponível e **prazo de uso**. Verba de parceiro costuma ter validade por trimestre ou ano fiscal, e o Q4 fecha em dezembro.
- Se a atividade precisa de **aprovação prévia** e quais canais são elegíveis (Google Ads, YouTube, LinkedIn).
- Regras de uso da marca SAP e do selo SAP Gold Partner nos anúncios e LPs.
- Que **comprovação** pedem no fim: prints, notas, relatório de leads. Isso define o que precisa ser medido desde o primeiro dia.
- Se exigem compartilhamento de leads com a SAP.

---

## 6. Mensagem por grupo (ângulo, não copy final)

A copy completa sai na próxima etapa, com `/anuncio`:

| Grupo | Ângulo | Prova |
|---|---|---|
| SAP BDC | "O que o BDC muda para quem já tem SAP, e por onde começar" | Melhor Parceiro SAP BDC 2026 LATAM |
| Datasphere | Implementação com prazo e governança de consumo | Solve Watch · 390+ projetos |
| SAC | Sair do Excel com planejamento e analytics no SAP | Cases M. Dias Branco (96% de redução), Lins Agroindustrial |
| BDC + Databricks | SAP e não SAP no mesmo lugar, sem copiar dado | Arquitetura de referência |
| BW e migração | "2027 está perto. Decida o destino do BW com calma, não na pressa" | Diagnóstico de caminho |
| Consultoria SAP dados | Especialista em dados SAP, não consultoria SAP genérica | 60+ especialistas · SAP Gold |
| Marca | Prova social | Klabin, COPEL, Aegea |

Regra para todos: falar de decisão de negócio, não de feature. É onde a Delaware, concorrente mais próximo em BDC, é fraca: fala para arquiteto, não para quem decide.

---

## 7. Landing pages

| Necessidade | Situação | Ação |
|---|---|---|
| Página BDC (maior volume de busca) | Existe, rejeição de 78,8% | **CRO antes de subir a campanha:** CTA acima da dobra, prova na primeira tela, formulário visível |
| LP de diagnóstico BDC (fundo) | Não existe | Página dedicada: uma promessa, prova, formulário curto, agendamento. Sem menu |
| LP de migração BW | Não existe | "Seu BW tem prazo", com guia de decisão (Datasphere, BW PCE no BDC, BW/4HANA) |
| Datasphere / Solve Watch / SAC | Existem | Usar como estão |

Se for para escolher uma coisa só antes de subir: **CRO da página BDC**, porque é para onde vai o maior volume ("sap bdc" + "sap business data cloud").

---

## 8. Mensuração: otimizar por reunião, não por formulário

O H1 mostrou o que acontece quando o Google otimiza por clique barato. Agora ele precisa aprender com o que vira pipeline.

1. **Conversões primárias:** reunião agendada e formulário de diagnóstico. Download de e-book como secundária.
2. **GCLID no HubSpot:** capturar no formulário e ativar a integração Google Ads ↔ HubSpot.
3. **Conversões offline:** devolver ao Google os estágios MQL → SQL → Oportunidade.
4. **UTM:** `utm_source=google&utm_medium=cpc&utm_campaign=bdc-[search|marca|demandgen]&utm_term={keyword}&utm_content={adgroupid}`
5. **Revisão semanal dos termos de pesquisa** nas primeiras 4 semanas, toda segunda-feira.
6. **Relatório de comprovação para a SAP** montado desde o primeiro dia, no formato que o programa pedir.

| KPI | Search BDC | Demand Gen | Marca |
|---|---|---|---|
| Principal | Custo por lead qualificado | Custo por visita engajada / lead | Parcela de impressões |
| Qualidade | % de termos de pesquisa relevantes (meta: > 80%) | % que volta ao site | CTR |
| Alerta | Termo irrelevante com gasto > R$ 20 | Rejeição > 70% na LP | Concorrente na marca |

---

## 9. Negativas essenciais

A lista completa está no CSV, já incluindo os termos que queimaram verba no H1:

- **Carreira:** vaga, emprego, salário, currículo, trainee, freelancer, jobs
- **Estudo:** curso, certificação, treinamento, tutorial, manual, apostila, pdf, udemy, openSAP
- **Acesso e suporte:** login, download, trial, sap help, note, registro
- **Fora do público:** pequenas empresas, micro, MEI, pessoal, planilha, excel, grátis, Business One, Omie, TOTVS, Fluig
- **IA genérica:** perplexity, chatgpt, lasy ai, 2short ai, automação de ia

---

## 10. Próximos passos

| # | Ação | Depende de |
|---|---|---|
| 1 | Confirmar valor, prazo e regras da verba SAP | Gerente de canal SAP |
| 2 | Pausar a campanha atual de e-book BDC e adicionar as negativas do CSV nas campanhas ativas | — |
| 3 | CRO da página /sap-business-data-cloud/ | — |
| 4 | Configurar GCLID + conversões offline no HubSpot | — |
| 5 | Definir a oferta de fundo (diagnóstico BDC: formato, duração, quem conduz) | Comercial |
| 6 | Escrever RSAs por grupo de anúncio com `/anuncio` | Itens 3 e 5 |
| 7 | Subir Search BDC + Marca com `/google-ads-ratos` | Itens 2, 4 e 6 |
| 8 | Roteiro e criativo para Demand Gen (vídeo curto) com `/video-editor` | Item 1 |
| 9 | Criar LPs de diagnóstico e de migração BW | Item 5 |

**Decisões em aberto:**
- Rodar só no Brasil ou incluir México/Colômbia em espanhol, aproveitando o prêmio LATAM? Com a demanda brasileira pequena, pode valer testar.
- Qual número usar na copy: "150+ empresas / 390+ projetos" (`_contexto/empresa.md`) ou "+200 soluções / +90 clientes" (`CLAUDE.md`)? Os dois arquivos estão diferentes.

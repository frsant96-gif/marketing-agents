# SAP Joule Work: de assistente de chat a camada operacional do ERP

**O SAP Joule deixou de ser uma caixa de perguntas. Com o Joule Work, ele passou a ser o ponto único de entrada para executar processos, coordenar agentes e operar o negócio em linguagem natural — sem abrir um único menu SAP.**

---

## O que é o SAP Joule Work?

O SAP Joule Work é a nova camada de engajamento do SAP Joule — um workspace unificado onde usuários descrevem o que precisam em linguagem natural e o Joule coordena os agentes, busca os dados e executa as transações necessárias para chegar ao resultado. Disponível em desktop, web e mobile, o Joule Work elimina a navegação tradicional entre módulos SAP e substitui menus por intenção: o usuário diz o que quer, não onde clicar.

A diferença em relação à versão anterior do Joule é estrutural. A versão original era um copiloto — respondia perguntas, sugeria ações, mas dependia do usuário para executar. O Joule Work orquestra agentes especializados que executam de ponta a ponta, dentro dos limites de governança configurados para cada papel e processo.

---

## Por que a SAP refez o Joule do zero

A SAP reconheceu publicamente que o Joule Studio original não entregou o que prometia. A ferramenta era limitada a interações pontuais, sem capacidade de coordenar fluxos complexos ou se integrar profundamente aos processos SAP. Desenvolvedores encontravam restrições que impediam construir aplicações reais sobre ela.

O Joule Studio 2.0, apresentado no SAPPHIRE 2026 com primeiros clientes recebendo a versão a partir de junho, foi reconstruído com três mudanças fundamentais:

**Intent-based, não script-based**
Em vez de configurar fluxos passo a passo, o desenvolvedor descreve a intenção de negócio. O Joule Studio 2.0 traduz essa intenção em agentes e workflows contextualizados nos dados e processos SAP da empresa.

**Model-agnostic com SAP semantics**
O Joule Studio 2.0 suporta múltiplos modelos de linguagem — SAP, Anthropic, OpenAI, Google — mas sempre com a semântica SAP, o conhecimento de processo e os controles empresariais já embutidos. O desenvolvedor escolhe o modelo; a governança e o contexto de negócio já estão no lugar.

**Pro-code para quem precisa de controle total**
Desenvolvedores podem usar Python ou TypeScript para construir aplicações e experiências completas — não apenas snippets de automação. Isso amplia o alcance do Joule para equipes técnicas que precisam de flexibilidade além do low-code.

---

## O que o Joule Work faz na prática

O Joule Work não é uma interface nova para as mesmas funções antigas. Ele redefine como os usuários interagem com o SAP no dia a dia.

**Workspace unificado por intenção**
O usuário abre o Joule Work — em vez de acessar transações separadas no S/4HANA, Ariba, SuccessFactors ou SAP Datasphere — e descreve o que precisa: "prepare o relatório de variação de custo do trimestre para as plantas do Brasil" ou "mostre os pedidos de compra acima do limite de aprovação pendentes desde segunda-feira". O Joule coordena os agentes necessários, busca os dados via Knowledge Graph e apresenta o resultado — incluindo visualizações geradas dinamicamente.

**Execução, não só consulta**
A diferença crítica do Joule Work em relação a qualquer copiloto anterior é a capacidade de executar transações. O usuário não recebe uma sugestão de o que fazer — o Joule faz, dentro dos controles de acesso e aprovação configurados para aquele papel. Lançar entradas, iniciar workflows, aprovar solicitações dentro dos limites de alçada: tudo via linguagem natural, com trilha de auditoria completa.

**Suporte a padrões abertos: MCP e A2A**
O Joule Work foi construído com suporte nativo a MCP (Model Context Protocol) e A2A (Agent-to-Agent), os padrões emergentes de interoperabilidade entre agentes de IA. Isso significa que o Joule pode coordenar agentes de terceiros e se integrar a sistemas fora do ecossistema SAP sem customizações proprietárias.

**Voz como canal de trabalho**
A parceria com LiveKit trouxe IA de voz para o Joule — não como feature demonstrativa, mas como canal de trabalho real para funções que operam longe de um teclado: chão de fábrica, logística, campo, atendimento presencial. O usuário interage com o Joule por voz e recebe respostas e confirmações da mesma forma, com o mesmo acesso às transações e dados.

**Mobile já disponível**
O aplicativo móvel do Joule Work está disponível em disponibilidade geral. O desktop e a versão completa estão no programa Early Adopter Care, com disponibilidade geral prevista para o segundo semestre de 2026.

---

## O que muda para usuários SAP Datasphere e Analytics Cloud

Para empresas que usam SAP Datasphere e SAP Analytics Cloud — dois produtos centrais no portfólio da Solveplan —, o Joule Work tem implicação direta.

O Joule está disponível no SAP Datasphere, permitindo que usuários naveguem pela plataforma, façam perguntas sobre dados e executem tarefas usando linguagem natural. Um analista financeiro que precisava navegar por espaços, views e modelos para chegar a um dado específico agora pode simplesmente perguntar — e o Joule encontra, contextualiza e apresenta.

Ao contrário de ferramentas de BI que exigem que o usuário saiba onde os dados estão, o Joule Work integrado ao Datasphere usa o Knowledge Graph para navegar pela estrutura de dados da empresa e retornar respostas precisas. Isso tem impacto direto em dois pontos:

- **Adoção:** usuários que evitavam o Datasphere por complexidade de navegação passam a interagir via linguagem natural
- **Velocidade:** análises que dependiam de um analista especializado para montar uma query passam a ser acessíveis para o usuário de negócio diretamente

Para a Solveplan, parceira SAP Gold especializada em SAP Datasphere e SAP Analytics Cloud, o Joule Work representa uma camada de valor adicional sobre ambientes que já estão implementados. Empresas com Datasphere bem estruturado e dados governados no SAP BDC chegam ao Joule Work com o contexto pronto — e a experiência de linguagem natural funcionando sobre dados reais, não sobre modelos genéricos.

---

## FAQ — SAP Joule Work

**O que é o SAP Joule Work?**
O SAP Joule Work é a nova camada de engajamento do Joule — um workspace unificado onde usuários operam processos SAP em linguagem natural, sem navegar entre módulos. Disponível em desktop, web e mobile, o Joule Work coordena agentes especializados para executar transações, buscar dados e apresentar resultados, com trilha de auditoria completa.

**Qual é a diferença entre Joule Work e o Joule anterior?**
O Joule original era um copiloto: respondia perguntas e sugeria ações, mas o usuário precisava executar manualmente. O Joule Work orquestra agentes que executam de ponta a ponta — lança entradas, inicia workflows, aprova dentro de alçadas — a partir de uma instrução em linguagem natural. A diferença é entre sugestão e execução.

**O que é o Joule Studio 2.0?**
O Joule Studio 2.0 é o ambiente para desenvolvedores construírem agentes e aplicações SAP. Reconstruído após limitações da versão anterior, ele é intent-based, model-agnostic e suporta Python e TypeScript. Os primeiros clientes começaram a receber a versão em junho de 2026, com semântica SAP, conhecimento de processo e controles empresariais já embutidos.

**O Joule Work está disponível no SAP Datasphere?**
Sim. O Joule está disponível no SAP Datasphere, permitindo que usuários naveguem pela plataforma, consultem dados e executem tarefas usando linguagem natural. O Knowledge Graph integrado ao Datasphere fornece o contexto necessário para que as respostas sejam precisas dentro do ambiente de dados específico da empresa.

**O Joule Work suporta voz?**
Sim. A parceria com LiveKit trouxe IA de voz ao Joule Work para funções que operam longe de teclados — manufatura, logística, campo e atendimento presencial. O usuário interage por voz com acesso às mesmas transações e dados disponíveis na interface gráfica.

**Como a Solveplan apoia empresas na adoção do Joule Work?**
A Solveplan implementa SAP Datasphere e SAP BDC — os componentes que fornecem o contexto de dados necessário para que o Joule Work funcione com precisão sobre os dados reais da empresa. Para organizações que querem avaliar sua prontidão para o Joule Work, a Solveplan realiza diagnósticos de maturidade do ambiente analítico como ponto de partida.

---

## O SAP que os usuários sempre quiseram — se os dados estiverem no lugar

O Joule Work resolve um problema antigo do ERP: a complexidade de navegação que mantinha o poder do sistema restrito a especialistas. Com linguagem natural como interface, o SAP passa a ser acessível para quem decide — não apenas para quem sabe operar transações.

Mas a experiência depende do que está embaixo. Joule Work sobre dados fragmentados entrega respostas fragmentadas. Sobre um ambiente SAP Datasphere bem estruturado e alimentado pelo SAP BDC, entrega respostas precisas, rastreáveis e acionáveis.

Fale com a Solveplan para entender se o seu ambiente de dados está pronto para o Joule Work.

**[Agendar conversa com a Solveplan]**

---

## Fontes

- Complete AI Training — [SAP expands Joule with agentic AI workspace at Sapphire 2026](https://completeaitraining.com/news/sap-expands-joule-with-agentic-ai-workspace-and-extends/)
- SiliconANGLE — [SAP recasts Joule as the front door to autonomous enterprise AI](https://siliconangle.com/2026/05/12/sap-recasts-joule-front-door-autonomous-enterprise-ai/)
- SAP News Center — [Announcing New Joule Studio for Enterprise Scale Agentic Development](https://news.sap.com/2026/05/new-joule-studio-enterprise-scale-agentic-development/)
- SAP Community — [SAP UX Update: The New Joule Work Engagement Layer](https://community.sap.com/t5/technology-blog-posts-by-sap/sap-ux-update-the-new-joule-work-engagement-layer-experiences/ba-p/14396478)
- SAP News Center — [The Future of the Enterprise Is Autonomous](https://news.sap.com/2026/05/future-enterprise-autonomous/)

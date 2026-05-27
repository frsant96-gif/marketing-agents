import sys, requests, json
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
WP = "https://solveplan.com/wp-json/wp/v2"

# ─── BLOCK HELPERS ────────────────────────────────────────────────────────────

def h5(text):
    return (
        '<!-- wp:heading {"level":5} -->\n'
        f'<h5 class="wp-block-heading"><strong>{text}</strong></h5>\n'
        '<!-- /wp:heading -->'
    )

def p(text):
    return f'<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->'

def ul(items):
    lis = ''.join(f'<li>{i}</li>' for i in items)
    return f'<!-- wp:list -->\n<ul class="wp-block-list">{lis}</ul>\n<!-- /wp:list -->'

def details(question, answer):
    return (
        '<!-- wp:details -->\n'
        f'<details class="wp-block-details"><summary>{question}</summary>'
        '<!-- wp:paragraph -->\n'
        f'<p>{answer}</p>\n'
        '<!-- /wp:paragraph --></details>\n'
        '<!-- /wp:details -->'
    )

CTA = (
    '<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n'
    '<div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"primary","textColor":"white","style":{"border":{"radius":"4px"}}} -->\n'
    '<div class="wp-block-button"><a class="wp-block-button__link has-white-color has-primary-background-color has-text-color has-background wp-element-button" '
    'href="https://bdcstrategy.solveplan.ai/" target="_blank" rel="noopener">Avalie a maturidade dos seus dados com a Solveplan</a></div>\n'
    '<!-- /wp:button --></div>\n'
    '<!-- /wp:buttons -->'
)

# Internal link helpers
BDC_URL = "https://solveplan.com/sap-business-data-cloud/"
DS_URL  = "https://solveplan.com/sap-datasphere/"
BLOG    = "https://solveplan.com/blog/"

def a(text, url):
    return f'<a href="{url}">{text}</a>'


# ─── POST 1: SAP AUTONOMOUS SUITE ─────────────────────────────────────────────

post1_parts = [
    p('Durante o SAP SAPPHIRE Orlando 2026, a SAP apresentou mais de 200 agentes e 50 assistentes prontos para operar processos de finanças, supply chain e RH. O SAP Autonomous Suite é onde tudo isso se concretiza.'),

    h5('O que é o SAP Autonomous Suite?'),
    p(f'O SAP Autonomous Suite é o conjunto de aplicações SAP equipadas com agentes de IA capazes de executar processos de negócio de ponta a ponta — sem intervenção manual em cada etapa. É a camada onde a visão Autonomous Enterprise da SAP se torna operacional.'),
    p(f'O que diferencia o SAP Autonomous Suite de outras iniciativas de automação é a camada de decisão: os agentes leem contexto real da empresa — via {a("SAP Business Data Cloud", BDC_URL)} e {a("SAP Knowledge Graph", BLOG+"sap-knowledge-graph/")} — e executam dentro das políticas e alçadas configuradas no ambiente SAP.'),

    h5('Os 5 domínios do SAP Autonomous Suite'),
    p('O SAP Autonomous Suite organiza seus agentes em cinco domínios operacionais, cada um com assistentes especializados para o contexto de processo:'),
    ul([
        '<strong>Autonomous Finance:</strong> automatiza o ciclo financeiro completo — lançamentos contábeis, reconciliações e fechamento mensal. O destaque é o Autonomous Close Assistant.',
        '<strong>Autonomous Spend:</strong> cobre o ciclo de compras e gestão de fornecedores — da criação de pedidos à validação de notas fiscais e conformidade contratual.',
        '<strong>Autonomous Supply Chain:</strong> agentes monitoram e ajustam planos de demanda, estoque e logística em tempo real. Rupturas, atrasos e variações de demanda são tratados automaticamente.',
        '<strong>Autonomous HCM:</strong> automatiza processos de recursos humanos — admissão, folha, benefícios e conformidade regulatória — operando dentro do SAP SuccessFactors.',
        '<strong>Autonomous CX:</strong> agentes de experiência do cliente operam em ciclos de venda, atendimento e pós-venda — respondendo a solicitações, atualizando registros e escalando exceções.',
    ]),

    h5('O caso mais concreto: fechamento financeiro em dias, não semanas'),
    p('O Autonomous Close Assistant é o componente do SAP Autonomous Suite com impacto mais imediato e mensurável para empresas que operam com SAP S/4HANA.'),
    p('O fechamento financeiro mensal, para a maioria das organizações, ainda depende de planilhas, cobranças entre áreas e horas extras nos últimos dias do mês. O Autonomous Close Assistant elimina os três pontos de maior atrito nesse processo:'),
    ul([
        '<strong>Lançamentos de diário:</strong> o agente identifica padrões recorrentes e executa lançamentos automaticamente, com trilha de auditoria completa.',
        '<strong>Reconciliações:</strong> cruzamento automático de contas a pagar, contas a receber e extratos bancários, com resolução de divergências dentro dos parâmetros configurados.',
        '<strong>Resolução de erros:</strong> detecção de inconsistências, classificação por criticidade e execução de correções ou acionamento do responsável quando necessário.',
    ]),
    p('Para empresas com operações em múltiplas entidades ou moedas — cenário comum em clientes da Solveplan —, o impacto é direto: menos retrabalho, menos dependência de especialistas para tarefas repetitivas e fechamento mais previsível.'),

    h5('Como o SAP Autonomous Suite se conecta ao SAP BDC e Joule'),
    p(f'O SAP Autonomous Suite não funciona isolado. Há duas condições que precisam estar no lugar:'),
    p(f'<strong>Fundação de dados:</strong> os agentes do Autonomous Suite operam sobre o {a("SAP Business AI Platform", BLOG+"sap-business-ai-platform/")}, cuja camada de dados é o {a("SAP Business Data Cloud", BDC_URL)} (BDC). O BDC fornece ao agente o contexto real da empresa — hierarquias, políticas, dados mestre governados. Sem essa fundação, o agente opera sobre informações fragmentadas.'),
    p(f'<strong>Joule como camada de orquestração:</strong> os {a("Joule Assistants", BLOG+"sap-joule-work/")} são a interface entre os usuários e os agentes do Autonomous Suite. Uma instrução em linguagem natural — "feche o mês para a entidade Brasil" — é traduzida por Joule em uma sequência de ações coordenadas entre múltiplos agentes. A Anthropic foi confirmada como o modelo de raciocínio primário que alimenta o Joule dentro do Autonomous Suite.'),

    h5('Automatizar sem fundação é ampliar erros'),
    p('O SAP Autonomous Suite muda a pergunta estratégica das empresas: de "como automatizo uma tarefa?" para "qual processo inteiro posso entregar a um agente?"'),
    p('Mas há uma condição que nenhum agente resolve por si mesmo: a qualidade da fundação de dados.'),
    p(f'Empresas com {a("SAP BDC", BDC_URL)} implementado e dados governados chegam ao Autonomous Suite com o terreno preparado. Os agentes encontram o contexto correto e operam dentro das políticas reais da empresa.'),
    p('Empresas que ainda operam com dados em silos encontram um obstáculo real: os agentes automatizam o que encontram. Se o que encontram são dados inconsistentes, a automação consolida erros em escala e velocidade que nenhuma equipe consegue corrigir manualmente.'),

    h5('Sua empresa está pronta para operar processos SAP de forma autônoma?'),
    p('O SAP Autonomous Suite muda o que é possível fazer com ERP. O que determina se sua empresa vai aproveitar essa mudança — ou apenas observá-la — é a qualidade da fundação de dados que você já tem hoje.'),
    p('Fale com a Solveplan para entender onde você está e o que precisa ser estruturado antes de implementar agentes nos seus processos SAP.'),

    CTA,

    h5('FAQ — SAP Autonomous Suite'),
    details('O que é o SAP Autonomous Suite?', 'O SAP Autonomous Suite é o conjunto de aplicações SAP com agentes de IA para automatizar processos de negócio de ponta a ponta — sem intervenção manual em cada etapa. Foi apresentado no SAP SAPPHIRE Orlando 2026 como parte da visão Autonomous Enterprise.'),
    details('Qual a diferença entre SAP Autonomous Suite e SAP Business AI Platform?', 'O SAP Business AI Platform é a fundação técnica — dados, plataforma e infraestrutura de IA. O SAP Autonomous Suite é onde essa fundação se torna aplicação: os agentes que executam processos reais de finanças, compras, supply chain, RH e CX.'),
    details('O que é o Autonomous Close Assistant?', 'É o agente que automatiza o fechamento financeiro — lançamentos, reconciliações e resolução de erros. Permite comprimir o ciclo de fechamento mensal, com trilha de auditoria completa e operação dentro das políticas SAP configuradas.'),
    details('Quais domínios o SAP Autonomous Suite cobre?', 'Cinco domínios: Autonomous Finance, Autonomous Spend, Autonomous Supply Chain, Autonomous HCM e Autonomous CX. Cada domínio tem agentes especializados no contexto de processo e nas políticas do setor.'),
    details('Preciso implementar SAP BDC antes de adotar o SAP Autonomous Suite?', 'O SAP BDC não é pré-requisito formal, mas é a camada que fornece ao agente o contexto correto para tomar decisões. Sem dados governados e com semântica de negócio, os agentes operam sobre informações fragmentadas — e automatizam erros em escala.'),
    details('Como a Solveplan apoia empresas que querem adotar o SAP Autonomous Suite?', 'A Solveplan implementa SAP BDC e SAP Datasphere — a fundação de dados necessária para que os agentes do SAP Autonomous Suite operem com contexto real. Para empresas que querem avaliar sua prontidão, a Solveplan realiza diagnósticos de maturidade analítica como ponto de partida.'),

    h5('Fontes'),
    ul([
        'SAP News Center — SAP Unveils the Autonomous Enterprise',
        'SAP News Center — New Era of Autonomous HCM',
        'SAPinsider — SAP Sapphire 2026: SAP Recasts ERP Around the Autonomous Enterprise and Business AI',
        'SAPinsider — SAP Sapphire 2026: The Autonomous Enterprise Arrives — with Guardrails',
        'SAP News Center Brasil — SAP apresenta a Autonomous Enterprise',
    ]),
]

# ─── POST 2: SAP BDC KNOWLEDGE CORE ──────────────────────────────────────────

post2_parts = [
    p(f'O SAP Knowledge Graph sabe tudo sobre como o ERP funciona. O {a("SAP Business Data Cloud", BDC_URL)} é o que faz ele saber como o <em>seu</em> ERP funciona.'),

    h5('O que é o Knowledge Core do SAP BDC?'),
    p(f'O Knowledge Core é o papel que o {a("SAP Business Data Cloud", BDC_URL)} (BDC) desempenha dentro da arquitetura de IA da SAP: ele é a camada que transforma o {a("SAP Knowledge Graph", BLOG+"sap-knowledge-graph/")} genérico no mapa específico da sua empresa.'),
    p('Na prática, o BDC não é um data warehouse com uma camada semântica por cima. Ele foi construído para reduzir o que a SAP chama de "AI readiness gap" — a distância entre o que os modelos de IA conseguem fazer e o que os dados disponíveis na empresa permitem que eles façam.'),

    h5('A lacuna que o BDC resolve: dados sem significado de negócio'),
    p('A maioria das empresas que usa SAP tem dados. O problema não é a quantidade — é o significado.'),
    p('Um data warehouse tradicional armazena tabelas com esquemas técnicos. Ele sabe que existe um campo <code>BUKRS</code> com o valor <code>1000</code>. Não sabe que esse valor representa a empresa Brasil, com determinada hierarquia de aprovação, política de crédito e moeda funcional.'),
    p(f'Essa diferença — entre dado técnico e dado com contexto de negócio — é o que separa um agente que executa uma tarefa de um agente que toma uma decisão. Quando o BDC estrutura os dados com semântica empresarial, cria o vocabulário que os agentes SAP — alimentados pelo Claude via {a("parceria SAP-Anthropic", BLOG+"sap-anthropic-parceria/")} — precisam para operar com precisão.'),

    h5('Como o BDC alimenta o Knowledge Graph com o contexto da empresa'),
    p(f'O {a("SAP Knowledge Graph", BLOG+"sap-knowledge-graph/")} fornece o contexto genérico do universo SAP: tabelas mapeadas do S/4HANA, campos com relações semânticas, processos codificados em 50 anos de ERP. É o mapa do que qualquer empresa SAP pode fazer.'),
    p('O SAP Business Data Cloud é a camada que personaliza esse mapa para a empresa específica.'),
    p('Quando o BDC integra os dados da organização — de fontes SAP e não-SAP — e os estrutura com semântica de negócio, estende o Knowledge Graph com cinco camadas de contexto proprietário:'),
    ul([
        '<strong>Hierarquias organizacionais reais:</strong> quais entidades jurídicas existem, como estão estruturadas, quais são as relações de aprovação entre elas.',
        '<strong>Dados mestre governados:</strong> clientes, fornecedores, materiais, centros de custo — com identidade unificada e sem duplicação entre sistemas.',
        '<strong>Histórico transacional:</strong> o que aconteceu, quando, quem aprovou e por quê.',
        '<strong>Regras de processo:</strong> políticas internas, limites de alçada, exceções negociadas.',
        '<strong>Dados externos integrados:</strong> fontes fora do ecossistema SAP trazidas ao mesmo contexto semântico.',
    ]),
    p('O resultado é um Knowledge Graph que não apenas sabe como um processo de fechamento funciona no universo SAP — sabe como ele funciona na sua empresa, com suas regras, sua estrutura e seu histórico.'),

    h5('SAP Domain Models: o elo entre dados e lógica de processo'),
    p('Dentro da arquitetura do BDC, os SAP Domain Models são modelos pré-treinados na lógica SAP que interpretam os dados estruturados pelo BDC em contexto de processo. Não traduzem apenas campos — traduzem significados de negócio.'),
    p('Um Domain Model de finanças sabe o que uma variação de custo significa dentro do ciclo de planejamento SAP — não apenas que dois números são diferentes. Essa camada de interpretação é o que permite que os agentes tomem decisões dentro do processo, e não apenas sobre os dados.'),
    p('Os Domain Models operam sobre os data products governados do BDC — unidades de dado verificadas, alinhadas às políticas da empresa e certificadas para uso em decisões de agentes.'),

    h5('Data products governados: a unidade de confiança do BDC'),
    p('Um data product no BDC não é um relatório ou uma tabela. É um ativo de dado certificado — validado pelo SAP Master Data Governance, alinhado às políticas da empresa e documentado para uso por agentes de IA.'),
    p('A relevância prática para quem usa agentes SAP é direta: agentes que operam sobre data products certificados tomam decisões com base em informações verificadas. Agentes que operam sobre dados não governados tomam decisões com base em suposições.'),
    p('Em 2026, o SAP Master Data Governance passou a ser integrado nativamente ao BDC — o que significa que a governança de dados mestre e a estruturação para IA acontecem no mesmo ambiente.'),

    h5('Implementar BDC é estruturar a fundação de tudo — perspectiva Solveplan'),
    p(f'Para a Solveplan, parceira SAP Gold especializada em implementação de {a("SAP BDC", BDC_URL)} e {a("SAP Datasphere", DS_URL)} na América Latina, o papel do BDC como Knowledge Core não é conceitual — é o que diferencia projetos de IA que funcionam de projetos que ficam presos em POCs.'),
    p('Quando uma empresa implementa o BDC com qualidade — dados mestre unificados, hierarquias organizacionais corretas, fontes externas integradas com semântica de negócio — chega ao ponto de ativar agentes com o contexto correto já disponível.'),
    p('A Solveplan vê frequentemente dois perfis ao avaliar prontidão para IA no SAP:'),
    p('<strong>Perfil A:</strong> dados mestre limpos, hierarquias mapeadas, BDC estruturado com semântica de negócio. Esses clientes chegam ao Autonomous Suite com o contexto no lugar — os agentes encontram o que precisam para operar.'),
    p('<strong>Perfil B:</strong> dados fragmentados, múltiplas fontes com definições conflitantes, sem governança estabelecida. Esses clientes ativam agentes e rapidamente percebem que a automação amplifica inconsistências em vez de eliminá-las.'),
    p('A recomendação da Solveplan é sempre a mesma: o investimento em BDC não é um custo de infraestrutura — é o investimento que determina o retorno de toda iniciativa de IA no SAP.'),

    h5('O ativo que determina o retorno de toda iniciativa de IA no SAP'),
    p('O SAP Business Data Cloud é a camada que transforma o Knowledge Graph genérico da SAP no conhecimento específico da sua empresa — e é esse conhecimento que determina a qualidade de cada decisão dos agentes.'),
    p('Fale com a Solveplan para avaliar o estado atual do seu ambiente de dados e entender o que precisa ser estruturado para que os agentes SAP operem com o contexto correto.'),

    CTA,

    h5('FAQ — SAP BDC Knowledge Core'),
    details('O que é o Knowledge Core no contexto do SAP BDC?', 'Knowledge Core é o papel do SAP Business Data Cloud como camada de dados governados e semanticamente estruturados que alimenta o SAP Knowledge Graph com o contexto específico da empresa — hierarquias, dados mestre, histórico transacional e regras de processo.'),
    details('Qual a diferença entre o SAP Knowledge Graph e o BDC como Knowledge Core?', 'O SAP Knowledge Graph é o mapa genérico de processos do universo SAP — compartilhado por todos os clientes. O BDC como Knowledge Core é a camada que personaliza esse mapa com os dados reais da empresa: sua estrutura, suas políticas, seu histórico.'),
    details('O que são SAP Domain Models?', 'SAP Domain Models são modelos pré-treinados na lógica de processo SAP que traduzem dados estruturados pelo BDC em contexto de negócio interpretável por agentes. Operam sobre data products certificados e permitem que agentes tomem decisões dentro do processo, não apenas sobre os dados.'),
    details('O que é um data product no SAP BDC?', 'Um data product é um ativo de dado certificado no BDC — verificado pelo SAP Master Data Governance, alinhado às políticas da empresa e documentado para uso por agentes de IA. É a unidade de dado confiável sobre a qual decisões autônomas podem ser tomadas.'),
    details('Por que a governança de dados mestre importa para agentes SAP?', 'Agentes que operam sobre dados mestre duplicados ou inconsistentes não conseguem distinguir o "cliente A" de três registros conflitantes. A governança de dados mestre — integrada nativamente ao BDC desde 2026 — é o que garante que o contexto que o agente usa para decidir é único, verificado e atualizado.'),
    details('Como a Solveplan implementa o BDC como Knowledge Core?', 'A Solveplan estrutura o SAP BDC com foco no contexto de negócio: unificação de dados mestre, mapeamento de hierarquias organizacionais, integração de fontes externas com semântica SAP e configuração de data products certificados. O objetivo é que o BDC entregue ao Knowledge Graph o contexto que os agentes precisam para operar.'),

    h5('Fontes'),
    ul([
        'SAP News Center — Accelerate the Autonomous Enterprise with SAP Business Data Cloud',
        'SAP — SAP Business Data Cloud',
        'SAVIC Technologies — SAP Business Data Cloud in 2026 Explained',
        'E3 Magazine — SAP Knowledge Graph and Vector Engine',
        'BARC — SAP data and analytics 2026: From roadmap to reality',
        'Futurum Group — Precision Over Prose: Why SAP Knowledge Graph is the Secret to Production-Ready AI',
    ]),
]

# ─── POST 3: SAP JOULE WORK ───────────────────────────────────────────────────

post3_parts = [
    p('Quantos usuários deixam de explorar o potencial do ERP porque não sabem navegar nele? Com o Joule Work, o SAP passou a ser operado em linguagem natural — e a complexidade de navegação deixou de ser uma barreira.'),

    h5('O que é o SAP Joule Work?'),
    p(f'O SAP Joule Work é a nova camada de engajamento do {a("SAP Joule", BLOG+"sap-business-ai-platform/")} — um workspace unificado onde usuários descrevem o que precisam fazer em linguagem natural e o Joule executa: abre processos, lança entradas, inicia workflows e coordena agentes em múltiplos sistemas.'),
    p(f'A diferença em relação à versão anterior do Joule é estrutural. A versão original era um copiloto — respondia perguntas, sugeria próximos passos, mas deixava a execução para o usuário. O Joule Work executa. Integra {a("SAP Datasphere", DS_URL)}, S/4HANA, Ariba, SuccessFactors e sistemas externos em um único ponto de trabalho.'),

    h5('Por que a SAP refez o Joule do zero?'),
    p('A SAP reconheceu publicamente que o Joule Studio original não entregou o que prometia. A ferramenta era limitada a interações predefinidas e não suportava a complexidade real dos processos empresariais.'),
    p('O Joule Studio 2.0, apresentado no SAPPHIRE 2026 com primeiros clientes recebendo a versão a partir de junho, foi reconstruído sobre três princípios:'),
    ul([
        '<strong>Intent-based, não script-based:</strong> o desenvolvedor descreve a intenção de negócio. O Joule Studio 2.0 traduz essa intenção em agentes e workflows contextualizados — sem precisar mapear cada passo manualmente.',
        '<strong>Múltiplos modelos de IA, semântica SAP sempre embutida:</strong> o Joule Studio 2.0 suporta modelos da SAP, Anthropic, OpenAI e Google. A empresa escolhe o modelo; a governança e o contexto de negócio são mantidos centralizados dentro do ecossistema SAP.',
        '<strong>Controle total para equipes técnicas:</strong> desenvolvedores podem construir aplicações e experiências completas com controle de cada etapa. Isso amplia o alcance do Joule Work para além dos casos de uso pré-construídos.',
    ]),

    h5('O que o Joule Work faz na prática?'),
    p('O Joule Work redefine como usuários interagem com o SAP no dia a dia — não é uma interface nova para as mesmas funções antigas:'),
    ul([
        '<strong>Workspace unificado por intenção:</strong> em vez de acessar transações separadas no S/4HANA, Ariba, SuccessFactors ou SAP Datasphere, o usuário descreve o que precisa — "analise as variações de custo do trimestre" — e o Joule Work coordena o que for necessário para entregar o resultado.',
        '<strong>Execução, não só consulta:</strong> a diferença crítica do Joule Work é a capacidade de executar transações. O usuário não recebe uma sugestão — o Joule executa o lançamento, redireciona o pedido, processa o ajuste.',
        '<strong>Integração com sistemas além do SAP:</strong> o Joule Work foi construído com suporte a padrões abertos de interoperabilidade entre agentes. Isso significa que o Joule pode coordenar ações em Salesforce, ServiceNow ou qualquer sistema conectado via integração aberta.',
        '<strong>Voz como canal de trabalho:</strong> a parceria com LiveKit trouxe IA de voz ao Joule — não como feature demonstrativa, mas como canal de trabalho real para manufatura, logística, campo e atendimento presencial.',
        '<strong>Mobile já disponível:</strong> o aplicativo móvel do Joule Work está em disponibilidade geral. O desktop e a versão completa estão no programa Early Adopter desde maio de 2026.',
    ]),

    h5('O que muda para usuários SAP Datasphere e Analytics Cloud'),
    p(f'Para empresas que usam {a("SAP Datasphere", DS_URL)} e SAP Analytics Cloud — dois produtos centrais no portfólio da Solveplan —, o Joule Work representa uma mudança direta na experiência de uso.'),
    p(f'O Joule está disponível no {a("SAP Datasphere", DS_URL)}, permitindo que usuários naveguem pela plataforma, façam perguntas sobre dados e executem tarefas em linguagem natural — sem precisar conhecer a estrutura de modelos ou a localização de cada dataset.'),
    p('Ao contrário de ferramentas de BI que exigem que o usuário saiba onde os dados estão, o Joule Work integrado ao Datasphere acessa o contexto semanticamente estruturado da plataforma e devolve respostas contextualizadas. O impacto prático em duas dimensões:'),
    ul([
        '<strong>Adoção:</strong> usuários que evitavam o Datasphere por complexidade de navegação passam a interagir via linguagem natural.',
        '<strong>Velocidade:</strong> análises que dependiam de um especialista para montar uma query passam a ser acessíveis para o usuário de negócio.',
    ]),

    h5('O SAP que os usuários sempre quiseram — se os dados estiverem no lugar'),
    p('O Joule Work resolve um problema antigo do ERP: a complexidade de navegação que mantinha o poder do sistema restrito a especialistas. Com linguagem natural como interface, o SAP passa a ser acessível para quem toma decisões — não apenas para quem configura transações.'),
    p(f'Mas a experiência depende do que está embaixo. Joule Work sobre dados fragmentados entrega respostas fragmentadas. Sobre dados bem governados — estruturados no {a("SAP BDC", BDC_URL)} com semântica de negócio — entrega o contexto que permite ao usuário tomar decisões.'),
    p(f'Para a Solveplan, parceira SAP Gold especializada em {a("SAP Datasphere", DS_URL)} e SAP Analytics Cloud, o Joule Work representa uma convergência direta entre infraestrutura de dados e experiência do usuário. O trabalho de estruturar dados no Datasphere e no BDC é o que determina a qualidade do que o Joule Work entrega.'),
    p('Fale com a Solveplan para entender se o seu ambiente de dados está pronto para o Joule Work.'),

    CTA,

    h5('FAQ — SAP Joule Work'),
    details('O que é o SAP Joule Work?', 'O SAP Joule Work é a nova camada de engajamento do Joule — um workspace unificado onde usuários operam processos SAP em linguagem natural. O Joule Work executa transações, coordena agentes e consulta dados em múltiplos sistemas SAP e de terceiros.'),
    details('Qual é a diferença entre Joule Work e o Joule anterior?', 'O Joule original sugeria ações — o usuário precisava executar. O Joule Work executa de ponta a ponta: lança entradas, inicia workflows, coordena agentes. A diferença é entre um copiloto e um operador.'),
    details('O que é o Joule Studio 2.0?', 'O ambiente para desenvolvedores construírem agentes e aplicações SAP. Reconstruído após as limitações da versão anterior, opera com intent-based design, suporta múltiplos modelos de IA e dá controle total às equipes técnicas para construir experiências além dos casos de uso pré-construídos.'),
    details('O Joule Work está disponível no SAP Datasphere?', 'Sim. O Joule está disponível no SAP Datasphere, permitindo que usuários consultem dados e executem tarefas em linguagem natural — sem precisar conhecer a estrutura técnica da plataforma.'),
    details('O Joule Work suporta voz?', 'Sim. A parceria com LiveKit trouxe IA de voz ao Joule Work para manufatura, logística, campo e atendimento presencial. O objetivo é que voz seja um canal de trabalho real, não uma demonstração.'),
    details('Como a Solveplan apoia empresas na adoção do Joule Work?', 'A Solveplan implementa SAP Datasphere e SAP BDC — os componentes que fornecem o contexto de dados para que o Joule Work entregue respostas precisas e ações confiáveis. Para empresas que querem avaliar sua prontidão para o Joule Work, a Solveplan realiza diagnósticos de maturidade analítica.'),

    h5('Fontes'),
    ul([
        'Complete AI Training — SAP expands Joule with agentic AI workspace at Sapphire 2026',
        'SiliconANGLE — SAP recasts Joule as the front door to autonomous enterprise AI',
        'SAP News Center — Announcing New Joule Studio for Enterprise Scale Agentic Development',
        'SAP Community — SAP UX Update: The New Joule Work Engagement Layer',
        'SAP News Center — The Future of the Enterprise Is Autonomous',
    ]),
]

# ─── POST 4: SAP KNOWLEDGE GRAPH ─────────────────────────────────────────────

post4_parts = [
    p(f'Enquanto modelos genéricos respondem com base na internet, o SAP Knowledge Graph ancora cada agente em 50 anos de engenharia ERP — e nos dados reais da sua empresa.'),

    h5('O que é o SAP Knowledge Graph?'),
    p(f'O SAP Knowledge Graph é a camada de conhecimento estruturado que fornece contexto empresarial para os agentes de IA do ecossistema SAP. Mapeia 452.000 tabelas e 7,3 milhões de campos do S/4HANA em relações semânticas compreensíveis por máquina — processos, entidades, políticas e hierarquias de aprovação codificados para uso por agentes.'),
    p(f'É componente central do SAP AI Foundation e opera com uma abordagem neuro-simbólica: combina redes neurais com conhecimento simbólico explícito. O resultado é IA que não apenas gera respostas plausíveis — raciocina dentro de um mapa verificável do negócio.'),

    h5('O problema que ele resolve: IA sem contexto de negócio erra com precisão'),
    p('Um modelo de linguagem genérico sabe o que é uma "reconciliação financeira" no sentido acadêmico. Não sabe como ela funciona na sua empresa: quais contas fazem parte do processo, quais as tolerâncias de variação aceitáveis, quem aprova exceções.'),
    p('Quando um agente sem contexto de negócio executa uma tarefa dentro do ERP, ele opera sobre estruturas que não entende. O resultado não é falha óbvia — é ação aparentemente correta que viola políticas internas ou produz inconsistências que só aparecem no próximo fechamento.'),
    p('O SAP Knowledge Graph resolve esse problema pela raiz. Em vez de depender de prompts genéricos ou documentação estática, os agentes acessam um mapa vivo do negócio — atualizado com a lógica real dos processos SAP.'),

    h5('O que o SAP AI Foundation entrega na prática'),
    p('O SAP AI Foundation foi construído sobre componentes técnicos que têm implicações diretas de negócio:'),
    p('<strong>O Knowledge Graph como mapa de decisões:</strong> as 452.000 tabelas do S/4HANA e seus relacionamentos não são apenas documentação. São o vocabulário que os agentes usam para interpretar cada instrução dentro do contexto correto do processo.'),
    p('<strong>Modelos especializados em dados de negócio:</strong> o SAP AI Foundation incorpora modelos treinados especificamente em dados do ERP, não apenas em texto. Isso garante precisão em domínios como finanças, logística e RH — onde terminologia técnica e lógica de processo são inseparáveis.'),
    p('<strong>Governança centralizada com trilha de auditoria:</strong> o Agent Hub — camada de governança do AI Foundation — centraliza o registro de agentes, controles de acesso por papel, trilhas de auditoria de decisões e mecanismos de override humano. Para equipes de compliance e auditoria, isso significa que cada ação de um agente é rastreável.'),

    h5('Por que isso muda a equação para quem usa agentes SAP'),
    p('A diferença prática entre um agente com e sem Knowledge Graph não é de qualidade de resposta — é de confiabilidade operacional.'),
    p('Um agente com acesso ao Knowledge Graph sabe, por exemplo, que uma variação de custo acima de determinado percentual exige aprovação do controller antes de ser lançada — porque essa regra está mapeada no contexto do processo, não apenas no manual de procedimentos.'),
    p('Para empresas que operam em ambientes SAP complexos — múltiplas entidades, moedas, legislações — essa camada de conhecimento é o que permite escalar automação com segurança, em vez de escalar com risco.'),
    p('A abordagem neuro-simbólica do SAP Knowledge Graph tem uma implicação adicional para CIOs e equipes de governança: as decisões dos agentes são explicáveis. O sistema pode mostrar por qual caminho de raciocínio chegou a uma ação — o que é essencial para auditoria e conformidade regulatória.'),

    h5('SAP BDC como extensão do Knowledge Graph para os dados da empresa'),
    p(f'O SAP Knowledge Graph fornece o contexto genérico do universo SAP — processos, tabelas e relações comuns a toda a base de clientes. É o que qualquer empresa SAP tem acesso.'),
    p(f'É aqui que o {a("SAP Business Data Cloud", BDC_URL)} entra como extensão do Knowledge Graph para o contexto específico da empresa.'),
    p(f'O {a("SAP BDC", BDC_URL)} integra dados de múltiplas fontes — SAP e não-SAP — em uma camada governada e com semântica de negócio. Quando essa camada está estruturada, o Knowledge Graph deixa de ser um mapa genérico do universo SAP e se torna o mapa específico da organização — com suas hierarquias, políticas, histórico e exceções.'),

    h5('Os agentes SAP são tão bons quanto o contexto que os alimenta'),
    p('O SAP Knowledge Graph é a base que diferencia automação empresarial de automação genérica. Mas o Knowledge Graph genérico é apenas o começo — o que determina a precisão dos agentes na sua empresa é a qualidade dos dados que alimentam sua instância.'),
    p('Fale com a Solveplan para entender o estado atual do seu ambiente de dados e o que precisa ser feito antes de ativar agentes SAP nos seus processos.'),

    CTA,

    h5('FAQ — SAP Knowledge Graph'),
    details('O que é o SAP Knowledge Graph?', 'O SAP Knowledge Graph é a camada de conhecimento estruturado do SAP AI Foundation que mapeia 452.000 tabelas e 7,3 milhões de campos do S/4HANA em relações semânticas. Fornece contexto empresarial para os agentes SAP — processos, políticas e hierarquias de aprovação codificados para uso por IA.'),
    details('Qual a diferença entre SAP Knowledge Graph e um modelo de linguagem comum?', 'Um modelo de linguagem genérico sabe o que os processos significam no sentido geral. O SAP Knowledge Graph mapeia como eles funcionam especificamente no universo SAP — e, com o BDC, como funcionam na sua empresa. Isso é o que permite que agentes tomem decisões dentro dos processos reais, não apenas gerem texto plausível sobre eles.'),
    details('O que é a abordagem neuro-simbólica do SAP AI Foundation?', 'Combina redes neurais com conhecimento simbólico explícito. Isso reduz erros e permite rastrear por que um agente tomou uma decisão — essencial para auditoria e conformidade em processos empresariais críticos.'),
    details('O SAP BDC é necessário para usar o SAP Knowledge Graph?', 'O SAP Knowledge Graph fornece o contexto genérico do universo SAP. O SAP BDC estende esse contexto com os dados específicos da empresa. Para agentes que operam em processos críticos — fechamento, compras, RH —, o BDC é o que garante que o contexto seja preciso para o ambiente específico da organização.'),
    details('Como a Solveplan apoia empresas que querem usar o SAP Knowledge Graph?', 'A Solveplan implementa SAP BDC e SAP Datasphere — a camada que alimenta o Knowledge Graph com dados reais, governados e semanticamente estruturados. Para empresas que querem avaliar sua prontidão para agentes SAP, a Solveplan realiza diagnósticos de maturidade analítica.'),

    h5('Fontes'),
    ul([
        'SAP News Center — SAP Unveils the Autonomous Enterprise',
        'SAVIC Technologies — SAP AI Foundation Architecture 2026: Knowledge Graph, SAP-RPT-1 & Agent Hub',
        'Constellation Research — SAP Sapphire 2026: AI agent accuracy, embedded domain knowledge and processes',
        'Futurum Group — Precision Over Prose: Why SAP Knowledge Graph is the Secret to Production-Ready AI',
        'E3 Magazine — SAP Knowledge Graph and Vector Engine',
    ]),
]

# ─── POST 5: SAP E ANTHROPIC ──────────────────────────────────────────────────

post5_parts = [
    p(f'A parceria entre SAP e Anthropic vai além de adicionar um modelo de linguagem ao portfólio. Claude passa a ser a camada de raciocínio dos agentes que vão operar seus processos SAP.'),

    h5('O que é a parceria entre SAP e Anthropic?'),
    p(f'A parceria entre SAP e Anthropic integra o Claude — família de modelos de linguagem da Anthropic — como capacidade primária de raciocínio dentro do {a("SAP Business AI Platform", BLOG+"sap-business-ai-platform/")}. Isso significa que os agentes {a("Joule", BLOG+"sap-joule-work/")} que executam processos em finanças, RH, compras e supply chain usam o Claude como motor de decisão.'),
    p('Na prática, quando um agente Joule precisa raciocinar sobre um processo complexo — fechar o trimestre, responder a uma consulta trabalhista, redirecionar um pedido de compra — é o Claude que coordena a cadeia de raciocínio dentro do contexto fornecido pelo ecossistema SAP.'),

    h5('Por que Claude — e não qualquer modelo de linguagem'),
    p('A escolha pelo Claude como modelo de raciocínio primário tem uma razão técnica específica para processos empresariais.'),
    p('Fluxos de trabalho no ERP raramente são lineares. Um fechamento financeiro envolve validar entradas, identificar inconsistências, acionar aprovações, executar correções e documentar cada passo — tudo dentro de políticas e hierarquias que variam por entidade e moeda.'),
    p('O Claude foi desenvolvido com capacidade de raciocínio em múltiplos passos: mantém contexto ao longo de uma cadeia de decisões, distingue quando executar de quando escalar para aprovação humana, e opera com precisão em domínios onde erros têm consequências financeiras ou regulatórias.'),
    p('Christian Klein, CEO da SAP, foi direto ao anunciar a parceria: "O Autonomous Enterprise requer IA que compreenda contexto empresarial de verdade. Claude traz o raciocínio que nossos agentes precisam para operar com confiança."'),

    h5('Como Claude opera dentro dos processos SAP'),
    p(f'A integração do Claude no {a("SAP Business AI Platform", BLOG+"sap-business-ai-platform/")} não funciona como uma API externa chamada pontualmente. Claude opera como camada de raciocínio nativa — com acesso ao {a("SAP Knowledge Graph", BLOG+"sap-knowledge-graph/")}, às políticas de processo e ao histórico transacional disponível via {a("SAP BDC", BDC_URL)}.'),
    p('Isso significa que quando o Joule recebe uma instrução — "processe os lançamentos de ajuste do fechamento de abril para a entidade Brasil" — o Claude não interpreta isso como texto genérico. Interpreta como uma instrução dentro do contexto real da empresa: quais contas estão envolvidas, quais as tolerâncias aceitáveis, quais aprovações são necessárias.'),
    p('Os domínios cobertos pela integração incluem:'),
    ul([
        '<strong>Finanças (S/4HANA):</strong> fechamento contábil, reconciliações, lançamentos de diário, análise de variações.',
        '<strong>RH (SAP SuccessFactors):</strong> respostas a consultas de colaboradores, processamento de benefícios, conformidade trabalhista.',
        '<strong>Compras (SAP Ariba):</strong> gestão de fornecedores, redirecionamento de pedidos, validação de contratos.',
        '<strong>Sistemas de terceiros:</strong> qualquer sistema conectado via integração aberta — o agente coordena ações que cruzam o perímetro SAP.',
    ]),
    p('Daniela Amodei, co-fundadora da Anthropic, descreveu o objetivo da parceria: "Construímos Claude para suportar raciocínio complexo com segurança. Aplicar isso ao núcleo dos processos empresariais — onde as decisões têm consequências reais — é exatamente onde queremos que o Claude opere."'),

    h5('Governança: IA que opera dentro dos seus controles — não ao lado deles'),
    p('Um dos pontos mais relevantes da parceria SAP-Anthropic para equipes de compliance, auditoria e TI é a forma como a governança foi desenhada.'),
    p(f'Claude não opera com acesso irrestrito ao ambiente SAP. Age dentro dos mesmos controles que governam decisões humanas: permissões por papel, limites de alçada, políticas de aprovação. O {a("SAP Knowledge Graph", BLOG+"sap-knowledge-graph/")} é o que torna esse controle possível — os agentes conhecem as regras porque elas estão mapeadas no contexto do processo.'),
    p('Isso tem implicação direta para setores com maior rigor regulatório. A Anthropic e a SAP anunciaram desenvolvimento conjunto de guardrails específicos para processos financeiros e de RH — onde erros de agente têm consequências legais e regulatórias.'),

    h5('O que a parceria significa para quem está adotando SAP BDC'),
    p(f'Para empresas que estão implementando ou evoluindo seu ambiente SAP — especialmente aquelas que já têm ou estão migrando para o {a("SAP Business Data Cloud", BDC_URL)} —, a parceria com a Anthropic tem uma implicação direta.'),
    p(f'O Claude opera sobre o contexto fornecido pelo {a("SAP Business AI Platform", BLOG+"sap-business-ai-platform/")}. O componente que torna esse contexto específico para a empresa é o {a("SAP BDC", BDC_URL)}.'),
    p('Em termos diretos: o Claude é tão preciso quanto os dados que o alimentam. Um agente com acesso ao BDC bem estruturado raciocina dentro do contexto real da empresa. Um agente com dados fragmentados raciocina sobre suposições — e automatiza decisões baseadas nessas suposições.'),
    p('Para a Solveplan, parceira SAP Gold especializada em implementação de SAP BDC e SAP Datasphere na América Latina, a parceria SAP-Anthropic reforça o que já orientava o trabalho com clientes: a fundação de dados não é infraestrutura — é o ativo que determina o que a IA consegue ou não consegue fazer dentro do seu negócio.'),

    h5('A IA que vai operar seus processos SAP depende do que você tem hoje'),
    p('A parceria SAP-Anthropic coloca o Claude no centro da camada de raciocínio do seu ERP. O que determina a qualidade desse raciocínio — e a confiabilidade das decisões que ele vai tomar nos seus processos — é a qualidade dos dados que você fornece a ele.'),
    p('Fale com a Solveplan para entender se o seu ambiente de dados está pronto para suportar agentes SAP com o nível de precisão que processos críticos exigem.'),

    CTA,

    h5('FAQ — Parceria SAP e Anthropic'),
    details('O que é a parceria entre SAP e Anthropic?', 'A parceria integra o Claude, da Anthropic, como modelo de raciocínio primário dos agentes Joule no SAP Business AI Platform. Claude coordena fluxos de trabalho em finanças, RH e compras dentro do contexto fornecido pelo ecossistema SAP — com governança centralizada e acesso ao SAP Knowledge Graph.'),
    details('Por que a SAP escolheu o Claude e não outro modelo?', 'Pela capacidade de raciocínio em múltiplos passos — necessária para coordenar fluxos empresariais não lineares com precisão. Claude mantém contexto ao longo de cadeias de decisão longas e distingue quando executar de quando escalar para aprovação humana.'),
    details('O SAP usa apenas o Claude ou outros modelos também?', 'O SAP Business AI Platform é multi-LLM: além do Claude, suporta modelos da OpenAI, Google e NVIDIA. O Claude atua como modelo de raciocínio primário nos agentes Joule para finanças, RH e compras, mas a arquitetura permite que cada empresa configure o modelo preferido por caso de uso.'),
    details('Como a governança funciona com IA agêntica no SAP?', 'Claude opera dentro dos controles já configurados no ambiente SAP — aprovações, limites de alçada, restrições de acesso por papel. O SAP Knowledge Graph é o que torna esse controle possível: os agentes conhecem as regras de processo porque elas estão mapeadas no contexto, não apenas documentadas em texto.'),
    details('A parceria SAP-Anthropic cobre setores específicos?', 'A parceria cobre finanças (S/4HANA), RH (SuccessFactors) e compras (Ariba) como domínios primários. SAP e Anthropic anunciaram desenvolvimento conjunto de guardrails específicos para processos financeiros e de RH — onde decisões de agente têm consequências regulatórias.'),
    details('O que a parceria significa para quem está implementando SAP BDC?', 'O Claude opera sobre o contexto fornecido pelo SAP BDC. Quanto melhor estruturado o BDC — dados mestre unificados, hierarquias corretas, políticas mapeadas —, mais preciso é o raciocínio do Claude dentro dos processos da empresa. A qualidade do BDC determina diretamente a qualidade das decisões dos agentes.'),

    h5('Fontes'),
    ul([
        'SAP News Center — SAP and Anthropic: Claude on SAP Business AI Platform',
        'ERP Today — How SAP Is Using Anthropic, NVIDIA and Palantir to Shape Its Autonomous Enterprise Stack',
        'The Next Web — SAP unveils Autonomous Enterprise with 200+ AI agents and Anthropic partnership',
        'SAP News Center — SAP Unveils the Autonomous Enterprise',
        'Digital Today — SAP expands alliance with Anthropic to ease AI agent development with Claude',
    ]),
]

# ─── POSTS CONFIG ─────────────────────────────────────────────────────────────

posts = [
    {
        "title": "SAP Autonomous Suite: como a SAP vai automatizar finanças, supply chain e RH com agentes de IA",
        "slug": "sap-autonomous-suite",
        "focus_kw": "SAP Autonomous Suite",
        "meta_title": "SAP Autonomous Suite: o que foi anunciado no SAPPHIRE 2026",
        "meta_desc": "O SAP Autonomous Suite automatiza finanças, supply chain e RH com agentes de IA. Entenda os 5 domínios, o Autonomous Close Assistant e o que sua empresa precisa fazer agora.",
        "parts": post1_parts,
    },
    {
        "title": "SAP BDC como Knowledge Core: por que os agentes SAP precisam conhecer a sua empresa, não só o SAP",
        "slug": "sap-bdc-knowledge-core",
        "focus_kw": "SAP Business Data Cloud",
        "meta_title": "SAP Business Data Cloud: o Knowledge Core que os agentes SAP precisam",
        "meta_desc": "O SAP BDC transforma o Knowledge Graph genérico da SAP no contexto específico da sua empresa. Entenda data products, Domain Models e por que isso determina o retorno de toda IA no SAP.",
        "parts": post2_parts,
    },
    {
        "title": "SAP Joule Work: de assistente de chat a camada operacional do ERP",
        "slug": "sap-joule-work",
        "focus_kw": "SAP Joule Work",
        "meta_title": "SAP Joule Work: o que mudou e o que isso significa para quem usa SAP",
        "meta_desc": "O SAP Joule Work executa processos em linguagem natural — lançamentos, workflows e análises no SAP Datasphere. Entenda o que mudou no Joule e o impacto para usuários SAP.",
        "parts": post3_parts,
    },
    {
        "title": "SAP Knowledge Graph: a camada que faz os agentes SAP entenderem o seu negócio",
        "slug": "sap-knowledge-graph",
        "focus_kw": "SAP Knowledge Graph",
        "meta_title": "SAP Knowledge Graph: o que é e por que os agentes SAP dependem dele",
        "meta_desc": "O SAP Knowledge Graph mapeia 452 mil tabelas do S/4HANA para dar contexto real aos agentes SAP. Entenda a abordagem neuro-simbólica e o que isso significa para o seu negócio.",
        "parts": post4_parts,
    },
    {
        "title": "SAP e Anthropic: por que o Claude se tornou o motor de raciocínio dos agentes SAP",
        "slug": "sap-anthropic-parceria",
        "focus_kw": "SAP Anthropic",
        "meta_title": "SAP e Anthropic: por que o Claude virou o motor dos agentes SAP",
        "meta_desc": "A parceria SAP e Anthropic integra o Claude como modelo de raciocínio dos agentes Joule. Entenda o que isso significa para finanças, RH e compras no seu ambiente SAP.",
        "parts": post5_parts,
    },
]

# ─── PUBLISH ──────────────────────────────────────────────────────────────────

results = []
for cfg in posts:
    content = '\n\n'.join(cfg["parts"])

    # Create post as draft
    resp = requests.post(
        f"{WP}/posts",
        auth=AUTH,
        json={
            "title": cfg["title"],
            "slug": cfg["slug"],
            "content": content,
            "status": "draft",
            "excerpt": cfg["meta_desc"],
            "meta": {
                "rank_math_focus_keyword": cfg["focus_kw"],
                "rank_math_title": cfg["meta_title"],
                "rank_math_description": cfg["meta_desc"],
            }
        }
    )

    if resp.status_code in (200, 201):
        post_id = resp.json()["id"]
        post_url = resp.json().get("link", "")
        print(f"✅ Criado: {cfg['slug']} — ID {post_id}")
        results.append({"slug": cfg["slug"], "id": post_id, "url": post_url})
    else:
        print(f"❌ Erro {resp.status_code}: {cfg['slug']} — {resp.text[:200]}")

print("\n=== RESUMO ===")
for r in results:
    print(f"  ID {r['id']} — /blog/{r['slug']} — {r['url']}")

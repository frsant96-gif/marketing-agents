import sys, requests
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
WP = "https://solveplan.com/wp-json/wp/v2"
POST_ID = 10689

BDC_URL  = "https://solveplan.com/sap-business-data-cloud/"
DS_URL   = "https://solveplan.com/sap-datasphere/"
BLOG     = "https://solveplan.com/blog/"

def h5(text):
    return (
        '<!-- wp:heading {"level":5} -->\n'
        f'<h5 class="wp-block-heading"><strong>{text}</strong></h5>\n'
        '<!-- /wp:heading -->'
    )

def p(text):
    return f'<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->'

def italic(items):
    return '\n\n'.join(
        f'<!-- wp:paragraph -->\n<p><em>{i}</em></p>\n<!-- /wp:paragraph -->'
        for i in items
    )

def details(question, answer):
    return (
        '<!-- wp:details -->\n'
        f'<details class="wp-block-details"><summary>{question}</summary>'
        '<!-- wp:paragraph -->\n'
        f'<p>{answer}</p>\n'
        '<!-- /wp:paragraph --></details>\n'
        '<!-- /wp:details -->'
    )

def a(text, url):
    return f'<a href="{url}">{text}</a>'

CTA = (
    '<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n'
    '<div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"primary","textColor":"white","style":{"border":{"radius":"4px"}}} -->\n'
    '<div class="wp-block-button"><a class="wp-block-button__link has-white-color has-primary-background-color has-text-color has-background wp-element-button" '
    'href="https://bdcstrategy.solveplan.ai/" target="_blank" rel="noopener">Avalie a maturidade dos seus dados com a Solveplan</a></div>\n'
    '<!-- /wp:button --></div>\n'
    '<!-- /wp:buttons -->'
)

parts = [
    p(f'O {a("SAP Knowledge Graph", BLOG+"sap-knowledge-graph/")} sabe tudo sobre como o ERP funciona. O {a("SAP Business Data Cloud", BDC_URL)} é o que faz ele saber como o <em>seu</em> ERP funciona.'),

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
    p(f'Quando o BDC integra os dados da organização — de fontes SAP e não-SAP — e os estrutura com semântica de negócio, estende o Knowledge Graph com cinco camadas de contexto proprietário:'),
    italic([
        f'<strong>Hierarquias organizacionais reais:</strong> quais entidades jurídicas existem, como estão estruturadas, quais são as relações de aprovação entre elas.',
        '<strong>Dados mestre governados:</strong> clientes, fornecedores, materiais, centros de custo — com identidade unificada e sem duplicação entre sistemas.',
        '<strong>Histórico transacional:</strong> o que aconteceu, quando, quem aprovou e por quê.',
        '<strong>Regras de processo:</strong> políticas internas, limites de alçada, exceções negociadas.',
        f'<strong>Dados externos integrados:</strong> fontes fora do ecossistema SAP trazidas ao mesmo contexto semântico via {a("SAP Datasphere", DS_URL)}.',
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
    p('Ao contrário de implementações que tratam o BDC apenas como caminho técnico de migração, a abordagem da Solveplan estrutura desde o início o contexto semântico: dados mestre unificados, hierarquias organizacionais corretas, fontes externas integradas com semântica de negócio.'),
    p('A Solveplan vê frequentemente dois perfis ao avaliar prontidão para IA no SAP:'),
    p(f'<strong>Perfil A:</strong> dados mestre limpos, hierarquias mapeadas, {a("BDC", BDC_URL)} estruturado com semântica de negócio. Esses clientes chegam ao {a("SAP Autonomous Suite", BLOG+"sap-autonomous-suite/")} com o contexto no lugar — os agentes encontram o que precisam para operar.'),
    p(f'<strong>Perfil B:</strong> dados fragmentados, múltiplas fontes com definições conflitantes, sem governança estabelecida. Esses clientes ativam agentes e rapidamente percebem que a automação amplifica inconsistências em vez de eliminá-las.'),
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
    italic([
        'SAP News Center — Accelerate the Autonomous Enterprise with SAP Business Data Cloud',
        'SAP — SAP Business Data Cloud',
        'SAVIC Technologies — SAP Business Data Cloud in 2026 Explained',
        'E3 Magazine — SAP Knowledge Graph and Vector Engine',
        'BARC — SAP data and analytics 2026: From roadmap to reality',
        'Futurum Group — Precision Over Prose: Why SAP Knowledge Graph is the Secret to Production-Ready AI',
    ]),
]

content = '\n\n'.join(parts)

r = requests.post(f"{WP}/posts/{POST_ID}", auth=AUTH, json={"content": content})
print("Update:", r.status_code)

# Verify
v = requests.get(f"{WP}/posts/{POST_ID}?context=edit", auth=AUTH).json()["content"]["raw"]
print(f"Chars:           {len(v)}")
print(f"H5 (com classe): {v.count('wp-block-heading')}")
print(f"FAQ (details):   {v.count('wp:details') // 2}")
print(f"wp:list:         {v.count('wp:list')}")
print(f"Links BDC:       {v.count('sap-business-data-cloud')}")
print(f"Links DS:        {v.count('sap-datasphere')}")
print(f"CTA:             {'OK' if 'bdcstrategy' in v else 'AUSENTE'}")
print(f"Corrompido:      {'SIM' if '<p>\\n<!-- wp:' in v else 'NAO'}")

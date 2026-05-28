import sys, requests
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
POST_ID = 10653
WP = "https://solveplan.com/wp-json/wp/v2"

BDC_URL = "https://solveplan.com/sap-business-data-cloud/"
DS_URL  = "https://solveplan.com/sap-datasphere/"
BLOG    = "https://solveplan.com/blog/"

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
    p(f'Durante o SAP SAPPHIRE Orlando 2026, a SAP apresentou uma nova arquitetura unificada de IA — e quem já tem {a("SAP BDC", BDC_URL)} está no centro disso.'),

    h5('O que é o SAP Business AI Platform?'),
    p(f'O SAP Business AI Platform é a arquitetura unificada que integra SAP Business Technology Platform, {a("SAP Business Data Cloud", BDC_URL)} e SAP AI Foundation em uma única fundação operacional. É sobre ela que os agentes Joule executam processos de negócio de ponta a ponta, com acesso a dados contextualizados e governança centralizada.'),
    p('Diferente de soluções genéricas de IA, o SAP Business AI Platform carrega 50 anos de lógica de ERP codificados em um Knowledge Graph — o que permite que agentes tomem decisões dentro dos processos reais da empresa, não apenas gerem texto.'),

    h5('Por que o SAP Business AI Platform representa uma mudança estrutural'),
    p('A SAP não lançou uma nova ferramenta. Reconfigurou a arquitetura do ERP.'),
    p(f'A visão Autonomous Enterprise — onde agentes executam processos de forma autônoma, sem intervenção manual — só é viável quando IA, dados e plataforma operam como uma fundação única. A fragmentação histórica do mercado de IA empresarial — modelos sem contexto de processo, dados sem governança, ferramentas sem integração — é o problema que o SAP Business AI Platform resolve na raiz.'),
    p('O resultado prático: um agente que fecha o mês, redireciona um pedido ou responde a uma consulta trabalhista não opera sobre texto genérico. Opera sobre as políticas, hierarquias e histórico reais da empresa. Essa diferença entre contexto genérico e contexto real é o que separa IA que imprime confiança de IA que amplifica erros.'),

    h5('SAP BDC e BTP dentro da nova arquitetura — o ponto que mais importa'),
    p(f'O SAP Business AI Platform reúne três componentes que já existiam no portfólio SAP:'),
    italic([
        f'<strong>{a("SAP Business Data Cloud", BDC_URL)}:</strong> a camada de dados — integra, governa e contextualiza dados de fontes SAP e não-SAP com semântica de negócio',
        '<strong>SAP Business Technology Platform:</strong> o ambiente de desenvolvimento, integração e extensibilidade',
        '<strong>SAP AI Foundation:</strong> a infraestrutura de modelos, orquestração e governança de IA',
    ]),
    p(f'Para quem já implementou {a("SAP BDC", BDC_URL)}, a implicação é imediata: a fundação de dados está no lugar. O BDC é o componente que transforma o Knowledge Graph genérico da SAP no mapa do negócio da empresa — e é esse mapa que determina a qualidade das decisões dos agentes.'),
    p('Empresas que ainda não estruturaram o ambiente de dados no SAP BDC chegam a essa arquitetura com uma lacuna real. Agentes sem dados bem governados tomam decisões sobre informações fragmentadas — e automação sobre dado fragmentado consolida erros mais rápido do que qualquer equipe humana conseguiria corrigir.'),
    p(f'A SAP demonstrou também integração zero-copy entre SAP BDC e Amazon Athena via parceria com AWS — o que amplia o alcance da plataforma para dados fora do ambiente SAP sem necessidade de replicação.'),

    h5('Joule, Knowledge Graph e a parceria com a Anthropic'),
    p(f'Três componentes definem o que o SAP Business AI Platform entrega na prática:'),

    h5('Joule'),
    p(f'O assistente da SAP deixou de ser um chatbot e passou a ser a camada de orquestração de agentes. No SAPPHIRE 2026, a SAP demonstrou Joule coordenando fluxos que atravessam RH, compras e supply chain sem intervenção manual. O Joule está disponível no {a("SAP Datasphere", DS_URL)}, permitindo que usuários consultem e executem tarefas diretamente na plataforma de dados usando linguagem natural.'),

    h5('SAP Knowledge Graph'),
    p(f'É a peça que diferencia o SAP Business AI Platform de qualquer solução genérica de IA empresarial. O Knowledge Graph codifica 50 anos de engenharia ERP em relações semânticas acessíveis por máquina — processos, entidades, políticas e hierarquias de aprovação. Um agente que raciocina sobre um pedido de compra não opera sobre dados brutos: opera sobre contexto estruturado que inclui as regras reais da empresa.'),

    h5('Parceria com a Anthropic'),
    p(f'A SAP confirmou a Anthropic como parceira de modelos de fundação. Os modelos Claude estão disponíveis no SAP AI Foundation para agentes Joule em RH, compras e supply chain. A arquitetura é multi-LLM — a empresa escolhe entre Anthropic, OpenAI, Google e outros provedores, mantendo governança centralizada dentro do ecossistema SAP.'),

    h5('Quem já tem SAP BDC está no lugar certo — o que fazer a partir daqui'),
    p('A pergunta mais frequente depois do SAP SAPPHIRE Orlando 2026 é direta: "o que eu preciso fazer agora?"'),
    p(f'Quem já tem {a("SAP BDC", BDC_URL)} implementado está no caminho certo. O próximo passo é avaliar quais processos têm maior potencial de automação com Joule e planejar a adoção do SAP Autonomous Suite.'),
    p('Quem opera com dados fragmentados — SAP e fontes externas sem integração governada — precisa resolver essa fundação antes de avançar para agentes. IA sobre dados inconsistentes não acelera o negócio: consolida os erros em maior velocidade.'),
    p('Empresas que estruturarem a fundação de dados primeiro tendem a reduzir o tempo entre implementação e captura de valor das iniciativas de IA.'),
    p(f'Para a Solveplan, parceira SAP Gold especializada em SAP BDC e {a("SAP Datasphere", DS_URL)} na América Latina, o SAP SAPPHIRE 2026 confirmou a direção que já orientava o trabalho com clientes: dados bem governados são o pré-requisito para qualquer iniciativa de IA que funcione na prática.'),

    h5('Sua empresa está pronta para os agentes SAP?'),
    p('O SAP Business AI Platform muda a natureza do ERP. O que determina se sua empresa vai aproveitar essa mudança — ou apenas observá-la — é a qualidade da fundação de dados que você já tem hoje.'),
    p('Fale com a Solveplan para entender onde você está e o que precisa ser feito antes de implementar IA nos seus processos SAP.'),

    CTA,

    h5('FAQ — SAP Business AI Platform'),
    details('O que é o SAP Business AI Platform?', 'O SAP Business AI Platform é a arquitetura unificada da SAP que integra SAP BTP, SAP Business Data Cloud e SAP AI Foundation em uma fundação única para construir, implantar e governar agentes de IA com contexto de negócio real. Foi apresentada no SAP SAPPHIRE Orlando 2026 como base da visão Autonomous Enterprise.'),
    details('Qual é a diferença entre SAP Business AI Platform e SAP BTP?', 'O SAP BTP é o ambiente de desenvolvimento e integração da SAP. O SAP Business AI Platform é a arquitetura mais ampla que unifica SAP BTP, SAP Business Data Cloud e SAP AI Foundation. O BTP continua sendo o ambiente de desenvolvimento, agora como parte de uma estrutura orientada a agentes.'),
    details('O que é o Joule e como ele se encaixa na plataforma?', 'Joule é o assistente de IA da SAP e a camada de orquestração de agentes dentro do SAP Business AI Platform. Coordena workflows fim-a-fim em RH, compras, supply chain e analytics — disponível em mais de 35 soluções SAP, incluindo o SAP Datasphere.'),
    details('Quem já tem SAP BDC precisa migrar para o SAP Business AI Platform?', 'Não é uma migração — é uma evolução. O SAP Business Data Cloud é um dos componentes centrais do SAP Business AI Platform. Quem já implementou BDC está na fundação correta para adotar os agentes Joule e o SAP Autonomous Suite.'),
    details('Qual é o papel da parceria entre SAP e Anthropic?', 'A Anthropic fornece modelos Claude como opção dentro do SAP AI Foundation, ao lado de OpenAI, Google e outros. A empresa escolhe o provedor; a governança e o contexto de negócio são mantidos centralizados dentro do ecossistema SAP.'),
    details('Como a Solveplan apoia empresas nessa transição?', 'A Solveplan implementa SAP BDC e SAP Datasphere — a fundação de dados necessária para operar o SAP Business AI Platform com contexto real de negócio. Para empresas que querem avaliar seu posicionamento atual, a Solveplan realiza diagnósticos de maturidade analítica como ponto de partida.'),

    h5('Fontes'),
    italic([
        'SAP News Center — SAP Unveils Business AI Platform to Power the Autonomous Enterprise',
        'SAP News Center — SAP Unveils the Autonomous Enterprise',
        'SAPinsider — SAP Sapphire 2026: SAP Recasts ERP Around the Autonomous Enterprise and Business AI',
        'Channel Insider — SAP Sapphire 2026 Intros Autonomous Enterprise Vision',
        'SAP — SAP Business AI Platform',
        'SAP News Center — SAP Business AI: Release Highlights Q1 2026',
    ]),
]

content = '\n\n'.join(parts)

r = requests.post(
    f"{WP}/posts/{POST_ID}",
    auth=AUTH,
    json={"content": content}
)
print("Update:", r.status_code)

# Verify
verify = requests.get(f"{WP}/posts/{POST_ID}?context=edit", auth=AUTH)
saved = verify.json()["content"]["raw"]
print(f"Chars: {len(saved)}")
print(f"H5 count:      {saved.count('wp-block-heading')}")
print(f"FAQ (details): {saved.count('wp:details')}")
print(f"wp:list:       {saved.count('wp:list')}")
print(f"DS link:       {'OK' if 'sap-datasphere' in saved else 'AUSENTE'}")
print(f"BDC link:      {'OK' if 'sap-business-data-cloud' in saved else 'AUSENTE'}")
print(f"CTA:           {'OK' if 'bdcstrategy.solveplan.ai' in saved else 'AUSENTE'}")
print(f"noreferrer:    {'SIM' if 'noreferrer' in saved else 'não'}")

import sys, requests
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "vjpT R0lO 9c2G vh2w WAqA RPfU")
WP = "https://solveplan.com/wp-json/wp/v2"
POST_ID = 10692

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

def ul(items):
    lis = ''.join(f'<li>{i}</li>' for i in items)
    return (
        '<!-- wp:list -->\n'
        f'<ul class="wp-block-list">{lis}</ul>\n'
        '<!-- /wp:list -->'
    )

def faq(question, answer):
    return h5(question) + '\n\n' + p(answer)

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
    p(f'A parceria SAP Anthropic — formalizada no SAPPHIRE 2026 — integra o Claude como camada de raciocínio primária dos agentes Joule. É a SAP Anthropic que define como os agentes entendem processos financeiros, de RH e compras dentro do contexto real do ERP.'),

    h5('O que é a parceria SAP Anthropic?'),
    p(f'A parceria SAP Anthropic integra o Claude — família de modelos da Anthropic — como capacidade primária de raciocínio dentro do {a("SAP Business AI Platform", BLOG+"sap-business-ai-platform/")}. Os agentes {a("Joule", BLOG+"sap-joule-work/")} que executam processos em finanças, RH, compras e supply chain usam o Claude como motor de decisão.'),
    p('Na prática, quando um agente Joule precisa raciocinar sobre um processo complexo — fechar o trimestre, responder a uma consulta trabalhista, redirecionar um pedido de compra — é o Claude que coordena a cadeia de raciocínio dentro do contexto fornecido pelo ecossistema SAP.'),

    h5('Por que Claude — e não qualquer modelo de linguagem'),
    p('A escolha pelo Claude como modelo de raciocínio primário tem uma razão técnica específica para processos empresariais.'),
    p(f'Ao contrário de modelos de linguagem genéricos, o Claude opera dentro do contexto do {a("SAP Knowledge Graph", BLOG+"sap-knowledge-graph/")} — com acesso às políticas reais da empresa. Fluxos de trabalho no ERP raramente são lineares: um fechamento financeiro envolve validar entradas, identificar inconsistências, acionar aprovações, executar correções e documentar cada passo — tudo dentro de políticas e hierarquias que variam por entidade e moeda.'),
    p('O Claude foi desenvolvido com capacidade de raciocínio em múltiplos passos: mantém contexto ao longo de uma cadeia de decisões, distingue quando executar de quando escalar para aprovação humana, e opera com precisão em domínios onde erros têm consequências financeiras ou regulatórias.'),
    p('Christian Klein, CEO da SAP, ao anunciar a parceria SAP Anthropic: <em>"O Autonomous Enterprise requer IA que compreenda contexto empresarial de verdade. Claude traz o raciocínio que nossos agentes precisam para operar com confiança."</em>'),

    h5('Como o Claude opera dentro dos processos SAP'),
    p(f'Na arquitetura SAP Anthropic, o Claude não funciona como uma API externa chamada pontualmente. Opera como camada de raciocínio nativa — com acesso ao {a("SAP Knowledge Graph", BLOG+"sap-knowledge-graph/")}, às políticas de processo e ao histórico transacional disponível via {a("SAP BDC", BDC_URL)}.'),
    p('Quando o Joule recebe uma instrução — <em>"processe os lançamentos de ajuste do fechamento de abril para a entidade Brasil"</em> — o Claude não interpreta isso como texto genérico. Interpreta como uma instrução dentro do contexto real da empresa: quais contas estão envolvidas, quais as tolerâncias aceitáveis, quais aprovações são necessárias.'),
    p('Os domínios cobertos pela integração SAP Anthropic incluem:'),
    ul([
        '<strong>Finanças (S/4HANA):</strong> fechamento contábil, reconciliações, lançamentos de diário, análise de variações.',
        '<strong>RH (SAP SuccessFactors):</strong> respostas a consultas de colaboradores, processamento de benefícios, conformidade trabalhista.',
        '<strong>Compras (SAP Ariba):</strong> gestão de fornecedores, redirecionamento de pedidos, validação de contratos.',
        '<strong>Sistemas de terceiros:</strong> qualquer sistema conectado via integração aberta — o agente coordena ações que cruzam o perímetro SAP.',
    ]),

    h5('Governança: IA que opera dentro dos seus controles'),
    p('Um dos pontos mais relevantes da parceria SAP Anthropic para equipes de compliance, auditoria e TI é a forma como a governança foi desenhada.'),
    p(f'O Claude não opera com acesso irrestrito ao ambiente SAP. Age dentro dos mesmos controles que governam decisões humanas: permissões por papel, limites de alçada, políticas de aprovação. O {a("SAP Knowledge Graph", BLOG+"sap-knowledge-graph/")} é o que torna esse controle possível — os agentes conhecem as regras porque elas estão mapeadas no contexto do processo.'),
    p('A Anthropic e a SAP anunciaram desenvolvimento conjunto de guardrails específicos para processos financeiros e de RH — onde erros de agente têm consequências legais e regulatórias.'),

    h5('O que a parceria SAP Anthropic significa para quem está adotando SAP BDC'),
    p(f'Para empresas implementando ou evoluindo seu ambiente SAP — especialmente as que já têm ou estão migrando para o {a("SAP Business Data Cloud", BDC_URL)} —, a parceria SAP Anthropic tem uma implicação direta.'),
    p(f'O Claude opera sobre o contexto fornecido pelo {a("SAP Business AI Platform", BLOG+"sap-business-ai-platform/")}. O componente que torna esse contexto específico para a empresa é o {a("SAP BDC", BDC_URL)}.'),
    p('Em termos diretos: o Claude é tão preciso quanto os dados que o alimentam. Um agente com acesso ao BDC bem estruturado raciocina dentro do contexto real da empresa. Um agente com dados fragmentados raciocina sobre suposições — e automatiza decisões baseadas nessas suposições.'),
    p(f'Para a Solveplan, parceira SAP Gold especializada em implementação de {a("SAP BDC", BDC_URL)} e {a("SAP Datasphere", DS_URL)} na América Latina, a parceria SAP Anthropic reforça o que já orientava o trabalho com clientes: a fundação de dados não é infraestrutura — é o ativo que determina o que a IA consegue ou não consegue fazer dentro do seu negócio.'),

    h5('A qualidade da SAP Anthropic na prática depende dos seus dados'),
    p('A parceria SAP Anthropic coloca o Claude no centro da camada de raciocínio do seu ERP. O que determina a qualidade desse raciocínio — e a confiabilidade das decisões que ele vai tomar nos seus processos — é a qualidade dos dados que você fornece a ele.'),
    p('Fale com a Solveplan para entender se o seu ambiente de dados está pronto para suportar agentes SAP com o nível de precisão que processos críticos exigem.'),

    CTA,

    h5('FAQ — SAP Anthropic'),

    faq('O que é a parceria SAP Anthropic?',
        'A parceria SAP Anthropic integra o Claude, da Anthropic, como modelo de raciocínio primário dos agentes Joule no SAP Business AI Platform. Claude coordena fluxos de trabalho em finanças, RH e compras dentro do contexto fornecido pelo ecossistema SAP — com governança centralizada e acesso ao SAP Knowledge Graph.'),

    faq('Por que a SAP escolheu o Claude na parceria SAP Anthropic?',
        'Pela capacidade de raciocínio em múltiplos passos — necessária para coordenar fluxos empresariais não lineares com precisão. Claude mantém contexto ao longo de cadeias de decisão longas e distingue quando executar de quando escalar para aprovação humana.'),

    faq('O SAP usa apenas o Claude ou outros modelos também?',
        'O SAP Business AI Platform é multi-LLM: além do Claude, suporta modelos da OpenAI, Google e NVIDIA. Na parceria SAP Anthropic, o Claude atua como modelo de raciocínio primário nos agentes Joule para finanças, RH e compras, mas a arquitetura permite que cada empresa configure o modelo preferido por caso de uso.'),

    faq('Como a governança funciona com IA agêntica no SAP?',
        'Claude opera dentro dos controles já configurados no ambiente SAP — aprovações, limites de alçada, restrições de acesso por papel. O SAP Knowledge Graph é o que torna esse controle possível: os agentes conhecem as regras de processo porque elas estão mapeadas no contexto, não apenas documentadas em texto.'),

    faq('A parceria SAP Anthropic cobre setores específicos?',
        'A parceria cobre finanças (S/4HANA), RH (SuccessFactors) e compras (Ariba) como domínios primários. SAP e Anthropic anunciaram desenvolvimento conjunto de guardrails específicos para processos financeiros e de RH — onde decisões de agente têm consequências regulatórias.'),

    faq('O que a parceria SAP Anthropic significa para quem está implementando SAP BDC?',
        'O Claude opera sobre o contexto fornecido pelo SAP BDC. Quanto melhor estruturado o BDC — dados mestre unificados, hierarquias corretas, políticas mapeadas —, mais preciso é o raciocínio do Claude dentro dos processos da empresa. A qualidade do BDC determina diretamente a qualidade das decisões dos agentes.'),

    h5('Fontes'),
    ul([
        'SAP News Center — SAP and Anthropic Partner to Bring Claude AI Models to SAP Business AI Platform',
        'SAP — SAP Business AI Platform',
        'Anthropic — Anthropic and SAP Partnership Announcement',
        'SAP Sapphire 2026 — Autonomous Enterprise Vision',
        'SAPinsider — Claude as the Reasoning Engine for SAP Agents',
    ]),
]

content = '\n\n'.join(parts)

r = requests.post(f"{WP}/posts/{POST_ID}", auth=AUTH, json={"content": content})
print("Update:", r.status_code)

v = requests.get(f"{WP}/posts/{POST_ID}?context=edit", auth=AUTH).json()["content"]["raw"]
print(f"Chars:           {len(v)}")
print(f"H5 (com classe): {v.count('wp-block-heading')}")
print(f"wp:list:         {v.count('wp:list')}")
print(f"wp:details:      {v.count('wp:details')}")
print(f"SAP Anthropic:   {v.count('SAP Anthropic')}")
print(f"Links BDC:       {v.count('sap-business-data-cloud')}")
print(f"CTA:             {'OK' if 'bdcstrategy' in v else 'AUSENTE'}")
print(f"Corrompido:      {'SIM' if '<p>\\n<!-- wp:' in v else 'NAO'}")

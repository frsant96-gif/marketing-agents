"""Cria o case Oji Papéis como RASCUNHO no WordPress, no mesmo modelo de blocos dos cases Lins e Aço Cearense.

Uso: WP_APP_PASSWORD="xxxx xxxx ..." python criar_rascunho.py <url-do-video-youtube>
A senha não fica gravada neste arquivo.
"""
import os, sys, pathlib, requests

sys.stdout.reconfigure(encoding="utf-8")

WP = "https://solveplan.com/wp-json"
AUTH = ("administrador", os.environ["WP_APP_PASSWORD"])
ICON_DIR = pathlib.Path(__file__).parent

SAC_URL = "https://solveplan.com/sap-analytics-cloud/"
SERVICOS_URL = "https://solveplan.com/servicos/"
VIDEO = sys.argv[1]

SLUG = "oji-papeis-sap-analytics-cloud"
TITLE = "Oji Papéis: SAP Analytics Cloud reduz ciclo orçamentário de 15 para 2 dias"
EXCERPT = ("A Oji Papéis implementou SAP Analytics Cloud em seis meses e reduziu o tempo de resposta do processo "
           "orçamentário de até 15 dias para aproximadamente 2 dias, centralizando informações e reduzindo a "
           "dependência de planilhas.")
SEO = {
    "rank_math_title": "Oji Papéis + SAP Analytics Cloud | Case Solveplan",
    "rank_math_description": ("Veja como a Oji Papéis implementou SAP Analytics Cloud em seis meses e reduziu o ciclo de "
                              "resposta orçamentária de 15 para 2 dias, centralizando dados e planejamento."),
    "rank_math_focus_keyword": ("SAP Analytics Cloud,case SAP Analytics Cloud,SAC Planning,planejamento orçamentário SAP,"
                                "Oji Papéis SAP"),
}

ICONS = [
    ("oji-icone-agilidade.png", "Ícone de relógio"),
    ("oji-icone-projeto.png", "Ícone de calendário"),
    ("oji-icone-centralizacao.png", "Ícone de banco de dados"),
]
CARDS = [
    "De 15 para 2 dias — tempo de resposta do processo orçamentário, redução superior a 80%",
    "6 meses de projeto — processos financeiros revisados, dados padronizados, dashboards e capacitação",
    "Um único ambiente — informações centralizadas e menos dependência de planilhas e controles paralelos",
]
BEFORE_LABEL = "Antes do projeto"


# ── blocos Gutenberg (mesma marcação do case da Lins) ─────────────────────────
def a(text, url):
    return f'<a href="{url}">{text}</a>'

def spacer(h=33):
    return f'<!-- wp:spacer {{"height":"{h}px"}} -->\n<div style="height:{h}px" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->'

def p(html):
    return f'<!-- wp:paragraph -->\n<p>{html}</p>\n<!-- /wp:paragraph -->'

def h2(text):
    return ('<!-- wp:heading {"style":{"elements":{"link":{"color":{"text":"#006cff"}}},"color":{"text":"#006cff"}}} -->\n'
            f'<h2 class="wp-block-heading has-text-color has-link-color" style="color:#006cff">{text}</h2>\n<!-- /wp:heading -->')

def ul(items):
    lis = "\n\n".join(f"<!-- wp:list-item -->\n<li>{i}</li>\n<!-- /wp:list-item -->" for i in items)
    return f'<!-- wp:list -->\n<ul class="wp-block-list">{lis}</ul>\n<!-- /wp:list -->'

def card(media_id, url, text):
    return ('<!-- wp:column -->\n<div class="wp-block-column">'
            f'<!-- wp:image {{"id":{media_id},"width":"100px","height":"auto","sizeSlug":"full","linkDestination":"none","align":"center"}} -->\n'
            f'<figure class="wp-block-image aligncenter size-full is-resized"><img src="{url}" alt="" class="wp-image-{media_id}" style="width:100px;height:auto"/></figure>\n'
            '<!-- /wp:image -->\n\n'
            f'<!-- wp:paragraph {{"align":"center"}} -->\n<p class="has-text-align-center">{text}</p>\n<!-- /wp:paragraph --></div>\n<!-- /wp:column -->')

def cards(media):
    cols = "\n\n".join(card(mid, url, txt) for (mid, url), txt in zip(media, CARDS))
    return ('<!-- wp:group {"layout":{"type":"constrained"}} -->\n<div class="wp-block-group"><!-- wp:group {"layout":{"type":"constrained"}} -->\n'
            f'<div class="wp-block-group"><!-- wp:columns -->\n<div class="wp-block-columns">{cols}</div>\n<!-- /wp:columns --></div>\n'
            '<!-- /wp:group --></div>\n<!-- /wp:group -->')

def before_after(before, after):
    def col(label, items):
        return (f'<!-- wp:column -->\n<div class="wp-block-column"><!-- wp:paragraph -->\n<p><em>{label}</em></p>\n<!-- /wp:paragraph -->\n\n'
                f'{ul(items)}</div>\n<!-- /wp:column -->')
    return f'<!-- wp:columns -->\n<div class="wp-block-columns">{col(BEFORE_LABEL, before)}\n\n{col("Depois da implementação", after)}</div>\n<!-- /wp:columns -->'

def embed(url):
    return ('<!-- wp:embed {"url":"' + url + '","type":"video","providerNameSlug":"youtube","responsive":true,"className":"wp-embed-aspect-16-9 wp-has-aspect-ratio"} -->\n'
            '<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">\n'
            f'{url}\n</div></figure>\n<!-- /wp:embed -->')

def button(text, url, primary=False):
    if primary:
        return ('<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n<div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"primary","textColor":"white","style":{"border":{"radius":"4px"}}} -->\n'
                f'<div class="wp-block-button"><a class="wp-block-button__link has-white-color has-primary-background-color has-text-color has-background wp-element-button" href="{url}" target="_blank" rel="noopener">{text}</a></div>\n'
                '<!-- /wp:button --></div>\n<!-- /wp:buttons -->')
    return ('<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n<div class="wp-block-buttons"><!-- wp:button {"style":{"color":{"background":"#006cff"}}} -->\n'
            f'<div class="wp-block-button"><a class="wp-block-button__link has-background wp-element-button" href="{url}" style="background-color:#006cff">{text}</a></div>\n'
            '<!-- /wp:button --></div>\n<!-- /wp:buttons -->')

def faq(q, ans):
    return (f'<!-- wp:details -->\n<details class="wp-block-details"><summary>{q}</summary><!-- wp:paragraph -->\n<p>{ans}</p>\n'
            '<!-- /wp:paragraph --></details>\n<!-- /wp:details -->')


def build(media):
    blocks = [
        spacer(),
        p("Em planejamento financeiro, esperar duas semanas por uma resposta pode significar tomar uma decisão com informações que já ficaram para trás."),
        p("Foi esse tipo de desafio que levou a Oji Papéis Especiais a transformar sua gestão orçamentária. Fundada em 2011, em Piracicaba (SP), a companhia faz parte do Grupo Oji Holdings Corporation, multinacional japonesa do setor de papel e celulose, e atua no Brasil com papéis térmicos e autocopiativos."),
        spacer(),
        cards(media),
        spacer(),
        p("Antes do projeto, o processo orçamentário convivia com planilhas, sistemas paralelos e informações descentralizadas. O acesso e a análise dos dados exigiam mais esforço, enquanto respostas relacionadas ao orçamento podiam levar até 15 dias."),
        p("A necessidade não era simplesmente substituir uma planilha por uma nova ferramenta. Era criar um processo de planejamento mais integrado, centralizado e capaz de acompanhar o ritmo das decisões do negócio."),
        spacer(),
        h2("Por que a Oji Papéis escolheu o SAP Analytics Cloud?"),
        p("A Oji já utilizava ERP SAP. A evolução para o SAP Analytics Cloud (SAC) permitiu ampliar o uso do ecossistema SAP para o planejamento, combinando dados, análises e processos orçamentários em uma experiência integrada."),
        p("O projeto foi conduzido em seis meses e envolveu revisão dos processos financeiros, mapeamento e padronização das informações, estruturação de dashboards e capacitação dos usuários."),
        p("A transformação também exigiu uma mudança de cultura. A familiaridade com as soluções SAP tornou a escolha do SAC natural, enquanto a adoção de uma nova forma de trabalhar representou um dos principais desafios da jornada."),
        before_after(
            ["Planilhas e sistemas paralelos no processo orçamentário", "Informações descentralizadas",
             "Mais esforço para acessar e analisar os dados", "Respostas sobre o orçamento em até 15 dias",
             "Planejamento concentrado em poucos usuários"],
            ["SAP Analytics Cloud integrado ao ecossistema SAP", "Informações centralizadas em um único ambiente",
             "Menos dependência de planilhas e controles paralelos", "Respostas sobre o orçamento em aproximadamente 2 dias",
             "Mais visibilidade das informações para diferentes áreas"],
        ),
        spacer(),
        h2("De 15 para 2 dias: o impacto no ciclo orçamentário"),
        p("O resultado mais direto do projeto aparece no tempo de resposta do processo orçamentário."),
        p("Após a implementação do SAP Analytics Cloud, o ciclo que podia levar até 15 dias passou a ser concluído em aproximadamente 2 dias. A redução supera 80% e representa uma mudança relevante na velocidade com que a companhia consegue acessar informações e responder às necessidades de planejamento."),
        p("A Oji também passou a trabalhar com informações centralizadas em um único ambiente, reduzindo a dependência de planilhas e controles paralelos."),
        p("Além da velocidade, a nova estrutura ampliou a visibilidade das informações para diferentes áreas, contribuindo para que o planejamento deixasse de ficar concentrado apenas em poucos usuários e se tornasse mais conectado à operação."),
        spacer(),
        h2("Oji Papéis, SAP Analytics Cloud e Solveplan"),
        p("O case da Oji Papéis mostra como a modernização do planejamento financeiro pode gerar impacto mensurável quando tecnologia, processos e adoção caminham juntos."),
        p("Em seis meses de projeto, a companhia estruturou um novo ambiente de planejamento e reduziu de 15 para 2 dias o tempo de resposta orçamentária, ao mesmo tempo em que avançou na centralização e no acesso às informações."),
        p("<strong>Assista ao vídeo do case</strong>"),
        embed(VIDEO),
        spacer(),
        h2("O que mudou no planejamento da Oji Papéis?"),
        p("A transformação pode ser observada em quatro frentes principais: centralização, agilidade, acesso e confiabilidade."),
        p("Com os dados organizados no SAP Analytics Cloud, o processo passou a oferecer uma visão mais clara do orçamento e a reduzir etapas que antes dependiam de controles paralelos."),
        p("Isso cria uma diferença importante na rotina financeira: menos tempo dedicado a localizar, consolidar e validar informações e mais condições para analisar cenários e apoiar decisões."),
        p("O ganho, portanto, não está apenas na redução do ciclo de 15 para 2 dias, mas também na mudança da forma como a informação orçamentária circula e é utilizada dentro da organização."),
        spacer(),
        h2("A atuação da Solveplan na implementação"),
        p("A Solveplan acompanhou a Oji durante a implementação do SAP Analytics Cloud, apoiando a revisão dos processos, a organização das informações e a adoção da nova solução."),
        p("Segundo a Oji, a Solveplan apoiou as diferentes etapas do projeto e contribuiu também com insights e conhecimentos relacionados ao portfólio SAP."),
        p("Essa atuação consultiva foi especialmente relevante porque o projeto não envolvia apenas tecnologia: havia também o desafio de transformar uma cultura de planejamento já estabelecida e apoiar os usuários na transição para um processo mais centralizado."),
        spacer(),
        h2("Do planejamento à evolução da estratégia de dados"),
        p("O SAP Analytics Cloud resolveu uma etapa importante da jornada: tornar o planejamento orçamentário mais rápido, centralizado e acessível."),
        p("A versão anterior deste case já apontava a intenção da Oji de ampliar essa evolução com SAP Business Data Cloud, conectando uma estratégia de dados mais abrangente às informações utilizadas no planejamento."),
        p("Essa direção reforça uma mudança que vem ocorrendo no ecossistema SAP: planejamento e analytics passam a fazer parte de uma arquitetura de dados mais integrada, na qual governança e contexto são fundamentais para ampliar o uso das informações no negócio."),
        p("Para a Oji, o projeto com SAC criou uma base importante para essa evolução."),
        spacer(),
        p("<strong>Quer evoluir o planejamento e a gestão de dados da sua empresa?</strong>"),
        button("Conheça as soluções e serviços da Solveplan", SERVICOS_URL),
        spacer(),
        '<!-- wp:heading {"level":5} -->\n<h5 class="wp-block-heading"><strong>FAQ — Oji Papéis e SAP Analytics Cloud</strong></h5>\n<!-- /wp:heading -->',
        faq("Qual solução SAP foi implementada na Oji Papéis?",
            f'A Oji Papéis implementou o {a("SAP Analytics Cloud", SAC_URL)} (SAC) para modernizar o planejamento orçamentário, centralizar informações e reduzir a dependência de planilhas e sistemas paralelos.'),
        faq("Quanto tempo durou a implementação do SAP Analytics Cloud na Oji?",
            "O projeto foi conduzido em seis meses e incluiu revisão dos processos financeiros, mapeamento e padronização de dados, dashboards e capacitação dos usuários."),
        faq("Qual foi a redução no tempo do processo orçamentário?",
            "Segundo a Oji, respostas orçamentárias que podiam levar até 15 dias passaram a ser obtidas em aproximadamente 2 dias, uma redução superior a 80%."),
        faq("Quais problemas existiam antes do SAP Analytics Cloud?",
            "O cenário anterior tinha dependência de planilhas e sistemas paralelos, informações descentralizadas e lentidão nas respostas relacionadas ao orçamento."),
        faq("Quais benefícios o SAP Analytics Cloud trouxe para a Oji Papéis?",
            "O projeto trouxe mais agilidade ao ciclo orçamentário, centralização das informações, redução de controles paralelos e maior acesso aos dados por diferentes áreas."),
        faq("Qual foi o papel da Solveplan no projeto?",
            "A Solveplan apoiou a implementação e a transformação dos processos de planejamento. A Oji destaca o apoio da consultoria ao longo das etapas e a contribuição com insights e soluções do ecossistema SAP."),
        faq("Qual é o próximo passo da estratégia de dados da Oji?",
            "A Oji registrou a intenção de evoluir sua estratégia de dados com SAP Business Data Cloud, ampliando a integração das informações para além do planejamento."),
        spacer(39),
        button("Avalie a maturidade dos seus dados com a Solveplan", "https://bdcstrategy.solveplan.ai/", primary=True),
    ]
    return "\n\n".join(blocks)


def upload_icon(fname, alt):
    existing = requests.get(f"{WP}/wp/v2/media", params={"search": fname.rsplit(".", 1)[0], "_fields": "id,source_url"}, auth=AUTH, timeout=30).json()
    if existing:
        return existing[0]["id"], existing[0]["source_url"]
    data = (ICON_DIR / fname).read_bytes()
    r = requests.post(f"{WP}/wp/v2/media", auth=AUTH, data=data, timeout=60,
                      headers={"Content-Disposition": f'attachment; filename="{fname}"', "Content-Type": "image/png"})
    r.raise_for_status()
    m = r.json()
    requests.post(f"{WP}/wp/v2/media/{m['id']}", auth=AUTH, json={"alt_text": alt}, timeout=30)
    return m["id"], m["source_url"]


if __name__ == "__main__":
    # Não duplica: se já existe um case com esse slug, para.
    found = requests.get(f"{WP}/wp/v2/case", params={"slug": SLUG, "status": "any", "_fields": "id,status"}, auth=AUTH, timeout=30).json()
    if found:
        sys.exit(f"Já existe case com slug {SLUG}: {found}")

    media = [upload_icon(f, alt) for f, alt in ICONS]
    print("Ícones:", media)

    r = requests.post(f"{WP}/wp/v2/case", auth=AUTH, timeout=60, json={
        "title": TITLE, "slug": SLUG, "status": "draft", "excerpt": EXCERPT, "content": build(media),
    })
    r.raise_for_status()
    post = r.json()
    pid = post["id"]
    print(f"Rascunho criado: ID {pid} · status {post['status']}")

    seo = requests.post(f"{WP}/rankmath/v1/updateMeta", auth=AUTH, timeout=30,
                        json={"objectType": "post", "objectID": pid, "meta": SEO})
    print("Rank Math:", seo.status_code, seo.text[:200])

    print(f"Editar: https://solveplan.com/wp-admin/post.php?post={pid}&action=edit")
    print(f"Prévia: https://solveplan.com/?post_type=case&p={pid}&preview=true")

"""Cria o case Grupo Aço Cearense como RASCUNHO no WordPress, no mesmo modelo de blocos do case da Lins (10585).

Uso: WP_APP_PASSWORD="xxxx xxxx ..." python criar_rascunho.py <pasta-dos-icones>
A senha não fica gravada neste arquivo.
"""
import os, sys, json, pathlib, requests

sys.stdout.reconfigure(encoding="utf-8")

WP = "https://solveplan.com/wp-json"
AUTH = ("administrador", os.environ["WP_APP_PASSWORD"])
ICON_DIR = pathlib.Path(sys.argv[1])

SAC_URL = "https://solveplan.com/sap-analytics-cloud/"
PLAN_URL = "https://solveplan.com/planejamento-e-simulacao/"
LINS_URL = "https://solveplan.com/case/lins-agroindustrial-sap-analytics-cloud/"
VIDEO = "https://youtu.be/wVj2x8VfYQs"

SLUG = "grupo-aco-cearense-sap-analytics-cloud"
TITLE = "Como o Grupo Aço Cearense integrou o planejamento com SAP Analytics Cloud"
EXCERPT = ("O Grupo Aço Cearense estruturou com a Solveplan um planejamento integrado com SAP Analytics Cloud Planning, "
           "conectado ao SAP IBP e ao SAP S/4HANA, reduzindo atividades manuais, ampliando a governança e integrando "
           "projeções operacionais e financeiras.")
SEO = {
    "rank_math_title": "Grupo Aço Cearense + SAP Analytics Cloud | Case Solveplan",
    "rank_math_description": ("Como o Grupo Aço Cearense conectou planejamento operacional e financeiro com SAP Analytics Cloud, "
                              "IBP e S/4HANA, menos trabalho manual e mais governança."),
    "rank_math_focus_keyword": "SAP Analytics Cloud,SAC Planning,planejamento integrado,planejamento orçamentário SAP,SAP IBP",
}

ICONS = [
    ("aco-icone-integracao.png", "Ícone de três pontos conectados"),
    ("aco-icone-escopo.png", "Ícone de camadas empilhadas"),
    ("aco-icone-areas.png", "Ícone de organograma"),
]
CARDS = [
    "SAC + IBP + S/4HANA — planejamento operacional e financeiro conectados em uma arquitetura única",
    "Da venda ao balanço — vendas, produção, custos, pessoas, investimentos, tributos, caixa e demonstrativos no mesmo modelo",
    "8 áreas com papéis definidos — Produção, Suprimentos, Vendas, RH, Logística, Fiscal, Finanças e Controladoria",
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

def ul(items, ordered=False):
    tag = "ol" if ordered else "ul"
    attrs = ' {"ordered":true}' if ordered else ""
    lis = "\n\n".join(f"<!-- wp:list-item -->\n<li>{i}</li>\n<!-- /wp:list-item -->" for i in items)
    return f'<!-- wp:list{attrs} -->\n<{tag} class="wp-block-list">{lis}</{tag}>\n<!-- /wp:list -->'

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
        p("Planejar uma operação industrial de grande porte exige conectar decisões comerciais, produtivas e financeiras que acontecem em ritmos diferentes. No Grupo Aço Cearense, essa complexidade envolvia vendas, suprimentos, pessoas, investimentos, custos, tributos, demonstrativos e diferentes etapas de consolidação."),
        p("Com 46 anos de atuação no mercado brasileiro do aço e presença no Ceará, Pará e Tocantins, o Grupo Aço Cearense reúne operações integradas de comercialização, metalurgia, siderurgia e logística."),
        spacer(),
        cards(media),
        spacer(),
        h2("O desafio"),
        p("Antes do projeto, determinadas etapas do planejamento e da consolidação dependiam de planilhas e de atividades manuais. Esse cenário ampliava o esforço operacional, dificultava a gestão integrada de versões e reduzia o tempo disponível para análises e simulações."),
        p("A resposta foi estruturar um modelo de planejamento integrado com SAP Analytics Cloud (SAC) Planning, conectado ao SAP IBP e ao SAP S/4HANA."),
        spacer(),
        h2("Por que o SAP Analytics Cloud foi escolhido?"),
        p("O objetivo do Grupo Aço Cearense era evoluir para um planejamento mais integrado, automatizado e governado, conectando projeções operacionais e financeiras em uma arquitetura única."),
        p("Com o SAP Analytics Cloud, cálculos antes realizados em planilhas puderam ser estruturados como regras de negócio no sistema, enquanto workflows de aprovação passaram a apoiar diferentes etapas do planejamento. A integração com SAP IBP e SAP S/4HANA também permitiu aproximar projeções operacionais, dados transacionais e planejamento financeiro."),
        p(f'A transformação, portanto, não se limitou à troca de ferramenta. O projeto reorganizou a forma como diferentes áreas participam do planejamento e como as informações percorrem o ciclo orçamentário. Conheça também a atuação da Solveplan em {a("Planejamento e Simulação", PLAN_URL)} com soluções SAP.'),
        before_after(
            ["Etapas do planejamento e da consolidação apoiadas em planilhas", "Atividades manuais em diferentes frentes",
             "Gestão de versões pouco integrada", "Informações intermediadas entre áreas em alguns processos",
             "Menos tempo para análises e simulações"],
            ["SAC Planning conectado ao SAP IBP e ao SAP S/4HANA", "Cálculos de planilha convertidos em regras de negócio",
             "Workflows de aprovação nas etapas do planejamento", "Extração automática de dados do SAP S/4HANA",
             "Responsabilidades definidas por área"],
        ),
        spacer(),
        p("<strong>Assista o case completo</strong>"),
        embed(VIDEO),
        p("No vídeo, o Grupo Aço Cearense apresenta a experiência da companhia com o planejamento integrado."),
        spacer(),
        h2("Um escopo que conecta diferentes dimensões do negócio"),
        p("O projeto contemplou diferentes dimensões do negócio, incluindo vendas, produção, custos, estoques, pessoas, despesas operacionais, investimentos, suprimentos, tributos, demonstrativos financeiros, fluxo de caixa, balanço patrimonial, operação florestal e simulações."),
        p("Essa amplitude é especialmente relevante porque o planejamento de uma companhia industrial não acontece de forma isolada. Uma projeção de vendas afeta produção e necessidade de matéria-prima; custos e investimentos influenciam caixa e resultado; movimentações de pessoas impactam despesas; e todas essas variáveis precisam convergir para demonstrativos e cenários consistentes."),
        p("Ao organizar essas frentes em uma arquitetura de planejamento comum, o Grupo Aço Cearense passou a trabalhar com regras, integrações e responsabilidades mais estruturadas."),
        spacer(),
        h2("SAP IBP, SAP S/4HANA e SAC Planning: como as informações se conectam"),
        p("Um dos pontos centrais do projeto foi a integração entre o planejamento operacional e o financeiro."),
        p("Na frente de Supply, por exemplo, as projeções de volume do SAP IBP passaram a se conectar às projeções financeiras no SAP Analytics Cloud. Em outras frentes, o SAC passou a receber dados automaticamente do SAP S/4HANA, reduzindo atividades de extração e preparação manual."),
        p("O projeto também substituiu cálculos em planilhas por regras de negócio, implantou workflows de aprovação e eliminou intermediações de dados entre áreas em determinados processos."),
        p("Na frente financeira, os dados planejados dos diferentes módulos passaram a ser integrados para apoiar consolidação, cálculo de tributos sobre o lucro e revisões periódicas do orçamento."),
        spacer(),
        h2("Quais benefícios o SAP Analytics Cloud trouxe para o Grupo Aço Cearense?"),
        p("Os benefícios aparecem em diferentes etapas do planejamento e variam conforme a frente de negócio."),
        p("Entre os principais ganhos estão a redução de atividades manuais, automação de extrações a partir do SAP S/4HANA, workflows de aprovação, maior governança, integração entre SAP IBP e SAC Planning e redução de ciclos de planejamento em áreas como Supply, Payroll, CAPEX e custos."),
        p("Na prática, o projeto reduziu a necessidade de replicar informações entre áreas e liberou mais tempo para análises. A governança também passou a definir responsabilidades para Produção, Suprimentos, Vendas, RH, Logística, Fiscal, Finanças e Controladoria."),
        p("Em resumo: menos trabalho manual, mais integração, processos mais governados e ciclos de planejamento mais ágeis."),
        spacer(),
        h2("Mais governança para um planejamento que atravessa toda a organização"),
        p("Em projetos de planejamento integrado, tecnologia e governança precisam avançar juntas. No Grupo Aço Cearense, esse aspecto ganhou importância porque diferentes áreas alimentam e consomem informações que impactam o orçamento e os demonstrativos."),
        p("Ao estruturar responsabilidades, regras de negócio e workflows, o projeto cria uma lógica mais clara para participação das áreas e reduz a dependência de controles paralelos."),
        p("Isso também favorece revisões periódicas e simulações de cenários, já que as informações passam a percorrer um processo mais conectado entre operação e finanças."),
        spacer(),
        h2("A atuação da Solveplan no projeto"),
        p("A Solveplan conduziu a transformação em conjunto com o Grupo Aço Cearense, estruturando as diferentes dimensões do planejamento em uma arquitetura integrada."),
        p("A construção por frentes permitiu respeitar particularidades de vendas, suprimentos, pessoas, investimentos, custos e finanças, ao mesmo tempo em que regras de negócio, integrações e governança eram organizadas para sustentar um processo mais conectado e escalável."),
        p("Para outras empresas, a recomendação do Grupo Aço Cearense é tratar uma iniciativa como essa como evolução de processo, e não apenas como troca de ferramenta: integrar áreas, definir responsabilidades, estruturar regras de negócio e reduzir atividades manuais são partes da mesma transformação."),
        p(f'Veja outro exemplo de transformação de planejamento com SAP Analytics Cloud no {a("case da Lins Agroindustrial", LINS_URL)}.'),
        spacer(),
        h2("Uma base mais preparada para ciclos de planejamento e revisão"),
        p("Com uma estrutura mais integrada, automatizada e governada, o Grupo Aço Cearense passa a ter uma base preparada para ciclos de planejamento e revisão mais ágeis, simulações de cenários e análises mais aprofundadas."),
        p("A evolução também cria condições para ampliar a integração entre planejamento operacional e financeiro e utilizar as informações de forma mais consistente na tomada de decisão."),
        p("O principal aprendizado do case está justamente nessa conexão: transformar o planejamento exige aproximar áreas, processos e dados para que a tecnologia consiga reduzir complexidade em vez de apenas digitalizá-la."),
        spacer(),
        p("<strong>Sua empresa também precisa conectar planejamento operacional e financeiro?</strong>"),
        button("Fale conosco", "https://solveplan.com/contato/"),
        spacer(),
        '<!-- wp:heading {"level":5} -->\n<h5 class="wp-block-heading"><strong>FAQ — SAP Analytics Cloud no Grupo Aço Cearense</strong></h5>\n<!-- /wp:heading -->',
        faq("Qual solução SAP foi implementada no Grupo Aço Cearense?",
            f'O {a("SAP Analytics Cloud", SAC_URL)} (SAC) Planning, integrado ao SAP IBP e ao SAP S/4HANA, para estruturar um planejamento mais integrado, automatizado e governado.'),
        faq("Qual era o principal desafio antes do projeto?",
            "Determinadas etapas do planejamento e da consolidação dependiam de planilhas e de atividades manuais. Isso ampliava o esforço operacional, dificultava a gestão integrada de versões e reduzia o tempo disponível para análises e simulações."),
        faq("Quais áreas fazem parte do escopo?",
            "Vendas, produção, custos, estoques, pessoas, despesas operacionais, investimentos, suprimentos, tributos, demonstrativos financeiros, fluxo de caixa, balanço patrimonial, operação florestal e simulações."),
        faq("Como SAP IBP e SAP Analytics Cloud se integram no projeto?",
            "Na frente de Supply, as projeções de volume do SAP IBP se conectam às projeções financeiras no SAP Analytics Cloud, aproximando o planejamento operacional do financeiro."),
        faq("Como o SAP S/4HANA participa da arquitetura?",
            "O SAP Analytics Cloud recebe dados automaticamente do SAP S/4HANA em diferentes frentes, o que reduz etapas manuais de extração e preparação e dá mais consistência ao planejamento."),
        faq("Quais benefícios o projeto trouxe?",
            "Redução de trabalho manual, workflows de aprovação, maior governança, integração entre áreas e sistemas, menos intermediação de dados e ciclos de planejamento mais ágeis em frentes como Supply, Payroll, CAPEX e custos."),
        faq("Qual foi o papel da Solveplan?",
            "A Solveplan conduziu o projeto com o Grupo Aço Cearense, organizando regras de negócio, integrações e governança em diferentes frentes para tornar o planejamento mais conectado e escalável."),
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

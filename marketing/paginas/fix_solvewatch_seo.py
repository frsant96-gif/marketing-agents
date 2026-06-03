import requests, json

WP_URL  = "https://solveplan.com"
WP_USER = "administrador"
WP_PASS = "vjpT R0lO 9c2G vh2w WAqA RPfU"
AUTH    = (WP_USER, WP_PASS)
PAGE_ID = 10736

RANK_MATH_TITLE = "Solve Watch | Monitoramento e Observabilidade para SAP Datasphere"
RANK_MATH_DESC  = (
    "Solve Watch é a plataforma de observabilidade para SAP Datasphere da Solveplan. "
    "Monitoramento 24/7, alertas proativos de falha, controle de Capacity Units e "
    "histórico de até 6 meses — em uma tela, sem configuração complexa."
)
IMAGE_ALT = "Dashboard do Solve Watch — observabilidade para SAP Datasphere"

# ── 1. Fetch current Elementor data ──────────────────────────────────────────
print("Buscando dados da página...")
r = requests.get(
    f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
    params={"context": "edit"},
    auth=AUTH,
)
r.raise_for_status()
page = r.json()
meta = page.get("meta", {})
el_data = json.loads(meta.get("_elementor_data", "[]"))

# ── 2. Traverse and modify Elementor nodes ────────────────────────────────────
changes = []

def patch_nodes(nodes):
    for node in nodes:
        nid      = node.get("id", "")
        wtype    = node.get("widgetType", "")
        settings = node.get("settings", {})

        # Fix H1: "Solve Watch" heading
        if wtype == "heading" and nid == "decd53e":
            if settings.get("header_size") != "h1":
                settings["header_size"] = "h1"
                changes.append(f"[OK] H1 corrigido: widget {nid} ('{settings.get('title')}')")

        # Fix alt text on hero image
        if wtype == "image" and nid == "053587e":
            img = settings.get("image", {})
            if not img.get("alt"):
                img["alt"] = IMAGE_ALT
                settings["image"] = img
                changes.append(f"[OK] Alt text adicionado: widget {nid}")

        for child in node.get("elements", []):
            patch_nodes([child])

patch_nodes(el_data)

if not changes:
    print("Nenhuma alteração necessária no Elementor.")
else:
    print(f"\nAlterações preparadas:")
    for c in changes:
        print(" ", c)

    # ── 3. Push Elementor data back ───────────────────────────────────────────
    print("\nSalvando no WordPress...")
    resp = requests.post(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
        auth=AUTH,
        json={"meta": {"_elementor_data": json.dumps(el_data)}},
    )
    resp.raise_for_status()
    print("[OK] Elementor data atualizado.")

# ── 4. Update RankMath via XML-RPC ────────────────────────────────────────────
print("\nAtualizando RankMath via XML-RPC...")
import xmlrpc.client

xmlrpc_url = f"{WP_URL}/xmlrpc.php"
client = xmlrpc.client.ServerProxy(xmlrpc_url)

try:
    result = client.wp.editPost(
        1,           # blog_id
        WP_USER,
        WP_PASS,
        PAGE_ID,
        {
            "custom_fields": [
                {"key": "rank_math_title",       "value": RANK_MATH_TITLE},
                {"key": "rank_math_description", "value": RANK_MATH_DESC},
                {"key": "rank_math_focus_keyword", "value": "monitoramento SAP Datasphere"},
            ]
        }
    )
    if result:
        print("[OK] RankMath title e description atualizados.")
    else:
        print("✗ XML-RPC retornou False — verifique as credenciais.")
except Exception as e:
    print(f"✗ Erro no XML-RPC: {e}")
    print("  → Atualize o title e description manualmente no RankMath dentro do Elementor.")

print("\nConcluído.")

import sys, json, requests
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "vjpT R0lO 9c2G vh2w WAqA RPfU")
POST_ID = 10484
MEDIA_ID = 11416
IMG_URL = "https://solveplan.com/wp-content/uploads/2026/07/sustentacao-analitica-sap-featured.png"
ALT = "sustentação analítica SAP"

resp = requests.get(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}?context=edit", auth=AUTH)
content = resp.json()["content"]["raw"]

image_block = (
    f'<!-- wp:image {{"id":{MEDIA_ID},"sizeSlug":"large","linkDestination":"none"}} -->\n'
    f'<figure class="wp-block-image size-large"><img src="{IMG_URL}" alt="{ALT}" class="wp-image-{MEDIA_ID}"/>'
    f'<figcaption class="wp-element-caption">Sustentação analítica SAP: única fonte da verdade, governança e qualidade, evolução de contexto.</figcaption></figure>\n'
    f'<!-- /wp:image -->\n\n'
)

marker = '<!-- wp:heading {"level":2} -->\n<h2 class="wp-block-heading">O que é sustentação analítica SAP?</h2>'
assert marker in content, "marker not found"
new_content = content.replace(marker, image_block + marker)

update = requests.post(
    f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}",
    auth=AUTH,
    json={"content": new_content}
)
print("Update content - Status:", update.status_code)

elementor_data = [{
    "id": "seo10484root",
    "elType": "container",
    "settings": {},
    "elements": [{
        "id": "seo10484widget",
        "elType": "widget",
        "settings": {"editor": new_content, "text_color": "#000000"},
        "elements": [],
        "widgetType": "text-editor"
    }],
    "isInner": False
}]
update2 = requests.post(
    f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}",
    auth=AUTH,
    json={"meta": {"_elementor_data": json.dumps(elementor_data, ensure_ascii=False)}}
)
print("Update elementor_data - Status:", update2.status_code)

verify = requests.get(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}?context=edit", auth=AUTH)
c = verify.json()["content"]["raw"]
print("Has wp:image block:", 'wp:image' in c)
print("Has img src:", IMG_URL in c)

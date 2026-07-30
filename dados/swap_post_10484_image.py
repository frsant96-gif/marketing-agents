import sys, json, requests, pathlib
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "vjpT R0lO 9c2G vh2w WAqA RPfU")
POST_ID = 10484
FOCUS_KEYWORD = "sustentação analítica SAP"
OLD_MEDIA_ID = 11416
OLD_IMG_URL = "https://solveplan.com/wp-content/uploads/2026/07/sustentacao-analitica-sap-featured.png"

img_path = pathlib.Path(__file__).parent.parent / "marketing" / "posts" / "sustentacao-analitica-pos-golive-erp" / "imagem" / "sustentacao-analitica-sap-featured-humanizada.png"

with open(img_path, "rb") as f:
    media_resp = requests.post(
        "https://solveplan.com/wp-json/wp/v2/media",
        auth=AUTH,
        headers={
            "Content-Disposition": 'attachment; filename="sustentacao-analitica-sap-featured-humanizada.png"',
            "Content-Type": "image/png",
        },
        data=f.read(),
    )
print("Upload - Status:", media_resp.status_code)
media_data = media_resp.json()
new_media_id = media_data.get("id")
print("Novo Media ID:", new_media_id)
if media_resp.status_code >= 400:
    print("Erro:", media_data)
    sys.exit(1)

requests.post(
    f"https://solveplan.com/wp-json/wp/v2/media/{new_media_id}",
    auth=AUTH,
    json={
        "alt_text": FOCUS_KEYWORD,
        "title": "Sustentação analítica SAP — profissional analisando dados após go-live de ERP",
        "caption": "Sustentação analítica SAP: acompanhamento contínuo do ERP após o go-live."
    }
)

new_img_url = media_data["source_url"]

# Set new featured image
requests.post(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}", auth=AUTH, json={"featured_media": new_media_id})

# Swap the in-body image block
resp = requests.get(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}?context=edit", auth=AUTH)
content = resp.json()["content"]["raw"]

old_block_start = content.find(f'<!-- wp:image {{"id":{OLD_MEDIA_ID}')
old_block_end = content.find('<!-- /wp:image -->') + len('<!-- /wp:image -->')
assert old_block_start != -1, "old image block not found"

new_block = (
    f'<!-- wp:image {{"id":{new_media_id},"sizeSlug":"large","linkDestination":"none"}} -->\n'
    f'<figure class="wp-block-image size-large"><img src="{new_img_url}" alt="{FOCUS_KEYWORD}" class="wp-image-{new_media_id}"/>'
    f'<figcaption class="wp-element-caption">Sustentação analítica SAP: acompanhamento contínuo do ERP após o go-live.</figcaption></figure>\n'
    f'<!-- /wp:image -->'
)

new_content = content[:old_block_start] + new_block + content[old_block_end:]

update = requests.post(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}", auth=AUTH, json={"content": new_content})
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
update2 = requests.post(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}", auth=AUTH, json={"meta": {"_elementor_data": json.dumps(elementor_data, ensure_ascii=False)}})
print("Update elementor_data - Status:", update2.status_code)

# Delete old media (the one with text) since it's no longer used
del_resp = requests.delete(f"https://solveplan.com/wp-json/wp/v2/media/{OLD_MEDIA_ID}?force=true", auth=AUTH)
print("Delete old media - Status:", del_resp.status_code)

verify = requests.get(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}?context=edit&_fields=featured_media,content", auth=AUTH)
vdata = verify.json()
print("Featured media:", vdata["featured_media"])
print("Contem nova imagem no corpo:", new_img_url in vdata["content"]["raw"])

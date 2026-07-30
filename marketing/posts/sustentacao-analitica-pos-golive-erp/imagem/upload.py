import sys, requests, pathlib
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "vjpT R0lO 9c2G vh2w WAqA RPfU")
POST_ID = 10484
FOCUS_KEYWORD = "sustentação analítica SAP"

img_path = pathlib.Path(__file__).parent / "sustentacao-analitica-sap-featured.png"

with open(img_path, "rb") as f:
    media_resp = requests.post(
        "https://solveplan.com/wp-json/wp/v2/media",
        auth=AUTH,
        headers={
            "Content-Disposition": 'attachment; filename="sustentacao-analitica-sap-featured.png"',
            "Content-Type": "image/png",
        },
        data=f.read(),
    )

print("Upload - Status:", media_resp.status_code)
media_data = media_resp.json()
media_id = media_data.get("id")
print("Media ID:", media_id)
if media_resp.status_code >= 400:
    print("Erro:", media_data.get("message"))
    sys.exit(1)

# Set alt text + title on the media item
update_resp = requests.post(
    f"https://solveplan.com/wp-json/wp/v2/media/{media_id}",
    auth=AUTH,
    json={
        "alt_text": FOCUS_KEYWORD,
        "title": "Sustentação analítica SAP — os 3 pilares pós go-live de ERP",
        "caption": "Sustentação analítica SAP: única fonte da verdade, governança e qualidade, evolução de contexto."
    }
)
print("Alt text update - Status:", update_resp.status_code)

# Set as featured image on the post
post_resp = requests.post(
    f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}",
    auth=AUTH,
    json={"featured_media": media_id}
)
print("Featured media set - Status:", post_resp.status_code)

verify = requests.get(f"https://solveplan.com/wp-json/wp/v2/posts/{POST_ID}?context=edit&_fields=featured_media", auth=AUTH)
print("Verificacao featured_media:", verify.json())

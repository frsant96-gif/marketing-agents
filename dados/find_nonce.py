import requests, sys, re, json
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')
AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")

r = requests.get("https://solveplan.com/wp-admin/post.php?post=10688&action=edit", auth=AUTH)
text = r.text

# Search for nonces
all_nonces = re.findall(r'"nonce"\s*:\s*"([a-zA-Z0-9_-]{6,20})"', text)
print("Nonces:", all_nonces[:10])

# Find rankMath object in the page
rm_idx = text.find("rankMath")
if rm_idx > 0:
    print("rankMath at:", rm_idx)
    print(text[rm_idx:rm_idx+600])
else:
    print("rankMath not found in page")

# Try the block editor URL (gutenberg)
r2 = requests.get("https://solveplan.com/wp-admin/site-editor.php", auth=AUTH)
print("\nSite editor status:", r2.status_code)

# Check for rest_nonce in any API call header
print("\nResponse headers:", dict(r.headers))

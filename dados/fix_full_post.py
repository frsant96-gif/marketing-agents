import sys, json, requests, re
from requests.auth import HTTPBasicAuth
sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth("administrador", "XR2W 5AJZ e70X IyuX v99m 8HmU")
POST_ID = 10653

# Check Rank Math updateMeta endpoint params
rm_info = requests.get("https://solveplan.com/wp-json/rankmath/v1/updateMeta", auth=AUTH)
print("updateMeta info:", rm_info.status_code, rm_info.text[:300])

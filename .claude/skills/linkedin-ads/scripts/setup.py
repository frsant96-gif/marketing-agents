"""Setup e autenticacao OAuth 2.0 para LinkedIn Ads."""

import sys
import os
import webbrowser
import urllib.parse
import http.server
import threading
import secrets
from pathlib import Path
from dotenv import load_dotenv, set_key
import requests

SKILL_DIR = Path(__file__).parent.parent
ENV_FILE = SKILL_DIR / ".env"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
SCOPES = "r_ads rw_ads r_ads_reporting"
REDIRECT_URI = "http://localhost:8765/callback"

load_dotenv(ENV_FILE)


def cmd_check():
    """Verifica dependencias e variaveis do .env."""
    print("=== Verificando dependencias ===")
    try:
        import requests
        print("[OK] requests")
    except ImportError:
        print("[FALTA] requests — rode: pip3 install requests python-dotenv")
        sys.exit(1)

    try:
        from dotenv import load_dotenv
        print("[OK] python-dotenv")
    except ImportError:
        print("[FALTA] python-dotenv — rode: pip3 install python-dotenv")
        sys.exit(1)

    print("\n=== Verificando .env ===")
    if not ENV_FILE.exists():
        print(f"[FALTA] {ENV_FILE} — criando template...")
        _create_env_template()
        print(f"[OK] Template criado em {ENV_FILE}")
        print("Preencha as variaveis e rode novamente.")
        sys.exit(0)

    required = ["LINKEDIN_CLIENT_ID", "LINKEDIN_CLIENT_SECRET"]
    ok = True
    for key in required:
        val = os.getenv(key, "")
        status = "[OK]" if val else "[FALTA]"
        print(f"{status} {key}")
        if not val:
            ok = False

    token = os.getenv("LINKEDIN_ACCESS_TOKEN", "")
    print(f"{'[OK]' if token else '[FALTA]'} LINKEDIN_ACCESS_TOKEN")

    if not ok:
        print("\nPreencha as variaveis faltando no .env e rode novamente.")
        sys.exit(1)
    print("\n[OK] Configuracao basica completa.")


def _create_env_template():
    template = """# LinkedIn Ads — Configuracao
# Os scripts leem este arquivo automaticamente.

# OBRIGATORIO: Credenciais do app LinkedIn (developers.linkedin.com)
LINKEDIN_CLIENT_ID=""
LINKEDIN_CLIENT_SECRET=""

# Gerado automaticamente pelo setup.py oauth
LINKEDIN_ACCESS_TOKEN=""
LINKEDIN_REFRESH_TOKEN=""
"""
    ENV_FILE.write_text(template)


def cmd_oauth():
    """Gera access token via OAuth 2.0 (abre browser)."""
    client_id = os.getenv("LINKEDIN_CLIENT_ID", "")
    client_secret = os.getenv("LINKEDIN_CLIENT_SECRET", "")
    if not client_id or not client_secret:
        print("[ERRO] LINKEDIN_CLIENT_ID e LINKEDIN_CLIENT_SECRET precisam estar no .env")
        sys.exit(1)

    state = secrets.token_urlsafe(16)
    auth_params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
        "state": state,
    }
    auth_link = f"{AUTH_URL}?{urllib.parse.urlencode(auth_params)}"

    code_holder = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            if "code" in params:
                code_holder["code"] = params["code"][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Autorizacao concluida! Pode fechar esta aba.")

        def log_message(self, *args):
            pass

    server = http.server.HTTPServer(("localhost", 8765), Handler)
    thread = threading.Thread(target=server.handle_request)
    thread.start()

    print(f"Abrindo browser para autorizacao...")
    webbrowser.open(auth_link)
    thread.join(timeout=120)

    if "code" not in code_holder:
        print("[ERRO] Timeout — nenhum codigo recebido.")
        sys.exit(1)

    resp = requests.post(TOKEN_URL, data={
        "grant_type": "authorization_code",
        "code": code_holder["code"],
        "redirect_uri": REDIRECT_URI,
        "client_id": client_id,
        "client_secret": client_secret,
    })
    if not resp.ok:
        print(f"[ERRO] {resp.status_code} — {resp.text}")
        sys.exit(1)

    data = resp.json()
    set_key(str(ENV_FILE), "LINKEDIN_ACCESS_TOKEN", data["access_token"])
    if "refresh_token" in data:
        set_key(str(ENV_FILE), "LINKEDIN_REFRESH_TOKEN", data["refresh_token"])

    print("[OK] Access token salvo no .env")
    print(f"     Expira em: {data.get('expires_in', '?')} segundos (~{data.get('expires_in', 0) // 86400} dias)")


def cmd_refresh():
    """Renova o access token usando o refresh token."""
    load_dotenv(ENV_FILE, override=True)
    client_id = os.getenv("LINKEDIN_CLIENT_ID", "")
    client_secret = os.getenv("LINKEDIN_CLIENT_SECRET", "")
    refresh_token = os.getenv("LINKEDIN_REFRESH_TOKEN", "")

    if not refresh_token:
        print("[ERRO] LINKEDIN_REFRESH_TOKEN nao encontrado. Rode setup.py oauth primeiro.")
        sys.exit(1)

    resp = requests.post(TOKEN_URL, data={
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
    })
    if not resp.ok:
        print(f"[ERRO] {resp.status_code} — {resp.text}")
        sys.exit(1)

    data = resp.json()
    set_key(str(ENV_FILE), "LINKEDIN_ACCESS_TOKEN", data["access_token"])
    print("[OK] Access token renovado e salvo no .env")


def cmd_test():
    """Testa conexao listando contas acessiveis."""
    sys.path.insert(0, str(SKILL_DIR / "scripts"))
    from lib import api_get, print_table
    load_dotenv(ENV_FILE, override=True)

    data = api_get("/adAccounts", {"q": "search"})
    accounts = data.get("elements", [])
    if not accounts:
        print("Nenhuma conta encontrada.")
        return

    rows = [{"ID": str(a["id"]).split(":")[-1], "Nome": a.get("name", ""), "Status": a.get("status", "")} for a in accounts]
    print(f"\n{len(rows)} conta(s) encontrada(s):\n")
    print_table(rows, ["ID", "Nome", "Status"])


COMMANDS = {"check": cmd_check, "oauth": cmd_oauth, "refresh": cmd_refresh, "test": cmd_test}

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd not in COMMANDS:
        print(f"Uso: setup.py [{'|'.join(COMMANDS)}]")
        sys.exit(1)
    COMMANDS[cmd]()

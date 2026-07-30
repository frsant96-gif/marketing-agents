#!/usr/bin/env python3
"""
Search Console Ratos - Biblioteca compartilhada
Auth (googleapiclient), .env loader, output helpers, error handling
Suporta Service Account e OAuth2 (compartilhado com ga4-ratos/google-ads-ratos)
"""

import json
import os
import sys
import time

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------

def ensure_sdk():
    """Verifica se o google-api-python-client esta instalado."""
    try:
        import googleapiclient.discovery  # noqa: F401
        return True
    except ImportError:
        print("ERRO: SDK 'google-api-python-client' nao instalado.", file=sys.stderr)
        print("  Instale com: pip3 install google-api-python-client google-auth", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# .env loader (sem depender de python-dotenv)
# ---------------------------------------------------------------------------

_ENV_SEARCH_PATHS = [
    os.path.expanduser("~/.claude/skills/search-console-ratos/.env"),
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env"),
]

# Fallback: buscar credenciais OAuth de skills irmas
_SHARED_ENV_PATHS = [
    os.path.expanduser("~/.claude/skills/ga4-ratos/.env"),
    os.path.expanduser("~/.claude/skills/google-ads-ratos/.env"),
]


def _load_env_file():
    """Carrega variaveis de um .env sem precisar de source no zshrc."""
    for env_path in _ENV_SEARCH_PATHS:
        if os.path.isfile(env_path):
            _parse_env(env_path)
            return env_path
    return None


def _load_shared_env():
    """Tenta carregar credenciais OAuth de ga4-ratos/google-ads-ratos como fallback."""
    for env_path in _SHARED_ENV_PATHS:
        if os.path.isfile(env_path):
            _parse_env(env_path)
            return env_path
    return None


def _parse_env(env_path):
    """Faz parse de um arquivo .env e seta env vars."""
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[7:]
            if "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and value and not os.environ.get(key):
                os.environ[key] = value


def mask_token(token):
    """Mascara token pra nao vazar em logs/output. Mostra so os 6 primeiros chars."""
    if not token or len(token) < 10:
        return "***"
    return f"{token[:6]}...{token[-4:]}"


# ---------------------------------------------------------------------------
# Auth & SDK init
# ---------------------------------------------------------------------------

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SCOPES_READWRITE = ["https://www.googleapis.com/auth/webmasters"]

_webmasters_client = None
_searchconsole_client = None


def _build_credentials(readwrite=False):
    """Constroi credenciais a partir do .env, na seguinte ordem:
    1. Service Account (GSC_CREDENTIALS_PATH)
    2. OAuth2 proprio (GSC_CLIENT_ID, GSC_CLIENT_SECRET, GSC_REFRESH_TOKEN)
    3. OAuth2 compartilhado (GA4/Google Ads ratos)
    4. Application Default Credentials
    """
    scopes = SCOPES_READWRITE if readwrite else SCOPES
    env_file = _load_env_file()

    # --- Modo 1: Service Account ---
    creds_path = os.environ.get("GSC_CREDENTIALS_PATH")
    if creds_path and os.path.isfile(creds_path):
        from google.oauth2 import service_account
        credentials = service_account.Credentials.from_service_account_file(
            creds_path, scopes=scopes,
        )
        print(f"Client inicializado via Service Account ({creds_path})", file=sys.stderr)
        return credentials

    # --- Modo 2: OAuth2 proprio ---
    client_id = os.environ.get("GSC_CLIENT_ID")
    client_secret = os.environ.get("GSC_CLIENT_SECRET")
    refresh_token = os.environ.get("GSC_REFRESH_TOKEN")

    if client_id and client_secret and refresh_token:
        credentials = _build_oauth_credentials(client_id, client_secret, refresh_token, scopes)
        source = env_file or "env vars (GSC)"
        print(f"Client inicializado via OAuth2 GSC ({source})", file=sys.stderr)
        return credentials

    # --- Modo 3: OAuth2 compartilhado (ga4-ratos / google-ads-ratos) ---
    shared_env = _load_shared_env()
    for prefix in ("GA4", "GOOGLE_ADS"):
        cid = os.environ.get(f"{prefix}_CLIENT_ID")
        csecret = os.environ.get(f"{prefix}_CLIENT_SECRET")
        rtoken = os.environ.get(f"{prefix}_REFRESH_TOKEN")
        if cid and csecret and rtoken:
            credentials = _build_oauth_credentials(cid, csecret, rtoken, scopes)
            print(f"Client inicializado via OAuth2 compartilhado {prefix} ({shared_env})", file=sys.stderr)
            return credentials

    # --- Modo 4: Application Default Credentials ---
    try:
        import google.auth
        credentials, _ = google.auth.default(scopes=scopes)
        print("Client inicializado via Application Default Credentials", file=sys.stderr)
        return credentials
    except Exception:
        pass

    print("ERRO: Credenciais do Search Console nao encontradas.", file=sys.stderr)
    print("  Opcao 1 (Service Account): Defina GSC_CREDENTIALS_PATH no .env", file=sys.stderr)
    print("  Opcao 2 (OAuth2): Defina GSC_CLIENT_ID, GSC_CLIENT_SECRET, GSC_REFRESH_TOKEN", file=sys.stderr)
    print("  Opcao 3 (Compartilhado): Configure ga4-ratos ou google-ads-ratos e as credenciais serao reusadas", file=sys.stderr)
    print("", file=sys.stderr)
    print("  Crie o arquivo ~/.claude/skills/search-console-ratos/.env", file=sys.stderr)
    print("  Ou rode: /search-console-ratos setup", file=sys.stderr)
    sys.exit(1)


def _build_oauth_credentials(client_id, client_secret, refresh_token, scopes):
    """Constroi Credentials a partir de um refresh_token.

    NAO passamos 'scopes' aqui: o google-auth inclui o parametro 'scope' no
    request de refresh quando as credenciais tem scopes definidos, e o Google
    rejeita com 'invalid_scope' se o valor nao bater EXATAMENTE com o que foi
    concedido na autorizacao original. Omitindo, o refresh usa os escopos ja
    concedidos ao token, sem risco de mismatch.
    """
    from google.oauth2.credentials import Credentials
    return Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
    )


def init_webmasters_client(readwrite=False):
    """Inicializa o client da API 'webmasters' v3 (searchanalytics, sites, sitemaps)."""
    global _webmasters_client
    if _webmasters_client is not None:
        return _webmasters_client

    ensure_sdk()
    from googleapiclient.discovery import build

    credentials = _build_credentials(readwrite=readwrite)
    _webmasters_client = build("webmasters", "v3", credentials=credentials, cache_discovery=False)
    return _webmasters_client


def init_searchconsole_client():
    """Inicializa o client da API 'searchconsole' v1 (URL Inspection)."""
    global _searchconsole_client
    if _searchconsole_client is not None:
        return _searchconsole_client

    ensure_sdk()
    from googleapiclient.discovery import build

    credentials = _build_credentials(readwrite=False)
    _searchconsole_client = build("searchconsole", "v1", credentials=credentials, cache_discovery=False)
    return _searchconsole_client


def get_default_site_url():
    """Retorna a site_url padrao da env var GSC_SITE_URL."""
    _load_env_file()
    site_url = os.environ.get("GSC_SITE_URL")
    if not site_url:
        print("ERRO: Nenhum site informado.", file=sys.stderr)
        print("  Use --site https://exemplo.com/ ou defina GSC_SITE_URL.", file=sys.stderr)
        sys.exit(1)
    return site_url


def resolve_site_url(args_site=None):
    """Resolve site URL: argumento CLI > env var."""
    if args_site:
        return args_site
    return get_default_site_url()


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def print_json(obj):
    """Serializa e printa qualquer objeto para stdout.

    Escreve bytes UTF-8 direto no stdout.buffer: no console do Windows,
    print() normal decodifica pela codepage ativa (cp1252/cp850) e corrompe
    acentos mesmo com ensure_ascii=False.
    """
    text = json.dumps(obj, indent=2, ensure_ascii=False, default=str)
    try:
        sys.stdout.buffer.write((text + "\n").encode("utf-8"))
        sys.stdout.buffer.flush()
    except AttributeError:
        print(text)


def print_error(msg):
    """Printa erro formatado para stderr."""
    print(f"ERRO: {msg}", file=sys.stderr)


def format_search_analytics_response(response):
    """Converte resposta de searchanalytics.query em lista de dicts legivel."""
    rows_out = []
    for row in response.get("rows", []):
        r = {}
        keys = row.get("keys", [])
        for i, key in enumerate(keys):
            r[f"dim_{i}"] = key
        r["clicks"] = row.get("clicks", 0)
        r["impressions"] = row.get("impressions", 0)
        r["ctr"] = row.get("ctr", 0)
        r["position"] = row.get("position", 0)
        rows_out.append(r)

    return {
        "row_count": len(rows_out),
        "rows": rows_out,
    }


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------

def handle_gsc_error(func):
    """Decorator que trata erros da Search Console API."""
    def wrapper(*args, **kwargs):
        ensure_sdk()
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_str = str(e)
            error_data = {
                "error": True,
                "message": error_str,
            }

            if "403" in error_str or "PERMISSION_DENIED" in error_str or "Forbidden" in error_str:
                error_data["hint"] = (
                    "Sem permissao. Verifique se a service account ou usuario OAuth "
                    "foi adicionado como usuario (proprietario ou completo) na propriedade "
                    "dentro do Google Search Console."
                )

            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str or "quota" in error_str.lower():
                error_data["hint"] = "Rate limit atingido. Aguarde alguns minutos antes de tentar novamente."

            if "401" in error_str or "UNAUTHENTICATED" in error_str or "invalid_grant" in error_str:
                error_data["hint"] = (
                    "Credenciais expiradas ou invalidas. "
                    "Verifique o refresh_token ou service account."
                )

            if "404" in error_str or "NOT_FOUND" in error_str:
                error_data["hint"] = (
                    "Site nao encontrado. Verifique a site_url (deve ser exatamente igual "
                    "a como esta cadastrada no Search Console, ex: 'https://solveplan.com/' "
                    "ou 'sc-domain:solveplan.com')."
                )

            print(json.dumps(error_data, indent=2, ensure_ascii=False, default=str))
            sys.exit(1)
    return wrapper


# ---------------------------------------------------------------------------
# Rate limiting helpers
# ---------------------------------------------------------------------------

def safe_delay(seconds=0.5):
    """Delay entre requests para evitar rate limiting."""
    time.sleep(seconds)


# ---------------------------------------------------------------------------
# Common argparse helpers
# ---------------------------------------------------------------------------

def add_site_arg(parser):
    """Adiciona argumento --site ao parser."""
    parser.add_argument(
        "--site",
        help="Site URL cadastrada no GSC (ex: https://solveplan.com/ ou sc-domain:solveplan.com). Padrao: GSC_SITE_URL"
    )


def add_date_args(parser, default_days=28):
    """Adiciona argumentos de data ao parser."""
    parser.add_argument(
        "--days",
        type=int,
        default=default_days,
        help=f"Quantidade de dias pra tras a partir de hoje (default: {default_days}). "
             "O GSC tem delay de ~2-3 dias nos dados mais recentes."
    )
    parser.add_argument("--start-date", help="Data inicio (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="Data fim (YYYY-MM-DD)")


def add_limit_arg(parser, default=25):
    """Adiciona argumento --limit ao parser."""
    parser.add_argument("--limit", type=int, default=default, help=f"Limite de resultados (default: {default})")


def build_date_range(args):
    """Constroi start_date/end_date a partir dos argumentos.
    Sem depender de datetime 'hoje' explicito no request (a API aceita 'today'-relativo
    via calculo local), calculamos com base na data atual do sistema.
    """
    from datetime import date, timedelta

    if args.start_date:
        end_date = args.end_date or date.today().isoformat()
        return args.start_date, end_date

    end_date = date.today() - timedelta(days=2)  # GSC tem delay nos ultimos ~2 dias
    start_date = end_date - timedelta(days=args.days)
    return start_date.isoformat(), end_date.isoformat()


def build_dimension_filter_groups(filters):
    """Constroi dimensionFilterGroups a partir de uma lista de tuplas (dimension, operator, expression)."""
    if not filters:
        return None
    return [{
        "filters": [
            {"dimension": dim, "operator": op, "expression": expr}
            for dim, op, expr in filters
        ]
    }]

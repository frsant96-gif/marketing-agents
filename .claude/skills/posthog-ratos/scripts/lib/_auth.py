"""Auth e config compartilhada para os scripts do posthog-ratos."""
import os
import sys
from pathlib import Path

import requests
import yaml

SKILL_DIR = Path(__file__).resolve().parent.parent.parent
HOME_SKILL_DIR = Path.home() / ".claude" / "skills" / "posthog-ratos"


def _load_env_file(path: Path):
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def load_config():
    _load_env_file(HOME_SKILL_DIR / ".env")
    _load_env_file(SKILL_DIR / ".env")

    api_key = os.environ.get("POSTHOG_API_KEY", "").strip()
    host = os.environ.get("POSTHOG_HOST", "https://eu.posthog.com").strip().rstrip("/")
    project_id = os.environ.get("POSTHOG_PROJECT_ID", "").strip()

    if not api_key:
        sys.exit(
            "Erro: POSTHOG_API_KEY nao configurada. Rode o setup do posthog-ratos "
            f"e preencha {HOME_SKILL_DIR / '.env'}"
        )

    return {"api_key": api_key, "host": host, "project_id": project_id}


def resolve_project(nome_ou_id: str):
    """Resolve um nome de cliente cadastrado em contas.yaml para o project_id do PostHog."""
    contas_path = SKILL_DIR / "contas.yaml"
    if not contas_path.exists():
        return nome_ou_id

    data = yaml.safe_load(contas_path.read_text(encoding="utf-8")) or {}
    for cliente in data.get("clientes", []) or []:
        if str(cliente.get("nome", "")).strip().lower() == nome_ou_id.strip().lower():
            return str(cliente.get("project_id"))
    return nome_ou_id


def _headers(config):
    return {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json",
    }


def api_get(config, path, params=None):
    url = f"{config['host']}{path}"
    resp = requests.get(url, headers=_headers(config), params=params or {}, timeout=30)
    _raise_for_status(resp)
    return resp.json()


def api_post(config, path, json_body=None):
    url = f"{config['host']}{path}"
    resp = requests.post(url, headers=_headers(config), json=json_body or {}, timeout=60)
    _raise_for_status(resp)
    return resp.json()


def _raise_for_status(resp):
    if resp.status_code == 429:
        sys.exit("Erro: rate limit do PostHog (429). Aguarde 60s e tente novamente.")
    if resp.status_code == 401:
        sys.exit("Erro: API key invalida ou sem permissao (401). Verifique o .env.")
    if resp.status_code == 404:
        sys.exit(f"Erro: recurso nao encontrado (404) em {resp.url}")
    if not resp.ok:
        sys.exit(f"Erro HTTP {resp.status_code} em {resp.url}: {resp.text[:500]}")

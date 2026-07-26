"""Shared utilities for LinkedIn Ads scripts."""

import os
import sys
import json
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

SKILL_DIR = Path(__file__).parent.parent.parent
ENV_FILE = SKILL_DIR / ".env"
API_BASE_V2 = "https://api.linkedin.com/v2"
API_BASE_REST = "https://api.linkedin.com/rest"

load_dotenv(ENV_FILE)


def get_env(key: str) -> str:
    val = os.getenv(key, "")
    if not val:
        print(f"[ERRO] Variavel '{key}' nao encontrada no .env ({ENV_FILE})")
        sys.exit(1)
    return val


def get_headers(versioned: bool = False) -> dict:
    token = get_env("LINKEDIN_ACCESS_TOKEN")
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }
    if versioned:
        headers["LinkedIn-Version"] = "202503"
    return headers


def api_get(path: str, params: dict = None, versioned: bool = False) -> dict:
    base = API_BASE_REST if versioned else API_BASE_V2
    url = f"{base}{path}"
    resp = requests.get(url, headers=get_headers(versioned), params=params)
    if resp.status_code == 401:
        print("[ERRO] Token expirado ou invalido. Rode setup.py refresh para renovar.")
        sys.exit(1)
    if not resp.ok:
        print(f"[ERRO] {resp.status_code} — {resp.text}")
        sys.exit(1)
    return resp.json()


def api_get_raw_qs(path: str, query_string: str, versioned: bool = False) -> dict:
    """GET com querystring pre-formatada (Rest.li 2.0: List(...) e (key:value) nao podem
    passar pelo encoder padrao do requests, que percent-encoda virgulas/parenteses e quebra
    a sintaxe exigida pelo /adAnalytics versionado)."""
    base = API_BASE_REST if versioned else API_BASE_V2
    url = f"{base}{path}?{query_string}"
    resp = requests.get(url, headers=get_headers(versioned))
    if resp.status_code == 401:
        print("[ERRO] Token expirado ou invalido. Rode setup.py refresh para renovar.")
        sys.exit(1)
    if not resp.ok:
        print(f"[ERRO] {resp.status_code} — {resp.text}")
        sys.exit(1)
    return resp.json()


def restli_date(prefix: str, date_str: str) -> str:
    d = date_str.split("-")
    year, month, day = d[0], str(int(d[1])), str(int(d[2]))
    return f"{prefix}:(day:{day},month:{month},year:{year})"


def analytics_query_string(pivot: str, since: str, until: str, fields: str,
                            account_id: str = None, campaign_id: str = None,
                            time_granularity: str = None) -> str:
    """Monta a querystring Rest.li 2.0 exigida pelo /rest/adAnalytics versionado."""
    parts = [
        "q=analytics",
        f"pivot={pivot}",
        f"dateRange=({restli_date('start', since)},{restli_date('end', until)})",
        f"fields={fields}",
    ]
    if account_id:
        parts.append(f"accounts=List(urn%3Ali%3AsponsoredAccount%3A{account_id})")
    if campaign_id:
        parts.append(f"campaigns=List(urn%3Ali%3AsponsoredCampaign%3A{campaign_id})")
    if time_granularity:
        parts.append(f"timeGranularity={time_granularity}")
    return "&".join(parts)


def api_post(path: str, body: dict, versioned: bool = False) -> dict:
    base = API_BASE_REST if versioned else API_BASE_V2
    url = f"{base}{path}"
    resp = requests.post(url, headers=get_headers(versioned), json=body)
    if not resp.ok:
        print(f"[ERRO] {resp.status_code} — {resp.text}")
        sys.exit(1)
    return resp.json() if resp.text else {}


def api_patch(path: str, body: dict, versioned: bool = False) -> dict:
    base = API_BASE_REST if versioned else API_BASE_V2
    url = f"{base}{path}"
    resp = requests.patch(url, headers=get_headers(versioned), json=body)
    if not resp.ok:
        print(f"[ERRO] {resp.status_code} — {resp.text}")
        sys.exit(1)
    return resp.json() if resp.text else {}


def api_delete(path: str, versioned: bool = False) -> None:
    base = API_BASE_REST if versioned else API_BASE_V2
    url = f"{base}{path}"
    resp = requests.delete(url, headers=get_headers(versioned))
    if not resp.ok:
        print(f"[ERRO] {resp.status_code} — {resp.text}")
        sys.exit(1)


def account_urn(account_id: str) -> str:
    return f"urn:li:sponsoredAccount:{account_id}"


def campaign_urn(campaign_id: str) -> str:
    return f"urn:li:sponsoredCampaign:{campaign_id}"


def campaign_group_urn(group_id: str) -> str:
    return f"urn:li:sponsoredCampaignGroup:{group_id}"


def fmt_money(value_cents: float, currency: str = "BRL") -> str:
    return f"{currency} {value_cents / 100:.2f}"


def fmt_pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def print_table(rows: list[dict], cols: list[str]) -> None:
    if not rows:
        print("(sem resultados)")
        return
    widths = {c: len(c) for c in cols}
    for row in rows:
        for c in cols:
            widths[c] = max(widths[c], len(str(row.get(c, ""))))
    header = "  ".join(c.ljust(widths[c]) for c in cols)
    sep = "  ".join("-" * widths[c] for c in cols)
    print(header)
    print(sep)
    for row in rows:
        print("  ".join(str(row.get(c, "")).ljust(widths[c]) for c in cols))

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
API_BASE = "https://api.linkedin.com/rest"
LINKEDIN_VERSION = "202405"

load_dotenv(ENV_FILE)


def get_env(key: str) -> str:
    val = os.getenv(key, "")
    if not val:
        print(f"[ERRO] Variavel '{key}' nao encontrada no .env ({ENV_FILE})")
        sys.exit(1)
    return val


def get_headers() -> dict:
    token = get_env("LINKEDIN_ACCESS_TOKEN")
    return {
        "Authorization": f"Bearer {token}",
        "LinkedIn-Version": LINKEDIN_VERSION,
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }


def api_get(path: str, params: dict = None) -> dict:
    url = f"{API_BASE}{path}"
    resp = requests.get(url, headers=get_headers(), params=params)
    if resp.status_code == 401:
        print("[ERRO] Token expirado ou invalido. Rode setup.py refresh para renovar.")
        sys.exit(1)
    if not resp.ok:
        print(f"[ERRO] {resp.status_code} — {resp.text}")
        sys.exit(1)
    return resp.json()


def api_post(path: str, body: dict) -> dict:
    url = f"{API_BASE}{path}"
    resp = requests.post(url, headers=get_headers(), json=body)
    if not resp.ok:
        print(f"[ERRO] {resp.status_code} — {resp.text}")
        sys.exit(1)
    return resp.json() if resp.text else {}


def api_patch(path: str, body: dict) -> dict:
    url = f"{API_BASE}{path}"
    resp = requests.patch(url, headers=get_headers(), json=body)
    if not resp.ok:
        print(f"[ERRO] {resp.status_code} — {resp.text}")
        sys.exit(1)
    return resp.json() if resp.text else {}


def api_delete(path: str) -> None:
    url = f"{API_BASE}{path}"
    resp = requests.delete(url, headers=get_headers())
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

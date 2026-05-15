"""Criacao de grupos de campanha, campanhas e criativos. Sempre cria PAUSED."""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import api_post, account_urn, campaign_group_urn, campaign_urn, print_table
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")


def cmd_campaign_group(args):
    body = {
        "account": account_urn(args.account_id),
        "name": args.name,
        "status": "PAUSED",
        "runSchedule": {"start": 0},
    }
    if args.objective:
        body["objective"] = args.objective
    result = api_post("/adCampaignGroups", body)
    gid = result.get("id", "").split(":")[-1]
    print(f"[OK] Grupo criado — ID: {gid} | Nome: {args.name} | Status: PAUSED")


def cmd_campaign(args):
    body = {
        "account": account_urn(args.account_id),
        "campaignGroup": campaign_group_urn(args.group_id),
        "name": args.name,
        "status": "PAUSED",
        "type": args.type,
        "format": args.format,
        "costType": args.cost_type,
        "unitCost": {"amount": str(args.bid), "currencyCode": args.currency},
        "dailyBudget": {"amount": str(args.budget), "currencyCode": args.currency},
        "locale": {"country": "BR", "language": "pt"},
        "objectiveType": args.objective,
    }
    result = api_post("/adCampaigns", body)
    cid = result.get("id", "").split(":")[-1]
    print(f"[OK] Campanha criada — ID: {cid} | Nome: {args.name} | Status: PAUSED")
    print(f"     Tipo: {args.type} | Formato: {args.format} | Budget/dia: {args.currency} {args.budget}")


def cmd_creative(args):
    """Cria criativo de Single Image Ad (Sponsored Content)."""
    body = {
        "campaign": campaign_urn(args.campaign_id),
        "status": "PAUSED",
        "type": "SPONSORED_STATUS_UPDATE",
        "variables": {
            "data": {
                "com.linkedin.ads.SponsoredUpdateCreativeVariables": {
                    "activity": args.post_urn,
                }
            }
        },
    }
    result = api_post("/adCreatives", body)
    crid = result.get("id", "").split(":")[-1]
    print(f"[OK] Criativo criado — ID: {crid} | Status: PAUSED")
    print(f"     Post URN: {args.post_urn}")


COMMANDS = {
    "campaign-group": (cmd_campaign_group, [
        ("--account-id", True),
        ("--name", True),
        ("--objective", False),
    ]),
    "campaign": (cmd_campaign, [
        ("--account-id", True),
        ("--group-id", True),
        ("--name", True),
        ("--type", True),
        ("--format", True),
        ("--objective", True),
        ("--budget", True),
        ("--bid", True),
        ("--cost-type", False),
        ("--currency", False),
    ]),
    "creative": (cmd_creative, [
        ("--campaign-id", True),
        ("--post-urn", True),
    ]),
}

DEFAULTS = {"--cost-type": "CPM", "--currency": "BRL"}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(f"Uso: create.py [{' | '.join(COMMANDS)}] [--opcoes]")
        sys.exit(1)
    cmd_name = sys.argv[1]
    fn, arg_defs = COMMANDS[cmd_name]
    parser = argparse.ArgumentParser()
    for flag, required in arg_defs:
        parser.add_argument(flag, required=required, default=DEFAULTS.get(flag),
                            dest=flag.lstrip("-").replace("-", "_"))
    args = parser.parse_args(sys.argv[2:])
    print("[ATENCAO] Todos os objetos sao criados com status PAUSED. Ative manualmente apos revisar.")
    fn(args)

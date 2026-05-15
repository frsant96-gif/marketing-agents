"""Leitura de contas, campanhas, grupos, criativos e segmentacao."""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import api_get, account_urn, campaign_urn, campaign_group_urn, print_table
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")


def cmd_accounts(args):
    data = api_get("/adAccounts", {"q": "search", "search.type.values[0]": "BUSINESS"})
    rows = []
    for a in data.get("elements", []):
        rows.append({
            "ID": a["id"].split(":")[-1],
            "Nome": a.get("name", ""),
            "Moeda": a.get("currency", ""),
            "Status": a.get("status", ""),
        })
    print_table(rows, ["ID", "Nome", "Moeda", "Status"])


def cmd_campaign_groups(args):
    params = {
        "q": "search",
        "search.account.values[0]": account_urn(args.account_id),
        "count": 50,
    }
    data = api_get("/adCampaignGroups", params)
    rows = []
    for g in data.get("elements", []):
        rows.append({
            "ID": g["id"].split(":")[-1],
            "Nome": g.get("name", ""),
            "Status": g.get("status", ""),
            "Objetivo": g.get("objective", ""),
        })
    print_table(rows, ["ID", "Nome", "Status", "Objetivo"])


def cmd_campaigns(args):
    params = {
        "q": "search",
        "search.account.values[0]": account_urn(args.account_id),
        "count": 50,
    }
    if args.group_id:
        params["search.campaignGroup.values[0]"] = campaign_group_urn(args.group_id)
    data = api_get("/adCampaigns", params)
    rows = []
    for c in data.get("elements", []):
        budget = c.get("dailyBudget", {})
        rows.append({
            "ID": c["id"].split(":")[-1],
            "Nome": c.get("name", ""),
            "Status": c.get("status", ""),
            "Tipo": c.get("type", ""),
            "Formato": c.get("format", ""),
            "Budget/dia": f"{budget.get('currencyCode','')}{budget.get('amount','')}",
        })
    print_table(rows, ["ID", "Nome", "Status", "Tipo", "Formato", "Budget/dia"])


def cmd_creatives(args):
    params = {
        "q": "search",
        "search.campaign.values[0]": campaign_urn(args.campaign_id),
        "count": 50,
    }
    data = api_get("/adCreatives", params)
    rows = []
    for c in data.get("elements", []):
        rows.append({
            "ID": c["id"].split(":")[-1],
            "Status": c.get("status", ""),
            "Tipo": c.get("type", ""),
        })
    print_table(rows, ["ID", "Status", "Tipo"])


def cmd_targeting(args):
    """Lista facetas de segmentacao disponiveis (cargos, setores, etc.)."""
    params = {"facetUrn": args.facet}
    data = api_get("/adTargetingFacets", params)
    elements = data.get("elements", [])
    for e in elements[:50]:
        print(f"{e.get('urn', '')}  —  {e.get('name', {}).get('value', '')}")
    if len(elements) > 50:
        print(f"... ({len(elements)} total, mostrando 50)")


COMMANDS = {
    "accounts": (cmd_accounts, []),
    "campaign-groups": (cmd_campaign_groups, [("--account-id", True)]),
    "campaigns": (cmd_campaigns, [("--account-id", True), ("--group-id", False)]),
    "creatives": (cmd_creatives, [("--campaign-id", True)]),
    "targeting": (cmd_targeting, [("--facet", True)]),
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(f"Uso: read.py [{' | '.join(COMMANDS)}] [--opcoes]")
        sys.exit(1)

    cmd_name = sys.argv[1]
    fn, arg_defs = COMMANDS[cmd_name]
    parser = argparse.ArgumentParser()
    for flag, required in arg_defs:
        parser.add_argument(flag, required=required, dest=flag.lstrip("-").replace("-", "_"))
    args = parser.parse_args(sys.argv[2:])
    fn(args)

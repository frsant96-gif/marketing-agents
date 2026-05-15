"""Leitura de contas, campanhas, grupos, criativos e segmentacao."""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import api_get, account_urn, campaign_urn, print_table
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")


def extract_id(val) -> str:
    return str(val).split(":")[-1]


def cmd_accounts(args):
    data = api_get("/adAccounts", {"q": "search"}, versioned=True)
    rows = []
    for a in data.get("elements", []):
        rows.append({
            "ID": extract_id(a["id"]),
            "Nome": a.get("name", ""),
            "Moeda": a.get("currency", ""),
            "Status": a.get("status", ""),
        })
    print_table(rows, ["ID", "Nome", "Moeda", "Status"])


def cmd_campaign_groups(args):
    data = api_get("/adCampaignGroupsV2", {"q": "search"})
    rows = []
    for g in data.get("elements", []):
        acct = extract_id(g.get("account", ""))
        if args.account_id and acct != args.account_id:
            continue
        rows.append({
            "ID": extract_id(g["id"]),
            "Nome": g.get("name", ""),
            "Status": g.get("status", ""),
        })
    print_table(rows, ["ID", "Nome", "Status"])


def cmd_campaigns(args):
    params = {"q": "search", "count": 50}
    if args.status:
        params["search.status.values[0]"] = args.status
    data = api_get("/adCampaignsV2", params)
    rows = []
    for c in data.get("elements", []):
        acct = extract_id(c.get("account", ""))
        if args.account_id and acct != args.account_id:
            continue
        budget = c.get("dailyBudget", {})
        rows.append({
            "ID": extract_id(c["id"]),
            "Nome": c.get("name", ""),
            "Status": c.get("status", ""),
            "Tipo": c.get("type", ""),
            "Formato": c.get("format", ""),
            "Budget/dia": f"{budget.get('currencyCode','')}{budget.get('amount','')}",
        })
    print_table(rows, ["ID", "Nome", "Status", "Tipo", "Formato", "Budget/dia"])


def cmd_creatives(args):
    params = {"q": "search", "search.campaign.values[0]": campaign_urn(args.campaign_id)}
    data = api_get("/adCreativesV2", params)
    rows = []
    for c in data.get("elements", []):
        rows.append({
            "ID": extract_id(c["id"]),
            "Status": c.get("status", ""),
            "Tipo": c.get("type", ""),
        })
    print_table(rows, ["ID", "Status", "Tipo"])


COMMANDS = {
    "accounts": (cmd_accounts, []),
    "campaign-groups": (cmd_campaign_groups, [("--account-id", False)]),
    "campaigns": (cmd_campaigns, [("--account-id", False), ("--status", False)]),
    "creatives": (cmd_creatives, [("--campaign-id", True)]),
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

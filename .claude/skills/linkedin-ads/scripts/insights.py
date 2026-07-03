"""Analytics e metricas de performance do LinkedIn Ads."""

import sys
import argparse
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).parent))
from lib import api_get, account_urn, campaign_urn, fmt_money, fmt_pct, print_table

def analytics_get(params: dict) -> dict:
    return api_get("/adAnalytics", params, versioned=True)
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")


def parse_date(date_str: str) -> dict:
    d = datetime.strptime(date_str, "%Y-%m-%d")
    return {"year": d.year, "month": d.month, "day": d.day}


def date_range_params(since: str, until: str, prefix: str = "dateRange") -> dict:
    s = parse_date(since)
    u = parse_date(until)
    return {
        f"{prefix}.start.day": s["day"],
        f"{prefix}.start.month": s["month"],
        f"{prefix}.start.year": s["year"],
        f"{prefix}.end.day": u["day"],
        f"{prefix}.end.month": u["month"],
        f"{prefix}.end.year": u["year"],
    }


def default_dates(days: int = 30):
    end = datetime.today()
    start = end - timedelta(days=days)
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")


METRICS = "clicks,impressions,costInLocalCurrency,leads"


def cmd_account(args):
    since = args.since or default_dates(30)[0]
    until = args.until or default_dates(30)[1]
    params = {
        "q": "analytics",
        "pivot": "ACCOUNT",
        "accounts[0]": account_urn(args.account_id),
        "fields": METRICS,
        **date_range_params(since, until),
    }
    data = analytics_get(params)
    elements = data.get("elements", [])
    if not elements:
        print("Sem dados para o periodo.")
        return
    e = elements[0]
    cost = float(e.get("costInLocalCurrency", {}).get("value", 0))
    clicks = int(e.get("clicks", {}).get("value", 0))
    imps = int(e.get("impressions", {}).get("value", 0))
    leads = int(e.get("leads", {}).get("value", 0))
    ctr = clicks / imps if imps else 0
    cpl = cost / leads if leads else 0
    cpc = cost / clicks if clicks else 0

    print(f"\nPerformance da conta — {since} a {until}\n")
    print(f"  Impressoes:  {imps:,}")
    print(f"  Cliques:     {clicks:,}")
    print(f"  CTR:         {fmt_pct(ctr)}")
    print(f"  Leads:       {leads:,}")
    print(f"  Gasto:       {fmt_money(cost * 100)}")
    print(f"  CPC medio:   {fmt_money(cpc * 100)}")
    print(f"  CPL:         {fmt_money(cpl * 100)}")


def cmd_campaign(args):
    since = args.since or default_dates(30)[0]
    until = args.until or default_dates(30)[1]
    params = {
        "q": "analytics",
        "pivot": "CAMPAIGN",
        "accounts[0]": account_urn(args.account_id),
        "fields": METRICS,
        **date_range_params(since, until),
    }
    data = analytics_get(params)
    rows = []
    for e in data.get("elements", []):
        cost = float(e.get("costInLocalCurrency", {}).get("value", 0))
        clicks = int(e.get("clicks", {}).get("value", 0))
        imps = int(e.get("impressions", {}).get("value", 0))
        leads = int(e.get("leads", {}).get("value", 0))
        ctr = clicks / imps if imps else 0
        cpl = cost / leads if leads else 0
        campaign_id = e.get("pivotValues", [""])[0].split(":")[-1]
        rows.append({
            "Campanha ID": campaign_id,
            "Impressoes": f"{imps:,}",
            "Cliques": f"{clicks:,}",
            "CTR": fmt_pct(ctr),
            "Leads": leads,
            "Gasto": fmt_money(cost * 100),
            "CPL": fmt_money(cpl * 100),
        })
    rows.sort(key=lambda r: float(r["Gasto"].replace("BRL ", "").replace(",", "")), reverse=True)
    print_table(rows, ["Campanha ID", "Impressoes", "Cliques", "CTR", "Leads", "Gasto", "CPL"])


def cmd_creative(args):
    since = args.since or default_dates(30)[0]
    until = args.until or default_dates(30)[1]
    params = {
        "q": "analytics",
        "pivot": "CREATIVE",
        "campaigns[0]": campaign_urn(args.campaign_id),
        "fields": METRICS,
        **date_range_params(since, until),
    }
    data = analytics_get(params)
    rows = []
    for e in data.get("elements", []):
        cost = float(e.get("costInLocalCurrency", {}).get("value", 0))
        clicks = int(e.get("clicks", {}).get("value", 0))
        imps = int(e.get("impressions", {}).get("value", 0))
        leads = int(e.get("leads", {}).get("value", 0))
        creative_id = e.get("pivotValues", [""])[0].split(":")[-1]
        rows.append({
            "Criativo ID": creative_id,
            "Impressoes": f"{imps:,}",
            "Cliques": f"{clicks:,}",
            "CTR": fmt_pct(clicks / imps if imps else 0),
            "Leads": leads,
            "Gasto": fmt_money(cost * 100),
        })
    print_table(rows, ["Criativo ID", "Impressoes", "Cliques", "CTR", "Leads", "Gasto"])


def cmd_daily(args):
    since = args.since or default_dates(30)[0]
    until = args.until or default_dates(30)[1]
    params = {
        "q": "analytics",
        "pivot": "CAMPAIGN",
        "timeGranularity": "DAILY",
        "accounts[0]": account_urn(args.account_id),
        "fields": "clicks,impressions,costInLocalCurrency,leads",
        **date_range_params(since, until),
    }
    data = analytics_get(params)
    rows = []
    for e in data.get("elements", []):
        dr = e.get("dateRange", {}).get("start", {})
        date = f"{dr.get('year','')}-{str(dr.get('month','')).zfill(2)}-{str(dr.get('day','')).zfill(2)}"
        cost = float(e.get("costInLocalCurrency", {}).get("value", 0))
        clicks = int(e.get("clicks", {}).get("value", 0))
        imps = int(e.get("impressions", {}).get("value", 0))
        leads = int(e.get("leads", {}).get("value", 0))
        rows.append({
            "Data": date,
            "Impressoes": f"{imps:,}",
            "Cliques": f"{clicks:,}",
            "Leads": leads,
            "Gasto": fmt_money(cost * 100),
        })
    rows.sort(key=lambda r: r["Data"])
    print_table(rows, ["Data", "Impressoes", "Cliques", "Leads", "Gasto"])


COMMANDS = {
    "account": (cmd_account, [("--account-id", True), ("--since", False), ("--until", False)]),
    "campaign": (cmd_campaign, [("--account-id", True), ("--since", False), ("--until", False)]),
    "creative": (cmd_creative, [("--campaign-id", True), ("--since", False), ("--until", False)]),
    "daily": (cmd_daily, [("--account-id", True), ("--since", False), ("--until", False)]),
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(f"Uso: insights.py [{' | '.join(COMMANDS)}] [--opcoes]")
        sys.exit(1)
    cmd_name = sys.argv[1]
    fn, arg_defs = COMMANDS[cmd_name]
    parser = argparse.ArgumentParser()
    for flag, required in arg_defs:
        parser.add_argument(flag, required=required, dest=flag.lstrip("-").replace("-", "_"))
    args = parser.parse_args(sys.argv[2:])
    fn(args)

"""Analytics e metricas de performance do LinkedIn Ads."""

import sys
import argparse
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).parent))
from lib import api_get_raw_qs, analytics_query_string, fmt_money, fmt_pct, print_table
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")


def analytics_get(pivot, since, until, fields, **kwargs):
    qs = analytics_query_string(pivot, since, until, fields, **kwargs)
    return api_get_raw_qs("/adAnalytics", qs, versioned=True)


def default_dates(days: int = 30):
    end = datetime.today()
    start = end - timedelta(days=days)
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")


METRICS = "clicks,impressions,costInLocalCurrency"
# "leads" nao existe no schema atual (com.linkedin.adsexternalapi.reportingapi.v6.AdAnalyticsV6) —
# LinkedIn descontinuou esse campo agregado; leads reais precisam vir do Lead Gen Forms report
# ou do CRM (UTM/campanha_de_conversao). Mantido como METRICS por enquanto.
METRICS_LEADS = METRICS


def _num(e: dict, key: str, cast=float) -> float:
    """Campos do /adAnalytics vem como valor simples (nao {"value": N})."""
    v = e.get(key, 0)
    return cast(v) if v not in (None, "") else cast(0)


def cmd_account(args):
    since = args.since or default_dates(30)[0]
    until = args.until or default_dates(30)[1]
    data = analytics_get("ACCOUNT", since, until, METRICS_LEADS,
                          account_id=args.account_id, time_granularity="ALL")
    elements = data.get("elements", [])
    if not elements:
        print("Sem dados para o periodo.")
        return
    e = elements[0]
    cost = _num(e, "costInLocalCurrency")
    clicks = int(_num(e, "clicks"))
    imps = int(_num(e, "impressions"))
    ctr = clicks / imps if imps else 0
    cpc = cost / clicks if clicks else 0

    print(f"\nPerformance da conta — {since} a {until}\n")
    print(f"  Impressoes:  {imps:,}")
    print(f"  Cliques:     {clicks:,}")
    print(f"  CTR:         {fmt_pct(ctr)}")
    print(f"  Gasto:       {fmt_money(cost * 100)}")
    print(f"  CPC medio:   {fmt_money(cpc * 100)}")
    print(f"  (Leads nao disponiveis neste schema — usar Lead Gen Forms report ou CRM)")


def cmd_campaign(args):
    since = args.since or default_dates(30)[0]
    until = args.until or default_dates(30)[1]
    monthly = getattr(args, "monthly", False)
    time_granularity = "MONTHLY" if monthly else "ALL"
    fields = METRICS_LEADS + ",pivotValues,dateRange"
    data = analytics_get("CAMPAIGN", since, until, fields,
                          account_id=args.account_id, time_granularity=time_granularity)
    rows = []
    for e in data.get("elements", []):
        cost = _num(e, "costInLocalCurrency")
        clicks = int(_num(e, "clicks"))
        imps = int(_num(e, "impressions"))
        ctr = clicks / imps if imps else 0
        campaign_id = e.get("pivotValues", [""])[0].split(":")[-1]
        row = {
            "Campanha ID": campaign_id,
            "Impressoes": f"{imps:,}",
            "Cliques": f"{clicks:,}",
            "CTR": fmt_pct(ctr),
            "Gasto": fmt_money(cost * 100),
        }
        if monthly:
            dr = e.get("dateRange", {}).get("start", {})
            row["Mes"] = f"{dr.get('year','')}-{str(dr.get('month','')).zfill(2)}"
        rows.append(row)
    rows.sort(key=lambda r: float(r["Gasto"].replace("BRL ", "").replace(",", "")), reverse=True)
    cols = ["Mes", "Campanha ID", "Impressoes", "Cliques", "CTR", "Gasto"] if monthly \
        else ["Campanha ID", "Impressoes", "Cliques", "CTR", "Gasto"]
    print_table(rows, cols)


def cmd_creative(args):
    since = args.since or default_dates(30)[0]
    until = args.until or default_dates(30)[1]
    fields = METRICS_LEADS + ",pivotValues"
    data = analytics_get("CREATIVE", since, until, fields,
                          campaign_id=args.campaign_id, time_granularity="ALL")
    rows = []
    for e in data.get("elements", []):
        cost = _num(e, "costInLocalCurrency")
        clicks = int(_num(e, "clicks"))
        imps = int(_num(e, "impressions"))
        creative_id = e.get("pivotValues", [""])[0].split(":")[-1]
        rows.append({
            "Criativo ID": creative_id,
            "Impressoes": f"{imps:,}",
            "Cliques": f"{clicks:,}",
            "CTR": fmt_pct(clicks / imps if imps else 0),
            "Gasto": fmt_money(cost * 100),
        })
    print_table(rows, ["Criativo ID", "Impressoes", "Cliques", "CTR", "Gasto"])


def cmd_daily(args):
    since = args.since or default_dates(30)[0]
    until = args.until or default_dates(30)[1]
    fields = METRICS_LEADS + ",dateRange"
    data = analytics_get("CAMPAIGN", since, until, fields,
                          account_id=args.account_id, time_granularity="DAILY")
    rows = []
    for e in data.get("elements", []):
        dr = e.get("dateRange", {}).get("start", {})
        date = f"{dr.get('year','')}-{str(dr.get('month','')).zfill(2)}-{str(dr.get('day','')).zfill(2)}"
        cost = _num(e, "costInLocalCurrency")
        clicks = int(_num(e, "clicks"))
        imps = int(_num(e, "impressions"))
        rows.append({
            "Data": date,
            "Impressoes": f"{imps:,}",
            "Cliques": f"{clicks:,}",
            "Gasto": fmt_money(cost * 100),
        })
    rows.sort(key=lambda r: r["Data"])
    print_table(rows, ["Data", "Impressoes", "Cliques", "Gasto"])


COMMANDS = {
    "account": (cmd_account, [("--account-id", True), ("--since", False), ("--until", False)]),
    "campaign": (cmd_campaign, [("--account-id", True), ("--since", False), ("--until", False), ("--monthly", False)]),
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
        kwargs = {"dest": flag.lstrip("-").replace("-", "_")}
        if flag == "--monthly":
            kwargs["action"] = "store_true"
        else:
            kwargs["required"] = required
        parser.add_argument(flag, **kwargs)
    args = parser.parse_args(sys.argv[2:])
    fn(args)

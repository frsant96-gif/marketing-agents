"""Edicao de status, budget e configuracoes de campanhas e grupos."""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import api_patch, campaign_urn, campaign_group_urn
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

VALID_STATUSES = {"ACTIVE", "PAUSED", "ARCHIVED", "CANCELED", "DRAFT"}


def cmd_campaign_group(args):
    body = {}
    if args.status:
        if args.status not in VALID_STATUSES:
            print(f"[ERRO] Status invalido. Use: {', '.join(VALID_STATUSES)}")
            sys.exit(1)
        body["status"] = args.status
    if args.name:
        body["name"] = args.name
    if not body:
        print("[ERRO] Nada para atualizar. Passe --status ou --name.")
        sys.exit(1)
    api_patch(f"/adCampaignGroups/{campaign_group_urn(args.group_id)}", body)
    print(f"[OK] Grupo {args.group_id} atualizado: {body}")


def cmd_campaign(args):
    body = {}
    if args.status:
        if args.status not in VALID_STATUSES:
            print(f"[ERRO] Status invalido. Use: {', '.join(VALID_STATUSES)}")
            sys.exit(1)
        body["status"] = args.status
    if args.budget:
        body["dailyBudget"] = {"amount": str(args.budget), "currencyCode": args.currency or "BRL"}
    if args.name:
        body["name"] = args.name
    if not body:
        print("[ERRO] Nada para atualizar. Passe --status, --budget ou --name.")
        sys.exit(1)
    api_patch(f"/adCampaigns/{campaign_urn(args.campaign_id)}", body)
    print(f"[OK] Campanha {args.campaign_id} atualizada: {body}")


def cmd_creative(args):
    if not args.status:
        print("[ERRO] Passe --status para atualizar o criativo.")
        sys.exit(1)
    if args.status not in VALID_STATUSES:
        print(f"[ERRO] Status invalido. Use: {', '.join(VALID_STATUSES)}")
        sys.exit(1)
    api_patch(f"/adCreatives/{args.creative_id}", {"status": args.status})
    print(f"[OK] Criativo {args.creative_id} atualizado para {args.status}")


COMMANDS = {
    "campaign-group": (cmd_campaign_group, [
        ("--group-id", True), ("--status", False), ("--name", False),
    ]),
    "campaign": (cmd_campaign, [
        ("--campaign-id", True), ("--status", False), ("--budget", False),
        ("--name", False), ("--currency", False),
    ]),
    "creative": (cmd_creative, [
        ("--creative-id", True), ("--status", True),
    ]),
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(f"Uso: update.py [{' | '.join(COMMANDS)}] [--opcoes]")
        sys.exit(1)
    cmd_name = sys.argv[1]
    fn, arg_defs = COMMANDS[cmd_name]
    parser = argparse.ArgumentParser()
    for flag, required in arg_defs:
        parser.add_argument(flag, required=required, dest=flag.lstrip("-").replace("-", "_"))
    args = parser.parse_args(sys.argv[2:])
    fn(args)

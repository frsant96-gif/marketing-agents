"""Remocao de criativos e arquivamento de campanhas/grupos."""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import api_patch, api_delete, campaign_urn, campaign_group_urn
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")


def cmd_campaign(args):
    """Arquiva campanha (LinkedIn nao permite delecao fisica)."""
    api_patch(f"/adCampaigns/{campaign_urn(args.campaign_id)}", {"status": "ARCHIVED"})
    print(f"[OK] Campanha {args.campaign_id} arquivada.")


def cmd_campaign_group(args):
    """Arquiva grupo de campanha."""
    api_patch(f"/adCampaignGroups/{campaign_group_urn(args.group_id)}", {"status": "ARCHIVED"})
    print(f"[OK] Grupo {args.group_id} arquivado.")


def cmd_creative(args):
    """Arquiva criativo."""
    api_patch(f"/adCreatives/{args.creative_id}", {"status": "ARCHIVED"})
    print(f"[OK] Criativo {args.creative_id} arquivado.")


COMMANDS = {
    "campaign": (cmd_campaign, [("--campaign-id", True)]),
    "campaign-group": (cmd_campaign_group, [("--group-id", True)]),
    "creative": (cmd_creative, [("--creative-id", True)]),
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(f"Uso: delete.py [{' | '.join(COMMANDS)}] [--opcoes]")
        print("NOTA: LinkedIn nao deleta fisicamente — objetos sao ARQUIVADOS.")
        sys.exit(1)
    cmd_name = sys.argv[1]
    fn, arg_defs = COMMANDS[cmd_name]
    parser = argparse.ArgumentParser()
    for flag, required in arg_defs:
        parser.add_argument(flag, required=required, dest=flag.lstrip("-").replace("-", "_"))
    args = parser.parse_args(sys.argv[2:])
    print("[ATENCAO] Esta acao arquiva o objeto permanentemente no LinkedIn Ads.")
    confirm = input("Confirmar? (s/N): ").strip().lower()
    if confirm != "s":
        print("Operacao cancelada.")
        sys.exit(0)
    fn(args)

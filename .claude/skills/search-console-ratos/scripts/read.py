#!/usr/bin/env python3
"""
Search Console Ratos - Leitura de sites e sitemaps
Subcomandos: sites, sitemaps, sitemap-submit
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import (
    init_webmasters_client,
    resolve_site_url,
    add_site_arg,
    print_json,
    print_error,
    handle_gsc_error,
)


# ---------------------------------------------------------------------------
# sites — Lista sites acessiveis
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_sites(args):
    """Lista sites/propriedades do Search Console acessiveis pela conta autenticada."""
    client = init_webmasters_client()
    response = client.sites().list().execute()

    sites = []
    for entry in response.get("siteEntry", []):
        sites.append({
            "site_url": entry.get("siteUrl"),
            "permission_level": entry.get("permissionLevel"),
        })

    print_json({"sites": sites, "total": len(sites)})


# ---------------------------------------------------------------------------
# sitemaps — Lista sitemaps de um site
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_sitemaps(args):
    """Lista sitemaps cadastrados pra um site, com status de leitura/erros."""
    site_url = resolve_site_url(args.site)
    client = init_webmasters_client()
    response = client.sitemaps().list(siteUrl=site_url).execute()

    sitemaps = []
    for entry in response.get("sitemap", []):
        sitemaps.append({
            "path": entry.get("path"),
            "last_submitted": entry.get("lastSubmitted"),
            "last_downloaded": entry.get("lastDownloaded"),
            "is_pending": entry.get("isPending"),
            "is_sitemaps_index": entry.get("isSitemapsIndex"),
            "warnings": entry.get("warnings"),
            "errors": entry.get("errors"),
            "contents": entry.get("contents"),
        })

    print_json({"site_url": site_url, "sitemaps": sitemaps, "total": len(sitemaps)})


# ---------------------------------------------------------------------------
# sitemap-submit — Envia/resubmete um sitemap
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_sitemap_submit(args):
    """Envia (ou reenvia) um sitemap pro Google reprocessar."""
    site_url = resolve_site_url(args.site)
    client = init_webmasters_client(readwrite=True)

    if not args.feedpath:
        print_error("--feedpath e obrigatorio. Ex: --feedpath sitemap_index.xml")
        sys.exit(1)

    client.sitemaps().submit(siteUrl=site_url, feedpath=args.feedpath).execute()
    print_json({"status": "enviado", "site_url": site_url, "feedpath": args.feedpath})


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Search Console Ratos - Leitura")
    sub = parser.add_subparsers(dest="command")

    p_sites = sub.add_parser("sites", help="Lista sites acessiveis")

    p_sitemaps = sub.add_parser("sitemaps", help="Lista sitemaps de um site")
    add_site_arg(p_sitemaps)

    p_submit = sub.add_parser("sitemap-submit", help="Envia/resubmete um sitemap")
    add_site_arg(p_submit)
    p_submit.add_argument("--feedpath", help="Caminho do sitemap (ex: sitemap_index.xml)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "sites": cmd_sites,
        "sitemaps": cmd_sitemaps,
        "sitemap-submit": cmd_sitemap_submit,
    }

    cmd = commands.get(args.command)
    if cmd:
        cmd(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

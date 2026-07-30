#!/usr/bin/env python3
"""
Search Console Ratos - URL Inspection API
Subcomandos: url
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import (
    init_searchconsole_client,
    resolve_site_url,
    add_site_arg,
    print_json,
    print_error,
    handle_gsc_error,
)


# ---------------------------------------------------------------------------
# url — Inspeciona uma URL (status de indexacao, cobertura, mobile usability)
# ---------------------------------------------------------------------------

@handle_gsc_error
def cmd_url(args):
    """Inspeciona uma URL especifica: status de indexacao, canonical, cobertura, sitemaps."""
    if not args.url:
        print_error("--url e obrigatorio. Ex: --url https://solveplan.com/blog/artigo")
        sys.exit(1)

    site_url = resolve_site_url(args.site)
    client = init_searchconsole_client()

    body = {
        "inspectionUrl": args.url,
        "siteUrl": site_url,
    }

    response = client.urlInspection().index().inspect(body=body).execute()
    result = response.get("inspectionResult", {})

    index_status = result.get("indexStatusResult", {})
    mobile_usability = result.get("mobileUsabilityResult", {})
    rich_results = result.get("richResultsResult", {})

    output = {
        "url": args.url,
        "site": site_url,
        "verdict": index_status.get("verdict"),
        "coverage_state": index_status.get("coverageState"),
        "indexing_state": index_status.get("indexingState"),
        "last_crawl_time": index_status.get("lastCrawlTime"),
        "page_fetch_state": index_status.get("pageFetchState"),
        "google_canonical": index_status.get("googleCanonical"),
        "user_canonical": index_status.get("userCanonical"),
        "robots_txt_state": index_status.get("robotsTxtState"),
        "crawled_as": index_status.get("crawledAs"),
        "referring_urls": index_status.get("referringUrls"),
        "sitemap": index_status.get("sitemap"),
        "mobile_usability_verdict": mobile_usability.get("verdict"),
        "mobile_usability_issues": mobile_usability.get("issues"),
        "rich_results_verdict": rich_results.get("verdict"),
        "rich_results_detected_items": [
            item.get("richResultType") for item in rich_results.get("detectedItems", [])
        ],
    }

    print_json(output)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Search Console Ratos - URL Inspection")
    sub = parser.add_subparsers(dest="command")

    p_url = sub.add_parser("url", help="Inspeciona uma URL (indexacao, mobile, rich results)")
    add_site_arg(p_url)
    p_url.add_argument("--url", help="URL completa a inspecionar")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "url": cmd_url,
    }

    cmd = commands.get(args.command)
    if cmd:
        cmd(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

"""
buscar_cnpj.py — Busca CNPJ por nome de empresa via CNPJ.biz (gratuito)

Uso:
    python scripts/buscar_cnpj.py dados/Empresas_Kevin_Enriquecido_v2_2026-05-24.xlsx

Saída:
    Mesmo arquivo com coluna CNPJ preenchida
"""

import sys
import time
import re
import requests
from bs4 import BeautifulSoup
import openpyxl
from pathlib import Path

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


def limpar_nome(nome):
    """Remove sufixos jurídicos e caracteres especiais para melhorar a busca."""
    sufixos = [r'\bltda\.?\b', r'\bs\.?a\.?\b', r'\bsa\b', r'\bme\b', r'\beiro\b',
                r'\bltd\b', r'\beinc\b', r'\bs\/a\b', r'\bsa\b']
    nome = nome.lower()
    for s in sufixos:
        nome = re.sub(s, '', nome, flags=re.IGNORECASE)
    return nome.strip()


def buscar_cnpj_biz(nome_empresa, razao_social=None):
    """Busca CNPJ no CNPJ.biz por nome/razão social."""
    termos = [razao_social, nome_empresa]

    for termo in termos:
        if not termo:
            continue
        try:
            url = f"https://www.cnpj.biz/pesquisar.php?q={requests.utils.quote(termo)}"
            resp = requests.get(url, headers=HEADERS, timeout=10)
            soup = BeautifulSoup(resp.text, "html.parser")

            # Procurar resultados na página
            resultados = soup.select("table.resultado-pesquisa tbody tr") or \
                         soup.select(".search-results .result-item") or \
                         soup.select("a[href*='/cnpj/']")

            cnpjs = []
            for r in resultados:
                texto = r.get_text()
                matches = re.findall(r'\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}', texto)
                cnpjs.extend(matches)
                # Também pegar de href
                href = r.get('href', '')
                m = re.search(r'/cnpj/(\d{14})', href)
                if m:
                    c = m.group(1)
                    fmt = f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}"
                    cnpjs.append(fmt)

            cnpjs = list(dict.fromkeys(cnpjs))  # deduplica mantendo ordem

            if len(cnpjs) == 1:
                return cnpjs[0], "encontrado"
            elif len(cnpjs) > 1:
                return cnpjs[0], "ambíguo"

        except Exception as e:
            print(f"  Erro ao buscar '{termo}': {e}")

        time.sleep(1.5)  # respeitar rate limit

    return "pendente", "não encontrado"


def formatar_cnpj(cnpj_raw):
    """Formata CNPJ para XX.XXX.XXX/XXXX-XX."""
    digits = re.sub(r'\D', '', cnpj_raw)
    if len(digits) == 14:
        return f"{digits[:2]}.{digits[2:5]}.{digits[5:8]}/{digits[8:12]}-{digits[12:]}"
    return cnpj_raw


def main(caminho_excel):
    path = Path(caminho_excel)
    if not path.exists():
        print(f"Arquivo não encontrado: {path}")
        sys.exit(1)

    wb = openpyxl.load_workbook(path)
    ws = wb.active

    headers = [cell.value for cell in ws[1]]

    if 'CNPJ' not in headers:
        print("Coluna CNPJ não encontrada no arquivo.")
        sys.exit(1)

    idx_empresa = headers.index('EMPRESA') if 'EMPRESA' in headers else None
    idx_razao = headers.index('RAZAO SOCIAL') if 'RAZAO SOCIAL' in headers else None
    idx_cnpj = headers.index('CNPJ')

    total = ws.max_row - 1
    print(f"\nProcessando {total} empresas...\n")

    encontrados = 0
    ambiguos = 0
    pendentes = 0

    for i, row in enumerate(ws.iter_rows(min_row=2), start=1):
        empresa = row[idx_empresa].value if idx_empresa is not None else None
        razao = row[idx_razao].value if idx_razao is not None else None
        cnpj_atual = row[idx_cnpj].value

        # Pular se já tem CNPJ válido
        if cnpj_atual and cnpj_atual not in ('pendente', 'ambíguo', ''):
            print(f"[{i}/{total}] {empresa} — já tem CNPJ, pulando")
            encontrados += 1
            continue

        print(f"[{i}/{total}] Buscando: {empresa}...", end=' ', flush=True)
        cnpj, status = buscar_cnpj_biz(empresa, razao)
        row[idx_cnpj].value = cnpj
        print(f"{cnpj} ({status})")

        if status == "encontrado":
            encontrados += 1
        elif status == "ambíguo":
            ambiguos += 1
        else:
            pendentes += 1

        time.sleep(1)  # rate limit entre empresas

    wb.save(path)

    print(f"\n--- Resultado ---")
    print(f"Encontrados:  {encontrados}/{total}")
    print(f"Ambíguos:     {ambiguos}/{total} — revisar manualmente")
    print(f"Pendentes:    {pendentes}/{total} — revisar manualmente")
    print(f"\nArquivo salvo: {path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python scripts/buscar_cnpj.py <caminho_excel>")
        sys.exit(1)
    main(sys.argv[1])

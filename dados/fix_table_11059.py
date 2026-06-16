import json

path = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\dados\elementor_data_11059_current.json"

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_table_html = """<style>
.sw-compare-wrapper {
  max-width: 720px;
  margin: 0 auto;
}

.sw-compare-table {
  width: 100%;
  border-collapse: collapse;
  font-family: inherit;
  background: #0b1a2e;
  border-radius: 12px;
  overflow: hidden;
}

.sw-compare-table th,
.sw-compare-table td {
  padding: 16px 20px;
  text-align: center;
  border-bottom: 1px solid rgba(255,255,255,0.07);
  font-size: 14px;
  color: #c8d6e8;
}

.sw-compare-table th:first-child,
.sw-compare-table td:first-child {
  text-align: left;
  width: 55%;
  font-weight: 400;
  color: #c8d6e8;
}

.sw-compare-table thead th {
  background: transparent;
  color: #7a9cbf;
  font-size: 13px;
  font-weight: 600;
  padding-top: 24px;
  padding-bottom: 24px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.sw-compare-table thead th:first-child {
  color: #7a9cbf;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.sw-compare-table thead th.col-sw {
  color: #ffffff;
  font-size: 15px;
  font-weight: 700;
}

.sw-compare-table thead th.col-sw::before {
  content: "✦ ";
  color: #5de6c8;
}

.sw-compare-table tbody tr:last-child td {
  border-bottom: none;
}

.sw-compare-table tbody tr:hover td {
  background: rgba(255,255,255,0.03);
}

.sw-compare-table td.col-sw {
  color: #5de6c8;
  font-size: 20px;
}

.sw-compare-table td.col-native {
  color: #e05252;
  font-size: 20px;
}

.sw-compare-table td.col-native.parcial {
  color: #f0a830;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.sw-compare-table tr.highlight td:first-child {
  color: #ffffff;
  font-weight: 700;
}
</style>

<div class="sw-compare-wrapper">
<table class="sw-compare-table">
  <thead>
    <tr>
      <th>Capacidade</th>
      <th class="col-sw">Solve Watch</th>
      <th>Datasphere Nativo</th>
    </tr>
  </thead>
  <tbody>
    <tr class="highlight">
      <td>Leitura semântica e prontidão para IA</td>
      <td class="col-sw">✓</td>
      <td class="col-native">✕</td>
    </tr>
    <tr class="highlight">
      <td>Diagnóstico priorizado com severidade</td>
      <td class="col-sw">✓</td>
      <td class="col-native">✕</td>
    </tr>
    <tr class="highlight">
      <td>Recomendações validadas por arquiteto</td>
      <td class="col-sw">✓</td>
      <td class="col-native">✕</td>
    </tr>
    <tr>
      <td>Projeção de fechamento de Capacity Unit</td>
      <td class="col-sw">✓</td>
      <td class="col-native">✕</td>
    </tr>
    <tr>
      <td>Identificação de onde o custo vaza</td>
      <td class="col-sw">✓</td>
      <td class="col-native">✕</td>
    </tr>
    <tr>
      <td>Detecção de falha / histórico / inventário</td>
      <td class="col-sw">✓</td>
      <td class="col-native parcial">Parcial</td>
    </tr>
  </tbody>
</table>
</div>"""

def update_html_widget(elements, target_id, new_html):
    for el in elements:
        if el.get('id') == target_id:
            el['settings']['html'] = new_html
            return True
        if el.get('elements'):
            if update_html_widget(el['elements'], target_id, new_html):
                return True
    return False

found = update_html_widget(data, '945e1c6', new_table_html)
print(f"Widget encontrado e atualizado: {found}")

out_path = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\dados\elementor_data_11059_table.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

print(f"Salvo em: {out_path}")
print(f"Tamanho: {len(json.dumps(data, ensure_ascii=False))} chars")

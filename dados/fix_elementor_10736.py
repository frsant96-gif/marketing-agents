import json

path = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\dados\elementor_data_10736.json"

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# ── FAQ content ───────────────────────────────────────────────────────────────
faq_html = (
    '<p><strong style="color: inherit; font-family: inherit; font-size: 1.25rem;">Perguntas frequentes — Solve Watch</strong></p>\n'
    '<details class="wp-block-details">\n'
    '<summary>O que é o Solve Watch?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>O Solve Watch é um serviço gerenciado especializado em SAP Datasphere que combina tecnologia própria com especialistas Solveplan. Ele monitora continuamente seu ambiente, identifica riscos antes que impactem o negócio e entrega recomendações práticas para melhorar performance, governança e consumo de Capacity Units.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
    '<details class="wp-block-details">\n'
    '<summary>Quais problemas o Solve Watch resolve no SAP Datasphere?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>O Solve Watch resolve os principais problemas silenciosos do SAP Datasphere: falhas ocultas em cargas de dados, crescimento descontrolado de Capacity Units, falta de governança de objetos, retrabalho operacional e ambientes sem visibilidade histórica — problemas que o monitoramento nativo do SAP Datasphere não identifica.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
    '<details class="wp-block-details">\n'
    '<summary>Qual a diferença entre o Solve Watch e o monitoramento nativo do SAP Datasphere?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>O monitoramento nativo do SAP Datasphere entrega painéis básicos sem histórico, sem alertas proativos e sem análise. O Solve Watch adiciona histórico de performance, alertas configurados por criticidade de negócio, análise de FinOps para controle de Capacity Units e governança de metadados — com a interpretação de especialistas SAP em cima dos dados.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
    '<details class="wp-block-details">\n'
    '<summary>O Solve Watch é necessário antes de implementar IA sobre dados SAP?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>Sim. Toda iniciativa de IA sobre dados SAP depende de uma camada semântica governada — objetos com nome claro, descrições preenchidas, arquitetura consistente e metadados que fazem sentido. O Solve Watch identifica e estrutura esse ambiente antes de ativar soluções de IA, garantindo que a IA leia dados confiáveis.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
    '<details class="wp-block-details">\n'
    '<summary>Em quanto tempo o Solve Watch entrega resultados?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>Em 30 dias, o Solve Watch já identifica falhas ocultas, entrega um diagnóstico completo e estabelece o baseline de consumo de Capacity Units. Em 90 dias, o ambiente se torna previsível e a performance está otimizada. Em 180 dias, a empresa tem controle financeiro ampliado e maturidade operacional para crescer com segurança.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
    '<details class="wp-block-details">\n'
    '<summary>O Solve Watch funciona apenas com SAP Datasphere?</summary>\n'
    '<p><!-- wp:paragraph --></p>\n'
    '<p>Sim, o Solve Watch é especializado em SAP Datasphere. A Solveplan é parceira SAP Gold com foco em implementação e gestão de SAP Datasphere e SAP Business Data Cloud na América Latina — o que garante profundidade técnica e conhecimento do ecossistema SAP no serviço.</p>\n'
    '<p><!-- /wp:paragraph --></p>\n'
    '</details>\n'
)

faq_widget = {
    "id": "faq_solve_watch",
    "elType": "widget",
    "settings": {"editor": faq_html, "text_color": "#000000"},
    "elements": [],
    "widgetType": "text-editor"
}

# ── Find b649703 (final CTA heading) and insert FAQ before its parent container
def find_and_insert(elements, target_id, widget):
    """Recursively search for a container that has target_id as a direct child,
    then insert widget before that child."""
    for i, el in enumerate(elements):
        # Check direct children
        if 'elements' in el and el['elements']:
            for j, child in enumerate(el['elements']):
                if child.get('id') == target_id:
                    el['elements'].insert(j, widget)
                    return True, f"Inserted before {target_id} inside container {el['id']} at position {j}"
            # Recurse into children
            result, msg = find_and_insert(el['elements'], target_id, widget)
            if result:
                return True, msg
    return False, "Not found"

# Try inserting before b649703 (final CTA heading "Seu SAP Datasphere está saudável...")
found, msg = find_and_insert(data, 'b649703', faq_widget)
if found:
    print(f"OK: {msg}")
else:
    print("AVISO: Target b649703 nao encontrado — tentando top-level")
    top_elements = data[0]['elements']
    for i, el in enumerate(top_elements):
        if el.get('id') == 'b649703':
            top_elements.insert(i, faq_widget)
            print(f"OK: Inserido na posicao {i} (top-level)")
            found = True
            break
    if not found:
        print("AVISO: Adicionando ao final")
        data[0]['elements'].append(faq_widget)

# ── Save ──────────────────────────────────────────────────────────────────────
out_path = r"c:\Users\franc\solveplan.com\Roberto Molina - Marketing\1. MKT Estrategy\3. Agentes de IA\ccos-ratos\dados\elementor_data_10736_updated.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

size = len(json.dumps(data, ensure_ascii=False))
print(f"Arquivo salvo: {out_path}")
print(f"Tamanho: {size} chars")

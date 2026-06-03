const { chromium } = require('playwright');
const path = require('path');
const fs   = require('fs');
const { wrap, glowBR, glowTR, glowTL, glowCTR, glowTeal, stripL, stripLfull, logo, hdr } = require('../shared');

const BASE   = 'c:/Users/franc/solveplan.com/Roberto Molina - Marketing/1. MKT Estrategy/3. Agentes de IA/ccos-ratos';
const OUTPUT = path.join(BASE.replace(/\//g, path.sep), 'marketing', 'criativos', 'junho-2026', '01-datasphere-vs-bdc', 'slides');
fs.mkdirSync(OUTPUT, { recursive: true });

const TOTAL = 5;
const H = (n) => hdr(n, TOTAL);

const slides = [

// ── 01 CAPA ──────────────────────────────────────────────────────────────────
wrap('#0A0837', glowBR + glowTR + stripL, `
${H(1)}
<div class="body" style="justify-content:flex-start;padding-top:50px;">

  <span class="tag" style="background:#006AFF;color:#fff;margin-bottom:28px;">09 DE JUNHO</span>
  <div class="bar" style="margin-bottom:28px;"></div>

  <p style="font-family:'Prompt',sans-serif;font-size:76px;font-weight:800;line-height:1.06;margin-bottom:18px;">
    SAP Datasphere<br/>
    <span style="color:rgba(255,255,255,0.3);font-size:52px;font-weight:600;">vs</span><br/>
    SAP Business<br/><span class="accent">Data Cloud</span>
  </p>

  <div style="margin-top:auto;">
    <div class="div" style="margin-bottom:18px;"></div>
    <p style="font-family:'Montserrat',sans-serif;font-size:20px;font-weight:500;
       color:rgba(255,255,255,0.5);line-height:1.5;">
      Qual a diferença? Quando usar cada um?<br/>
      <span style="color:rgba(255,255,255,0.28);font-size:16px;">Muita gente confunde os dois. Explicamos em 5 slides →</span>
    </p>
  </div>
</div>
`),

// ── 02 SAP DATASPHERE ─────────────────────────────────────────────────────────
wrap('#0A0837', glowTL + stripLfull, `
${H(2)}
<div class="body" style="gap:0;">

  <span class="tag" style="background:#0057cc;color:#fff;margin-bottom:22px;">SAP DATASPHERE</span>
  <p style="font-family:'Prompt',sans-serif;font-size:52px;font-weight:800;line-height:1.1;
             margin-bottom:24px;">A plataforma de<br/>gestão de dados</p>

  <div class="div" style="margin-bottom:26px;"></div>

  ${[
    'Integra, modela e governa dados em ambientes SAP e não-SAP',
    'Criado para analistas e times de dados / TI',
    'Virtualiza fontes externas sem necessidade de replicação',
    'Já em uso em centenas de empresas SAP ao redor do mundo',
  ].map(t => `
  <div class="bullet">
    <div class="dot dot-blue"></div>
    <span class="btext">${t}</span>
  </div>`).join('')}

  <div style="margin-top:auto;">
    <div class="div" style="margin-bottom:18px;"></div>
    <p style="font-family:'Montserrat',sans-serif;font-size:18px;font-weight:600;
       color:rgba(255,255,255,0.45);">Em uma frase: é a plataforma onde o <span style="color:#fff;">dado existe</span>.</p>
  </div>
</div>
`),

// ── 03 SAP BDC ───────────────────────────────────────────────────────────────
wrap('linear-gradient(160deg,#0A0837 0%,#0d2240 100%)', glowTeal + stripLfull, `
${H(3)}
<div class="body" style="gap:0;">

  <span class="tag" style="background:#1BAD8D;color:#fff;margin-bottom:22px;">SAP BUSINESS DATA CLOUD</span>
  <p style="font-family:'Prompt',sans-serif;font-size:52px;font-weight:800;line-height:1.1;
             margin-bottom:24px;">A fundação com<br/>contexto de negócio</p>

  <div class="div" style="margin-bottom:26px;"></div>

  ${[
    'Inclui Datasphere + SAC + Databricks + Insight Apps pré-configurados',
    'Adiciona semântica de negócio — o dado não é só técnico, é contextualizado por processo',
    'Integração nativa com SAP AI Foundation para agentes e automação',
    'Pensado para que o dado vire decisão — não só relatório',
  ].map(t => `
  <div class="bullet">
    <div class="dot dot-teal"></div>
    <span class="btext">${t}</span>
  </div>`).join('')}

  <div style="margin-top:auto;">
    <div class="div" style="margin-bottom:18px;"></div>
    <p style="font-family:'Montserrat',sans-serif;font-size:18px;font-weight:600;
       color:rgba(255,255,255,0.45);">Em uma frase: é onde o dado <span style="color:#5de6c8;">serve pra decidir</span>.</p>
  </div>
</div>
`),

// ── 04 COMPARAÇÃO ─────────────────────────────────────────────────────────────
wrap('#0b1a2e', glowCTR, `
${H(4)}
<div class="body" style="gap:0;padding-top:22px;">

  <p style="font-family:'Montserrat',sans-serif;font-size:13px;font-weight:700;
     letter-spacing:2px;color:rgba(255,255,255,0.3);text-transform:uppercase;margin-bottom:20px;">
    A diferença que importa para quem decide
  </p>

  <!-- Table header -->
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px;margin-bottom:2px;">
    <div style="background:rgba(255,255,255,0.06);padding:14px 16px;border-radius:6px 0 0 0;"></div>
    <div style="background:#0057cc;padding:14px 16px;text-align:center;border-radius:0;">
      <span style="font-family:'Montserrat',sans-serif;font-size:14px;font-weight:700;color:#fff;">
        Datasphere
      </span>
    </div>
    <div style="background:#1BAD8D;padding:14px 16px;text-align:center;border-radius:0 6px 0 0;">
      <span style="font-family:'Montserrat',sans-serif;font-size:14px;font-weight:700;color:#fff;">
        SAP BDC
      </span>
    </div>
  </div>

  ${[
    ['O que é',    'Plataforma de dados',         'Fundação de dados + IA + insights'],
    ['Quem usa',   'Time de dados / TI',           'TI + Negócio + Agentes'],
    ['Output',     'Dado acessível',               'Decisão com contexto'],
    ['Quando ir',  'Ao estruturar o ambiente',     'Ao querer dado que vira ação'],
  ].map((row, i) => `
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px;margin-bottom:2px;">
    <div style="background:rgba(255,255,255,0.06);padding:14px 16px;display:flex;align-items:center;">
      <span style="font-family:'Montserrat',sans-serif;font-size:14px;font-weight:700;
            color:rgba(255,255,255,0.5);text-transform:uppercase;letter-spacing:1px;">${row[0]}</span>
    </div>
    <div style="background:rgba(0,87,204,0.15);padding:14px 16px;display:flex;align-items:center;justify-content:center;border:1px solid rgba(0,87,204,0.3);border-top:none;">
      <span style="font-family:'Montserrat',sans-serif;font-size:15px;font-weight:500;
            color:rgba(255,255,255,0.85);text-align:center;">${row[1]}</span>
    </div>
    <div style="background:rgba(27,173,141,0.15);padding:14px 16px;display:flex;align-items:center;justify-content:center;border:1px solid rgba(27,173,141,0.3);border-top:none;">
      <span style="font-family:'Montserrat',sans-serif;font-size:15px;font-weight:500;
            color:#5de6c8;text-align:center;">${row[2]}</span>
    </div>
  </div>`).join('')}

  <div style="margin-top:auto;padding-top:20px;">
    <div class="div" style="margin-bottom:16px;"></div>
    <p style="font-family:'Montserrat',sans-serif;font-size:15px;color:rgba(255,255,255,0.35);">
      Dados sem governança não viram IA confiável. Viram automação de erros.
    </p>
  </div>
</div>
`),

// ── 05 CTA ────────────────────────────────────────────────────────────────────
wrap('#0A0837', glowCTR + glowBR, `
${H(5)}
<div class="body" style="justify-content:center;gap:0;">

  <span class="tag" style="background:#006AFF;color:#fff;margin-bottom:28px;">QUAL USAR?</span>

  ${[
    { cond: 'Estruturando o ambiente de dados', rec: 'Comece com o Datasphere', color: '#0057cc' },
    { cond: 'Já tem Datasphere e quer ativar com IA', rec: 'SAP BDC é o próximo passo', color: '#1BAD8D' },
    { cond: 'Iniciando do zero com visão de longo prazo', rec: 'Vá direto ao BDC', color: '#1BAD8D' },
  ].map(s => `
  <div style="display:flex;gap:18px;align-items:flex-start;margin-bottom:24px;">
    <div style="flex-shrink:0;width:8px;height:8px;border-radius:50%;background:${s.color};margin-top:9px;"></div>
    <div>
      <p style="font-family:'Montserrat',sans-serif;font-size:16px;color:rgba(255,255,255,0.45);
         margin-bottom:4px;">${s.cond} →</p>
      <p style="font-family:'Prompt',sans-serif;font-size:26px;font-weight:700;
         color:${s.color === '#1BAD8D' ? '#5de6c8' : '#fff'};">${s.rec}</p>
    </div>
  </div>`).join('')}

  <div style="margin-top:24px;">
    <div class="div" style="margin-bottom:22px;"></div>
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <div>
        <p style="font-family:'Prompt',sans-serif;font-size:22px;font-weight:800;margin-bottom:4px;">
          solve<span style="color:#006AFF;">plan</span>
        </p>
        <p style="font-family:'Montserrat',sans-serif;font-size:13px;color:rgba(255,255,255,0.35);">
          Parceiro SAP Gold · +90 clientes
        </p>
      </div>
      <span style="font-family:'Montserrat',sans-serif;font-size:14px;font-weight:700;
            color:#5de6c8;">Fale comigo →</span>
    </div>
  </div>
</div>
`),

];

(async () => {
  const browser = await chromium.launch();
  for (const [i, html] of slides.entries()) {
    const page = await browser.newPage();
    await page.setViewportSize({ width: 1080, height: 1080 });
    await page.setContent(html, { waitUntil: 'networkidle' });
    const file = path.join(OUTPUT, `slide-${String(i + 1).padStart(2, '0')}.png`);
    await page.screenshot({ path: file, clip: { x: 0, y: 0, width: 1080, height: 1080 } });
    await page.close();
    console.log(`✓ slide-${String(i + 1).padStart(2, '0')}.png`);
  }
  await browser.close();
  console.log(`\n✅ ${slides.length} slides gerados em:\n${OUTPUT}`);
})();

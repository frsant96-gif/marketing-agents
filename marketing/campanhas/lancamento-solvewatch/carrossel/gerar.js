const { chromium } = require('playwright');
const path = require('path');
const fs   = require('fs');
const { wrap, glowBR, glowTR, glowTL, glowCTR, glowTeal, stripL, stripLfull, logo, hdr } = require('./shared');

const BASE   = 'c:/Users/franc/solveplan.com/Roberto Molina - Marketing/1. MKT Estrategy/3. Agentes de IA/ccos-ratos';
const OUTPUT = path.join(BASE.replace(/\//g, path.sep), 'marketing', 'campanhas', 'lancamento-solvewatch', 'carrossel', 'slides');
fs.mkdirSync(OUTPUT, { recursive: true });

const TOTAL = 7;
const H = (n) => hdr(n, TOTAL);

const slides = [

// ── 01 CAPA ──────────────────────────────────────────────────────────────────
wrap('#0A0837', glowBR + glowTR + stripL, `
${H(1)}
<div class="body" style="justify-content:flex-start;padding-top:50px;">

  <span class="tag" style="background:#006AFF;color:#fff;margin-bottom:28px;">LANÇAMENTO SOLVE WATCH</span>
  <div class="bar" style="margin-bottom:28px;"></div>

  <p style="font-family:'Prompt',sans-serif;font-size:64px;font-weight:800;line-height:1.12;margin-bottom:18px;">
    Seu Datasphere<br/>
    está em produção.<br/>
    <span class="accent">Quem está cuidando<br/>dele?</span>
  </p>

  <div style="margin-top:auto;">
    <div class="div" style="margin-bottom:18px;"></div>
    <p style="font-family:'Montserrat',sans-serif;font-size:18px;font-weight:500;
       color:rgba(255,255,255,0.45);">4 dores que aparecem depois do go-live →</p>
  </div>
</div>
`),

// ── 02 CONTEXTO ───────────────────────────────────────────────────────────────
wrap('#0A0837', glowTL + stripLfull, `
${H(2)}
<div class="body" style="gap:0;justify-content:center;">

  <span class="tag" style="background:rgba(255,255,255,0.08);color:#fff;margin-bottom:22px;">DEPOIS DO GO-LIVE</span>
  <p style="font-family:'Prompt',sans-serif;font-size:44px;font-weight:800;line-height:1.15;
             margin-bottom:24px;">O desafio muda<br/>de figura.</p>

  <div class="div" style="margin-bottom:26px;"></div>

  <p style="font-family:'Montserrat',sans-serif;font-size:20px;font-weight:500;line-height:1.6;color:rgba(255,255,255,0.75);">
    Não é mais sobre implementar. É sobre manter o ambiente saudável, previsível e pronto pra evoluir — todos os dias, sem parar.
  </p>
</div>
`),

// ── 03 CONFIABILIDADE ─────────────────────────────────────────────────────────
wrap('#0b1a2e', glowCTR, `
${H(3)}
<div class="body" style="gap:0;justify-content:center;">

  <span class="tag" style="background:#0057cc;color:#fff;margin-bottom:22px;">CONFIABILIDADE</span>
  <p style="font-family:'Prompt',sans-serif;font-size:44px;font-weight:800;line-height:1.15;
             margin-bottom:24px;">A carga falha<br/>de madrugada.</p>

  <div class="div" style="margin-bottom:26px;"></div>

  <p style="font-family:'Montserrat',sans-serif;font-size:20px;font-weight:500;line-height:1.6;color:rgba(255,255,255,0.75);">
    O negócio descobre primeiro — antes de qualquer alerta chegar pra quem cuida do ambiente.
  </p>
</div>
`),

// ── 04 CUSTOS ─────────────────────────────────────────────────────────────────
wrap('linear-gradient(160deg,#0A0837 0%,#0d2240 100%)', glowTeal + stripLfull, `
${H(4)}
<div class="body" style="gap:0;justify-content:center;">

  <span class="tag" style="background:#1BAD8D;color:#fff;margin-bottom:22px;">CUSTOS</span>
  <p style="font-family:'Prompt',sans-serif;font-size:44px;font-weight:800;line-height:1.15;
             margin-bottom:24px;">O consumo cresce<br/>em silêncio.</p>

  <div class="div" style="margin-bottom:26px;"></div>

  <p style="font-family:'Montserrat',sans-serif;font-size:20px;font-weight:500;line-height:1.6;color:rgba(255,255,255,0.75);">
    A fatura, não. E quando alguém percebe, já é tarde pra agir com previsibilidade sobre as Capacity Units.
  </p>
</div>
`),

// ── 05 GOVERNANÇA ─────────────────────────────────────────────────────────────
wrap('#0A0837', glowTR + stripLfull, `
${H(5)}
<div class="body" style="gap:0;justify-content:center;">

  <span class="tag" style="background:rgba(255,255,255,0.08);color:#fff;margin-bottom:22px;">GOVERNANÇA</span>
  <p style="font-family:'Prompt',sans-serif;font-size:44px;font-weight:800;line-height:1.15;
             margin-bottom:24px;">Várias mãos<br/>construíram o<br/>ambiente.</p>

  <div class="div" style="margin-bottom:26px;"></div>

  <p style="font-family:'Montserrat',sans-serif;font-size:20px;font-weight:500;line-height:1.6;color:rgba(255,255,255,0.75);">
    Times diferentes, fornecedores diferentes — e ninguém enxerga o todo.
  </p>
</div>
`),

// ── 06 PRONTIDÃO PARA IA ──────────────────────────────────────────────────────
wrap('#0b1a2e', glowCTR + glowTeal, `
${H(6)}
<div class="body" style="gap:0;justify-content:center;">

  <span class="tag" style="background:#006AFF;color:#fff;margin-bottom:22px;">PRONTIDÃO PARA IA</span>
  <p style="font-family:'Prompt',sans-serif;font-size:44px;font-weight:800;line-height:1.15;
             margin-bottom:24px;">A IA não gera<br/>valor sozinha.</p>

  <div class="div" style="margin-bottom:26px;"></div>

  <p style="font-family:'Montserrat',sans-serif;font-size:20px;font-weight:500;line-height:1.6;color:rgba(255,255,255,0.75);">
    Sem contexto e sem governança nos dados, todo investimento em IA fica raso.
  </p>
</div>
`),

// ── 07 CTA ────────────────────────────────────────────────────────────────────
wrap('#0A0837', glowCTR + glowBR, `
${H(7)}
<div class="body" style="justify-content:center;gap:0;">

  <span class="tag" style="background:#006AFF;color:#fff;margin-bottom:28px;">SOLVE WATCH</span>

  <p style="font-family:'Prompt',sans-serif;font-size:40px;font-weight:800;line-height:1.2;margin-bottom:18px;">
    Gestão inteligente e<br/>contínua do SAP Datasphere.
  </p>

  <div class="div" style="margin-bottom:22px;"></div>

  <p style="font-family:'Montserrat',sans-serif;font-size:20px;font-weight:600;color:#5de6c8;margin-bottom:36px;">
    Seu Datasphere sob gestão.<br/>Seus dados prontos para IA.
  </p>

  <div style="margin-top:auto;">
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
            color:#5de6c8;">Solicitar avaliação →</span>
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

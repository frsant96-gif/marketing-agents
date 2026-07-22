const { chromium } = require('playwright');
const path = require('path');
const fs   = require('fs');
const { glowBR, glowTR, glowCTR, glowTeal, logo } = require('./shared');

const BASE   = 'c:/Users/franc/solveplan.com/Roberto Molina - Marketing/1. MKT Estrategy/3. Agentes de IA/ccos-ratos';
const OUTPUT = path.join(BASE.replace(/\//g, path.sep), 'marketing', 'campanhas', 'lancamento-solvewatch', 'hero-lp', 'slides');
fs.mkdirSync(OUTPUT, { recursive: true });

const W = 1600, H = 900;

const fonts = `<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">`;

const tiles = [
  { label: 'IDENTIFICA', bg: '#FFFFFF',  color: '#0A0837' },
  { label: 'ATUA',       bg: '#FF6A2B',  color: '#FFFFFF' },
  { label: 'ALERTA',     bg: '#EDEFF3',  color: '#0A0837' },
  { label: 'GESTÃO',     bg: '#B9C0CC',  color: '#0A0837' },
  { label: 'CUSTOS',     bg: '#0A0E19',  color: '#FFFFFF' },
  { label: 'RISCOS',     bg: '#7B8794',  color: '#FFFFFF' },
];

const cube = `
<div style="display:grid;grid-template-columns:repeat(3,120px);grid-template-rows:repeat(2,120px);gap:4px;transform:rotate(-6deg) skewY(-3deg);box-shadow:0 40px 80px rgba(0,0,0,0.45);">
  ${tiles.map(t => `
  <div style="background:${t.bg};color:${t.color};display:flex;align-items:center;justify-content:center;
       font-family:'Montserrat',sans-serif;font-weight:700;font-size:13px;letter-spacing:0.5px;
       border-radius:4px;text-align:center;">
    ${t.label}
  </div>`).join('')}
</div>`;

const html = `<!DOCTYPE html><html><head><meta charset="UTF-8">${fonts}
<style>
  *{margin:0;padding:0;box-sizing:border-box;}
  body{width:${W}px;height:${H}px;overflow:hidden;font-family:'Montserrat',sans-serif;color:#fff;
       position:relative;background:#0A0E19;}
  .glow{position:absolute;border-radius:50%;pointer-events:none;z-index:1;}
  .wrap{position:relative;z-index:2;display:flex;align-items:center;justify-content:space-between;
        height:100%;padding:0 90px;}
  .left{max-width:760px;}
  .badge{display:inline-block;font-family:'Montserrat',sans-serif;font-size:12px;font-weight:700;
         letter-spacing:1.6px;padding:7px 16px;border-radius:4px;text-transform:uppercase;
         background:#006AFF;color:#fff;margin-bottom:26px;}
  h1{font-family:'Prompt',sans-serif;font-size:52px;font-weight:800;line-height:1.15;margin-bottom:22px;}
  h1 .accent{color:#5de6c8;}
  p.sub{font-family:'Montserrat',sans-serif;font-size:19px;font-weight:500;line-height:1.6;
        color:rgba(255,255,255,0.75);max-width:600px;margin-bottom:36px;}
  .cta{display:inline-block;background:#006AFF;color:#fff;font-family:'Montserrat',sans-serif;
       font-weight:700;font-size:16px;padding:16px 32px;border-radius:6px;margin-bottom:20px;}
  .trust{font-family:'Montserrat',sans-serif;font-size:13px;color:rgba(255,255,255,0.4);}
  .headerlogo{position:absolute;top:40px;left:90px;z-index:3;}
</style></head><body>
${glowBR}${glowTeal}
<div class="headerlogo">${logo}</div>
<div class="wrap">
  <div class="left">
    <span class="badge">LANÇAMENTO SOLVE WATCH</span>
    <h1>Seu SAP Datasphere entrou em produção.<br/><span class="accent">Agora começa o verdadeiro desafio.</span></h1>
    <p class="sub">A carga falha de madrugada. O consumo cresce em silêncio. Ninguém cuida do ambiente como um todo. O Solve Watch identifica, alerta e prioriza — antes que o negócio sinta.</p>
    <div class="cta">Solicitar avaliação do ambiente →</div>
    <div class="trust">Parceiro SAP Gold · Melhor Parceiro SAP Business Data Cloud 2026 — América Latina</div>
  </div>
  <div style="flex-shrink:0;">${cube}</div>
</div>
</body></html>`;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: W, height: H });
  await page.setContent(html, { waitUntil: 'networkidle' });
  const file = path.join(OUTPUT, 'hero-lp.png');
  await page.screenshot({ path: file, clip: { x: 0, y: 0, width: W, height: H } });
  await page.close();
  await browser.close();
  console.log(`✅ hero-lp.png gerado em:\n${file}`);
})();

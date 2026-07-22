const { chromium } = require('playwright');
const path = require('path');
const fs   = require('fs');
const { logo } = require('./shared');

const BASE   = 'c:/Users/franc/solveplan.com/Roberto Molina - Marketing/1. MKT Estrategy/3. Agentes de IA/ccos-ratos';
const OUTPUT = path.join(BASE.replace(/\//g, path.sep), 'marketing', 'campanhas', 'lancamento-solvewatch', 'hero-lp', 'slides');
fs.mkdirSync(OUTPUT, { recursive: true });

const W = 1600, H = 900;
const S = 220; // cube side

const fonts = `<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">`;

// True 3D cube: top face split 2x2 (Identifica/Alerta/Gestão/Riscos), front face Custos, right face Atua
const cube = `
<div class="scene">
  <div class="cube">
    <div class="face top">
      <div class="quad" style="background:#F4F6FA;color:#0A0837;">IDENTIFICA</div>
      <div class="quad" style="background:#E3E7EE;color:#0A0837;">ALERTA</div>
      <div class="quad" style="background:#CBD2DC;color:#0A0837;">GESTÃO</div>
      <div class="quad" style="background:#AEB7C4;color:#0A0837;">RISCOS</div>
    </div>
    <div class="face front">CUSTOS</div>
    <div class="face right">ATUA</div>
  </div>
</div>`;

const html = `<!DOCTYPE html><html><head><meta charset="UTF-8">${fonts}
<style>
  *{margin:0;padding:0;box-sizing:border-box;}
  body{width:${W}px;height:${H}px;overflow:hidden;font-family:'Montserrat',sans-serif;color:#fff;
       position:relative;background:#0A0E19;}

  .wrap{position:relative;z-index:2;display:flex;align-items:center;justify-content:space-between;
        height:100%;padding:0 100px;}
  .left{max-width:660px;}
  .eyebrow{display:flex;align-items:center;gap:12px;margin-bottom:32px;}
  .eyebrow .bar{width:36px;height:2px;background:#006AFF;}
  .eyebrow span{font-family:'Montserrat',sans-serif;font-size:12px;font-weight:700;
         letter-spacing:2.5px;text-transform:uppercase;color:rgba(255,255,255,0.5);}
  h1{font-family:'Prompt',sans-serif;font-size:46px;font-weight:800;line-height:1.22;margin-bottom:24px;
     letter-spacing:-0.5px;}
  h1 .accent{color:#006AFF;}
  p.sub{font-family:'Montserrat',sans-serif;font-size:18px;font-weight:400;line-height:1.65;
        color:rgba(255,255,255,0.6);max-width:520px;margin-bottom:40px;}
  .cta-row{display:flex;align-items:center;gap:24px;margin-bottom:56px;}
  .cta{display:inline-block;background:#006AFF;color:#fff;font-family:'Montserrat',sans-serif;
       font-weight:600;font-size:15px;padding:15px 30px;border-radius:4px;}
  .trust{font-family:'Montserrat',sans-serif;font-size:13px;color:rgba(255,255,255,0.35);
         padding-top:24px;border-top:1px solid rgba(255,255,255,0.08);}
  .headerlogo{position:absolute;top:48px;left:100px;z-index:3;}

  /* ── cube ── */
  .scene{flex-shrink:0;width:520px;height:520px;display:flex;align-items:center;justify-content:center;
         perspective:1400px;}
  .cube{position:relative;width:${S}px;height:${S}px;transform-style:preserve-3d;
        transform:rotateX(-28deg) rotateY(38deg);}
  .face{position:absolute;width:${S}px;height:${S}px;display:flex;align-items:center;justify-content:center;
        font-family:'Montserrat',sans-serif;font-weight:700;font-size:15px;letter-spacing:0.5px;}
  .top{background:#fff;transform:rotateX(90deg) translateZ(${S/2}px);
       display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:2px;
       background:rgba(255,255,255,0.15);}
  .quad{display:flex;align-items:center;justify-content:center;font-size:14px;}
  .front{background:#0A0E19;border:1px solid rgba(255,255,255,0.08);transform:translateZ(${S/2}px);color:#fff;}
  .right{background:#FF6A2B;transform:rotateY(-90deg) translateZ(${S/2}px);color:#fff;}
</style></head><body>
<div class="headerlogo">${logo}</div>
<div class="wrap">
  <div class="left">
    <div class="eyebrow"><div class="bar"></div><span>Lançamento Solve Watch</span></div>
    <h1>Seu SAP Datasphere entrou em produção.<br/>Agora começa <span class="accent">o verdadeiro desafio.</span></h1>
    <p class="sub">A carga falha de madrugada. O consumo cresce em silêncio. Ninguém cuida do ambiente como um todo. O Solve Watch identifica, alerta e prioriza — antes que o negócio sinta.</p>
    <div class="cta-row">
      <div class="cta">Solicitar avaliação do ambiente →</div>
    </div>
    <div class="trust">Parceiro SAP Gold · Melhor Parceiro SAP Business Data Cloud 2026 — América Latina</div>
  </div>
  ${cube}
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

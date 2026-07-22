const { chromium } = require('playwright');
const path = require('path');
const fs   = require('fs');
const { logo } = require('./shared');

const BASE   = 'c:/Users/franc/solveplan.com/Roberto Molina - Marketing/1. MKT Estrategy/3. Agentes de IA/ccos-ratos';
const OUTPUT = path.join(BASE.replace(/\//g, path.sep), 'marketing', 'campanhas', 'lancamento-solvewatch', 'hero-lp', 'slides');
fs.mkdirSync(OUTPUT, { recursive: true });

const W = 1600, H = 900;
const S = 190; // cube side
const HUB = { x: 1300, y: 500 };

const fonts = `<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">`;

// ── Concept: rede caótica (ambiente sem gestão, vermelho) que se organiza
// e converge pro cubo do Solve Watch (hub azul), à direita. ──────────────

function rand(min, max) { return min + Math.random() * (max - min); }

// Zona caótica — nós espalhados, cor vermelho/laranja apagado
const chaosNodes = [];
for (let i = 0; i < 46; i++) {
  chaosNodes.push({
    x: rand(70, 880),
    y: rand(420, 860),
    r: rand(2, 5),
    c: Math.random() > 0.5 ? '#ff5757' : '#ff8a3d',
    o: rand(0.25, 0.65),
  });
}
// linhas caóticas conectando nós próximos, cruzando-se
const chaosEdges = [];
for (let i = 0; i < chaosNodes.length; i++) {
  const a = chaosNodes[i];
  const others = chaosNodes
    .map((b, j) => ({ b, j, d: Math.hypot(a.x - b.x, a.y - b.y) }))
    .filter(o => o.j !== i && o.d < 180)
    .sort((x, y) => x.d - y.d)
    .slice(0, 2);
  others.forEach(o => chaosEdges.push({ a, b: o.b }));
}

// Zona organizada — grid limpo, azul/teal, convergindo pro hub
const orderNodes = [];
const cols = 5, rows = 4;
for (let c = 0; c < cols; c++) {
  for (let r = 0; r < rows; r++) {
    orderNodes.push({
      x: 950 + c * 62,
      y: 400 + r * 90,
      r: 3.5,
      c: '#5de6c8',
    });
  }
}
// cada nó da grade se conecta em linha reta ao hub
const orderEdges = orderNodes.map(n => ({ a: n, b: HUB }));

// nós de transição ligando o caos à ordem (gradiente vermelho → azul)
const bridgeEdges = [];
for (let i = 0; i < 10; i++) {
  const a = chaosNodes[Math.floor(rand(0, chaosNodes.length))];
  const b = orderNodes[Math.floor(rand(0, orderNodes.length))];
  bridgeEdges.push({ a, b });
}

const svgLines = (edges, stroke, opacity, dash = '') => edges.map(e =>
  `<line x1="${e.a.x}" y1="${e.a.y}" x2="${e.b.x}" y2="${e.b.y}" stroke="${stroke}" stroke-width="1" opacity="${opacity}" ${dash}/>`
).join('');

const svgDots = (nodes) => nodes.map(n =>
  `<circle cx="${n.x}" cy="${n.y}" r="${n.r}" fill="${n.c}" opacity="${n.o ?? 0.9}"/>`
).join('');

const network = `
<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" style="position:absolute;top:0;left:0;z-index:1;">
  <defs>
    <linearGradient id="bridge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ff5757"/>
      <stop offset="100%" stop-color="#5de6c8"/>
    </linearGradient>
  </defs>
  ${svgLines(chaosEdges, '#ff5757', 0.18)}
  ${bridgeEdges.map(e => `<line x1="${e.a.x}" y1="${e.a.y}" x2="${e.b.x}" y2="${e.b.y}" stroke="url(#bridge)" stroke-width="1" opacity="0.35"/>`).join('')}
  ${svgLines(orderEdges, '#5de6c8', 0.3)}
  <circle cx="${HUB.x}" cy="${HUB.y}" r="150" fill="none" stroke="#006AFF" stroke-width="1" opacity="0.25"/>
  <circle cx="${HUB.x}" cy="${HUB.y}" r="200" fill="none" stroke="#006AFF" stroke-width="1" opacity="0.14"/>
  ${svgDots(chaosNodes)}
  ${svgDots(orderNodes)}
</svg>`;

// True 3D cube: top face split 2x2 (Identifica/Alerta/Gestão/Riscos), front face Custos, right face Atua
const cube = `
<div class="scene" style="left:${HUB.x - 260}px;top:${HUB.y - 260}px;">
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
       position:relative;background:#05070c;}

  .headerlogo{position:absolute;top:48px;left:100px;z-index:3;}

  .copy{position:absolute;top:150px;left:100px;z-index:3;max-width:640px;}
  .eyebrow{display:flex;align-items:center;gap:12px;margin-bottom:28px;}
  .eyebrow .bar{width:36px;height:2px;background:#ff5757;}
  .eyebrow span{font-family:'Montserrat',sans-serif;font-size:12px;font-weight:700;
         letter-spacing:2.5px;text-transform:uppercase;color:rgba(255,255,255,0.5);}
  h1{font-family:'Prompt',sans-serif;font-size:50px;font-weight:800;line-height:1.18;margin-bottom:22px;
     letter-spacing:-0.5px;}
  h1 .fade{color:rgba(255,255,255,0.28);}
  p.sub{font-family:'Montserrat',sans-serif;font-size:17px;font-weight:400;line-height:1.65;
        color:rgba(255,255,255,0.55);max-width:460px;}

  .bottom{position:absolute;left:100px;bottom:64px;z-index:3;}
  .cta{display:inline-flex;align-items:center;gap:10px;background:#006AFF;color:#fff;
       font-family:'Montserrat',sans-serif;font-weight:600;font-size:15px;padding:15px 28px;border-radius:4px;
       margin-bottom:18px;}
  .trust{font-family:'Montserrat',sans-serif;font-size:12.5px;color:rgba(255,255,255,0.32);}

  .hubtag{position:absolute;z-index:3;left:${HUB.x - 66}px;top:${HUB.y + 168}px;
          font-family:'Montserrat',sans-serif;font-size:12px;font-weight:700;letter-spacing:2px;
          color:#5de6c8;text-transform:uppercase;}

  /* ── cube ── */
  .scene{position:absolute;width:520px;height:520px;display:flex;align-items:center;justify-content:center;
         perspective:1400px;z-index:2;}
  .cube{position:relative;width:${S}px;height:${S}px;transform-style:preserve-3d;
        transform:rotateX(-28deg) rotateY(38deg);}
  .face{position:absolute;width:${S}px;height:${S}px;display:flex;align-items:center;justify-content:center;
        font-family:'Montserrat',sans-serif;font-weight:700;font-size:13px;letter-spacing:0.5px;}
  .top{transform:rotateX(90deg) translateZ(${S/2}px);
       display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:2px;
       background:rgba(255,255,255,0.15);}
  .quad{display:flex;align-items:center;justify-content:center;font-size:12px;}
  .front{background:#0A0E19;border:1px solid rgba(255,255,255,0.08);transform:translateZ(${S/2}px);color:#fff;}
  .right{background:#FF6A2B;transform:rotateY(-90deg) translateZ(${S/2}px);color:#fff;}
</style></head><body>
${network}
<div class="headerlogo">${logo}</div>
<div class="copy">
  <div class="eyebrow"><div class="bar"></div><span>Lançamento Solve Watch</span></div>
  <h1>Seu SAP Datasphere<br/>entrou em produção.<br/><span class="fade">Ninguém cuida do resto.</span></h1>
  <p class="sub">Falha que ninguém vê a tempo. Custo que cresce sem explicação. Ambiente sem dono. O Solve Watch organiza esse caos — identifica, alerta e prioriza antes que o negócio sinta.</p>
</div>
${cube}
<div class="hubtag">Solve Watch</div>
<div class="bottom">
  <div class="cta">Solicitar avaliação do ambiente →</div>
  <div class="trust">Parceiro SAP Gold · Melhor Parceiro SAP BDC 2026</div>
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

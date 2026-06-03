const { chromium } = require('playwright');
const path = require('path');
const fs   = require('fs');
const { wrap, glowBR, glowTR, glowTL, glowCTR, glowTeal, stripL, stripLfull, logo, hdr } = require('../shared');

const BASE   = 'c:/Users/franc/solveplan.com/Roberto Molina - Marketing/1. MKT Estrategy/3. Agentes de IA/ccos-ratos';
const OUTPUT = path.join(BASE.replace(/\//g, path.sep), 'marketing', 'criativos', 'junho-2026', '03-jornada-bdc', 'slides');
fs.mkdirSync(OUTPUT, { recursive: true });

const TOTAL = 6;
const H = (n) => hdr(n, TOTAL);

const etapas = [
  {
    num: '01',
    name: 'Assessment',
    time: '4 — 6 semanas',
    acontece: 'Mapeamos o estado atual do ambiente de dados — fontes, qualidade, governança e lacunas.',
    recebe: 'Diagnóstico claro de onde você está, o que precisa resolver e um roadmap priorizado por impacto.',
    color: '#006AFF',
  },
  {
    num: '02',
    name: 'Fundação de dados',
    time: '3 — 6 meses',
    acontece: 'Estruturamos o ambiente base — Datasphere, dados mestre, governança inicial e integração das fontes prioritárias.',
    recebe: 'Ambiente de dados operacional, com dado confiável chegando nas áreas certas e rastreabilidade estabelecida.',
    color: '#4A6BFF',
  },
  {
    num: '03',
    name: 'Ativação do SAP BDC',
    time: '2 — 4 meses',
    acontece: 'Ativamos a semântica de negócio, Insight Apps e integração com SAC e AI Foundation.',
    recebe: 'Dado que vira decisão — dashboards executivos, planejamento integrado, base pronta para agentes Joule.',
    color: '#1BAD8D',
  },
  {
    num: '04',
    name: 'Resultado sustentável',
    time: 'Contínuo (AMS)',
    acontece: 'AMS, melhoria contínua e evolução de modelos conforme o negócio muda.',
    recebe: 'Ambiente que cresce com a empresa — não que precisa ser refeito a cada mudança de processo.',
    color: '#5de6c8',
  },
];

// ── Slide 1: CAPA ─────────────────────────────────────────────────────────────
const capa = wrap('#0A0837', glowBR + glowTR + stripL, `
${H(1)}
<div class="body" style="justify-content:flex-start;padding-top:48px;">
  <span class="tag" style="background:#1BAD8D;color:#fff;margin-bottom:26px;">24 DE JUNHO · SAP BDC</span>
  <div class="bar" style="background:#1BAD8D;margin-bottom:26px;"></div>

  <p style="font-family:'Prompt',sans-serif;font-size:72px;font-weight:800;line-height:1.05;margin-bottom:20px;">
    Da implementação SAP<br/>ao <span style="color:#5de6c8;">SAP BDC</span>
  </p>

  <p style="font-family:'Montserrat',sans-serif;font-size:26px;font-weight:500;
     line-height:1.4;color:rgba(255,255,255,0.55);margin-bottom:0;">
    O que muda em cada etapa —<br/>e o que esperar
  </p>

  <div style="margin-top:auto;">
    <div class="div" style="margin-bottom:18px;"></div>

    <!-- Mini timeline indicator -->
    <div style="display:flex;gap:12px;align-items:center;">
      ${['Assessment','Fundação','Ativação BDC','Resultado'].map((s, i) => `
      <div style="display:flex;align-items:center;gap:8px;">
        <div style="width:10px;height:10px;border-radius:50%;
             background:${['#006AFF','#4A6BFF','#1BAD8D','#5de6c8'][i]};"></div>
        <span style="font-family:'Montserrat',sans-serif;font-size:13px;
              color:rgba(255,255,255,0.35);">${s}</span>
        ${i < 3 ? '<div style="width:20px;height:1px;background:rgba(255,255,255,0.15);"></div>' : ''}
      </div>`).join('')}
    </div>
  </div>
</div>
`);

// ── Slides 2-5: Etapas ────────────────────────────────────────────────────────
const etapaSlides = etapas.map((e, i) => wrap(
  'linear-gradient(150deg,#0A0837 0%,#091525 100%)',
  glowTL + stripLfull,
  `
  ${H(i + 2)}
  <div class="body" style="gap:0;padding-top:28px;">

    <!-- Header da etapa -->
    <div style="display:flex;align-items:center;gap:16px;margin-bottom:10px;">
      <div style="width:52px;height:52px;border-radius:50%;background:${e.color};
           display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <span style="font-family:'Prompt',sans-serif;font-size:22px;font-weight:800;
              color:#fff;">${e.num}</span>
      </div>
      <div>
        <p style="font-family:'Montserrat',sans-serif;font-size:11px;font-weight:700;
           letter-spacing:2px;color:rgba(255,255,255,0.3);text-transform:uppercase;
           margin-bottom:4px;">ETAPA ${e.num}</p>
        <p style="font-family:'Prompt',sans-serif;font-size:40px;font-weight:800;
           line-height:1;color:#fff;">${e.name}</p>
      </div>
    </div>

    <!-- Tempo badge -->
    <div style="display:inline-flex;align-items:center;gap:8px;margin-bottom:22px;
         background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);
         border-radius:20px;padding:8px 16px;align-self:flex-start;">
      <div style="width:6px;height:6px;border-radius:50%;background:${e.color};"></div>
      <span style="font-family:'Montserrat',sans-serif;font-size:14px;font-weight:600;
            color:rgba(255,255,255,0.6);">Tempo médio: ${e.time}</span>
    </div>

    <div class="div" style="margin-bottom:22px;"></div>

    <!-- O que acontece -->
    <div style="margin-bottom:18px;">
      <p style="font-family:'Montserrat',sans-serif;font-size:11px;font-weight:700;
         letter-spacing:2px;color:rgba(255,255,255,0.3);text-transform:uppercase;
         margin-bottom:12px;">O QUE ACONTECE</p>
      <p style="font-family:'Montserrat',sans-serif;font-size:19px;font-weight:500;
         line-height:1.6;color:rgba(255,255,255,0.7);">${e.acontece}</p>
    </div>

    <!-- O que você recebe -->
    <div style="background:rgba(${e.color === '#5de6c8' ? '93,230,200' : '0,106,255'},0.08);
         border:1px solid rgba(${e.color === '#5de6c8' ? '93,230,200' : '0,106,255'},0.2);
         border-radius:10px;padding:20px 22px;margin-top:auto;">
      <p style="font-family:'Montserrat',sans-serif;font-size:11px;font-weight:700;
         letter-spacing:2px;color:${e.color};text-transform:uppercase;margin-bottom:12px;">
         O QUE VOCÊ RECEBE</p>
      <p style="font-family:'Montserrat',sans-serif;font-size:19px;font-weight:500;
         line-height:1.6;color:rgba(255,255,255,0.9);">${e.recebe}</p>
    </div>
  </div>
  `
));

// ── Slide 6: CTA ──────────────────────────────────────────────────────────────
const cta = wrap('#0A0837', glowCTR + glowTeal, `
${H(6)}
<div class="body" style="justify-content:center;gap:0;">

  <p style="font-family:'Prompt',sans-serif;font-size:56px;font-weight:800;line-height:1.1;
     margin-bottom:24px;">
    A jornada não precisa<br/>ser feita de uma vez.<br/>
    <span style="color:rgba(255,255,255,0.35);">O que não pode acontecer</span><br/>
    <span style="color:#5de6c8;">é não começar.</span>
  </p>

  <div class="div" style="margin-bottom:26px;"></div>

  <!-- Mini roadmap dots -->
  <div style="display:flex;gap:0;align-items:center;margin-bottom:28px;">
    ${[
      { label: 'Assessment', color: '#006AFF' },
      { label: 'Fundação', color: '#4A6BFF' },
      { label: 'Ativação BDC', color: '#1BAD8D' },
      { label: 'Resultado', color: '#5de6c8' },
    ].map((s, i, arr) => `
    <div style="display:flex;flex-direction:column;align-items:center;flex:1;">
      <div style="width:14px;height:14px;border-radius:50%;background:${s.color};"></div>
      <p style="font-family:'Montserrat',sans-serif;font-size:12px;font-weight:600;
         color:rgba(255,255,255,0.4);margin-top:8px;text-align:center;">${s.label}</p>
    </div>
    ${i < arr.length - 1 ? '<div style="flex:1;height:2px;background:rgba(255,255,255,0.1);margin-bottom:20px;"></div>' : ''}`
    ).join('')}
  </div>

  <div style="display:flex;align-items:center;justify-content:space-between;">
    <div>
      <p style="font-family:'Prompt',sans-serif;font-size:24px;font-weight:800;margin-bottom:4px;">
        solve<span style="color:#006AFF;">plan</span>
      </p>
      <p style="font-family:'Montserrat',sans-serif;font-size:12px;color:rgba(255,255,255,0.3);">
        Parceiro SAP Gold · +90 clientes · +13 anos · América Latina
      </p>
    </div>
    <span style="font-family:'Montserrat',sans-serif;font-size:14px;font-weight:700;
          color:#5de6c8;border:1px solid rgba(93,230,200,0.35);padding:12px 20px;border-radius:8px;">
      Fale comigo →
    </span>
  </div>
</div>
`);

const slides = [capa, ...etapaSlides, cta];

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

const { chromium } = require('playwright');
const path = require('path');
const fs   = require('fs');
const { wrap, glowBR, glowTR, glowTL, glowCTR, glowTeal, stripL, stripLfull, logo, hdr } = require('../shared');

const BASE   = 'c:/Users/franc/solveplan.com/Roberto Molina - Marketing/1. MKT Estrategy/3. Agentes de IA/ccos-ratos';
const OUTPUT = path.join(BASE.replace(/\//g, path.sep), 'marketing', 'criativos', 'junho-2026', '02-5-dores-fpa', 'slides');
fs.mkdirSync(OUTPUT, { recursive: true });

const TOTAL = 7;
const H = (n) => hdr(n, TOTAL);

const dores = [
  {
    num: '01',
    title: 'O ciclo de fechamento\né longo demais',
    dor: 'Semanas consolidando dados de múltiplas fontes. Cada área tem uma versão diferente do mesmo número. O relatório sai quando a decisão já foi tomada.',
    bdc: 'Integra todas as fontes com semântica unificada. O fechamento começa com o dado já consolidado — não com reconciliação.',
    icon: '⏱',
  },
  {
    num: '02',
    title: 'Planejamento\nvive em Excel',
    dor: 'Modelos que quebram quando alguém abre errado. Versões em pastas diferentes, sem controle. Ninguém sabe qual planilha é a oficial.',
    bdc: 'Substitui o Excel como sistema de planejamento por um ambiente governado, com trilha de auditoria e versão única da verdade.',
    icon: '📊',
  },
  {
    num: '03',
    title: 'Dado que existe\nmas ninguém confia',
    dor: 'Divergências entre o que o ERP mostra e o que as áreas reportam. Mesmo cliente cadastrado de formas diferentes. Qual número é o certo?',
    bdc: 'Master Data Governance integrado — dado mestre unificado, validado, com política de qualidade centralizada e rastreável.',
    icon: '⚠',
  },
  {
    num: '04',
    title: 'Sem visibilidade\nde custos de plataforma',
    dor: 'A empresa usa SAP Datasphere mas não sabe onde está consumindo recursos. Cargas que custam mais do que deveriam. Nenhuma previsibilidade.',
    bdc: 'Visibilidade nativa de consumo de Capacity Units — com histórico e projeção de custo antes do invoice.',
    icon: '💸',
  },
  {
    num: '05',
    title: 'IA sem fundação\nde dados pronta',
    dor: 'A empresa quer agentes SAP, mas os dados não estão preparados. IA sobre dado fragmentado consolida erros mais rápido do que qualquer time corrige.',
    bdc: 'É a camada de dados governados e contextualizados que transforma automação genérica em automação confiável.',
    icon: '🤖',
  },
];

// ── Slide 1: CAPA ─────────────────────────────────────────────────────────────
const capa = wrap('#0A0837', glowBR + glowTR + stripL, `
${H(1)}
<div class="body" style="justify-content:flex-start;padding-top:44px;">
  <span class="tag" style="background:#6B3BE8;color:#fff;margin-bottom:26px;">17 DE JUNHO · FP&A</span>
  <div class="bar" style="background:#6B3BE8;margin-bottom:26px;"></div>

  <p style="font-family:'Prompt',sans-serif;font-size:82px;font-weight:800;line-height:1.03;margin-bottom:20px;">
    5 dores de dados<br/>que travam o<br/><span style="color:#6B3BE8;">FP&A</span>
  </p>

  <div style="margin-top:auto;">
    <div class="div" style="margin-bottom:18px;"></div>
    <p style="font-family:'Montserrat',sans-serif;font-size:20px;font-weight:500;
       color:rgba(255,255,255,0.45);">
      e o que o SAP BDC faz por cada uma →
    </p>
  </div>
</div>
`);

// ── Slides 2-6: Cada Dor ───────────────────────────────────────────────────────
const dorSlides = dores.map((d, i) => wrap(
  'linear-gradient(160deg,#0A0837 0%,#110a2e 100%)',
  glowTL + stripLfull,
  `
  ${H(i + 2)}
  <div class="body" style="gap:0;padding-top:24px;">

    <!-- Number -->
    <p style="font-family:'Prompt',sans-serif;font-size:100px;font-weight:800;line-height:1;
       color:rgba(107,59,232,0.22);margin-bottom:-30px;margin-left:-4px;">${d.num}</p>

    <!-- Title -->
    <p style="font-family:'Prompt',sans-serif;font-size:54px;font-weight:800;line-height:1.1;
       white-space:pre-line;margin-bottom:26px;position:relative;z-index:1;">${d.title}</p>

    <!-- Dor -->
    <div style="background:rgba(220,50,50,0.1);border:1px solid rgba(220,50,50,0.25);
         border-radius:10px;padding:18px 20px;margin-bottom:16px;">
      <p style="font-family:'Montserrat',sans-serif;font-size:11px;font-weight:700;
         letter-spacing:2px;color:rgba(220,100,100,0.8);text-transform:uppercase;
         margin-bottom:10px;">O que acontece</p>
      <p style="font-family:'Montserrat',sans-serif;font-size:17px;font-weight:500;
         line-height:1.55;color:rgba(255,255,255,0.7);">${d.dor}</p>
    </div>

    <!-- BDC -->
    <div style="background:rgba(93,230,200,0.08);border:1px solid rgba(93,230,200,0.25);
         border-radius:10px;padding:18px 20px;margin-top:auto;">
      <p style="font-family:'Montserrat',sans-serif;font-size:11px;font-weight:700;
         letter-spacing:2px;color:#5de6c8;text-transform:uppercase;margin-bottom:10px;">
         O que o SAP BDC faz</p>
      <p style="font-family:'Montserrat',sans-serif;font-size:17px;font-weight:500;
         line-height:1.55;color:rgba(255,255,255,0.85);">${d.bdc}</p>
    </div>
  </div>
  `
));

// ── Slide 7: CTA ──────────────────────────────────────────────────────────────
const cta = wrap('#0A0837', glowCTR, `
${H(7)}
<div class="body" style="justify-content:center;gap:0;align-items:flex-start;">

  <p style="font-family:'Prompt',sans-serif;font-size:52px;font-weight:800;line-height:1.15;
     margin-bottom:28px;">
    Qual dessas dores está<br/>travando o seu <span style="color:#6B3BE8;">FP&A</span> hoje?
  </p>

  <div class="div" style="margin-bottom:28px;"></div>

  <p style="font-family:'Montserrat',sans-serif;font-size:18px;font-weight:500;
     line-height:1.6;color:rgba(255,255,255,0.6);margin-bottom:32px;">
    A Solveplan implementa SAP BDC e SAP Datasphere na América Latina.<br/>
    Mais de 90 clientes. Mais de 390 projetos entregues. Parceiro SAP Gold.
  </p>

  <div style="display:flex;align-items:center;gap:20px;margin-top:auto;">
    <div>
      <p style="font-family:'Prompt',sans-serif;font-size:26px;font-weight:800;margin-bottom:4px;">
        solve<span style="color:#006AFF;">plan</span>
      </p>
      <p style="font-family:'Montserrat',sans-serif;font-size:13px;color:rgba(255,255,255,0.3);">
        Parceiro SAP Gold · América Latina
      </p>
    </div>
    <div style="flex:1;"></div>
    <span style="font-family:'Montserrat',sans-serif;font-size:15px;font-weight:700;
          color:#5de6c8;border:1px solid rgba(93,230,200,0.4);padding:12px 22px;border-radius:8px;">
      Fale comigo →
    </span>
  </div>
</div>
`);

const slides = [capa, ...dorSlides, cta];

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

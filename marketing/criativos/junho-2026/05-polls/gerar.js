const { chromium } = require('playwright');
const path = require('path');
const fs   = require('fs');
const { wrap, glowCTR, glowBR, stripL, logo } = require('../shared');

const BASE   = 'c:/Users/franc/solveplan.com/Roberto Molina - Marketing/1. MKT Estrategy/3. Agentes de IA/ccos-ratos';
const OUTPUT = path.join(BASE.replace(/\//g, path.sep), 'marketing', 'criativos', 'junho-2026', '05-polls', 'cards');
fs.mkdirSync(OUTPUT, { recursive: true });

const polls = [
  {
    slug: 'poll-10-junho',
    date: '10 DE JUNHO',
    question: 'Qual é o maior\ngargalo de dados\nna sua empresa hoje?',
    options: [
      { letter: 'A', text: 'Planilhas Excel como sistema de consolidação' },
      { letter: 'B', text: 'Dados em silos — cada área tem a sua versão' },
      { letter: 'C', text: 'Dado existe mas não é confiável / há divergências' },
      { letter: 'D', text: 'Falta de governança — ninguém sabe qual versão é a certa' },
    ],
    cta: 'Vote no LinkedIn →',
  },
  {
    slug: 'poll-23-junho',
    date: '23 DE JUNHO',
    question: 'Sua empresa usa SAP.\nEm qual estágio está\na estratégia de dados?',
    options: [
      { letter: 'A', text: 'Excel como ferramenta de análise — SAP é só sistema de transação' },
      { letter: 'B', text: 'Usando Datasphere — saímos do Excel, ainda estruturando' },
      { letter: 'C', text: 'Implementando ou avaliando SAP BDC' },
      { letter: 'D', text: 'Temos SAP mas não sabemos por onde começar' },
    ],
    cta: 'Vote no LinkedIn →',
  },
];

const buildHtml = (p) => wrap(
  '#0A0837',
  glowCTR + glowBR + stripL,
  `
  <!-- HEADER -->
  <div style="display:flex;justify-content:space-between;align-items:center;padding:46px 58px 0;position:relative;z-index:2;">
    ${logo}
    <span style="font-family:'Montserrat',sans-serif;font-size:11px;font-weight:700;
          color:rgba(255,255,255,0.28);letter-spacing:2px;">ENQUETE</span>
  </div>

  <!-- BODY -->
  <div style="flex:1;padding:28px 58px 44px;display:flex;flex-direction:column;position:relative;z-index:2;">

    <!-- Date chip -->
    <span style="display:inline-block;align-self:flex-start;background:#006AFF;color:#fff;
          font-family:'Montserrat',sans-serif;font-size:11px;font-weight:700;letter-spacing:1.5px;
          padding:6px 14px;border-radius:4px;text-transform:uppercase;margin-bottom:22px;">${p.date}</span>

    <!-- Question -->
    <p style="font-family:'Prompt',sans-serif;font-size:58px;font-weight:800;line-height:1.12;
              white-space:pre-line;margin-bottom:32px;">${p.question}</p>

    <!-- Divider -->
    <div style="width:100%;height:1px;background:rgba(255,255,255,0.12);margin-bottom:28px;"></div>

    <!-- Options -->
    <div style="display:flex;flex-direction:column;gap:14px;flex:1;">
      ${p.options.map(o => `
        <div style="display:flex;align-items:center;gap:18px;background:rgba(255,255,255,0.06);
             border:1px solid rgba(255,255,255,0.1);border-radius:10px;padding:14px 20px;">
          <span style="font-family:'Montserrat',sans-serif;font-size:16px;font-weight:800;
                color:#006AFF;min-width:22px;">${o.letter}</span>
          <span style="font-family:'Montserrat',sans-serif;font-size:16px;font-weight:500;
                line-height:1.45;color:rgba(255,255,255,0.85);">${o.text}</span>
        </div>`).join('')}
    </div>

    <!-- CTA -->
    <div style="margin-top:22px;display:flex;align-items:center;justify-content:space-between;">
      <span style="font-family:'Montserrat',sans-serif;font-size:14px;font-weight:600;
            color:rgba(255,255,255,0.4);">solveplan.com</span>
      <span style="font-family:'Montserrat',sans-serif;font-size:15px;font-weight:700;
            color:#5de6c8;letter-spacing:0.5px;">${p.cta}</span>
    </div>
  </div>
  `
);

(async () => {
  const browser = await chromium.launch();
  for (const poll of polls) {
    const html = buildHtml(poll);
    const page = await browser.newPage();
    await page.setViewportSize({ width: 1080, height: 1080 });
    await page.setContent(html, { waitUntil: 'networkidle' });
    const file = path.join(OUTPUT, `${poll.slug}.png`);
    await page.screenshot({ path: file, clip: { x: 0, y: 0, width: 1080, height: 1080 } });
    await page.close();
    console.log(`✓ ${poll.slug}.png`);
  }
  await browser.close();
  console.log(`\n✅ ${polls.length} poll covers gerados em:\n${OUTPUT}`);
})();

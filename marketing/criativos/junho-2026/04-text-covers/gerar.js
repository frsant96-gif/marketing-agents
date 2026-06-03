const { chromium } = require('playwright');
const path = require('path');
const fs   = require('fs');
const { wrap, glowBR, glowTR, glowTL, stripL, logo } = require('../shared');

const BASE   = 'c:/Users/franc/solveplan.com/Roberto Molina - Marketing/1. MKT Estrategy/3. Agentes de IA/ccos-ratos';
const OUTPUT = path.join(BASE.replace(/\//g, path.sep), 'marketing', 'criativos', 'junho-2026', '04-text-covers', 'cards');
fs.mkdirSync(OUTPUT, { recursive: true });

// tag color by pilar
const COLORS = {
  'EDUCAÇÃO':    { bg: '#006AFF', text: '#fff' },
  'AUTORIDADE':  { bg: '#6B3BE8', text: '#fff' },
  'ARTIGO':      { bg: '#E8713B', text: '#fff' },
  'CASE':        { bg: '#1BAD8D', text: '#fff' },
  'ENGAGEMENT':  { bg: '#E83B8C', text: '#fff' },
};

const posts = [
  {
    slug: '05-06-o-que-e-sap-bdc',
    date: '05 JUN',
    tag: 'EDUCAÇÃO',
    line1: 'Toda empresa SAP tem dado.',
    line2: 'A maioria não tem dado confiável.',
    line2color: '#5de6c8',
    note: 'SAP Business Data Cloud',
  },
  {
    slug: '08-06-sap-business-ai-platform',
    date: '08 JUN',
    tag: 'AUTORIDADE',
    line1: 'A SAP não lançou uma nova ferramenta.',
    line2: 'Ela reconfigurou a arquitetura do ERP.',
    line2color: '#006AFF',
    note: 'SAPPHIRE 2026 • SAP Business AI Platform',
  },
  {
    slug: '11-06-sap-anthropic-fpa',
    date: '11 JUN',
    tag: 'AUTORIDADE',
    line1: 'A SAP firmou parceria com a Anthropic.',
    line2: 'A maioria perdeu o ponto mais importante.',
    line2color: '#5de6c8',
    note: 'SAP + Anthropic • FP&A',
  },
  {
    slug: '15-06-reforma-tributaria-dados',
    date: '15 JUN',
    tag: 'AUTORIDADE',
    line1: 'A reforma tributária de 2026',
    line2: 'não é problema de contabilidade.',
    line2color: '#FFB547',
    note: 'Reforma Tributária • Arquitetura de Dados SAP',
  },
  {
    slug: '16-06-knowledge-graph',
    date: '16 JUN',
    tag: 'ARTIGO',
    line1: 'IA sem contexto do negócio',
    line2: 'erra com precisão.',
    line2color: '#5de6c8',
    note: 'SAP Knowledge Graph • AI Foundation',
  },
  {
    slug: '18-06-governanca-cfo',
    date: '18 JUN',
    tag: 'AUTORIDADE',
    line1: 'Governança de dados não é projeto de TI.',
    line2: 'É decisão estratégica do CFO.',
    line2color: '#006AFF',
    note: 'Governança • FP&A • SAP BDC',
  },
  {
    slug: '19-06-cfos-dados',
    date: '19 JUN',
    tag: 'AUTORIDADE',
    line1: 'Os CFOs que mais avançam em 2026',
    line2: 'não têm as melhores planilhas.',
    line2color: '#5de6c8',
    note: 'FP&A • Dados • Liderança executiva',
  },
  {
    slug: '22-06-joule-work',
    date: '22 JUN',
    tag: 'ARTIGO',
    line1: 'O SAP Joule deixou de ser',
    line2: 'uma caixa de perguntas.',
    line2color: '#006AFF',
    note: 'SAP Joule Work • SAP Datasphere',
  },
  {
    slug: '25-06-case-vale',
    date: '25 JUN',
    tag: 'CASE',
    line1: 'A Vale saiu de 100+ planilhas',
    line2: 'para −50% no tempo de reporting.',
    line2color: '#5de6c8',
    note: 'Case Vale • SAPPHIRE 2026 • SAP EPM',
  },
  {
    slug: '26-06-consolidacao-societaria',
    date: '26 JUN',
    tag: 'EDUCAÇÃO',
    line1: 'Consolidação societária:',
    line2: 'o mais complexo. E o que mais ganha.',
    line2color: '#FFB547',
    note: 'Consolidação • SAP BDC • CFO de grupo',
  },
  {
    slug: '29-06-bdc-knowledge-core',
    date: '29 JUN',
    tag: 'ARTIGO',
    line1: 'Um agente SAP age com base',
    line2: 'no que sabe sobre o seu negócio.',
    line2color: '#5de6c8',
    note: 'SAP BDC Knowledge Core • Agentes',
  },
  {
    slug: '30-06-encerramento-junho',
    date: '30 JUN',
    tag: 'AUTORIDADE',
    line1: 'O que junho nos ensinou',
    line2: 'sobre dados corporativos.',
    line2color: '#006AFF',
    note: 'Retrospectiva • SAP • FP&A • Dados',
  },
];

const buildHtml = (p) => {
  const tc = COLORS[p.tag] || COLORS['AUTORIDADE'];

  // Adjust font size based on line length
  const maxLen = Math.max(p.line1.length, p.line2.length);
  const fontSize = maxLen > 42 ? 52 : maxLen > 34 ? 60 : 68;

  return wrap(
    'linear-gradient(150deg, #0A0837 0%, #0d1f4a 100%)',
    glowBR + glowTL + stripL,
    `
    <!-- HEADER -->
    <div style="display:flex;justify-content:space-between;align-items:center;
         padding:46px 58px 0;position:relative;z-index:2;">
      ${logo}
      <span style="font-family:'Montserrat',sans-serif;font-size:12px;font-weight:600;
            color:rgba(255,255,255,0.28);letter-spacing:1.5px;">${p.date}</span>
    </div>

    <!-- BODY -->
    <div style="flex:1;padding:40px 58px 50px;display:flex;flex-direction:column;
         justify-content:center;position:relative;z-index:2;">

      <!-- Tag -->
      <span style="display:inline-block;align-self:flex-start;background:${tc.bg};
            color:${tc.text};font-family:'Montserrat',sans-serif;font-size:11px;
            font-weight:700;letter-spacing:1.8px;padding:7px 16px;border-radius:4px;
            text-transform:uppercase;margin-bottom:28px;">${p.tag}</span>

      <!-- Accent bar -->
      <div style="width:52px;height:4px;background:${tc.bg};border-radius:2px;margin-bottom:28px;"></div>

      <!-- Hook text -->
      <p style="font-family:'Prompt',sans-serif;font-size:${fontSize}px;font-weight:800;
                line-height:1.15;color:#fff;margin-bottom:6px;">${p.line1}</p>
      <p style="font-family:'Prompt',sans-serif;font-size:${fontSize}px;font-weight:800;
                line-height:1.15;color:${p.line2color};margin-bottom:0;">${p.line2}</p>
    </div>

    <!-- FOOTER -->
    <div style="padding:0 58px 46px;position:relative;z-index:2;">
      <div style="width:100%;height:1px;background:rgba(255,255,255,0.1);margin-bottom:20px;"></div>
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <span style="font-family:'Montserrat',sans-serif;font-size:13px;font-weight:500;
              color:rgba(255,255,255,0.35);">${p.note}</span>
        <span style="font-family:'Prompt',sans-serif;font-size:15px;font-weight:700;
              color:rgba(255,255,255,0.5);">solveplan.com</span>
      </div>
    </div>
    `
  );
};

(async () => {
  const browser = await chromium.launch();
  for (const post of posts) {
    const html = buildHtml(post);
    const page = await browser.newPage();
    await page.setViewportSize({ width: 1080, height: 1080 });
    await page.setContent(html, { waitUntil: 'networkidle' });
    const file = path.join(OUTPUT, `${post.slug}.png`);
    await page.screenshot({ path: file, clip: { x: 0, y: 0, width: 1080, height: 1080 } });
    await page.close();
    console.log(`✓ ${post.slug}.png`);
  }
  await browser.close();
  console.log(`\n✅ ${posts.length} text covers gerados em:\n${OUTPUT}`);
})();

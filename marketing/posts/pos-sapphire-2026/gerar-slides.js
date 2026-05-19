const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const BASE = 'c:/Users/franc/solveplan.com/Roberto Molina - Marketing/1. MKT Estrategy/3. Agentes de IA/ccos-ratos';
const OUTPUT = `${BASE}/marketing/posts/pos-sapphire-2026/slides`;
const LOGO_SRC = path.join(BASE.replace(/\//g, path.sep), 'marca', 'logo-escuro1.png.png');
const LOGO = 'logo.png'; // copiado ao lado do HTML temporário

const fonts = `<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">`;

const css = `
  *{margin:0;padding:0;box-sizing:border-box;}
  body{width:1080px;height:1080px;overflow:hidden;font-family:'Montserrat',sans-serif;color:#fff;display:flex;flex-direction:column;position:relative;}
  .logo{height:44px;width:auto;display:block;}
  .num{font-family:'Montserrat',sans-serif;font-size:13px;font-weight:600;color:rgba(255,255,255,0.3);letter-spacing:2px;}
  .hdr{display:flex;justify-content:space-between;align-items:center;padding:48px 60px 0;position:relative;z-index:2;}
  .body{flex:1;padding:32px 60px 52px;display:flex;flex-direction:column;gap:28px;position:relative;z-index:2;}
  .tag{display:inline-block;align-self:flex-start;background:#006AFF;color:#fff;font-family:'Montserrat',sans-serif;font-size:13px;font-weight:700;letter-spacing:1.5px;padding:7px 18px;border-radius:4px;text-transform:uppercase;}
  .bar{width:52px;height:4px;background:#006AFF;border-radius:2px;margin:24px 0 20px;}
  .div{width:100%;height:1px;background:rgba(255,255,255,0.1);margin:20px 0;}
  .accent{color:#006AFF;}
  .green{color:#94FF96;}
  .glow{position:absolute;border-radius:50%;pointer-events:none;}
`;

const wrap = (bg, decorators, content) => `<!DOCTYPE html><html><head><meta charset="UTF-8">${fonts}
<style>${css}body{background:${bg};}</style></head><body>
${decorators}
${content}
</body></html>`;

// ─── DECORATORS ───────────────────────────────────────────────────
const glowBR  = `<div class="glow" style="bottom:-100px;right:-100px;width:560px;height:560px;background:radial-gradient(circle,rgba(0,106,255,0.2) 0%,transparent 65%);"></div>`;
const glowTR  = `<div class="glow" style="top:-60px;right:-60px;width:420px;height:420px;background:radial-gradient(circle,rgba(0,106,255,0.18) 0%,transparent 65%);"></div>`;
const glowCTR = `<div class="glow" style="top:50%;left:50%;transform:translate(-50%,-50%);width:750px;height:750px;background:radial-gradient(circle,rgba(0,106,255,0.22) 0%,transparent 65%);"></div>`;
const stripL  = `<div style="position:absolute;top:0;left:0;width:6px;height:100%;background:linear-gradient(180deg,#006AFF 0%,transparent 100%);z-index:3;"></div>`;
const stripLfull = `<div style="position:absolute;top:0;left:0;width:6px;height:100%;background:#006AFF;z-index:3;"></div>`;

const logoHtml = `<span style="font-family:'Prompt',sans-serif;font-size:20px;font-weight:800;color:#fff;letter-spacing:-0.5px;">solve<span style="color:#006AFF;">plan</span></span>`;
const hdr = (n) => `<div class="hdr">${logoHtml}<span class="num">0${n} / 08</span></div>`;

// ─── SLIDES ───────────────────────────────────────────────────────
const slides = [

// 01 — CAPA
wrap('#0A0837', glowBR + glowTR + stripL, `
${hdr(1)}
<div class="body" style="justify-content:flex-start;padding-top:60px;">
  <span class="tag">SAP Sapphire 2026 · Orlando</span>
  <div class="bar"></div>
  <p style="font-family:'Prompt',sans-serif;font-size:104px;font-weight:800;line-height:0.97;margin-bottom:40px;">
    O SAPPHIRE<br/><span class="accent">2026</span><br/>não foi<br/>sobre IA.
  </p>
  <p style="font-family:'Prompt',sans-serif;font-size:38px;font-weight:600;line-height:1.35;color:rgba(255,255,255,0.6);margin-bottom:0;">
    Foi sobre o fim do ERP<br/>como você conhece.
  </p>
  <div style="margin-top:auto;">
    <div class="div"></div>
    <p style="font-size:17px;font-weight:500;color:rgba(255,255,255,0.4);">O que vimos em Orlando e o que isso muda pra você →</p>
  </div>
</div>
`),

// 02 — QUOTE CHRISTIAN KLEIN
wrap('linear-gradient(160deg,#0A0837 40%,#001a4d 100%)', glowCTR, `
${hdr(2)}
<div class="body">
  <div>
    <span class="tag">SAP Sapphire · Keynote</span>
    <div style="width:72px;height:5px;background:#006AFF;border-radius:3px;margin:28px 0 24px;"></div>
    <p style="font-family:'Montserrat',sans-serif;font-size:18px;font-weight:600;color:rgba(255,255,255,0.45);margin-bottom:20px;">Christian Klein, CEO da SAP:</p>
    <p style="font-family:'Prompt',sans-serif;font-size:64px;font-weight:800;line-height:1.08;margin-bottom:36px;">
      <span class="accent">"</span>Almost right<br/>just isn't<br/>good enough.<span class="accent">"</span>
    </p>
  </div>
  <div>
    <div class="div"></div>
    <p style="font-size:20px;font-weight:500;line-height:1.7;color:rgba(255,255,255,0.7);">
      Para processos críticos de negócio — fechamento financeiro, planejamento, supply chain —<br/>
      <strong style="color:#fff;">erro aceitável não é mais uma opção.</strong>
    </p>
    <p style="font-size:17px;font-weight:500;color:rgba(255,255,255,0.4);margin-top:20px;line-height:1.6;">
      A SAP não está construindo um assistente de IA.<br/>Está reconstruindo o ERP com IA no núcleo.
    </p>
  </div>
</div>
`),

// 03 — NOVA ARQUITETURA
wrap('#0A0E19', glowTR, `
${hdr(3)}
<div class="body" style="justify-content:flex-start;">
  <div style="margin-bottom:20px;">
    <span class="tag">Nova Arquitetura</span>
    <div class="bar"></div>
    <p style="font-family:'Prompt',sans-serif;font-size:46px;font-weight:800;line-height:1.1;margin-bottom:8px;">
      SAP Business<br/><span class="accent">AI Platform</span>
    </p>
    <p style="font-size:16px;font-weight:500;color:rgba(255,255,255,0.45);">Uma plataforma unificada. Tudo conectado.</p>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:0;">
    <div style="background:rgba(0,106,255,0.12);border:1px solid rgba(0,106,255,0.45);border-radius:10px;padding:24px 28px;">
      <p style="font-size:11px;font-weight:700;color:#006AFF;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;">Camada 1</p>
      <p style="font-family:'Prompt',sans-serif;font-size:24px;font-weight:700;">SAP Business Technology Platform</p>
      <p style="font-size:14px;color:rgba(255,255,255,0.5);margin-top:4px;">Base de integração, extensibilidade e desenvolvimento</p>
    </div>
    <div style="background:rgba(0,106,255,0.2);border:1px solid rgba(0,106,255,0.65);border-radius:10px;padding:24px 28px;">
      <p style="font-size:11px;font-weight:700;color:#006AFF;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;">Camada 2 — O diferencial</p>
      <p style="font-family:'Prompt',sans-serif;font-size:24px;font-weight:700;">SAP Business Data Cloud</p>
      <p style="font-size:14px;color:rgba(255,255,255,0.5);margin-top:4px;">Knowledge Graph + Dremio Lakehouse nativo <span style="color:rgba(255,255,255,0.3);font-size:12px;">(aquisição Q3 2026)</span></p>
    </div>
    <div style="background:rgba(148,255,150,0.07);border:1px solid rgba(148,255,150,0.3);border-radius:10px;padding:24px 28px;">
      <p style="font-size:11px;font-weight:700;color:#94FF96;letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;">Camada 3 — GA agora</p>
      <p style="font-family:'Prompt',sans-serif;font-size:24px;font-weight:700;">AI Foundation + Joule Studio 2.0</p>
      <p style="font-size:14px;color:rgba(255,255,255,0.5);margin-top:4px;">Agentes que criam, orquestram e governam processos autônomos</p>
    </div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;">
      ${['NVIDIA','AWS','Google Cloud','Microsoft','Anthropic','+ 6 parceiros'].map(p=>`<span style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.12);border-radius:6px;padding:5px 12px;font-size:12px;font-weight:600;color:rgba(255,255,255,0.5);">${p}</span>`).join('')}
    </div>
  </div>
</div>
`),

// 04 — 50+ ASSISTENTES
wrap('#0A0837', glowTR, `
${hdr(4)}
<div class="body" style="justify-content:flex-start;gap:0;">
  <div style="margin-bottom:18px;">
    <span class="tag">SAP Autonomous Suite</span>
    <div class="bar"></div>
    <p style="font-family:'Prompt',sans-serif;font-size:27px;font-weight:700;color:rgba(255,255,255,0.7);line-height:1.35;margin-bottom:0;">
      "A evolução mais significativa do portfólio SAP <span class="accent">em toda a história da empresa.</span>"
    </p>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;gap:14px;">
    <div style="display:flex;gap:14px;flex:1;">
      <div style="flex:1;background:rgba(0,106,255,0.15);border:1px solid rgba(0,106,255,0.4);border-radius:10px;padding:20px;text-align:center;display:flex;flex-direction:column;justify-content:center;">
        <p style="font-family:'Prompt',sans-serif;font-size:96px;font-weight:800;color:#006AFF;line-height:1;">50+</p>
        <p style="font-size:15px;font-weight:600;color:#fff;margin-top:8px;">assistentes<br/>por domínio</p>
      </div>
      <div style="flex:1;background:rgba(0,106,255,0.15);border:1px solid rgba(0,106,255,0.4);border-radius:10px;padding:20px;text-align:center;display:flex;flex-direction:column;justify-content:center;">
        <p style="font-family:'Prompt',sans-serif;font-size:96px;font-weight:800;color:#006AFF;line-height:1;">200+</p>
        <p style="font-size:15px;font-weight:600;color:#fff;margin-top:8px;">agentes<br/>especializados</p>
      </div>
    </div>
    <div style="background:rgba(148,255,150,0.07);border:1px solid rgba(148,255,150,0.3);border-radius:10px;padding:22px 28px;">
      <p style="font-size:12px;font-weight:700;color:#94FF96;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:8px;">Resultado concreto</p>
      <p style="font-family:'Prompt',sans-serif;font-size:22px;font-weight:700;">Fechamento financeiro</p>
      <p style="font-size:18px;color:rgba(255,255,255,0.6);margin-top:6px;">
        <span style="text-decoration:line-through;color:rgba(255,255,255,0.3);">Semanas</span>
        <span style="color:#94FF96;font-weight:700;margin:0 12px;">→</span>
        <strong class="green">Dias</strong>
      </p>
    </div>
    <div style="background:rgba(255,255,255,0.04);border-radius:10px;padding:18px 28px;">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px;">
        <div>
          <p style="font-size:11px;font-weight:700;color:rgba(255,255,255,0.35);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:6px;">€100M fundo de parceiros</p>
          <div style="display:flex;gap:6px;flex-wrap:wrap;">
            ${['Finance','Supply Chain','Procurement','RH','CX'].map(d=>`<span style="background:rgba(0,106,255,0.2);border:1px solid rgba(0,106,255,0.35);border-radius:6px;padding:5px 12px;font-size:12px;font-weight:600;color:rgba(255,255,255,0.7);">${d}</span>`).join('')}
          </div>
        </div>
        <div style="text-align:right;flex-shrink:0;">
          <p style="font-family:'Prompt',sans-serif;font-size:32px;font-weight:800;color:#94FF96;line-height:1;">680+</p>
          <p style="font-size:12px;color:rgba(255,255,255,0.4);margin-top:2px;">agentes no<br/>SAP AI Agent Hub</p>
        </div>
      </div>
    </div>
  </div>
</div>
`),

// 05 — SAP + ECOSSISTEMA (foco Anthropic / FP&A)
wrap('#0A0E19', glowBR, `
${hdr(5)}
<div class="body" style="justify-content:flex-start;padding-top:28px;">
  <div style="margin-bottom:20px;">
    <span class="tag">11 Parcerias Estratégicas</span>
    <div class="bar"></div>
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:wrap;">
      ${['Anthropic','AWS','Google Cloud','Microsoft','NVIDIA','Mistral','Cohere','Parloa','n8n','Vercel','+ 1'].map((p,i)=>`<span style="background:${i===0?'rgba(148,255,150,0.1)':'rgba(255,255,255,0.04)'};border:1px solid ${i===0?'rgba(148,255,150,0.4)':'rgba(255,255,255,0.1)'};border-radius:6px;padding:5px 12px;font-size:${i===0?'15px':'12px'};font-weight:${i===0?'700':'500'};color:${i===0?'#94FF96':'rgba(255,255,255,0.5)'};">${p}</span>`).join('')}
    </div>
    <p style="font-size:15px;font-weight:500;color:rgba(255,255,255,0.4);line-height:1.6;">
      Anthropic para raciocínio · AWS zero-copy data · Google/Microsoft interop agent-to-agent
    </p>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:space-between;">
    <div>
      <div class="div" style="margin-bottom:20px;"></div>
      <p style="font-size:13px;font-weight:700;color:rgba(255,255,255,0.35);letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;">O que a parceria com a Anthropic habilita no FP&A</p>
    </div>
    ${[
      ['Análise de variações', 'Real x Budget explicadas em linguagem natural'],
      ['Projeção de caixa', 'Com sugestões de ação corretiva automáticas'],
      ['Fechamento contábil', 'Suporte automatizado, sem retrabalho manual'],
      ['Análise sob demanda', 'Financeira e operacional em segundos'],
    ].map(([t,d])=>`
    <div style="display:flex;gap:16px;align-items:flex-start;">
      <div style="min-width:8px;height:8px;background:#006AFF;border-radius:50%;margin-top:8px;flex-shrink:0;"></div>
      <div>
        <p style="font-size:19px;font-weight:700;color:#fff;">${t}</p>
        <p style="font-size:15px;color:rgba(255,255,255,0.45);margin-top:3px;">${d}</p>
      </div>
    </div>`).join('')}
  </div>
</div>
`),

// 06 — CASE VALE
wrap('#0A0837', glowBR, `
${hdr(6)}
<div class="body" style="justify-content:flex-start;padding-top:32px;">
  <span class="tag">Caso Real · SAPPHIRE 2026</span>
  <div class="bar"></div>
  <p style="font-family:'Prompt',sans-serif;font-size:58px;font-weight:800;line-height:1.05;margin-bottom:12px;">
    <span class="accent">Vale</span> apresentou<br/>ao vivo em Orlando.
  </p>
  <p style="font-size:18px;font-weight:500;color:rgba(255,255,255,0.45);margin-bottom:32px;">174 mil funcionários · 20 países · 24 mil centros de custo</p>
  <div>
    <div style="display:flex;gap:14px;margin-bottom:14px;">
      <div style="flex:1;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:10px;padding:24px;">
        <p style="font-size:11px;font-weight:700;color:rgba(255,255,255,0.35);letter-spacing:2px;text-transform:uppercase;margin-bottom:10px;">Antes</p>
        <p style="font-family:'Prompt',sans-serif;font-size:21px;font-weight:700;color:rgba(255,255,255,0.7);line-height:1.35;">+100 planilhas Excel<br/>consolidadas<br/>manualmente</p>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <p style="font-family:'Prompt',sans-serif;font-size:36px;font-weight:800;color:#006AFF;">→</p>
      </div>
      <div style="flex:1;background:rgba(0,106,255,0.15);border:1px solid rgba(0,106,255,0.5);border-radius:10px;padding:24px;">
        <p style="font-size:11px;font-weight:700;color:#006AFF;letter-spacing:2px;text-transform:uppercase;margin-bottom:10px;">Depois</p>
        <p style="font-family:'Prompt',sans-serif;font-size:21px;font-weight:700;line-height:1.35;">SAP EPM<br/>integrado,<br/>governado e escalável</p>
      </div>
    </div>
    <div style="background:rgba(148,255,150,0.07);border:1px solid rgba(148,255,150,0.35);border-radius:10px;padding:32px;text-align:center;margin-bottom:16px;">
      <p style="font-family:'Prompt',sans-serif;font-size:104px;font-weight:800;color:#94FF96;line-height:1;">~50%</p>
      <p style="font-size:20px;font-weight:600;color:#fff;margin-top:4px;">redução no tempo de reporting financeiro</p>
    </div>
    <p style="font-size:14px;font-weight:500;color:rgba(255,255,255,0.35);text-align:center;">
      + agilidade em simulações · + precisão no planejamento · melhor alocação de capital
    </p>
  </div>
</div>
`),

// 07 — O QUE MUDA PRA VOCÊ
wrap('#0A0E19', glowTR + stripL, `
${hdr(7)}
<div class="body" style="justify-content:flex-start;padding-top:32px;">
  <span class="tag">O que isso muda pra você</span>
  <div class="bar"></div>
  <p style="font-family:'Prompt',sans-serif;font-size:42px;font-weight:800;line-height:1.2;margin-bottom:32px;">
    Se a sua empresa ainda faz isso,<br/><span class="accent">o mercado já passou à frente.</span>
  </p>
  ${[
    'Fecha o mês em planilhas Excel',
    'Consolida dados manualmente entre sistemas',
    'Leva semanas pra gerar um cenário financeiro',
    'Depende de relatórios estáticos para decisões críticas',
    'Tem dados dispersos sem governança centralizada',
  ].map(item=>`
  <div style="display:flex;align-items:center;gap:18px;padding:20px 24px;background:rgba(255,255,255,0.04);border-left:3px solid rgba(255,255,255,0.12);border-radius:0 8px 8px 0;margin-bottom:12px;">
    <p style="font-size:17px;font-weight:500;color:rgba(255,255,255,0.65);">${item}</p>
  </div>`).join('')}
  <div style="margin-top:24px;padding:28px 32px;background:rgba(0,106,255,0.15);border:1px solid rgba(0,106,255,0.4);border-radius:10px;">
    <p style="font-family:'Prompt',sans-serif;font-size:22px;font-weight:700;line-height:1.5;">
      O SAP BDC foi construído exatamente para isso.<br/>
      <span class="accent">E a janela de vantagem é agora.</span>
    </p>
  </div>
</div>
`),

// 08 — CTA
wrap('linear-gradient(160deg,#0A0837 0%,#001233 100%)', glowCTR + stripLfull, `
${hdr(8)}
<div class="body" style="justify-content:space-between;text-align:center;padding-top:40px;">
  <div>
    <p style="font-size:12px;font-weight:700;color:rgba(255,255,255,0.35);letter-spacing:3px;text-transform:uppercase;margin-bottom:28px;">Parceiro SAP Gold · América Latina</p>
    <p style="font-family:'Prompt',sans-serif;font-size:64px;font-weight:800;line-height:1.05;margin-bottom:24px;">
      Vimos o SAPPHIRE.<br/>Agora queremos<br/><span class="accent">ver o seu cenário.</span>
    </p>
    <p style="font-size:19px;font-weight:500;color:rgba(255,255,255,0.5);line-height:1.65;">
      Se quiser entender o que o SAP BDC entrega<br/>
      no seu ambiente atual — sem hype,<br/>
      com diagnóstico real — é só chamar.
    </p>
  </div>
  <div style="display:inline-block;background:#006AFF;border-radius:8px;padding:22px 56px;">
    <p style="font-family:'Prompt',sans-serif;font-size:24px;font-weight:700;">Comente ou mande mensagem direta</p>
  </div>
  <div style="width:100%;">
    <div class="div"></div>
    <div style="display:flex;justify-content:center;gap:52px;margin-top:8px;">
      <div>
        <p style="font-family:'Prompt',sans-serif;font-size:44px;font-weight:800;color:#006AFF;">+200</p>
        <p style="font-size:14px;color:rgba(255,255,255,0.4);">soluções entregues</p>
      </div>
      <div style="width:1px;background:rgba(255,255,255,0.1);"></div>
      <div>
        <p style="font-family:'Prompt',sans-serif;font-size:44px;font-weight:800;color:#006AFF;">+90</p>
        <p style="font-size:14px;color:rgba(255,255,255,0.4);">clientes atendidos</p>
      </div>
      <div style="width:1px;background:rgba(255,255,255,0.1);"></div>
      <div>
        <p style="font-family:'Prompt',sans-serif;font-size:44px;font-weight:800;color:#006AFF;">SAP</p>
        <p style="font-size:14px;color:rgba(255,255,255,0.4);">Gold Partner</p>
      </div>
    </div>
  </div>
</div>
`),

];

async function run() {
  if (!fs.existsSync(OUTPUT)) fs.mkdirSync(OUTPUT, { recursive: true });

  const tmpDir = path.join(require('os').tmpdir(), 'solveplan-slides');
  if (!fs.existsSync(tmpDir)) fs.mkdirSync(tmpDir, { recursive: true });

  // logo copiado ao lado dos HTMLs para referência relativa
  fs.copyFileSync(LOGO_SRC, path.join(tmpDir, 'logo.png'));

  const browser = await chromium.launch({ args: ['--allow-file-access-from-files', '--disable-web-security'] });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1080, height: 1080 });

  for (let i = 0; i < slides.length; i++) {
    const tmp = path.join(tmpDir, `slide-${i}.html`);
    fs.writeFileSync(tmp, slides[i], 'utf8');
    await page.goto(`file:///${tmp.replace(/\\/g, '/')}`, { waitUntil: 'load' });
    // aguarda todas as imagens carregarem
    await page.evaluate(() => Promise.all(
      [...document.images].map(img =>
        img.complete ? Promise.resolve() : new Promise(r => { img.onload = r; img.onerror = r; })
      )
    ));
    await page.waitForTimeout(300);
    const file = path.join(OUTPUT, `slide-0${i + 1}.png`);
    await page.screenshot({ path: file });
    fs.unlinkSync(tmp);
    console.log(`✓ slide-0${i + 1}.png`);
  }

  await browser.close();
  fs.rmSync(tmpDir, { recursive: true, force: true });
  console.log(`\nPronto! ${slides.length} slides em:\n${OUTPUT}`);
}

run().catch(err => { console.error(err); process.exit(1); });

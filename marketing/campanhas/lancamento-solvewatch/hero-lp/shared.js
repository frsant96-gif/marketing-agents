// Design system compartilhado — Criativos Junho 2026

const fonts = `<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">`;

const css = `
  *{margin:0;padding:0;box-sizing:border-box;}
  body{width:1080px;height:1080px;overflow:hidden;font-family:'Montserrat',sans-serif;color:#fff;
       display:flex;flex-direction:column;position:relative;}
  .logo{font-family:'Prompt',sans-serif;font-size:22px;font-weight:800;color:#fff;letter-spacing:-0.5px;}
  .logo b{color:#006AFF;}
  .tag{display:inline-block;align-self:flex-start;font-family:'Montserrat',sans-serif;
       font-size:12px;font-weight:700;letter-spacing:1.6px;padding:7px 16px;border-radius:4px;
       text-transform:uppercase;}
  .bar{width:52px;height:4px;background:#006AFF;border-radius:2px;}
  .div{width:100%;height:1px;background:rgba(255,255,255,0.1);}
  .accent{color:#006AFF;}
  .teal{color:#5de6c8;}
  .muted{color:rgba(255,255,255,0.45);}
  .glow{position:absolute;border-radius:50%;pointer-events:none;}
  .hdr{display:flex;justify-content:space-between;align-items:center;
       padding:46px 58px 0;position:relative;z-index:2;}
  .body{flex:1;padding:30px 58px 50px;display:flex;flex-direction:column;
        position:relative;z-index:2;}
  .num{font-family:'Montserrat',sans-serif;font-size:12px;font-weight:600;
       color:rgba(255,255,255,0.28);letter-spacing:2px;}
  .bullet{display:flex;align-items:flex-start;gap:16px;margin-bottom:22px;}
  .dot{flex-shrink:0;width:7px;height:7px;border-radius:50%;margin-top:9px;}
  .dot-blue{background:#006AFF;}
  .dot-teal{background:#5de6c8;}
  .dot-white{background:rgba(255,255,255,0.5);}
  .btext{font-size:20px;font-weight:500;line-height:1.55;color:rgba(255,255,255,0.85);}
  .section-label{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;
                  margin-bottom:10px;}
`;

const glowBR  = `<div class="glow" style="bottom:-110px;right:-110px;width:560px;height:560px;background:radial-gradient(circle,rgba(0,106,255,0.22) 0%,transparent 65%);"></div>`;
const glowTR  = `<div class="glow" style="top:-70px;right:-70px;width:400px;height:400px;background:radial-gradient(circle,rgba(0,106,255,0.16) 0%,transparent 65%);"></div>`;
const glowTL  = `<div class="glow" style="top:-80px;left:-80px;width:380px;height:380px;background:radial-gradient(circle,rgba(0,106,255,0.13) 0%,transparent 65%);"></div>`;
const glowCTR = `<div class="glow" style="top:50%;left:50%;transform:translate(-50%,-50%);width:780px;height:780px;background:radial-gradient(circle,rgba(0,106,255,0.18) 0%,transparent 65%);"></div>`;
const glowTeal= `<div class="glow" style="bottom:-80px;right:-80px;width:520px;height:520px;background:radial-gradient(circle,rgba(93,230,200,0.18) 0%,transparent 65%);"></div>`;
const stripL  = `<div style="position:absolute;top:0;left:0;width:6px;height:100%;background:linear-gradient(180deg,#006AFF 0%,rgba(0,106,255,0) 100%);z-index:3;"></div>`;
const stripLfull = `<div style="position:absolute;top:0;left:0;width:6px;height:100%;background:#006AFF;z-index:3;"></div>`;

const logo = `<div class="logo">solve<b>plan</b></div>`;

const wrap = (bg, decor, content, extraCss = '') =>
  `<!DOCTYPE html><html><head><meta charset="UTF-8">${fonts}
<style>${css}body{background:${bg};}${extraCss}</style></head><body>
${decor}
${content}
</body></html>`;

const hdr = (n, total, tag = '') =>
  `<div class="hdr">${logo}${tag ? `<span class="num">${tag}</span>` : `<span class="num">0${n} / 0${total}</span>`}</div>`;

module.exports = { fonts, css, glowBR, glowTR, glowTL, glowCTR, glowTeal, stripL, stripLfull, logo, wrap, hdr };

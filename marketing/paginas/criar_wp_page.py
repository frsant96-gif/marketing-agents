import requests
import sys

WP_URL = "https://solveplan.com"
WP_USER = "administrador"
WP_PASS = "vjpT R0lO 9c2G vh2w WAqA RPfU"

HTML_CONTENT = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;600;700;800&family=Montserrat:wght@400;500;600&display=swap');

.sw-wrap *, .sw-wrap *::before, .sw-wrap *::after { box-sizing: border-box; }
.sw-wrap {
  --navy:     #0A0E19;
  --surface:  #0D1230;
  --card:     #111828;
  --blue:     #006AFF;
  --blue-dim: #004FC4;
  --green:    #94FF96;
  --white:    #FFFFFF;
  --muted:    #8A93B2;
  --border:   rgba(255,255,255,0.08);
  --radius:   12px;
  font-family: 'Montserrat', sans-serif;
  background: var(--navy);
  color: var(--white);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  margin: 0 -20px;
}

/* HERO */
.sw-hero {
  padding: 80px 48px 100px;
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: center;
}
.sw-hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(148,255,150,0.08);
  border: 1px solid rgba(148,255,150,0.25);
  border-radius: 20px;
  padding: 6px 14px;
  font-size: 12px;
  font-weight: 600;
  color: var(--green);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 24px;
}
.sw-hero h1 {
  font-family: 'Prompt', sans-serif;
  font-weight: 800;
  font-size: clamp(32px, 4vw, 50px);
  line-height: 1.1;
  letter-spacing: -0.02em;
  margin-bottom: 24px;
  color: var(--white);
}
.sw-hero h1 em { font-style: normal; color: var(--blue); }
.sw-hero-sub {
  font-size: 17px;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 40px;
  max-width: 480px;
}
.sw-hero-actions {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}
.sw-btn-primary {
  background: var(--blue);
  color: var(--white) !important;
  border: none;
  border-radius: 8px;
  padding: 14px 32px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 15px;
  cursor: pointer;
  text-decoration: none !important;
  display: inline-block;
  transition: background 0.2s, transform 0.15s;
  box-shadow: 0 4px 24px rgba(0,106,255,0.35);
}
.sw-btn-primary:hover { background: var(--blue-dim); transform: translateY(-2px); }
.sw-btn-secondary {
  color: var(--muted) !important;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none !important;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: color 0.2s;
}
.sw-btn-secondary:hover { color: var(--white) !important; }
.sw-hero-stats {
  display: flex;
  gap: 32px;
  margin-top: 48px;
  padding-top: 32px;
  border-top: 1px solid var(--border);
}
.sw-hero-stat-value {
  font-family: 'Prompt', sans-serif;
  font-weight: 700;
  font-size: 28px;
  color: var(--white);
  line-height: 1;
}
.sw-hero-stat-label { font-size: 12px; color: var(--muted); margin-top: 4px; }

/* Mockup */
.sw-mockup-frame {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: 0 32px 80px rgba(0,0,0,0.5);
  position: relative;
}
.sw-mockup-topbar {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.sw-dot { width: 10px; height: 10px; border-radius: 50%; }
.sw-dot-r { background: #FF5F57; }
.sw-dot-y { background: #FEBC2E; }
.sw-dot-g { background: #28C840; }
.sw-mockup-title { margin-left: 8px; font-size: 12px; color: var(--muted); font-weight: 500; }
.sw-mockup-body { padding: 24px; }
.sw-dash-row { display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; margin-bottom: 16px; }
.sw-dash-kpi { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 12px; }
.sw-dash-kpi-val { font-family: 'Prompt', sans-serif; font-weight: 700; font-size: 20px; color: var(--white); }
.sw-dash-kpi-val.green { color: var(--green); }
.sw-dash-kpi-val.red   { color: #FF6B6B; }
.sw-dash-kpi-val.blue  { color: #60A5FA; }
.sw-dash-kpi-label { font-size: 10px; color: var(--muted); margin-top: 2px; }
.sw-calendar-grid { display: grid; grid-template-columns: repeat(7,1fr); gap: 4px; margin-bottom: 16px; }
.sw-cal-day { aspect-ratio: 1; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 9px; font-weight: 600; }
.sw-cal-day.ok   { background: rgba(148,255,150,0.18); color: var(--green); }
.sw-cal-day.warn { background: rgba(254,188,46,0.18); color: #FEBC2E; }
.sw-cal-day.err  { background: rgba(255,107,107,0.18); color: #FF6B6B; }
.sw-cal-day.empty { background: var(--surface); color: var(--muted); }
.sw-heatmap-grid { display: grid; grid-template-columns: repeat(24,1fr); gap: 2px; }
.sw-heat-cell { aspect-ratio: 1; border-radius: 2px; }
.sw-heat-cell.h0 { background: rgba(0,106,255,0.05); }
.sw-heat-cell.h1 { background: rgba(0,106,255,0.2); }
.sw-heat-cell.h2 { background: rgba(0,106,255,0.4); }
.sw-heat-cell.h3 { background: rgba(0,106,255,0.65); }
.sw-heat-cell.h4 { background: rgba(255,107,107,0.8); }
.sw-mockup-label { font-size: 10px; color: var(--muted); margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.06em; }
.sw-float-badge {
  position: absolute;
  bottom: -16px; left: -16px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
  min-width: 220px;
}
.sw-float-icon {
  width: 36px; height: 36px;
  background: rgba(148,255,150,0.12);
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  font-size: 18px;
}
.sw-float-text { font-size: 12px; }
.sw-float-text strong { display: block; color: var(--white); font-size: 13px; }
.sw-float-text span { color: var(--muted); }

/* SECTIONS */
.sw-section { padding: 80px 48px; }
.sw-section-inner { max-width: 1200px; margin: 0 auto; }
.sw-section-bg { background: var(--surface); }
.sw-section-form { background: linear-gradient(135deg, #081035 0%, #0A0E19 60%); border-top: 1px solid var(--border); }
.sw-section-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  font-weight: 600;
  color: var(--blue);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 16px;
}
.sw-section-tag::before { content: ''; display: block; width: 20px; height: 2px; background: var(--blue); border-radius: 2px; }
.sw-wrap h2 {
  font-family: 'Prompt', sans-serif;
  font-weight: 700;
  font-size: clamp(28px, 3vw, 40px);
  line-height: 1.2;
  letter-spacing: -0.02em;
  color: var(--white);
  margin-bottom: 16px;
}
.sw-wrap h2 em { font-style: normal; color: var(--blue); }
.sw-section-desc { font-size: 16px; color: var(--muted); line-height: 1.7; max-width: 560px; margin-bottom: 56px; }
.sw-divider { height: 1px; background: var(--border); margin: 0 48px; }

/* DORES */
.sw-dores-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 24px; }
.sw-dor-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 32px;
  position: relative;
  overflow: hidden;
  transition: border-color 0.25s, transform 0.2s;
}
.sw-dor-card:hover { border-color: rgba(0,106,255,0.4); transform: translateY(-4px); }
.sw-dor-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--blue), #60A5FA);
  opacity: 0;
  transition: opacity 0.25s;
}
.sw-dor-card:hover::before { opacity: 1; }
.sw-dor-number { font-family: 'Prompt', sans-serif; font-size: 48px; font-weight: 800; color: rgba(0,106,255,0.12); line-height: 1; margin-bottom: 16px; }
.sw-dor-card h3 { font-family: 'Prompt', sans-serif; font-weight: 700; font-size: 18px; color: var(--white); margin-bottom: 12px; }
.sw-dor-card p { font-size: 14px; color: var(--muted); line-height: 1.7; }
.sw-dor-quote {
  margin-top: 20px;
  padding: 12px 16px;
  background: rgba(0,106,255,0.07);
  border-left: 3px solid var(--blue);
  border-radius: 0 6px 6px 0;
  font-size: 13px;
  color: #A0B0CC;
  font-style: italic;
}

/* SOLUÇÃO */
.sw-solucao-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }
.sw-beneficios-list { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 40px; }
.sw-beneficio-item { display: flex; align-items: flex-start; gap: 14px; }
.sw-beneficio-icon {
  width: 40px; height: 40px; min-width: 40px;
  background: rgba(0,106,255,0.12);
  border: 1px solid rgba(0,106,255,0.2);
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  font-size: 18px;
}
.sw-beneficio-text strong { display: block; font-size: 14px; font-weight: 600; color: var(--white); margin-bottom: 4px; }
.sw-beneficio-text span { font-size: 13px; color: var(--muted); line-height: 1.5; }
.sw-tagline-box {
  background: linear-gradient(135deg, rgba(0,106,255,0.15), rgba(0,106,255,0.05));
  border: 1px solid rgba(0,106,255,0.25);
  border-radius: 12px;
  padding: 28px 32px;
  margin-bottom: 40px;
}
.sw-tagline-box p { font-family: 'Prompt', sans-serif; font-weight: 600; font-size: 20px; color: var(--white); line-height: 1.4; }
.sw-tagline-box p span { color: var(--green); }
.sw-placeholder {
  background: var(--card);
  border: 2px dashed rgba(0,106,255,0.25);
  border-radius: var(--radius);
  padding: 40px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  gap: 16px;
}
.sw-placeholder-icon { font-size: 48px; }
.sw-placeholder p { color: var(--muted); font-size: 14px; line-height: 1.6; max-width: 280px; }
.sw-placeholder p strong { color: var(--white); }

/* FUNCIONALIDADES */
.sw-features-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 24px; }
.sw-feature-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 32px;
  display: flex;
  gap: 20px;
  transition: border-color 0.2s, transform 0.2s;
}
.sw-feature-card:hover { border-color: rgba(0,106,255,0.35); transform: translateY(-3px); }
.sw-feature-card.highlight {
  border-color: rgba(0,106,255,0.3);
  background: linear-gradient(135deg, rgba(0,106,255,0.08), var(--card));
  grid-column: 1 / -1;
  align-items: center;
  gap: 48px;
}
.sw-feature-icon-wrap {
  width: 52px; min-width: 52px; height: 52px;
  background: rgba(0,106,255,0.12);
  border: 1px solid rgba(0,106,255,0.2);
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  font-size: 24px;
}
.sw-feature-card.highlight .sw-feature-icon-wrap { width: 64px; min-width: 64px; height: 64px; font-size: 30px; }
.sw-feature-badge {
  display: inline-block;
  background: rgba(148,255,150,0.1);
  border: 1px solid rgba(148,255,150,0.3);
  color: var(--green);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 20px;
  margin-bottom: 10px;
}
.sw-feature-content h3 { font-family: 'Prompt', sans-serif; font-weight: 700; font-size: 18px; color: var(--white); margin-bottom: 8px; }
.sw-feature-content p { font-size: 14px; color: var(--muted); line-height: 1.65; }
.sw-mini-heatmap { display: grid; grid-template-columns: repeat(24,1fr); gap: 2px; margin-top: 16px; }
.sw-mh-cell { aspect-ratio: 1; border-radius: 2px; }

/* COMPARATIVO */
.sw-comp-table { width: 100%; border-collapse: collapse; margin-top: 48px; }
.sw-comp-table th { font-family: 'Prompt', sans-serif; font-weight: 700; font-size: 15px; padding: 16px 24px; text-align: left; }
.sw-comp-table th:nth-child(2) {
  background: rgba(0,106,255,0.08);
  border: 1px solid rgba(0,106,255,0.2);
  border-bottom: none;
  color: var(--white);
  text-align: center;
  width: 200px;
}
.sw-comp-table th:nth-child(3) { color: var(--muted); text-align: center; width: 200px; }
.sw-comp-table th:first-child { color: var(--muted); font-size: 13px; }
.sw-comp-table td { padding: 14px 24px; font-size: 14px; border-bottom: 1px solid var(--border); }
.sw-comp-table td:first-child { color: var(--white); }
.sw-comp-table td:nth-child(2) {
  background: rgba(0,106,255,0.05);
  border-left: 1px solid rgba(0,106,255,0.2);
  border-right: 1px solid rgba(0,106,255,0.2);
  text-align: center;
}
.sw-comp-table td:nth-child(3) { text-align: center; color: var(--muted); }
.sw-check { color: var(--green); font-size: 18px; }
.sw-cross { color: #FF6B6B; font-size: 18px; }
.sw-partial { color: #FEBC2E; font-size: 13px; font-weight: 600; }

/* CREDIBILIDADE */
.sw-cred-header { display: flex; align-items: flex-start; justify-content: space-between; gap: 48px; margin-bottom: 56px; }
.sw-sap-badge {
  flex-shrink: 0;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 28px;
  display: flex; align-items: center; gap: 16px;
  min-width: 260px;
}
.sw-sap-icon {
  width: 48px; height: 48px;
  background: #0070A0;
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Prompt', sans-serif;
  font-weight: 800; font-size: 14px;
  color: var(--white);
}
.sw-sap-info strong { display: block; font-size: 15px; font-weight: 700; color: var(--white); }
.sw-sap-info span { font-size: 12px; color: var(--muted); }
.sw-clients-label { font-size: 12px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 24px; }
.sw-clients-row { display: flex; align-items: center; gap: 20px; flex-wrap: wrap; }
.sw-client-logo {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px 20px;
  font-family: 'Prompt', sans-serif;
  font-weight: 700; font-size: 13px;
  color: var(--muted);
  transition: border-color 0.2s, color 0.2s;
}
.sw-exp-stats { display: grid; grid-template-columns: repeat(3,1fr); gap: 24px; margin-top: 48px; }
.sw-exp-stat { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); padding: 28px; text-align: center; }
.sw-exp-stat-val { font-family: 'Prompt', sans-serif; font-weight: 800; font-size: 40px; color: var(--blue); line-height: 1; margin-bottom: 8px; }
.sw-exp-stat-label { font-size: 14px; color: var(--muted); line-height: 1.5; }

/* FORM */
.sw-form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: start; }
.sw-form-left h2 { margin-bottom: 16px; }
.sw-form-left > p { font-size: 16px; color: var(--muted); line-height: 1.7; margin-bottom: 40px; }
.sw-demo-includes { display: flex; flex-direction: column; gap: 14px; }
.sw-demo-item { display: flex; align-items: center; gap: 12px; font-size: 14px; color: var(--muted); }
.sw-demo-item::before {
  content: '✓';
  width: 22px; height: 22px; min-width: 22px;
  background: rgba(148,255,150,0.1);
  border: 1px solid rgba(148,255,150,0.3);
  color: var(--green);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 700;
}
.sw-form-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 40px;
  box-shadow: 0 24px 64px rgba(0,0,0,0.4);
}
.sw-form-card h3 { font-family: 'Prompt', sans-serif; font-weight: 700; font-size: 22px; color: var(--white); margin-bottom: 8px; }
.sw-form-card > p { font-size: 14px; color: var(--muted); margin-bottom: 32px; }
.sw-form-group { margin-bottom: 20px; }
.sw-wrap label { display: block; font-size: 13px; font-weight: 600; color: #A0B0CC; margin-bottom: 8px; letter-spacing: 0.02em; }
.sw-wrap input, .sw-wrap select {
  width: 100%;
  background: var(--surface);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 8px;
  padding: 12px 16px;
  color: var(--white);
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
  transition: border-color 0.2s;
  outline: none;
  -webkit-appearance: none;
}
.sw-wrap input::placeholder { color: #4A5A7A; }
.sw-wrap input:focus, .sw-wrap select:focus { border-color: var(--blue); box-shadow: 0 0 0 3px rgba(0,106,255,0.12); }
.sw-wrap select option { background: #1A1F35; }
.sw-form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.sw-btn-submit {
  width: 100%;
  background: var(--blue);
  color: var(--white) !important;
  border: none;
  border-radius: 8px;
  padding: 15px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700; font-size: 15px;
  cursor: pointer;
  margin-top: 8px;
  transition: background 0.2s, transform 0.15s;
  box-shadow: 0 4px 24px rgba(0,106,255,0.4);
}
.sw-btn-submit:hover { background: var(--blue-dim); transform: translateY(-2px); }
.sw-form-note { font-size: 12px; color: var(--muted); text-align: center; margin-top: 16px; line-height: 1.5; }

/* RESPONSIVE */
@media (max-width: 900px) {
  .sw-hero { grid-template-columns: 1fr; padding: 60px 20px 60px; gap: 48px; }
  .sw-dores-grid { grid-template-columns: 1fr; }
  .sw-solucao-grid { grid-template-columns: 1fr; gap: 40px; }
  .sw-features-grid { grid-template-columns: 1fr; }
  .sw-feature-card.highlight { flex-direction: column; gap: 24px; }
  .sw-form-grid { grid-template-columns: 1fr; gap: 40px; }
  .sw-cred-header { flex-direction: column; }
  .sw-exp-stats { grid-template-columns: 1fr; }
  .sw-beneficios-list { grid-template-columns: 1fr; }
  .sw-section { padding: 60px 20px; }
  .sw-divider { margin: 0 20px; }
  .sw-wrap { margin: 0 -15px; }
}
</style>

<div class="sw-wrap">

<!-- HERO -->
<div class="sw-section">
  <div class="sw-hero">
    <div class="sw-hero-content">
      <div class="sw-hero-eyebrow">✦ Solve Watch — Novo</div>
      <h1>
        Você só descobre que algo falhou quando<br>
        <em>o usuário reclama.</em>
      </h1>
      <p class="sw-hero-sub">
        O Solve Watch é a plataforma de observabilidade e governança para SAP Datasphere — visibilidade total do seu ambiente em uma tela, 24 horas por dia.
      </p>
      <div class="sw-hero-actions">
        <a href="#sw-demo" class="sw-btn-primary">Solicitar demonstração gratuita</a>
        <a href="#sw-funcionalidades" class="sw-btn-secondary">Ver como funciona →</a>
      </div>
      <div class="sw-hero-stats">
        <div>
          <div class="sw-hero-stat-value">24/7</div>
          <div class="sw-hero-stat-label">Monitoramento contínuo</div>
        </div>
        <div>
          <div class="sw-hero-stat-value">30min</div>
          <div class="sw-hero-stat-label">Atualização automática</div>
        </div>
        <div>
          <div class="sw-hero-stat-value">14+</div>
          <div class="sw-hero-stat-label">Funcionalidades nativas</div>
        </div>
      </div>
    </div>

    <div style="position:relative">
      <div class="sw-mockup-frame">
        <div class="sw-mockup-topbar">
          <div class="sw-dot sw-dot-r"></div>
          <div class="sw-dot sw-dot-y"></div>
          <div class="sw-dot sw-dot-g"></div>
          <span class="sw-mockup-title">Solve Watch — Dashboard</span>
        </div>
        <div class="sw-mockup-body">
          <div class="sw-dash-row">
            <div class="sw-dash-kpi"><div class="sw-dash-kpi-val green">94%</div><div class="sw-dash-kpi-label">Saúde das cargas</div></div>
            <div class="sw-dash-kpi"><div class="sw-dash-kpi-val red">3</div><div class="sw-dash-kpi-label">Falhas hoje</div></div>
            <div class="sw-dash-kpi"><div class="sw-dash-kpi-val blue">148</div><div class="sw-dash-kpi-label">Execuções / dia</div></div>
            <div class="sw-dash-kpi"><div class="sw-dash-kpi-val">14h30</div><div class="sw-dash-kpi-label">Próx. execução</div></div>
          </div>
          <div class="sw-mockup-label">Calendário de Cargas — Junho 2026</div>
          <div class="sw-calendar-grid">
            <div class="sw-cal-day empty">D</div><div class="sw-cal-day empty">S</div><div class="sw-cal-day empty">T</div><div class="sw-cal-day empty">Q</div><div class="sw-cal-day empty">Q</div><div class="sw-cal-day empty">S</div><div class="sw-cal-day empty">S</div>
            <div class="sw-cal-day ok">2</div><div class="sw-cal-day ok">3</div><div class="sw-cal-day ok">4</div><div class="sw-cal-day warn">5</div><div class="sw-cal-day ok">6</div><div class="sw-cal-day ok">7</div><div class="sw-cal-day err">8</div>
            <div class="sw-cal-day ok">9</div><div class="sw-cal-day ok">10</div><div class="sw-cal-day ok">11</div><div class="sw-cal-day ok">12</div><div class="sw-cal-day warn">13</div><div class="sw-cal-day ok">14</div><div class="sw-cal-day ok">15</div>
            <div class="sw-cal-day ok">16</div><div class="sw-cal-day ok">17</div><div class="sw-cal-day ok">18</div><div class="sw-cal-day ok">19</div><div class="sw-cal-day ok">20</div><div class="sw-cal-day err">21</div><div class="sw-cal-day ok">22</div>
          </div>
          <div class="sw-mockup-label" style="margin-top:14px">Heatmap de Concorrência</div>
          <div class="sw-heatmap-grid">
            <div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h4"></div><div class="sw-heat-cell h4"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div>
            <div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h4"></div><div class="sw-heat-cell h4"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div>
            <div class="sw-heat-cell h1"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div>
            <div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h4"></div><div class="sw-heat-cell h4"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h3"></div><div class="sw-heat-cell h2"></div><div class="sw-heat-cell h1"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div><div class="sw-heat-cell h0"></div>
          </div>
        </div>
      </div>
      <div class="sw-float-badge">
        <div class="sw-float-icon">✓</div>
        <div class="sw-float-text">
          <strong>Carga financeira recuperada</strong>
          <span>Detectado e corrigido em 4min</span>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="sw-divider"></div>

<!-- DORES -->
<div class="sw-section">
  <div class="sw-section-inner">
    <div class="sw-section-tag">O problema</div>
    <h2>Três situações que todo time<br>de Datasphere conhece bem</h2>
    <p class="sw-section-desc">Não é falta de competência. É falta de visibilidade. O Datasphere nativo não foi feito para monitoramento — e isso tem um custo real.</p>
    <div class="sw-dores-grid">
      <div class="sw-dor-card">
        <div class="sw-dor-number">01</div>
        <h3>Você fica sabendo tarde demais</h3>
        <p>Quando uma carga falha, o primeiro aviso não vem do sistema — vem do usuário reclamando que o dashboard está desatualizado. Às vezes a falha tem dias.</p>
        <div class="sw-dor-quote">"Descobrimos que o RF de fechamento estava falhando há 3 dias. O relatório do board estava errado."</div>
      </div>
      <div class="sw-dor-card">
        <div class="sw-dor-number">02</div>
        <h3>Capacity Units fora de controle</h3>
        <p>O cliente recebe alerta da SAP de que está perto do limite quando já ultrapassou. Sem visibilidade de quais objetos consomem mais, otimizar vira chute.</p>
        <div class="sw-dor-quote">"Estouramos o contratado no 18° dia do mês. Não sabíamos de onde veio o consumo extra."</div>
      </div>
      <div class="sw-dor-card">
        <div class="sw-dor-number">03</div>
        <h3>Governança impossível de comprovar</h3>
        <p>Auditoria interna, SOX, LGPD — e não há registro consolidado de como os dados são monitorados. O ambiente cresceu sem padrão e ninguém tem a visão do todo.</p>
        <div class="sw-dor-quote">"A auditoria perguntou como monitoramos os dados. Não tínhamos uma resposta boa."</div>
      </div>
    </div>
  </div>
</div>

<!-- SOLUÇÃO -->
<div class="sw-section sw-section-bg">
  <div class="sw-section-inner">
    <div class="sw-solucao-grid">
      <div>
        <div class="sw-section-tag">A solução</div>
        <h2>Os olhos do seu Datasphere, <em>24/7</em></h2>
        <div class="sw-tagline-box">
          <p>O Solve Watch é a plataforma que entrega o que a SAP nativa não dá: <span>visão integrada de saúde, performance, volumetria e custo</span> — em uma tela, sem que você precise montar um time dedicado para isso.</p>
        </div>
        <div class="sw-beneficios-list">
          <div class="sw-beneficio-item">
            <div class="sw-beneficio-icon">👁️</div>
            <div class="sw-beneficio-text"><strong>Visibilidade total</strong><span>Tudo em uma tela, sem abrir 10 painéis diferentes</span></div>
          </div>
          <div class="sw-beneficio-item">
            <div class="sw-beneficio-icon">🔔</div>
            <div class="sw-beneficio-text"><strong>Alertas proativos</strong><span>Você sabe antes do usuário reclamar</span></div>
          </div>
          <div class="sw-beneficio-item">
            <div class="sw-beneficio-icon">⚡</div>
            <div class="sw-beneficio-text"><strong>Performance identificada</strong><span>Objetos lentos com métricas reais de CPU e memória</span></div>
          </div>
          <div class="sw-beneficio-item">
            <div class="sw-beneficio-icon">💰</div>
            <div class="sw-beneficio-text"><strong>Capacity Units sob controle</strong><span>Antecipe o estouro antes da SAP cobrar</span></div>
          </div>
          <div class="sw-beneficio-item">
            <div class="sw-beneficio-icon">📋</div>
            <div class="sw-beneficio-text"><strong>Governança automática</strong><span>Padrões, nomenclatura e maturidade monitorados</span></div>
          </div>
          <div class="sw-beneficio-item">
            <div class="sw-beneficio-icon">📉</div>
            <div class="sw-beneficio-text"><strong>Menor custo operacional</strong><span>O time foca em estratégia, não em monitoramento manual</span></div>
          </div>
        </div>
      </div>
      <div class="sw-placeholder">
        <div class="sw-placeholder-icon">📸</div>
        <p><strong>Substituir por print real</strong><br>Tela de Resumo do Dia ou Saúde das Cargas</p>
      </div>
    </div>
  </div>
</div>

<!-- FUNCIONALIDADES -->
<div class="sw-section" id="sw-funcionalidades">
  <div class="sw-section-inner">
    <div class="sw-section-tag">Funcionalidades</div>
    <h2>Do primeiro acesso,<br>você já tem respostas</h2>
    <p class="sw-section-desc">Valor real desde o dia 1. Sem configuração complexa, sem necessidade de time dedicado.</p>
    <div class="sw-features-grid">
      <div class="sw-feature-card highlight">
        <div>
          <div class="sw-feature-badge">Diferencial único no mercado</div>
          <div class="sw-feature-icon-wrap">🗓️</div>
        </div>
        <div class="sw-feature-content" style="flex:1">
          <h3>Cronograma de Concorrência</h3>
          <p>Heatmap 7 dias × 24 horas mostrando quantos Replication Flows estão programados para rodar simultaneamente. Identifica janelas críticas de sobrecarga antes que o sistema entre em colapso — e permite redistribuir cargas com antecedência. Nenhuma outra ferramenta do mercado brasileiro faz isso.</p>
          <div class="sw-mini-heatmap" style="max-width:400px">
            <div class="sw-mh-cell" style="background:rgba(0,106,255,0.05)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.1)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.2)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.4)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.65)"></div><div class="sw-mh-cell" style="background:rgba(255,107,107,0.8)"></div><div class="sw-mh-cell" style="background:rgba(255,107,107,0.8)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.65)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.4)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.2)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.1)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.2)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.1)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.2)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.4)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.65)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.4)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.2)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.1)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.05)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.05)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.05)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.05)"></div><div class="sw-mh-cell" style="background:rgba(0,106,255,0.05)"></div>
          </div>
        </div>
      </div>
      <div class="sw-feature-card">
        <div class="sw-feature-icon-wrap">📅</div>
        <div class="sw-feature-content">
          <h3>Calendário de Cargas</h3>
          <p>Visão mensal de todas as execuções. Em 2 segundos você sabe se a semana foi tranquila ou problemática — sem abrir nenhum outro painel.</p>
        </div>
      </div>
      <div class="sw-feature-card">
        <div class="sw-feature-icon-wrap">⚡</div>
        <div class="sw-feature-content">
          <h3>Análise de Performance</h3>
          <p>Identifica os objetos mais lentos do ambiente — CDS Views, Analytic Models e Transformation Flows — com duração média, CPU e memória. Tuning onde realmente importa.</p>
        </div>
      </div>
      <div class="sw-feature-card">
        <div class="sw-feature-icon-wrap">📊</div>
        <div class="sw-feature-content">
          <h3>Controle de Capacity Units</h3>
          <p>Visão clara de consumo por objeto, por Space e por área de negócio. Atribua custo às áreas que consomem e antecipe o estouro antes da fatura chegar.</p>
        </div>
      </div>
      <div class="sw-feature-card">
        <div class="sw-feature-icon-wrap">📦</div>
        <div class="sw-feature-content">
          <h3>TOP 20 Volumetria</h3>
          <p>Ranking dos maiores objetos com tendência de crescimento. Planeje particionamento, arquivamento e remodelagem antes de virar problema de capacidade.</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- COMPARATIVO -->
<div class="sw-section sw-section-bg">
  <div class="sw-section-inner">
    <div class="sw-section-tag">Comparativo</div>
    <h2>O que o monitoramento<br>nativo da SAP <em>não entrega</em></h2>
    <p class="sw-section-desc">O Datasphere tem painéis nativos — mas eles mostram o que está acontecendo agora, sem histórico, sem alertas e sem análise.</p>
    <table class="sw-comp-table">
      <thead>
        <tr>
          <th>Capacidade</th>
          <th>✦ Solve Watch</th>
          <th>Datasphere Nativo</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Visão consolidada em uma tela</td><td><span class="sw-check">✓</span></td><td><span class="sw-cross">✗</span></td></tr>
        <tr><td>Histórico de até 6 meses</td><td><span class="sw-check">✓</span></td><td><span class="sw-cross">✗</span></td></tr>
        <tr><td>Alertas proativos de falha</td><td><span class="sw-check">✓</span></td><td><span class="sw-cross">✗</span></td></tr>
        <tr><td>Detecção de cargas crônicas (falha recorrente)</td><td><span class="sw-check">✓</span></td><td><span class="sw-cross">✗</span></td></tr>
        <tr><td>Heatmap de concorrência de execuções</td><td><span class="sw-check">✓</span></td><td><span class="sw-cross">✗</span></td></tr>
        <tr><td>Análise de performance por objeto</td><td><span class="sw-check">✓</span></td><td><span class="sw-partial">Parcial</span></td></tr>
        <tr><td>Controle e previsão de Capacity Units</td><td><span class="sw-check">✓</span></td><td><span class="sw-partial">Parcial</span></td></tr>
        <tr><td>Ranking de volumetria com tendência</td><td><span class="sw-check">✓</span></td><td><span class="sw-cross">✗</span></td></tr>
        <tr><td>Governança e score de maturidade</td><td><span class="sw-check">✓</span></td><td><span class="sw-cross">✗</span></td></tr>
        <tr><td>Validação de padrões de nomenclatura</td><td><span class="sw-check">✓</span></td><td><span class="sw-cross">✗</span></td></tr>
        <tr><td>Relatório pronto para auditoria</td><td><span class="sw-check">✓ (roadmap)</span></td><td><span class="sw-cross">✗</span></td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- CREDIBILIDADE -->
<div class="sw-section">
  <div class="sw-section-inner">
    <div class="sw-section-tag">Credibilidade</div>
    <h2>Construído por quem já vive<br>o SAP Datasphere na prática</h2>
    <div class="sw-cred-header">
      <div style="max-width:520px">
        <p style="color:var(--muted);font-size:16px;line-height:1.7;margin-bottom:32px;">O Solve Watch não é uma ferramenta genérica de monitoramento adaptada para SAP. Foi projetado pela Solveplan — especialista em SAP Datasphere no Brasil desde 2012 — para resolver problemas que só quem opera o produto em produção conhece.</p>
        <div class="sw-clients-label">Empresas que confiam na Solveplan para SAP Datasphere</div>
        <div class="sw-clients-row">
          <div class="sw-client-logo">Zilor</div>
          <div class="sw-client-logo">Usina Lins</div>
          <div class="sw-client-logo">Comporte</div>
          <div class="sw-client-logo">Pedro Agroindustrial</div>
          <div class="sw-client-logo">SJC Bioenergia</div>
        </div>
      </div>
      <div class="sw-sap-badge">
        <div class="sw-sap-icon">SAP</div>
        <div class="sw-sap-info">
          <strong>SAP Gold Partner</strong>
          <span>Parceiro certificado desde 2012</span>
        </div>
      </div>
    </div>
    <div class="sw-exp-stats">
      <div class="sw-exp-stat"><div class="sw-exp-stat-val">13+</div><div class="sw-exp-stat-label">Anos de experiência com plataformas SAP de dados</div></div>
      <div class="sw-exp-stat"><div class="sw-exp-stat-val">100%</div><div class="sw-exp-stat-label">Foco em SAP Analytics e Datasphere — não somos genéricos</div></div>
      <div class="sw-exp-stat"><div class="sw-exp-stat-val">+90</div><div class="sw-exp-stat-label">Clientes atendidos com soluções SAP de dados e analytics</div></div>
    </div>
  </div>
</div>

<!-- FORMULÁRIO -->
<div class="sw-section sw-section-form" id="sw-demo">
  <div class="sw-section-inner">
    <div class="sw-form-grid">
      <div class="sw-form-left">
        <div class="sw-section-tag">Demonstração gratuita</div>
        <h2>Veja o Solve Watch<br>no seu ambiente</h2>
        <p>Em uma sessão de 30 a 45 minutos, mostramos o produto funcionando com dados reais e respondemos todas as suas dúvidas técnicas e comerciais.</p>
        <div class="sw-demo-includes">
          <div class="sw-demo-item">Visão completa das funcionalidades disponíveis hoje</div>
          <div class="sw-demo-item">Como seria a implementação no seu ambiente</div>
          <div class="sw-demo-item">Roadmap de funcionalidades previstas</div>
          <div class="sw-demo-item">Modelo comercial e condições de contratação</div>
        </div>
      </div>
      <div class="sw-form-card">
        <h3>Solicitar demonstração</h3>
        <p>Retornamos em até 1 dia útil para agendar.</p>
        <form action="#" method="POST">
          <div class="sw-form-row">
            <div class="sw-form-group">
              <label for="sw-nome">Nome</label>
              <input type="text" id="sw-nome" name="nome" placeholder="Seu nome completo" required>
            </div>
            <div class="sw-form-group">
              <label for="sw-empresa">Empresa</label>
              <input type="text" id="sw-empresa" name="empresa" placeholder="Nome da empresa" required>
            </div>
          </div>
          <div class="sw-form-group">
            <label for="sw-email">E-mail corporativo</label>
            <input type="email" id="sw-email" name="email" placeholder="voce@empresa.com.br" required>
          </div>
          <div class="sw-form-row">
            <div class="sw-form-group">
              <label for="sw-cargo">Cargo</label>
              <select id="sw-cargo" name="cargo">
                <option value="" disabled selected>Selecione</option>
                <option>CIO / CDO / Diretor de TI</option>
                <option>Gerente de TI / Dados</option>
                <option>Coordenador de TI / Dados</option>
                <option>Arquiteto de Dados</option>
                <option>Analista / Consultor</option>
                <option>Outro</option>
              </select>
            </div>
            <div class="sw-form-group">
              <label for="sw-rfs">Nº de Replication Flows</label>
              <select id="sw-rfs" name="rfs">
                <option value="" disabled selected>Selecione</option>
                <option>Menos de 10</option>
                <option>10 a 50</option>
                <option>50 a 100</option>
                <option>Mais de 100</option>
              </select>
            </div>
          </div>
          <button type="submit" class="sw-btn-submit">Quero ver o Solve Watch em ação →</button>
          <p class="sw-form-note">Sem compromisso. Sem spam.<br>Seus dados são usados apenas para contato comercial.</p>
        </form>
      </div>
    </div>
  </div>
</div>

</div>
"""

def create_page():
    endpoint = f"{WP_URL}/wp-json/wp/v2/pages"
    payload = {
        "title": "Solve Watch — Observabilidade para SAP Datasphere",
        "slug": "solve-watch",
        "status": "draft",
        "content": HTML_CONTENT,
        "meta": {
            "rank_math_title": "Solve Watch: Monitoramento e Governança para SAP Datasphere | Solveplan",
            "rank_math_description": "Plataforma de observabilidade para SAP Datasphere. Alertas proativos, controle de Capacity Units e governança em tempo real. Desenvolvido pela Solveplan, SAP Gold Partner."
        }
    }
    resp = requests.post(
        endpoint,
        json=payload,
        auth=(WP_USER, WP_PASS),
        timeout=30
    )
    if resp.status_code in (200, 201):
        data = resp.json()
        print("OK - Pagina criada com sucesso!")
        print(f"  ID: {data.get('id')}")
        print(f"  Status: {data.get('status')}")
        print(f"  Editar: {WP_URL}/wp-admin/post.php?post={data.get('id')}&action=edit")
        print(f"  Preview: {data.get('link')}")
    else:
        print(f"ERRO {resp.status_code}")
        print(resp.text[:500])

if __name__ == "__main__":
    create_page()

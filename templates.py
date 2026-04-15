HTML_PAGE = '''<!DOCTYPE html>
<html lang="te">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>తెలుగు నేర్చుకుందాం — Telugu Learning</title>
<link href="https://fonts.googleapis.com/css2?family=Tiro+Telugu&family=Nunito:wght@400;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --saffron: #FF6B2B;
    --saffron-light: #FF8C5A;
    --saffron-glow: rgba(255, 107, 43, 0.18);
    --deep-teal: #0B4D5E;
    --teal: #1A7A8A;
    --teal-light: #2BA8BF;
    --cream: #FDF6EC;
    --cream-dark: #F5E6D0;
    --gold: #D4A017;
    --gold-light: #F0C040;
    --text-dark: #1C1C2E;
    --text-mid: #3D3D55;
    --text-soft: #7A7A9A;
    --white: #FFFFFF;
    --green-success: #2ECC71;
    --red-hint: #E74C3C;
    --shadow: 0 8px 40px rgba(11, 77, 94, 0.13);
    --shadow-card: 0 4px 24px rgba(11, 77, 94, 0.10);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'Nunito', sans-serif;
    background: var(--cream);
    color: var(--text-dark);
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* ─── DECORATIVE BG ─────────────────────────── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
      radial-gradient(ellipse 700px 400px at 10% 0%, rgba(255,107,43,0.09) 0%, transparent 70%),
      radial-gradient(ellipse 500px 500px at 90% 100%, rgba(26,122,138,0.10) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
  }

  /* ─── HEADER ────────────────────────────────── */
  header {
    background: linear-gradient(135deg, var(--deep-teal) 0%, var(--teal) 100%);
    padding: 0 2rem;
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 4px 24px rgba(11,77,94,0.35);
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .logo-emblem {
    width: 44px; height: 44px;
    background: var(--saffron);
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Tiro Telugu', serif;
    font-size: 22px;
    color: white;
    box-shadow: 0 4px 14px rgba(255,107,43,0.5);
  }

  .logo-text h1 {
    font-family: 'Tiro Telugu', serif;
    font-size: 20px;
    color: white;
    line-height: 1.1;
    letter-spacing: 0.3px;
  }
  .logo-text span {
    font-size: 11px;
    color: rgba(255,255,255,0.65);
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
  }

  .header-badge {
    background: rgba(255,255,255,0.13);
    border: 1px solid rgba(255,255,255,0.22);
    color: rgba(255,255,255,0.85);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.8px;
  }

  /* ─── MAIN LAYOUT ───────────────────────────── */
  .app-wrapper {
    position: relative;
    z-index: 1;
    max-width: 1200px;
    margin: 0 auto;
    padding: 2.5rem 1.5rem 4rem;
    display: grid;
    grid-template-columns: 320px 1fr;
    gap: 2.5rem;
    align-items: start;
  }

  /* ─── SIDEBAR ───────────────────────────────── */
  .sidebar {
    position: sticky;
    top: 88px;
  }

  /* Module Selector */
  .module-selector {
    background: var(--white);
    border-radius: 18px;
    padding: 10px;
    margin-bottom: 24px;
    box-shadow: var(--shadow-card);
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .module-btn {
    padding: 12px 16px;
    border-radius: 12px;
    border: 2px solid transparent;
    background: var(--cream);
    cursor: pointer;
    transition: all 0.2s;
    text-align: left;
    display: flex;
    flex-direction: column;
  }

  .module-btn:hover {
    background: var(--cream-dark);
  }

  .module-btn.active {
    border-color: var(--saffron);
    background: var(--saffron-glow);
  }

  .module-btn .m-te {
    font-family: 'Tiro Telugu', serif;
    font-size: 16px;
    font-weight: bold;
    color: var(--deep-teal);
  }

  .module-btn .m-en {
    font-size: 11px;
    color: var(--text-soft);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 2px;
  }

  .sidebar-title {
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--text-soft);
    margin-bottom: 16px;
    padding-left: 4px;
  }

  .lesson-card {
    background: var(--white);
    border-radius: 18px;
    padding: 20px 22px;
    margin-bottom: 12px;
    cursor: pointer;
    border: 3px solid transparent;
    transition: all 0.22s ease;
    box-shadow: var(--shadow-card);
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .lesson-card:hover {
    border-color: var(--teal-light);
    transform: translateX(6px);
    box-shadow: 0 8px 32px rgba(11,77,94,0.15);
  }

  .lesson-card.active {
    border-color: var(--saffron);
    background: linear-gradient(135deg, #fff7f2 0%, var(--white) 100%);
    box-shadow: 0 8px 32px var(--saffron-glow);
  }

  .lesson-icon {
    width: 48px; height: 48px;
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Tiro Telugu', serif;
    font-size: 20px;
    flex-shrink: 0;
    background: var(--cream-dark);
    color: var(--deep-teal);
    transition: all 0.22s;
  }
  .lesson-card.active .lesson-icon {
    background: var(--saffron);
    color: white;
  }

  .lesson-meta { flex: 1; min-width: 0; }
  .lesson-meta .title-te {
    font-family: 'Tiro Telugu', serif;
    font-size: 18px;
    color: var(--text-dark);
    line-height: 1.3;
  }
  .lesson-meta .title-en {
    font-size: 12px;
    color: var(--text-soft);
    margin-top: 4px;
  }

  .level-pill {
    font-size: 11px;
    font-weight: 800;
    padding: 4px 10px;
    border-radius: 20px;
    letter-spacing: 0.5px;
    flex-shrink: 0;
  }
  .level-pill.easy { background: #e8f8ef; color: #1a7a4a; }
  .level-pill.medium { background: #fff3e0; color: #b45309; }

  /* ─── MAIN PANEL ────────────────────────────── */
  .main-panel { min-width: 0; }

  .lesson-header {
    background: linear-gradient(135deg, var(--deep-teal) 0%, var(--teal) 60%, var(--teal-light) 100%);
    border-radius: 24px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.8rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(11,77,94,0.25);
  }

  .lesson-header::after {
    content: '';
    position: absolute;
    right: -30px; top: -30px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 65%);
    pointer-events: none;
  }

  .lesson-header-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 8px;
  }

  .lesson-title-te {
    font-family: 'Tiro Telugu', serif;
    font-size: 32px;
    color: white;
    line-height: 1.2;
  }

  .lesson-title-en {
    font-size: 14px;
    color: rgba(255,255,255,0.65);
    margin-top: 4px;
    font-weight: 600;
    letter-spacing: 0.5px;
  }

  .speak-all-btn {
    background: var(--saffron);
    border: none;
    color: white;
    padding: 10px 20px;
    border-radius: 12px;
    font-family: 'Nunito', sans-serif;
    font-weight: 800;
    font-size: 13px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s;
    box-shadow: 0 4px 14px rgba(255,107,43,0.45);
    flex-shrink: 0;
  }
  .speak-all-btn:hover { background: var(--saffron-light); transform: translateY(-1px); }
  .speak-all-btn:active { transform: translateY(0); }

  /* progress row */
  .progress-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 14px;
  }
  .progress-bar-track {
    flex: 1;
    height: 6px;
    background: rgba(255,255,255,0.2);
    border-radius: 10px;
    overflow: hidden;
  }
  .progress-bar-fill {
    height: 100%;
    background: var(--gold-light);
    border-radius: 10px;
    transition: width 0.5s ease;
  }
  .progress-label {
    font-size: 12px;
    color: rgba(255,255,255,0.7);
    font-weight: 700;
    white-space: nowrap;
  }

  /* ─── PARAGRAPH CARDS ───────────────────────── */
  .para-card {
    background: var(--white);
    border-radius: 20px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.2rem;
    box-shadow: var(--shadow-card);
    border: 2px solid transparent;
    transition: all 0.25s ease;
    position: relative;
  }

  .para-card.completed {
    border-color: var(--green-success);
    background: linear-gradient(135deg, #f0fff6 0%, var(--white) 100%);
  }

  .para-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 28px; height: 28px;
    border-radius: 50%;
    background: var(--cream-dark);
    color: var(--text-soft);
    font-size: 12px;
    font-weight: 800;
    margin-bottom: 14px;
    transition: all 0.25s;
  }
  .para-card.completed .para-number {
    background: var(--green-success);
    color: white;
  }

  /* Telugu text */
  .telugu-text {
    font-family: 'Tiro Telugu', serif;
    font-size: 24px;
    line-height: 1.9;
    color: var(--text-dark);
    margin-bottom: 1rem;
    cursor: default;
    white-space: pre-wrap;
  }

  .telugu-word {
    display: inline;
    border-radius: 4px;
    cursor: pointer;
    padding: 2px 4px;
    margin: 1px;
    transition: all 0.15s ease;
    border-bottom: 2px solid transparent;
  }

  .telugu-word:hover {
    background: rgba(255, 107, 43, 0.12);
    border-bottom-color: var(--saffron);
    color: var(--deep-teal);
  }

  .telugu-word.highlighted {
    background: var(--saffron-glow);
    border-bottom-color: var(--saffron);
  }

  /* Explanation Box */
  .explanation-section {
    margin-top: 20px;
    background: var(--white);
    border-radius: 16px;
    border: 1.5px solid var(--cream-dark);
    overflow: hidden;
  }

  .explanation-header {
    background: var(--cream-dark);
    padding: 10px 18px;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    font-weight: 800;
    color: var(--deep-teal);
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  .explanation-content {
    padding: 18px;
  }

  .exp-te {
    font-family: 'Tiro Telugu', serif;
    font-size: 18px;
    line-height: 1.7;
    color: var(--text-dark);
    margin-bottom: 12px;
    display: block;
  }

  .exp-en {
    font-size: 14px;
    line-height: 1.6;
    color: var(--text-mid);
    font-style: italic;
    display: block;
    border-top: 1px solid #eee;
    padding-top: 12px;
  }

  /* Action row */
  .para-actions {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 9px 16px;
    border-radius: 10px;
    border: none;
    font-family: 'Nunito', sans-serif;
    font-weight: 700;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.18s ease;
  }

  .btn-speak {
    background: var(--teal);
    color: white;
    box-shadow: 0 3px 12px rgba(26,122,138,0.3);
  }
  .btn-speak:hover { background: var(--deep-teal); transform: translateY(-1px); }
  .btn-speak.speaking {
    background: var(--saffron);
    animation: pulse-btn 1.2s infinite;
  }

  .btn-hint {
    background: var(--cream-dark);
    color: var(--text-mid);
  }
  .btn-hint:hover { background: #ead8be; }

  .btn-done {
    background: var(--green-success);
    color: white;
    box-shadow: 0 3px 12px rgba(46,204,113,0.3);
    margin-left: auto;
  }
  .btn-done:hover { background: #27ae60; }
  .btn-done.undone {
    background: white;
    color: var(--green-success);
    border: 2px solid var(--green-success);
    box-shadow: none;
  }

  @keyframes pulse-btn {
    0%, 100% { box-shadow: 0 3px 12px rgba(255,107,43,0.3); }
    50% { box-shadow: 0 3px 22px rgba(255,107,43,0.6); }
  }

  /* ─── TRANSLITERATION PANEL ─────────────────── */
  .hint-panel {
    display: none;
    margin-top: 14px;
    background: linear-gradient(135deg, #f0f9fb 0%, #e8f4f6 100%);
    border-radius: 14px;
    padding: 14px 18px;
    border-left: 4px solid var(--teal-light);
    animation: slideDown 0.25s ease;
  }

  .hint-panel.visible { display: block; }

  @keyframes slideDown {
    from { opacity: 0; transform: translateY(-8px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .hint-label {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--teal);
    margin-bottom: 6px;
  }

  .transliteration-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 15px;
    color: var(--deep-teal);
    line-height: 1.7;
    font-style: italic;
  }

  .translation-text {
    font-size: 13px;
    color: var(--text-soft);
    margin-top: 6px;
    font-weight: 600;
  }

  /* ─── WORD TOOLTIP ──────────────────────────── */
  .word-tooltip {
    position: fixed;
    background: var(--deep-teal);
    color: white;
    padding: 10px 14px;
    border-radius: 12px;
    font-size: 13px;
    pointer-events: none;
    z-index: 1000;
    opacity: 0;
    transition: opacity 0.15s ease;
    max-width: 220px;
    box-shadow: 0 8px 24px rgba(11,77,94,0.4);
  }
  .word-tooltip.visible { opacity: 1; }
  .word-tooltip .w-te {
    font-family: 'Tiro Telugu', serif;
    font-size: 16px;
    font-weight: bold;
    color: var(--gold-light);
    display: block;
    margin-bottom: 4px;
  }
  .word-tooltip .w-meaning {
    font-weight: 700;
    color: white;
    display: block;
  }
  .word-tooltip .w-roman {
    font-size: 11px;
    color: rgba(255,255,255,0.6);
    display: block;
    margin-top: 2px;
    font-style: italic;
    font-family: 'Space Grotesk', sans-serif;
  }

  /* ─── WORDS TABLE ───────────────────────────── */
  .words-section {
    margin-top: 16px;
    padding-top: 14px;
    border-top: 1.5px solid var(--cream-dark);
  }

  .words-toggle {
    display: flex;
    align-items: center;
    gap: 8px;
    cursor: pointer;
    user-select: none;
    margin-bottom: 0;
  }

  .words-toggle-label {
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--text-soft);
  }

  .words-toggle-icon {
    font-size: 13px;
    color: var(--text-soft);
    transition: transform 0.2s;
    margin-left: auto;
  }
  .words-toggle.open .words-toggle-icon { transform: rotate(180deg); }

  .words-grid {
    display: none;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 8px;
    margin-top: 12px;
  }
  .words-grid.visible { display: grid; }

  .word-chip {
    background: var(--cream);
    border-radius: 10px;
    padding: 10px 12px;
    cursor: pointer;
    transition: all 0.18s;
    border: 1.5px solid var(--cream-dark);
  }
  .word-chip:hover {
    background: var(--cream-dark);
    border-color: var(--teal-light);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(11,77,94,0.10);
  }

  .chip-te {
    font-family: 'Tiro Telugu', serif;
    font-size: 17px;
    color: var(--deep-teal);
    display: block;
    margin-bottom: 4px;
  }

  .chip-meaning {
    font-size: 12px;
    color: var(--text-soft);
    font-weight: 600;
    display: block;
  }

  .chip-roman {
    font-size: 11px;
    color: var(--teal-light);
    font-family: 'Space Grotesk', sans-serif;
    font-style: italic;
    display: block;
    margin-top: 2px;
  }

  /* ─── EMPTY / LOADING STATE ─────────────────── */
  .empty-state {
    text-align: center;
    padding: 5rem 2rem;
    color: var(--text-soft);
  }
  .empty-state .big-emoji { font-size: 56px; margin-bottom: 16px; }
  .empty-state p { font-size: 15px; line-height: 1.6; }

  /* ─── SPEECH STATUS ─────────────────────────── */
  .speech-status {
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: var(--deep-teal);
    color: white;
    padding: 12px 20px;
    border-radius: 14px;
    font-size: 13px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 10px;
    box-shadow: 0 8px 28px rgba(11,77,94,0.4);
    transform: translateY(80px);
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    z-index: 200;
  }
  .speech-status.active {
    transform: translateY(0);
    opacity: 1;
  }
  .speech-status .dots span {
    display: inline-block;
    width: 6px; height: 6px;
    background: var(--saffron);
    border-radius: 50%;
    margin: 0 2px;
    animation: bounce-dot 1.2s ease infinite;
  }
  .speech-status .dots span:nth-child(2) { animation-delay: 0.2s; }
  .speech-status .dots span:nth-child(3) { animation-delay: 0.4s; }

  @keyframes bounce-dot {
    0%, 80%, 100% { transform: scale(0.7); opacity: 0.5; }
    40% { transform: scale(1.2); opacity: 1; }
  }

  /* ─── RESPONSIVE ─────────────────────────────── */
  /* Desktop focused layout - No mobile-only overrides needed */
  .lessons-row {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .lesson-card {
    background: var(--white);
    border-radius: 18px;
    padding: 20px;
    cursor: pointer;
    border: 3px solid transparent;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: var(--shadow-card);
    display: flex;
    align-items: center;
    gap: 16px;
    width: 100%;
  }

  .lesson-card:hover {
    border-color: var(--teal-light);
    transform: translateY(-2px);
    box-shadow: 0 12px 32px rgba(11, 77, 94, 0.15);
  }

  .lesson-card.active {
    border-color: var(--saffron);
    background: linear-gradient(135deg, #fff7f2 0%, var(--white) 100%);
    box-shadow: 0 8px 32px var(--saffron-glow);
  }

  /* ─── CELEBRATION ────────────────────────────── */
  @keyframes celebrate {
    0% { transform: scale(1); }
    50% { transform: scale(1.06); }
    100% { transform: scale(1); }
  }
  .celebrating { animation: celebrate 0.5s ease; }

  /* scrollbar */
  ::-webkit-scrollbar { width: 6px; height: 6px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: var(--cream-dark); border-radius: 3px; }
</style>
</head>
<body>

<!-- HEADER -->
<header>
  <div class="logo">
    <div class="logo-emblem">త</div>
    <div class="logo-text">
      <h1>తెలుగు నేర్చుకుందాం</h1>
      <span>Telugu Learning · 8th Class</span>
    </div>
  </div>
  <div class="header-badge">🎓 Class VIII</div>
</header>

<!-- WORD TOOLTIP -->
<div class="word-tooltip" id="wordTooltip">
  <span class="w-te" id="tt-te"></span>
  <span class="w-meaning" id="tt-meaning"></span>
  <span class="w-roman" id="tt-roman"></span>
</div>

<!-- SPEECH STATUS -->
<div class="speech-status" id="speechStatus">
  <span>🔊 Reading aloud</span>
  <div class="dots">
    <span></span><span></span><span></span>
  </div>
</div>

<!-- APP WRAPPER -->
<div class="app-wrapper">

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="sidebar-title">📑 మాడ్యూల్ · Module</div>
    <div id="moduleSelector" class="module-selector"></div>

    <div class="sidebar-title">📚 పాఠాలు · Lessons</div>
    <div id="lessonsList" class="lessons-row"></div>
  </aside>

  <!-- MAIN PANEL -->
  <main class="main-panel">
    <div id="lessonView">
      <div class="empty-state">
        <div class="big-emoji">📖</div>
        <p>ఎడమ వైపు నుండి ఒక పాఠాన్ని ఎంచుకోండి<br>
        <span style="font-size:13px; color:#aaa;">Choose a lesson from the left to begin</span></p>
      </div>
    </div>
  </main>

</div>

<script>
// ─── STATE ───────────────────────────────────────────
let currentModuleId = null;
let currentLesson = null;
let completedParas = new Set();
let isSpeaking = false;
const tooltip = document.getElementById('wordTooltip');

// ─── INIT ────────────────────────────────────────────
async function init() {
  console.log('Fetching modules...');
  const res = await fetch('/api/modules');
  const modules = await res.json();
  renderModules(modules);

  if (modules.length > 0) {
    loadModule(modules[0].id);
  }
}

// ─── MODULES ─────────────────────────────────────────
function renderModules(modules) {
  const container = document.getElementById('moduleSelector');
  container.innerHTML = modules.map(m => `
    <div class="module-btn" onclick="loadModule('${m.id}')" id="mbtn-${m.id}">
      <span class="m-te">${m.title_te}</span>
      <span class="m-en">${m.title}</span>
    </div>
  `).join('');
}

async function loadModule(moduleId) {
  currentModuleId = moduleId;
  document.querySelectorAll('.module-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('mbtn-' + moduleId)?.classList.add('active');

  // Clear lesson view
  document.getElementById('lessonView').innerHTML = `
    <div class="empty-state">
      <div class="big-emoji">📖</div>
      <p>పాఠాన్ని ఎంచుకోండి<br>
      <span style="font-size:13px; color:#aaa;">Choose a lesson to begin</span></p>
    </div>
  `;

  console.log('Fetching lessons for module:', moduleId);
  const res = await fetch('/api/lessons/' + moduleId);
  const lessons = await res.json();
  renderSidebar(lessons);
}

// ─── SIDEBAR ─────────────────────────────────────────
function renderSidebar(lessons) {
  const list = document.getElementById('lessonsList');
  // Dynamic icons based on first letter of title
  list.innerHTML = lessons.map((l, i) => `
    <div class="lesson-card" onclick="loadLesson(${l.id})" id="lcard-${l.id}">
      <div class="lesson-icon">${l.title.charAt(0)}</div>
      <div class="lesson-meta">
        <div class="title-te">${l.title}</div>
        <div class="title-en">${l.title_meaning}</div>
      </div>
      <div class="level-pill ${l.level_en === 'Easy' ? 'easy' : (l.level_en === 'Medium' ? 'medium' : 'hard')}">${l.level}</div>
    </div>
  `).join('');
}

// ─── LOAD LESSON ─────────────────────────────────────
async function loadLesson(id) {
  document.querySelectorAll('.lesson-card').forEach(c => c.classList.remove('active'));
  document.getElementById('lcard-' + id)?.classList.add('active');

  const res = await fetch(`/api/lesson/${currentModuleId}/${id}`);
  currentLesson = await res.json();
  completedParas.clear();
  renderLesson();
}

// ─── RENDER LESSON ────────────────────────────────────
function renderLesson() {
  const l = currentLesson;
  const total = l.paragraphs.length;
  const done = completedParas.size;
  const pct = Math.round((done / total) * 100);

  const view = document.getElementById('lessonView');
  view.innerHTML = `
    <div class="lesson-header">
      <div class="lesson-header-top">
        <div>
          <div class="lesson-title-te">${l.title}</div>
          <div class="lesson-title-en">${l.title_meaning}</div>
        </div>
        <button class="speak-all-btn" onclick="speakAll()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
            <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
            <path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
          </svg>
          అన్నీ చదవండి
        </button>
      </div>
      <div class="progress-row">
        <div class="progress-bar-track">
          <div class="progress-bar-fill" id="progressFill" style="width:${pct}%"></div>
        </div>
        <div class="progress-label" id="progressLabel">${done}/${total} పూర్తయింది</div>
      </div>
    </div>

    <div id="parasContainer">
      ${l.paragraphs.map((p, i) => renderParaCard(p, i)).join('')}
    </div>
  `;
}

function renderParaCard(p, index) {
  const wordMap = {};
  p.words.forEach(w => { wordMap[w.word] = w; });

  // Build clickable Telugu text
  let tokens = tokenizeText(p.telugu, p.words);
  let htmlText = tokens.map(tok => {
    if (tok.type === 'word' && wordMap[tok.text]) {
      const w = wordMap[tok.text];
      return `<span class="telugu-word"
        data-word="${escHtml(w.word)}"
        data-meaning="${escHtml(w.meaning)}"
        data-roman="${escHtml(w.transliteration)}"
        onmouseenter="showTooltip(event, this)"
        onmouseleave="hideTooltip()"
        onclick="speakWord('${escJs(w.word)}')"
      >${tok.text}</span>`;
    }
    return `<span>${tok.text}</span>`;
  }).join('');

  const wordsHtml = p.words.map(w => `
    <div class="word-chip" onclick="speakWord('${escJs(w.word)}')">
      <span class="chip-te">${w.word}</span>
      <span class="chip-meaning">${w.meaning}</span>
      <span class="chip-roman">${w.transliteration}</span>
    </div>
  `).join('');

  const explanationHtml = (p.explanation_te || p.explanation_en) ? `
    <div class="explanation-section">
      <div class="explanation-header">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
        </svg>
        భావం · Meaning
      </div>
      <div class="explanation-content">
        ${p.explanation_te ? `<span class="exp-te">${p.explanation_te}</span>` : ''}
        ${p.explanation_en ? `<span class="exp-en">${p.explanation_en}</span>` : ''}
      </div>
    </div>
  ` : '';

  return `
    <div class="para-card" id="para-${p.id}">
      <div class="para-number">${index + 1}</div>

      <div class="telugu-text">${htmlText}</div>

      <div class="para-actions">
        <button class="btn btn-speak" onclick="speakPara('${escJs(p.id)}', '${escJs(p.telugu)}')" id="spk-${p.id}">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
            <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
          </svg>
          వినండి (Listen)
        </button>
        <button class="btn btn-hint" onclick="toggleHint('${p.id}')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <circle cx="12" cy="12" r="10"/>
            <line x1="12" y1="16" x2="12" y2="12"/>
            <line x1="12" y1="8" x2="12.01" y2="8"/>
          </svg>
          Pronunciation Help
        </button>
        <button class="btn btn-done ${completedParas.has(p.id) ? '' : 'undone'}" onclick="markDone('${p.id}')">
          ✓ చదివాను (Done)
        </button>
      </div>

      <div class="hint-panel" id="hint-${p.id}">
        <div class="hint-label">🔤 Pronunciation Guide (Roman Script)</div>
        <div class="transliteration-text" style="white-space: pre-wrap;">${p.transliteration}</div>
        <div class="translation-text">📖 Translation: ${p.translation}</div>
      </div>

      ${explanationHtml}

      <div class="words-section">
        <div class="words-toggle" onclick="toggleWords('${p.id}')">
          <span style="font-size:14px">📝</span>
          <span class="words-toggle-label">Word Meanings · పదాల అర్థాలు (${p.words.length} words)</span>
          <span class="words-toggle-icon">▼</span>
        </div>
        <div class="words-grid" id="words-${p.id}">
          ${wordsHtml}
        </div>
      </div>
    </div>
  `;
}

// ─── TOKENIZE ─────────────────────────────────────────
function tokenizeText(text, words) {
  // Split into segments, marking known words
  const sortedWords = [...words].sort((a, b) => b.word.length - a.word.length);
  let remaining = text;
  let result = [];

  while (remaining.length > 0) {
    let matched = false;
    for (const w of sortedWords) {
      if (remaining.startsWith(w.word)) {
        result.push({ type: 'word', text: w.word });
        remaining = remaining.slice(w.word.length);
        matched = true;
        break;
      }
    }
    if (!matched) {
      // Add punctuation/space as plain text
      if (result.length > 0 && result[result.length - 1].type === 'plain') {
        result[result.length - 1].text += remaining[0];
      } else {
        result.push({ type: 'plain', text: remaining[0] });
      }
      remaining = remaining.slice(1);
    }
  }
  return result;
}

// ─── TOOLTIP ──────────────────────────────────────────
function showTooltip(e, el) {
  document.getElementById('tt-te').textContent = el.dataset.word;
  document.getElementById('tt-meaning').textContent = el.dataset.meaning;
  document.getElementById('tt-roman').textContent = el.dataset.roman;
  tooltip.classList.add('visible');
  el.classList.add('highlighted');
  moveTooltip(e);
}

function hideTooltip() {
  tooltip.classList.remove('visible');
  document.querySelectorAll('.telugu-word.highlighted').forEach(el => el.classList.remove('highlighted'));
}

document.addEventListener('mousemove', (e) => {
  if (tooltip.classList.contains('visible')) moveTooltip(e);
});

function moveTooltip(e) {
  let x = e.clientX + 16, y = e.clientY - 10;
  if (x + 230 > window.innerWidth) x = e.clientX - 240;
  if (y + 100 > window.innerHeight) y = e.clientY - 100;
  tooltip.style.left = x + 'px';
  tooltip.style.top = y + 'px';
}

// ─── HINT PANEL ───────────────────────────────────────
function toggleHint(id) {
  const panel = document.getElementById('hint-' + id);
  panel.classList.toggle('visible');
}

function toggleWords(id) {
  const grid = document.getElementById('words-' + id);
  const toggle = grid.previousElementSibling;
  grid.classList.toggle('visible');
  toggle.classList.toggle('open');
}

// ─── MARK DONE ────────────────────────────────────────
function markDone(id) {
  const card = document.getElementById('para-' + id);
  const btn = card.querySelector('.btn-done');
  if (completedParas.has(id)) {
    completedParas.delete(id);
    card.classList.remove('completed');
    card.querySelector('.para-number').style.background = '';
    btn.classList.add('undone');
  } else {
    completedParas.add(id);
    card.classList.add('completed');
    card.classList.add('celebrating');
    btn.classList.remove('undone');
    setTimeout(() => card.classList.remove('celebrating'), 500);
  }
  updateProgress();
}

function updateProgress() {
  if (!currentLesson) return;
  const total = currentLesson.paragraphs.length;
  const done = completedParas.size;
  const pct = Math.round((done / total) * 100);
  const fill = document.getElementById('progressFill');
  const label = document.getElementById('progressLabel');
  if (fill) fill.style.width = pct + '%';
  if (label) label.textContent = `${done}/${total} పూర్తయింది`;
}

// ─── SPEECH ───────────────────────────────────────────
const speechStatus = document.getElementById('speechStatus');

function speak(text, onEnd) {
  if (!('speechSynthesis' in window)) {
    alert('మీ బ్రౌజర్ వాయిస్ సపోర్ట్ లేదు.\\\\nYour browser does not support text-to-speech.\\\\nPlease use Chrome or Edge.');
    return;
  }
  window.speechSynthesis.cancel();
  const utt = new SpeechSynthesisUtterance(text);

  // Try to find Telugu voice
  const voices = window.speechSynthesis.getVoices();
  const teVoice = voices.find(v => v.lang === 'te-IN' || v.lang.startsWith('te'));
  if (teVoice) utt.voice = teVoice;
  else {
    // fallback: Indian English
    const inVoice = voices.find(v => v.lang === 'en-IN');
    if (inVoice) utt.voice = inVoice;
  }

  utt.lang = 'te-IN';
  utt.rate = 0.82;
  utt.pitch = 1.05;

  utt.onstart = () => { speechStatus.classList.add('active'); isSpeaking = true; };
  utt.onend = () => {
    speechStatus.classList.remove('active');
    isSpeaking = false;
    if (onEnd) onEnd();
  };
  utt.onerror = () => {
    speechStatus.classList.remove('active');
    isSpeaking = false;
  };

  window.speechSynthesis.speak(utt);
}

function speakPara(id, text) {
  const btn = document.getElementById('spk-' + id);
  if (isSpeaking) {
    window.speechSynthesis.cancel();
    isSpeaking = false;
    speechStatus.classList.remove('active');
    document.querySelectorAll('.btn-speak').forEach(b => b.classList.remove('speaking'));
    return;
  }
  document.querySelectorAll('.btn-speak').forEach(b => b.classList.remove('speaking'));
  btn.classList.add('speaking');
  speak(text, () => btn.classList.remove('speaking'));
}

function speakWord(word) {
  speak(word);
}

function speakAll() {
  if (!currentLesson) return;
  const texts = currentLesson.paragraphs.map(p => p.telugu);
  let i = 0;
  function next() {
    if (i < texts.length) {
      speak(texts[i], () => { i++; setTimeout(next, 500); });
    }
  }
  next();
}

// Reload voices on change
window.speechSynthesis.onvoiceschanged = () => { /* voices ready */ };

// ─── HELPERS ──────────────────────────────────────────
function escHtml(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function escJs(s) {
  if (!s) return "";
  return String(s)
    .replace(/\\\\/g, '\\\\\\\\')
    .replace(/'/g, "\\\\'")
    .replace(/"/g, '\\\\x22')
    .replace(/`/g, '\\\\x60')
    .replace(/\\n/g, '\\\\n')
    .replace(/\\r/g, '\\\\r');
}

// ─── BOOT ─────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', init);
</script>
</body>
</html>
'''

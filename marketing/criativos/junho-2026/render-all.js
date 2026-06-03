const { execSync } = require('child_process');
const path = require('path');

const BASE = path.join(__dirname);

const scripts = [
  { name: 'Carrossel: Datasphere vs BDC (09/06)', file: '01-datasphere-vs-bdc/gerar.js' },
  { name: 'Carrossel: 5 Dores FP&A (17/06)',      file: '02-5-dores-fpa/gerar.js' },
  { name: 'Carrossel: Jornada BDC (24/06)',        file: '03-jornada-bdc/gerar.js' },
  { name: 'Text Covers — 12 posts de texto',       file: '04-text-covers/gerar.js' },
  { name: 'Poll Covers — 2 enquetes',              file: '05-polls/gerar.js' },
];

console.log('\n🎨  Gerando criativos — Junho 2026\n' + '─'.repeat(52));

let total = 0;
for (const s of scripts) {
  console.log(`\n▸ ${s.name}`);
  try {
    execSync(`node "${path.join(BASE, s.file)}"`, { stdio: 'inherit' });
    total++;
  } catch (err) {
    console.error(`  ✗ ERRO em ${s.file}:`, err.message);
  }
}

console.log('\n' + '─'.repeat(52));
console.log(`✅  ${total}/${scripts.length} scripts concluídos.`);
console.log('\n📁  Arquivos gerados em:');
console.log(`    ${path.join(BASE)}`);
console.log('    01-datasphere-vs-bdc/slides/ → 5 PNGs');
console.log('    02-5-dores-fpa/slides/       → 7 PNGs');
console.log('    03-jornada-bdc/slides/       → 6 PNGs');
console.log('    04-text-covers/cards/        → 12 PNGs');
console.log('    05-polls/cards/              → 2 PNGs');
console.log(`\n    Total: 32 imagens\n`);

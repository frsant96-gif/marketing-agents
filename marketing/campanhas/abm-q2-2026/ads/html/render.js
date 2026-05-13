const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const ads = [
  'seg-quimica-multinacionais',
  'seg-holdings-consumo',
  'seg-manufatura-automotivo',
  'seg-energia-utilities',
  'seg-agro-industrial',
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1200, height: 628 });

  for (const ad of ads) {
    const htmlPath = path.resolve(__dirname, `${ad}.html`);
    const pngPath = path.resolve(__dirname, `${ad}.png`);

    await page.goto(`file://${htmlPath}`);
    // Wait for Google Fonts to load
    await page.waitForTimeout(1500);

    await page.screenshot({ path: pngPath, clip: { x: 0, y: 0, width: 1200, height: 628 } });
    console.log(`✓ ${ad}.png`);
  }

  await browser.close();
  console.log('\nPronto! 5 PNGs gerados em ads/html/');
})();

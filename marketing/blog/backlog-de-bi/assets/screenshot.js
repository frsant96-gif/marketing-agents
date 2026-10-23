const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 628 } });
  await page.goto('file:///' + path.join(__dirname, 'featured.html').replace(/\/g, '/'));
  await page.screenshot({ path: path.join(__dirname, '..', 'imagem-destacada.png') });
  await browser.close();
  console.log('done');
})();

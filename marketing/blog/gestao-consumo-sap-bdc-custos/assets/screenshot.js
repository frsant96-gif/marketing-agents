const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  const htmlPath = path.join(__dirname, 'featured.html');
  await page.goto('file:///' + htmlPath.replace(/\\/g, '/'));
  await page.screenshot({ path: path.join(__dirname, 'featured.png') });
  await browser.close();
  console.log('done');
})();

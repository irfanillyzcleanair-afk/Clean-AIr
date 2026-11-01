// Screenshots each [htmlPath, outPath, width?, height?] job (default 1080x1350) (called by render.py).
const { chromium } = require('playwright');
const { pathToFileURL } = require('url');
(async () => {
  const jobs = JSON.parse(process.argv[2]);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const [html, out, w = 1080, h = 1350] of jobs) {
    await page.setViewportSize({ width: w, height: h });
    await page.goto(pathToFileURL(html).href, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: out, type: 'jpeg', quality: 92 });
    console.log('rendered', out.split('/').pop());
  }
  await browser.close();
})();

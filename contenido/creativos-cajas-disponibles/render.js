// Exporta cada _*.html a png/<nombre>.png (1920x1080)
const { chromium } = require('playwright');
const path = require('path');
const lista = require('./_lista.json');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  for (const k of (process.argv[2] ? [process.argv[2]] : lista)) {
    await p.goto('file://' + path.join(__dirname, `_${k}.html`));
    await p.waitForLoadState('networkidle');
    await p.screenshot({ path: path.join(__dirname, 'png', `${k}.png`) });
  }
  await b.close();
})();

// Exporta cada _*.html a PNG. Horizontales (1920x1080) a png/, historias H-* (1080x1920) a png/historias/
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const lista = require('./_lista.json');
(async () => {
  const b = await chromium.launch();
  fs.mkdirSync(path.join(__dirname, 'png', 'historias'), { recursive: true });
  for (const k of (process.argv[2] ? [process.argv[2]] : lista)) {
    const h = k.startsWith('H-');
    const p = await b.newPage({ viewport: h ? { width: 1080, height: 1920 } : { width: 1920, height: 1080 } });
    await p.goto('file://' + path.join(__dirname, `_${k}.html`));
    await p.waitForLoadState('networkidle');
    await p.screenshot({ path: path.join(__dirname, 'png', h ? 'historias' : '', `${h ? k.slice(2) : k}.png`) });
    await p.close();
  }
  await b.close();
})();

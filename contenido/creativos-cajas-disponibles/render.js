// Exporta cada _*.html a PNG: horizontales (1920x1080) a png/, historias H-* (1080x1920) a png/historias/,
// carrusel K-* (1080x1350) a png/carrusel/
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const lista = [...require('./_lista.json'), ...(fs.existsSync(path.join(__dirname, '_lista_carrusel.json')) ? require('./_lista_carrusel.json') : [])];
(async () => {
  const b = await chromium.launch();
  for (const k of (process.argv[2] ? [process.argv[2]] : lista)) {
    const tipo = k.startsWith('H-') ? 'historias' : k.startsWith('K-') ? 'carrusel' : '';
    const vp = { historias: [1080, 1920], carrusel: [1080, 1350], '': [1920, 1080] }[tipo];
    fs.mkdirSync(path.join(__dirname, 'png', tipo), { recursive: true });
    // Horizontales al doble de resolución (3840x2160) para que se vean nítidos
    const p = await b.newPage({ viewport: { width: vp[0], height: vp[1] }, deviceScaleFactor: tipo === '' ? 2 : 1 });
    await p.goto('file://' + path.join(__dirname, `_${k}.html`));
    await p.waitForLoadState('networkidle');
    await p.screenshot({ path: path.join(__dirname, 'png', tipo, `${tipo ? k.slice(2) : k}.png`) });
    await p.close();
  }
  await b.close();
})();

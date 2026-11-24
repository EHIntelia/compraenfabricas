// Convierte el HTML del acuerdo a documento imprimible tamaño carta.
// Uso: node a-pdf.js entrada.html salida.pdf   (requiere playwright)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [entrada, salida] = process.argv.slice(2);
  if (!entrada || !salida) { console.error('Uso: node a-pdf.js entrada.html salida.pdf'); process.exit(1); }
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(entrada));
  await p.pdf({ path: salida, format: 'Letter', printBackground: true, scale: 0.85,
    margin: { top: '14mm', bottom: '14mm', left: '14mm', right: '14mm' } });
  await b.close();
  console.log('Listo:', salida);
})();

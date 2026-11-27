// Convierte el HTML del acuerdo a documento imprimible tamaño carta.
// Si no cabe en una hoja, reduce la escala poco a poco (hasta 0.70).
// Uso: node a-pdf.js entrada.html salida.pdf   (requiere playwright)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const [entrada, salida] = process.argv.slice(2);
  if (!entrada || !salida) { console.error('Uso: node a-pdf.js entrada.html salida.pdf'); process.exit(1); }
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(entrada));
  let buf, escala;
  for (escala of [0.85, 0.8, 0.76, 0.73, 0.7]) {
    buf = await p.pdf({ format: 'Letter', printBackground: true, scale: escala,
      margin: { top: '12mm', bottom: '12mm', left: '14mm', right: '14mm' } });
    const hojas = (buf.toString('latin1').match(/\/Type\s*\/Page[^s]/g) || []).length;
    if (hojas <= 1) break;
  }
  fs.writeFileSync(salida, buf);
  await b.close();
  console.log('Listo:', salida, '(escala ' + escala + ')');
})();

const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[2] + '/hoja.html'); await p.waitForTimeout(300);
  await p.pdf({ path: process.argv[2] + '/HOJA_DE_TRABAJO_CLASE_EN_VIVO.pdf', format: 'Letter', printBackground: true, margin: {top:0,bottom:0,left:0,right:0} });
  await b.close();
})();

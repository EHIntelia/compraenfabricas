const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path'); const { execSync } = require('child_process');
const SRC = process.argv[2], OUT = process.argv[3];
const ALL = [
 ['ComentaA_Curso_Chroma',400],['ComentaB_Curso_Chroma',360],['ComentaD_Curso_Chroma',520],
 ['ComentaA_Full_Curso_Chroma',640],['ComentaB_Full_Curso_Chroma',640],['ComentaD_Full_Curso_Chroma',640]];
const wanted = process.argv.slice(4);
const canvas = JSON.parse(fs.readFileSync(path.join(SRC,'canvas.json'),'utf8'));
const items = (wanted.length?wanted:ALL.map(x=>x[0])).map(n=>[n,canvas.boards[n+'.dc.html'].h]);
(async () => {
  const browser = await chromium.launch();
  fs.mkdirSync(OUT,{recursive:true});
  for (const [name,h] of items) {
    const src = fs.readFileSync(path.join(SRC,name+'.dc.html'),'utf8');
    const style = src.match(/<helmet>\s*<style>([\s\S]*?)<\/style>/)[1];
    const body = src.match(/<\/helmet>([\s\S]*?)<\/x-dc>/)[1];
    const html = `<!doctype html><html><head><meta charset="utf-8"><style>${style}</style></head><body>${body}</body></html>`;
    const page = await browser.newPage({viewport:{width:1080,height:h},deviceScaleFactor:1});
    await page.setContent(html); await page.waitForTimeout(300);
    const dir = path.join(OUT,'frames_'+name); fs.rmSync(dir,{recursive:true,force:true}); fs.mkdirSync(dir);
    const fps=30, N=6*fps;
    for (let i=0;i<N;i++){
      await page.evaluate(t=>{for(const a of document.getAnimations()){a.pause();a.currentTime=t;}}, i*1000/fps);
      await page.screenshot({path:path.join(dir,String(i).padStart(4,'0')+'.png')});
    }
    await page.close();
    execSync(`ffmpeg -y -loglevel error -framerate ${fps} -i ${dir}/%04d.png -c:v libx264 -pix_fmt yuv420p -crf 16 ${path.join(OUT,name+'.mp4')}`);
    fs.rmSync(dir,{recursive:true,force:true});
    console.log('ok',name);
  }
  await browser.close();
})();

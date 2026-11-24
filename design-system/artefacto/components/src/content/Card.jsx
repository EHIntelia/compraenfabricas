import React from 'react';
export function Card({tone='white',padding=24,children,style}){
  const t={white:{background:'#fff',border:'1px solid var(--cef-borde)'},cream:{background:'var(--cef-crema)',border:'1px solid var(--cef-borde)'},peach:{background:'var(--cef-durazno)',border:'1px solid transparent'},dark:{background:'var(--cef-tinta)',color:'#fff',border:'1px solid transparent'}}[tone];
  return <div style={{borderRadius:'var(--radius-lg)',padding,boxShadow:tone==='white'?'var(--shadow-sm)':'none',fontFamily:'var(--font-sans)',...t,...style}}>{children}</div>;
}
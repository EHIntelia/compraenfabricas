import React from 'react';
export function Badge({variant='peach',children,style}){
  const v={peach:{background:'var(--cef-durazno)',color:'var(--cef-naranja-700)'},gradient:{background:'var(--gradient-estrella)',color:'#fff'},dark:{background:'var(--cef-tinta)',color:'#fff'},outline:{background:'#fff',color:'var(--cef-naranja-700)',boxShadow:'inset 0 0 0 1.5px var(--cef-naranja-700)'},success:{background:'var(--cef-verde-bg)',color:'var(--cef-verde)'}}[variant];
  return <span style={{display:'inline-flex',alignItems:'center',gap:6,fontFamily:'var(--font-sans)',fontWeight:700,fontSize:12,letterSpacing:'var(--ls-badge)',textTransform:'uppercase',padding:'6px 12px',borderRadius:'var(--radius-pill)',lineHeight:1.2,whiteSpace:'nowrap',...v,...style}}>{children}</span>;
}
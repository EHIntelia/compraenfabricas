import React from 'react';
export function PeachBox({title,children,style}){
  return <div style={{background:'var(--cef-durazno)',borderLeft:'5px solid var(--cef-naranja)',borderRadius:'var(--radius-md)',padding:'18px 20px',fontFamily:'var(--font-sans)',fontSize:16,lineHeight:1.5,color:'var(--cef-tinta)',...style}}>{title&&<div style={{fontWeight:700,color:'var(--cef-naranja-700)',marginBottom:4}}>{title}</div>}{children}</div>;
}
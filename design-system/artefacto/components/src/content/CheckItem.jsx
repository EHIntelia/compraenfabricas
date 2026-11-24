import React from 'react';
export function CheckItem({children,style}){
  return <div style={{display:'flex',gap:12,alignItems:'flex-start',fontFamily:'var(--font-sans)',fontSize:16,lineHeight:1.45,...style}}><span style={{flex:'none',width:22,height:22,borderRadius:999,background:'var(--gradient-estrella)',color:'#fff',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:13,fontWeight:700,marginTop:1}}>✓</span><span>{children}</span></div>;
}
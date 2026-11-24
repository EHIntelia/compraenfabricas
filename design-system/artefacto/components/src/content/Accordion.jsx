import React from 'react';
export function Accordion({items=[],defaultOpen=-1}){
  const [o,setO]=React.useState(defaultOpen);
  return <div style={{display:'grid',gap:10,fontFamily:'var(--font-sans)'}}>{items.map((it,i)=>{const open=o===i;return <div key={i} style={{background:'#fff',border:'1px solid '+(open?'var(--cef-naranja)':'var(--cef-borde)'),borderRadius:'var(--radius-md)',overflow:'hidden',transition:'border-color var(--dur-base)'}}>
    <button onClick={()=>setO(open?-1:i)} style={{all:'unset',boxSizing:'border-box',width:'100%',cursor:'pointer',display:'flex',justifyContent:'space-between',alignItems:'center',gap:12,padding:'16px 18px',fontWeight:700,fontSize:16,color:'var(--cef-tinta)'}}>{it.q}<span style={{flex:'none',width:28,height:28,borderRadius:999,background:open?'var(--gradient-estrella)':'var(--cef-durazno)',color:open?'#fff':'var(--cef-naranja-700)',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:18,transition:'transform var(--dur-base)',transform:open?'rotate(45deg)':'none'}}>+</span></button>
    {open&&<div style={{padding:'0 18px 18px',color:'var(--cef-gris)',fontSize:15,lineHeight:1.55}}>{it.a}</div>}</div>})}</div>;
}
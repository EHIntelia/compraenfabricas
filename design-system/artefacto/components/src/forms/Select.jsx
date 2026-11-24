import React from 'react';
export function Select({label,options=[],value,onChange,placeholder}){
  const [f,setF]=React.useState(false);
  return <label style={{display:'grid',gap:6,fontFamily:'var(--font-sans)'}}>{label&&<span style={{fontWeight:700,fontSize:14}}>{label}</span>}
    <select value={value} onChange={onChange} onFocus={()=>setF(true)} onBlur={()=>setF(false)} style={{...{display:'block',width:'100%',fontFamily:'var(--font-sans)',fontSize:16,padding:'14px 16px',borderRadius:'var(--radius-md)',background:'#fff',color:'var(--cef-tinta)',outline:'none',transition:'border-color var(--dur-fast),box-shadow var(--dur-fast)'},appearance:'none',paddingRight:40,border:'1.5px solid '+(f?'var(--cef-naranja)':'var(--cef-borde)'),boxShadow:f?'0 0 0 4px rgba(249,115,22,.15)':'none',backgroundImage:'linear-gradient(45deg,transparent 50%,#EA580C 50%),linear-gradient(135deg,#EA580C 50%,transparent 50%)',backgroundPosition:'calc(100% - 22px) 50%,calc(100% - 16px) 50%',backgroundSize:'6px 6px',backgroundRepeat:'no-repeat'}}>
    {placeholder&&<option value="">{placeholder}</option>}{options.map(o=><option key={o} value={o}>{o}</option>)}</select></label>;
}
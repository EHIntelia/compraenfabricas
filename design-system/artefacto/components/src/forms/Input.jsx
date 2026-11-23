import React from 'react';
export function Input({label,placeholder,type='text',value,onChange,error,hint,disabled}){
  const [f,setF]=React.useState(false);
  return <label style={{display:'grid',gap:6,fontFamily:'var(--font-sans)'}}>{label&&<span style={{fontWeight:700,fontSize:14}}>{label}</span>}
    <input type={type} placeholder={placeholder} value={value} onChange={onChange} disabled={disabled} onFocus={()=>setF(true)} onBlur={()=>setF(false)} style={{...{display:'block',width:'100%',fontFamily:'var(--font-sans)',fontSize:16,padding:'14px 16px',borderRadius:'var(--radius-md)',background:'#fff',color:'var(--cef-tinta)',outline:'none',transition:'border-color var(--dur-fast),box-shadow var(--dur-fast)'},border:'1.5px solid '+(error?'var(--cef-naranja-700)':f?'var(--cef-naranja)':'var(--cef-borde)'),boxShadow:f?'0 0 0 4px rgba(249,115,22,.15)':'none',opacity:disabled?.5:1}}/>
    {(error||hint)&&<span style={{fontSize:13,color:error?'var(--cef-naranja-700)':'var(--cef-gris)'}}>{error||hint}</span>}</label>;
}
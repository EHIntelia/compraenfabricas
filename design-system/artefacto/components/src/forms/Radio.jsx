import React from 'react';
export function Radio({options=[],value,defaultValue,onChange,name='radio'}){
  const [v,setV]=React.useState(defaultValue);const cur=value??v;
  return <div style={{display:'grid',gap:10,fontFamily:'var(--font-sans)'}}>{options.map(o=>{const on=cur===o;return <label key={o} style={{display:'flex',gap:12,alignItems:'center',padding:'14px 16px',borderRadius:'var(--radius-md)',border:'1.5px solid '+(on?'var(--cef-naranja)':'var(--cef-borde)'),background:on?'var(--cef-crema)':'#fff',cursor:'pointer',fontSize:15,fontWeight:on?700:400}}>
    <span style={{flex:'none',width:20,height:20,borderRadius:999,border:'2px solid '+(on?'var(--cef-naranja)':'var(--cef-borde)'),display:'inline-flex',alignItems:'center',justifyContent:'center'}}>{on&&<span style={{width:10,height:10,borderRadius:999,background:'var(--gradient-estrella)'}}></span>}</span>
    <input type="radio" name={name} checked={on} onChange={()=>{setV(o);onChange&&onChange(o)}} style={{display:'none'}}/>{o}</label>})}</div>;
}
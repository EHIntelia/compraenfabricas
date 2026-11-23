import React from 'react';
export function Checkbox({label,checked,defaultChecked=false,onChange,disabled}){
  const [c,setC]=React.useState(defaultChecked);const on=checked??c;
  return <label style={{display:'flex',gap:10,alignItems:'center',fontFamily:'var(--font-sans)',fontSize:15,cursor:disabled?'not-allowed':'pointer',opacity:disabled?.5:1}}>
    <span style={{flex:'none',width:22,height:22,borderRadius:6,background:on?'var(--gradient-estrella)':'#fff',border:on?'none':'1.5px solid var(--cef-borde)',color:'#fff',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:13,fontWeight:700}}>{on?'✓':''}</span>
    <input type="checkbox" checked={on} disabled={disabled} onChange={e=>{setC(e.target.checked);onChange&&onChange(e.target.checked)}} style={{display:'none'}}/>{label}</label>;
}
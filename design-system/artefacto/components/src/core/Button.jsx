import React from 'react';
const sizes={sm:{padding:'10px 18px',fontSize:14},md:{padding:'14px 24px',fontSize:16},lg:{padding:'18px 32px',fontSize:18}};
export function Button({variant='primary',size='md',fullWidth=false,disabled=false,icon,children,onClick,type='button',style}){
  const [h,setH]=React.useState(false);const [p,setP]=React.useState(false);
  const base={display:'inline-flex',alignItems:'center',justifyContent:'center',gap:8,fontFamily:'var(--font-sans)',fontWeight:700,borderRadius:'var(--radius-pill)',border:'2px solid transparent',cursor:disabled?'not-allowed':'pointer',width:fullWidth?'100%':undefined,transition:'transform var(--dur-fast) var(--ease-out),box-shadow var(--dur-base),background var(--dur-base)',transform:p&&!disabled?'scale(.98)':'none',opacity:disabled?.45:1,lineHeight:1.2,...sizes[size]};
  const v={primary:{background:h&&!disabled?'var(--gradient-estrella-hover)':'var(--gradient-estrella)',color:'#fff',boxShadow:h&&!disabled?'0 10px 28px rgba(234,88,12,.35)':'var(--shadow-accent)'},
    secondary:{background:h&&!disabled?'var(--cef-durazno)':'#fff',color:'var(--cef-naranja-700)',borderColor:'var(--cef-naranja)'},
    dark:{background:h&&!disabled?'#000':'var(--cef-tinta)',color:'#fff'},
    ghost:{background:h&&!disabled?'var(--cef-durazno)':'transparent',color:'var(--cef-naranja-700)'}}[variant];
  return <button type={type} disabled={disabled} onClick={onClick} onMouseEnter={()=>setH(true)} onMouseLeave={()=>{setH(false);setP(false)}} onMouseDown={()=>setP(true)} onMouseUp={()=>setP(false)} style={{...base,...v,...style}}>{icon}{children}</button>;
}
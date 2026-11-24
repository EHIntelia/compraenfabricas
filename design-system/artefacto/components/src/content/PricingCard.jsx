import React from 'react';
import {Badge} from '../core/Badge.jsx';
import {Button} from '../core/Button.jsx';
import {CheckItem} from './CheckItem.jsx';
export function PricingCard({name,price,oldPrice,period,features=[],cta='Inscribirme',featured=false,badge,onSelect}){
  return <div style={{position:'relative',background:'#fff',borderRadius:'var(--radius-xl)',padding:'28px 24px',border:featured?'2px solid var(--cef-naranja)':'1px solid var(--cef-borde)',boxShadow:featured?'var(--shadow-lg)':'var(--shadow-sm)',fontFamily:'var(--font-sans)',display:'flex',flexDirection:'column',gap:16}}>
    {(badge||featured)&&<div style={{position:'absolute',top:-13,left:24}}><Badge variant={featured?'gradient':'peach'}>{badge||'Más popular'}</Badge></div>}
    <div style={{fontWeight:700,fontSize:18}}>{name}</div>
    <div style={{display:'flex',alignItems:'baseline',gap:8}}>{oldPrice&&<span style={{color:'var(--cef-gris)',textDecoration:'line-through',fontSize:16}}>{oldPrice}</span>}<span style={{fontWeight:900,fontSize:40,letterSpacing:'-0.02em',color:featured?'var(--cef-naranja-700)':'var(--cef-tinta)'}}>{price}</span>{period&&<span style={{color:'var(--cef-gris)',fontSize:14}}>{period}</span>}</div>
    <div style={{display:'grid',gap:10}}>{features.map((f,i)=><CheckItem key={i}>{f}</CheckItem>)}</div>
    <Button variant={featured?'primary':'secondary'} fullWidth onClick={onSelect}>{cta}</Button>
  </div>;
}
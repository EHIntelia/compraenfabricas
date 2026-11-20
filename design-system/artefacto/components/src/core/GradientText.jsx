import React from 'react';
export function GradientText({children,style}){
  return <span style={{background:'var(--gradient-estrella)',WebkitBackgroundClip:'text',backgroundClip:'text',color:'transparent',WebkitTextFillColor:'transparent',...style}}>{children}</span>;
}
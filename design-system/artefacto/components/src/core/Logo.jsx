import React from 'react';
const files={horizontal:'logo-horizontal.png',vertical:'logo-vertical.png',icon:'icono.png'};
export function Logo({variant='horizontal',height=32,basePath='assets/',style}){
  return <img src={basePath+files[variant]} alt="Compra en fábricas" style={{height,width:'auto',display:'block',...style}}/>;
}
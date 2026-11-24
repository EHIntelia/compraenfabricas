import * as React from 'react';
/** Contenedor redondeado con borde suave. */
export interface CardProps{tone?:'white'|'cream'|'peach'|'dark';padding?:number;children?:React.ReactNode;style?:React.CSSProperties}
export declare function Card(props:CardProps):JSX.Element;
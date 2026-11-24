import * as React from 'react';
/** Etiqueta en mayúsculas: CLASE EN VIVO, MÁS POPULAR, REGALO DE BIENVENIDA. */
export interface BadgeProps{variant?:'peach'|'gradient'|'dark'|'outline'|'success';children?:React.ReactNode;style?:React.CSSProperties}
export declare function Badge(props:BadgeProps):JSX.Element;
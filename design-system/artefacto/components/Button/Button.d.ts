import * as React from 'react';
/** Botón principal de la marca. Primary usa el degradado estrella.
 * @startingPoint section="Core" subtitle="Gradient pill CTA" viewport="700x260" */
export interface ButtonProps{variant?:'primary'|'secondary'|'dark'|'ghost';size?:'sm'|'md'|'lg';fullWidth?:boolean;disabled?:boolean;icon?:React.ReactNode;children?:React.ReactNode;onClick?:()=>void;type?:'button'|'submit';style?:React.CSSProperties}
export declare function Button(props:ButtonProps):JSX.Element;
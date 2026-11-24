import * as React from 'react';
/** Preguntas frecuentes plegables. */
export interface AccordionProps{items?:{q:React.ReactNode;a:React.ReactNode}[];defaultOpen?:number}
export declare function Accordion(props:AccordionProps):JSX.Element;
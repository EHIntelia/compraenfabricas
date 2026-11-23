import * as React from 'react';
/** Grupo de opciones tipo tarjeta (encuestas, calificación de leads). */
export interface RadioProps{options?:string[];value?:string;defaultValue?:string;onChange?:(v:string)=>void;name?:string}
export declare function Radio(props:RadioProps):JSX.Element;
import * as React from 'react';
/** Campo de texto para formularios de registro. */
export interface InputProps{label?:string;placeholder?:string;type?:string;value?:string;onChange?:(e:React.ChangeEvent<HTMLInputElement>)=>void;error?:string;hint?:string;disabled?:boolean}
export declare function Input(props:InputProps):JSX.Element;
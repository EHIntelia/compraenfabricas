import * as React from 'react';
/** Casilla con relleno en degradado al marcar. */
export interface CheckboxProps{label?:React.ReactNode;checked?:boolean;defaultChecked?:boolean;onChange?:(v:boolean)=>void;disabled?:boolean}
export declare function Checkbox(props:CheckboxProps):JSX.Element;
import * as React from 'react';
/** Logo oficial (PNG). basePath apunta a la carpeta assets/ relativa a la página. */
export interface LogoProps{variant?:'horizontal'|'vertical'|'icon';height?:number;basePath?:string;style?:React.CSSProperties}
export declare function Logo(props:LogoProps):JSX.Element;
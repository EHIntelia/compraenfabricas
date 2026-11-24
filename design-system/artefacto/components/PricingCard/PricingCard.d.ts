import * as React from 'react';
/** Tarjeta de plan/precio para landings de cursos y mentorías.
 * @startingPoint section="Content" subtitle="Plan card with gradient badge" viewport="700x460" */
export interface PricingCardProps{name:string;price:string;oldPrice?:string;period?:string;features?:React.ReactNode[];cta?:string;featured?:boolean;badge?:string;onSelect?:()=>void}
export declare function PricingCard(props:PricingCardProps):JSX.Element;
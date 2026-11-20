import * as React from 'react';
/** Preguntas frecuentes plegables. */
export interface AccordionProps{items?:{q:React.ReactNode;a:React.ReactNode}[];defaultOpen?:number}
export declare function Accordion(props:AccordionProps):JSX.Element;
/** Contenedor redondeado con borde suave. */
export interface CardProps{tone?:'white'|'cream'|'peach'|'dark';padding?:number;children?:React.ReactNode;style?:React.CSSProperties}
export declare function Card(props:CardProps):JSX.Element;
/** Ítem de lista con check en degradado (beneficios, lo que incluye). */
export interface CheckItemProps{children?:React.ReactNode;style?:React.CSSProperties}
export declare function CheckItem(props:CheckItemProps):JSX.Element;
/** Caja destacada durazno con barra naranja a la izquierda, para notas o reglas. */
export interface PeachBoxProps{title?:React.ReactNode;children?:React.ReactNode;style?:React.CSSProperties}
export declare function PeachBox(props:PeachBoxProps):JSX.Element;
/** Tarjeta de plan/precio para landings de cursos y mentorías.
 * @startingPoint section="Content" subtitle="Plan card with gradient badge" viewport="700x460" */
export interface PricingCardProps{name:string;price:string;oldPrice?:string;period?:string;features?:React.ReactNode[];cta?:string;featured?:boolean;badge?:string;onSelect?:()=>void}
export declare function PricingCard(props:PricingCardProps):JSX.Element;
/** Etiqueta en mayúsculas: CLASE EN VIVO, MÁS POPULAR, REGALO DE BIENVENIDA. */
export interface BadgeProps{variant?:'peach'|'gradient'|'dark'|'outline'|'success';children?:React.ReactNode;style?:React.CSSProperties}
export declare function Badge(props:BadgeProps):JSX.Element;
/** Botón principal de la marca. Primary usa el degradado estrella.
 * @startingPoint section="Core" subtitle="Gradient pill CTA" viewport="700x260" */
export interface ButtonProps{variant?:'primary'|'secondary'|'dark'|'ghost';size?:'sm'|'md'|'lg';fullWidth?:boolean;disabled?:boolean;icon?:React.ReactNode;children?:React.ReactNode;onClick?:()=>void;type?:'button'|'submit';style?:React.CSSProperties}
export declare function Button(props:ButtonProps):JSX.Element;
/** Pinta parte de un titular con el degradado naranja → naranja oscuro. */
export interface GradientTextProps{children?:React.ReactNode;style?:React.CSSProperties}
export declare function GradientText(props:GradientTextProps):JSX.Element;
/** Logo oficial (PNG). basePath apunta a la carpeta assets/ relativa a la página. */
export interface LogoProps{variant?:'horizontal'|'vertical'|'icon';height?:number;basePath?:string;style?:React.CSSProperties}
export declare function Logo(props:LogoProps):JSX.Element;
/** Casilla con relleno en degradado al marcar. */
export interface CheckboxProps{label?:React.ReactNode;checked?:boolean;defaultChecked?:boolean;onChange?:(v:boolean)=>void;disabled?:boolean}
export declare function Checkbox(props:CheckboxProps):JSX.Element;
/** Campo de texto para formularios de registro. */
export interface InputProps{label?:string;placeholder?:string;type?:string;value?:string;onChange?:(e:React.ChangeEvent<HTMLInputElement>)=>void;error?:string;hint?:string;disabled?:boolean}
export declare function Input(props:InputProps):JSX.Element;
/** Grupo de opciones tipo tarjeta (encuestas, calificación de leads). */
export interface RadioProps{options?:string[];value?:string;defaultValue?:string;onChange?:(v:string)=>void;name?:string}
export declare function Radio(props:RadioProps):JSX.Element;
/** Selector nativo con estilo de marca. */
export interface SelectProps{label?:string;options?:string[];value?:string;onChange?:(e:React.ChangeEvent<HTMLSelectElement>)=>void;placeholder?:string}
export declare function Select(props:SelectProps):JSX.Element;
declare global { interface Window { CompraEnFBricasDesignSystem_e5b2dc: { Accordion: typeof Accordion; Card: typeof Card; CheckItem: typeof CheckItem; PeachBox: typeof PeachBox; PricingCard: typeof PricingCard; Badge: typeof Badge; Button: typeof Button; GradientText: typeof GradientText; Logo: typeof Logo; Checkbox: typeof Checkbox; Input: typeof Input; Radio: typeof Radio; Select: typeof Select } } }

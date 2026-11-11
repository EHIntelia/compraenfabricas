// Helpers de la página de cada caja (/producto/$codigo). Los datos vienen de src/lib/cajas.ts.
import { CAJAS, cajaId, type Caja } from "@/lib/cajas";
import { categoriaDe } from "@/lib/tracking";
import { MXN_PER_USD } from "@/lib/site";
import { APARTADO_PCT, PRECIO_REVENTA, WA_NUMERO } from "@/config/producto";

/** Disponible = no vendida y no oculta. */
export const disponible = (c: Caja) => !c.vendida && !c.hidden;

export const cajasDisponibles = () => CAJAS.filter(disponible).sort((a, b) => a.priceMxn - b.priceMxn);

export function buscarCaja(codigo: string): Caja | undefined {
  let k = codigo;
  try {
    k = decodeURIComponent(codigo);
  } catch {
    /* ya venía decodificado */
  }
  k = k.trim().toLowerCase();
  return CAJAS.find((c) => cajaId(c).toLowerCase() === k);
}

export const urlProducto = (c: Caja) => `/producto/${encodeURIComponent(cajaId(c))}`;

/** Cajas disponibles parecidas: primero misma categoría, luego precio más cercano. */
export function similares(c: Caja | undefined, n: number): Caja[] {
  const pool = cajasDisponibles().filter((x) => !c || cajaId(x) !== cajaId(c));
  if (!c) return pool.slice(0, n);
  const cat = categoriaDe(c.name);
  return [...pool]
    .sort((a, b) => {
      const ca = categoriaDe(a.name) === cat ? 0 : 1;
      const cb = categoriaDe(b.name) === cat ? 0 : 1;
      return ca - cb || Math.abs(a.priceMxn - c.priceMxn) - Math.abs(b.priceMxn - c.priceMxn);
    })
    .slice(0, n);
}

export const fmt = (n: number) => Math.round(n).toLocaleString("en-US");
export const usdDe = (mxn: number) => Math.round(mxn / MXN_PER_USD);
export const precioPieza = (c: Caja) => Math.round(c.priceMxnPerPiece);
export const apartadoDe = (c: Caja) => Math.round(c.priceMxn * APARTADO_PCT);

export function nombreModelo(c: Caja) {
  return c.model && !c.name.includes(c.model) ? `${c.model} ${c.name}` : c.name;
}

/** Margen de ejemplo. undefined si no hay precio de reventa capturado (y entonces no se muestra). */
export function margenEjemplo(c: Caja) {
  const venta = PRECIO_REVENTA[cajaId(c)];
  if (!venta || venta <= 0) return undefined;
  const porPieza = venta - c.priceMxnPerPiece;
  return { venta, porPieza: Math.round(porPieza), porCaja: Math.round(porPieza * c.pieces) };
}

const wa = (text: string) => `https://wa.me/${WA_NUMERO}?text=${encodeURIComponent(text)}`;

export const waApartar = (c: Caja) =>
  wa(`Hola, quiero apartar la caja ${c.name} (${cajaId(c)}) de ${c.pieces} piezas por $${fmt(c.priceMxn)}`);

export const waDuda = (c: Caja) => wa(`Hola, tengo una duda sobre la caja ${c.name} (${cajaId(c)})`);

export const waPedirVideo = (c: Caja) =>
  wa(`Hola, no pude ver el video de la caja ${c.name} (${cajaId(c)}). ¿Me lo pueden mandar por aquí?`);

export const waVendida = (c: Caja) =>
  wa(`Vi que la caja ${c.name} (${cajaId(c)}) ya se vendió. ¿Me avisan cuando llegue otra igual o una parecida?`);

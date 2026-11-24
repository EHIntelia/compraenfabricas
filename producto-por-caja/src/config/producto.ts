// ============================================================
// EDITABLE — textos y datos de la página de cada caja (/producto/$codigo)
// Todo lo que Eduardo/equipo puede cambiar sin tocar el diseño está aquí.
// ============================================================

/** WhatsApp que recibe los apartados y dudas: +52 81 2018 1761 */
export const WA_NUMERO = "5218120181761";

/** Porcentaje del apartado (20%) */
export const APARTADO_PCT = 0.2;

/**
 * Precio de REVENTA por pieza (MXN) para la línea "margen de ejemplo".
 * Clave = código de la caja (el mismo de la URL, ej. "CF-027").
 * Si una caja no está aquí, la línea de margen NO se muestra.
 * Pon solo precios reales que hayas visto en el mercado. No inventar.
 */
export const PRECIO_REVENTA: Record<string, number> = {
  // "CF-XXX": 0,
};

/** Preguntas frecuentes de la página de cada caja. */
export type FaqProducto = { q: string; a: string; link?: { href: string; texto: string } };

export const FAQ_PRODUCTO: FaqProducto[] = [
  {
    q: "¿Cómo aparto?",
    // Mismo proceso que ya dice /productos ("Elige tu caja y apártala con el 20% por WhatsApp").
    a: "Toca el botón “Apartar” y mándanos el mensaje por WhatsApp. Apartas tu caja con el 20% del precio total.",
  },
  {
    q: "¿Cuándo pago el resto?",
    // Tomado de la FAQ actual de /productos. Confirma que sigue vigente.
    a: "Tienes 7 días después de apartar para pagar el 80% restante más el envío por paquetería nacional.",
  },
  {
    q: "¿Cuánto tarda en llegar?",
    // Tomado de la FAQ actual de /productos. Confirma que sigue vigente.
    a: "Las cajas ya están en México. Si completas tu pago antes de las 4 pm, te llega en 1 a 2 días hábiles.",
  },
  {
    q: "¿Me dan factura?",
    // TODO(Eduardo): escribir si se da factura, con qué datos y si cuesta extra. Texto genérico mientras tanto.
    a: "Escríbenos por WhatsApp y te confirmamos si podemos facturar tu compra.",
  },
  {
    q: "¿Hacen envíos fuera de México?",
    // Tomado de la FAQ actual de /productos.
    a: "Sí, enviamos directo desde China a otros países (excepto Cuba). Es un proceso distinto: cotiza tu envío y te mandamos el precio.",
    link: { href: "/cotizador", texto: "Cotiza tu envío internacional →" },
  },
];

/** Puntos de "Compra con confianza" (todos reales, confirmados por Eduardo). */
export const CONFIANZA: string[] = [
  "Te hacemos un acuerdo de compra por escrito.",
  "Recibos de cada pago con nuestro sello oficial.",
  "Te mandamos videos de tu pedido y hacemos videollamada contigo cuando esté listo.",
  "Estamos en Monterrey, N.L.",
  "No usamos pago contra entrega.",
];

/** Banner de la clase en vivo. Se oculta solo después de `ocultarDespuesDe`. */
export const CLASE_BANNER = {
  titulo: "Clase en vivo con Eduardo",
  fecha: "Sábado 21 de noviembre",
  hora: "11 am hora CDMX",
  precio: "$990 MXN",
  href: "/clase",
  // 21 nov 2026, 2 pm hora CDMX (UTC-6)
  ocultarDespuesDe: "2026-11-21T20:00:00Z",
};

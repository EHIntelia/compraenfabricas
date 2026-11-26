# Creativos horizontales: cajas disponibles (25 nov 2026)

PNG en `png/`, exportados al doble (3840×2160) para que se vean nítidos. Las cajas vendidas después de hacerlos (`VENDIDAS` en `generar.py`) salen tachadas con sello VENDIDO: TK70 desde el 26 nov 2026. Diseño con el design system de Compra en fábricas (naranjas, Arial 900, tarjetas blancas, caja durazno).

**Datos:** `src/lib/cajas.ts` del proyecto Lovable "China Direct Connect" al 25 nov 2026. Entran solo las cajas que no están vendidas, ocultas ni apartadas (12). Quedaron fuera las apartadas: CH-M814, Walkie-talkie, SAG11 y S2 Max.
Precio por pieza = `priceMxnPerPiece` redondeado; "10 piezas" = precio por pieza × 10. Fotos: `compraenfabricas.com/og/producto/<código>.jpg`.

| Propuesta | Archivo | Uso sugerido |
|---|---|---|
| A · Catálogo 12 cajas | `A-catalogo-12-cajas.png` | Post/anuncio con todo el inventario |
| B · Una caja por imagen | `B01…B12-*.png` | Carrusel o anuncio por producto |
| C · 6 cajas por imagen | `C1-desde-157-por-pieza.png`, `C2-camaras-relojes-y-mas.png` | Carrusel de 2 |
| D · Lista de precios | `D-lista-de-precios.png` | WhatsApp, difusión, estados |

## Historias (vertical 1080×1920) · `png/historias/`

Las mismas propuestas en vertical, sin nada importante en las zonas que tapa Instagram (arriba el perfil, abajo la barra de respuesta).

| Propuesta | Archivo |
|---|---|
| B · Una caja por historia | `historias/B01…B12-*.png` |
| C · 6 cajas por historia | `historias/C1-desde-157-por-pieza.png`, `historias/C2-mas-cajas-disponibles.png` |
| D · Lista de precios (las 12) | `historias/D-lista-de-precios.png` |

En vertical no se hizo el catálogo A: las 12 cajas en una historia quedan muy chicas. Para verlas todas juntas está la D.

## Carrusel de Instagram (1080×1350, 4:5) · `png/carrusel/`

Gancho: el presupuesto. Con el mínimo de 10 piezas, el primer inventario cuesta menos de $2,000 (10 mochilas a $157). Los productos se agrupan por cuánto cuesta llevarse 10 piezas, que es como decide quien empieza.

| # | Lámina |
|---|---|
| 1 | Gancho: "Tu primer inventario por menos de $2,000" + 6 productos con precio |
| 1b / 1c | Portadas alternativas con el hook "Ya no tienes excusa para no empezar tu negocio": 1b con productos, 1c como chat: "Tú" escribe 3 excusas (capital, complicado, tarda meses) y Compra en fábricas contesta cada una con un dato real (portada elegida) |
| 1d / 1e / 1f | Portadas "excusas tachadas" con menos texto: 1d minimal, 1e "Tus excusas" → "Ya no aplican. Empieza tu negocio con menos de $1,600" (elegida), 1f tachón tipo marcador con etiquetas |
| 2 | Así funciona (3 pasos) + aviso de una sola caja por modelo |
| 3 | Menos de $2,000: mochila, bocina KOS-500, micrófono MK26 |
| 4 | Menos de $3,500: MK50, MS18, dashcam D8, QY77 |
| 5 | Menos de $7,000: ventilador F118, cámara Q8, reloj TK70 |
| 6 | Premium: traductor S85 Pro, cámara de bolsillo 4K |
| 7 | "¿Cómo sé que es real?": puntos de confianza del sitio + sello |
| 8 | CTA: DM con la palabra CAJA, WhatsApp y web; recordatorio de guardar |

Caption con hashtags: `carrusel-caption.md`. Se genera con `python3 carrusel.py && node render.js`.

**Actualizar** (cuando se venda o aparte una caja): editar `CAJAS` en `generar.py`, poner la foto en `fotos/` y correr (genera horizontales e historias):
```
python3 generar.py && node render.js
```

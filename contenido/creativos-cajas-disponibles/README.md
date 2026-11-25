# Creativos horizontales: cajas disponibles (25 nov 2026)

PNG 1920×1080 en `png/`. Diseño con el design system de Compra en fábricas (naranjas, Arial 900, tarjetas blancas, caja durazno).

**Datos:** `src/lib/cajas.ts` del proyecto Lovable "China Direct Connect" al 25 nov 2026. Entran solo las cajas que no están vendidas, ocultas ni apartadas (12). Quedaron fuera las apartadas: CH-M814, Walkie-talkie, SAG11 y S2 Max.
Precio por pieza = `priceMxnPerPiece` redondeado; "10 piezas" = precio por pieza × 10. Fotos: `compraenfabricas.com/og/producto/<código>.jpg`.

| Propuesta | Archivo | Uso sugerido |
|---|---|---|
| A · Catálogo 12 cajas | `A-catalogo-12-cajas.png` | Post/anuncio con todo el inventario |
| B · Una caja por imagen | `B01…B12-*.png` | Carrusel o anuncio por producto |
| C · 6 cajas por imagen | `C1-desde-157-por-pieza.png`, `C2-camaras-relojes-y-mas.png` | Carrusel de 2 |
| D · Lista de precios | `D-lista-de-precios.png` | WhatsApp, difusión, estados |

**Actualizar** (cuando se venda o aparte una caja): editar `CAJAS` en `generar.py`, poner la foto en `fotos/` y correr:
```
python3 generar.py && node render.js
```

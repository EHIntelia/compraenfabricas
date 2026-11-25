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

## Historias (vertical 1080×1920) · `png/historias/`

Las mismas propuestas en vertical, sin nada importante en las zonas que tapa Instagram (arriba el perfil, abajo la barra de respuesta).

| Propuesta | Archivo |
|---|---|
| B · Una caja por historia | `historias/B01…B12-*.png` |
| C · 6 cajas por historia | `historias/C1-desde-157-por-pieza.png`, `historias/C2-mas-cajas-disponibles.png` |
| D · Lista de precios (las 12) | `historias/D-lista-de-precios.png` |

En vertical no se hizo el catálogo A: las 12 cajas en una historia quedan muy chicas. Para verlas todas juntas está la D.

**Actualizar** (cuando se venda o aparte una caja): editar `CAJAS` en `generar.py`, poner la foto en `fotos/` y correr (genera horizontales e historias):
```
python3 generar.py && node render.js
```

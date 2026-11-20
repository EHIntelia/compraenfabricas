# Compra en Fábricas · Design System

Copia en el repo del artefacto **"Compra en Fábricas Design System"**: https://claude.ai/code/artifact/9d3023df-4501-4216-86f3-183723e634fd

- **Fuente de verdad:** el artefacto en claude.ai. Esta carpeta es un respaldo; si se cambia algo allá, hay que volver a copiarlo aquí (y al revés).
- **Copiado:** 20 nov 2026.
- **Guía de marca completa:** [`artefacto/README.md`](artefacto/README.md). Marca **solo en naranjas, sin rojos**; logo oficial en `artefacto/assets/logo-horizontal.png`.

## Qué hay en `artefacto/`

| Ruta | Contenido |
|---|---|
| `README.md` | Guía de marca: voz, colores, tipografía, logo, sellos, componentes |
| `design-system.json` | Índice del artefacto (grupos de assets, último cambio) |
| `tokens.json`, `tokens.css`, `styles.css` | Tokens de color, tipo, espaciado |
| `assets/` | Logos, ícono, sello oficial, notas |
| `assets/photos/` | Fotos de Eduardo, banco de 52 imágenes 16:9 (`banco/`) y fotos de producto (`productos/`) |
| `components/` | Componentes React (Button, Badge, Card, PricingCard…), `bundle.js`, previews |
| `guidelines/` | Tarjetas de guía (CTA, peach box, fotos, degradado, tipografía display) |
| `ui_kits/landing/` | Landing → registro → gracias |
| `archived/` | Versión anterior del sistema (referencia) |

No se copió `uploads/` del artefacto: son los mismos archivos que ya están en `assets/` (logos, fotos de Eduardo y banco).

## Fotos de producto · `artefacto/assets/photos/productos/`

Fotos tipo catálogo de proveedor (generadas con Grok), 2:3, 1152×1728, fondo liso de color, sin verde (sirven sobre chroma key). Producto genérico, no material de la marca.

| Archivo | Producto | Fondo | Usada en |
|---|---|---|---|
| `peluche-oso-mono-rojo.jpg` | Oso de peluche café con moño rojo | durazno `#FEF3E2` | Proveedores China (chroma) · card 1 |
| `sudadera-roja-capucha.jpg` | Sudadera roja con capucha, sin estampado | rosa `#FFE4E6` | Proveedores China (chroma) · card 3 |
| `silla-oficina-malla-negra.jpg` | Silla de oficina negra de malla | lila `#E0E7FF` | Proveedores China (chroma) · card 5 |

### Prompt base (Grok, formato 2:3 Póster)

```
Professional e-commerce product photo of [PRODUCTO CON COLORES Y DETALLES]. Centered, filling about 70-75% of the frame, with generous empty margin around the product. Seamless solid [COLOR] background (#HEX), soft even studio lighting, very soft shadow. Clean B2B wholesale catalog style, sharp focus. Leave empty space in the top-left corner. Vertical 2:3. No text, no logos, no watermark, no props, no green tones.
```

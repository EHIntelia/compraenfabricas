# Compra en Fábricas · Design System (recursos)

Recursos de marca guardados en el repo para reutilizar en futuros diseños.

- **Design System (fuente):** artefacto "Compra en Fábricas Design System": https://claude.ai/code/artifact/9d3023df-4501-4216-86f3-183723e634fd
- **Colores base:** naranja `#F97316`, rojo `#DC2626`, tinta `#1A1A1A`, durazno `#FCE4DC`, crema `#FFF8F5`. Tipografía Arial 900, degradado naranja → rojo.

## Imágenes de producto · `imagenes/productos/`

Fotos tipo catálogo de proveedor (generadas con Grok), formato 2:3, 1152×1728, fondo liso de color. Sirven para simular fichas de producto o de proveedor chino.

| Archivo | Producto | Fondo | Usada en |
|---|---|---|---|
| `peluche-oso-mono-rojo.jpg` | Oso de peluche café con moño rojo | durazno `#FEF3E2` | Proveedores China (chroma) · card 1 |
| `sudadera-roja-capucha.jpg` | Sudadera roja con capucha, sin estampado | rosa `#FFE4E6` | Proveedores China (chroma) · card 3 |
| `silla-oficina-malla-negra.jpg` | Silla de oficina negra de malla | lila `#E0E7FF` | Proveedores China (chroma) · card 5 |

Ninguna imagen tiene verde, así que funcionan sobre chroma key.

### Prompt base (Grok, formato 2:3 Póster)

```
Professional e-commerce product photo of [PRODUCTO CON COLORES Y DETALLES]. Centered, filling about 70-75% of the frame, with generous empty margin around the product. Seamless solid [COLOR] background (#HEX), soft even studio lighting, very soft shadow. Clean B2B wholesale catalog style, sharp focus. Leave empty space in the top-left corner. Vertical 2:3. No text, no logos, no watermark, no props, no green tones.
```

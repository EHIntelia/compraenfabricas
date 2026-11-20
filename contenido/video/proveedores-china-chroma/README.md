# Proveedores China · cards animadas · chroma verde

Animación para poner **encima de un video** (fondo verde `#00FF00` para quitarlo con chroma key).

- **Contexto del video:** "te pasan el contacto de X proveedor, luego de X proveedor… pero no te dicen cómo comprar". La frase la decimos nosotros en el video; la animación **no lleva copy propio**, solo simula proveedores.
- **Formato:** 1080×1080, loop de 12 s.
- **Canvas (fuente editable):** artefacto "Clase Importación China (copia)", fila **"Proveedores China · contactos sin cómo comprar"**: https://claude.ai/artifact/AJtuKHrqGFKxq3tsV6nVtp (privado; se comparte desde Share).
- **Código:** [`disenos/Proveedores_China_Chroma.dc.html`](disenos/Proveedores_China_Chroma.dc.html) (copia de lo que hay en el canvas).

## Qué pasa en la animación

Llegan 6 cards de proveedor, una cada 1.5 s, volando desde los lados y desde abajo, y se van apilando como si te pasaran un contacto tras otro. Se quedan todas en pantalla y a los 11.2 s salen hacia abajo; luego el loop vuelve a empezar.

| # | Entra | Tipo | Proveedor (inventado) | Mercancía |
|---|---|---|---|---|
| 1 | 0.3 s · izquierda | Ficha de producto (estilo marketplace B2B) | Yiwu Lekang Toys | Peluches |
| 2 | 1.8 s · derecha | Tarjeta de presentación 名片 (azul marino) | Shenzhen Xinyuda Electronic | Audífonos, power banks, smartwatches |
| 3 | 3.3 s · abajo | Ficha de producto | Guangzhou Meiyi Garment | Sudaderas |
| 4 | 4.8 s · izquierda | Tarjeta de presentación (roja con dorado) | Yongkang Jinchu Kitchenware | Sartenes, ollas, teteras |
| 5 | 6.3 s · derecha | Ficha de producto | Foshan Haoju Furniture | Sillas de oficina |
| 6 | 7.8 s · abajo | Tarjeta de presentación (negra con rosa) | Guangzhou Yanmei Cosmetics | Labiales, skincare |

## Fotos de producto

Las cards 1, 3 y 5 usan fotos generadas con Grok (peluche, sudadera, silla). Los originales están en [`design-system/artefacto/assets/photos/productos/`](../../../design-system/artefacto/assets/photos/productos/); en el canvas van subidas en versión ligera (600×900).

## Notas para chroma

- Sin sombras ni transparencias: todo entra y sale con movimiento, para que el recorte quede limpio.
- Ningún elemento usa verde (los íconos de WeChat/WhatsApp van en el color de cada tarjeta).
- Nombres de empresas y personas son inventados; teléfonos van con `****`. No se usa logo ni marca de Alibaba, solo el estilo de ficha.

## Video listo

[`export/proveedores-china-chroma-1080.mp4`](export/proveedores-china-chroma-1080.mp4): MP4 H.264, 1080×1080, 30 fps, 12 s, fondo verde `#00FF00`. Se renderizó cuadro por cuadro desde el diseño, así que el loop es exacto (el último cuadro empata con el primero).

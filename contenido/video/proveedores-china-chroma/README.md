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

## Notas para chroma

- Sin sombras ni transparencias: todo entra y sale con movimiento, para que el recorte quede limpio.
- Ningún elemento usa verde (los íconos de WeChat/WhatsApp van en el color de cada tarjeta).
- Nombres de empresas y personas son inventados; teléfonos van con `****`. No se usa logo ni marca de Alibaba, solo el estilo de ficha.

## Cómo exportarlo a video

Abrir el artboard en el canvas (Play / vista completa) y grabar la pantalla a 1080×1080, o usar la exportación del canvas si está disponible. Recortar 12 s para un loop exacto.

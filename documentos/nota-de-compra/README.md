# Nota de compra · Compra en fábricas

Plantilla de la nota de compra (antes "acuerdo de compra") para clientes que apartan o compran cajas. Usa el logo y los colores del design system de Compra en fábricas (naranja #F97316, rojo #DC2626, degradado naranja a rojo, tinta #1A1A1A, durazno #FCE4DC).

La nota tiene 4 partes: tu pedido (con foto), elige tu envío (opciones de paquetería con seguro), cuánto pagas (total por opción, un solo pago) y datos para tu pago.

## Cómo generar uno

1. Copia `datos-ejemplo.json` con el nombre del cliente y llénalo: orden, fecha, cliente, producto (piezas, precio por pieza, foto), opciones de envío y datos bancarios.
2. Genera el HTML:
   ```
   python3 generar.py datos-cliente.json nota.html
   ```
3. Conviértelo a documento imprimible:
   ```
   node a-pdf.js nota.html nota.pdf
   ```

Los totales se calculan solos: piezas × precio por pieza, más el envío de cada opción.

## Importante: este repositorio es público

- **No subas aquí los datos reales de clientes** (nombre, teléfono, dirección) ni las notas ya llenas. Guárdalos en Drive, en la carpeta del cliente dentro de "Compra en China".
- **No subas los datos bancarios reales.** El ejemplo usa una cuenta en ceros.
- **El sello oficial no está en el repositorio.** Pon tu copia local en `assets/sello-oficial.png` (está en `.gitignore`). Sin él, la nota sale sin sello.

## Archivos

- `generar.py`: arma el HTML de la nota a partir del JSON.
- `a-pdf.js`: convierte el HTML a documento tamaño carta.
- `datos-ejemplo.json`: datos de ejemplo, sin datos reales.
- `assets/logo-horizontal.png`: logo oficial del design system.
- `assets/ejemplo-producto.jpg`: foto de ejemplo (lentes YJ12).
- `ejemplo/nota-ejemplo.pdf`: cómo se ve con los datos de ejemplo.
- `clientes/`: copias de notas reales **sin datos privados** (teléfono, dirección y cuenta ocultos, nombre abreviado, sin sello). La nota completa de cada cliente está en Drive, en su carpeta dentro de "Compra en China".
  - `CF-2026-007_nota_sin_datos_privados.pdf`: Rocío R., 93 lentes YJ12, envío DHL Express a Zacatecas.

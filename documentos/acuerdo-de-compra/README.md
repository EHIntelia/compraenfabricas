# Acuerdo de compra · Compra en fábricas

Plantilla del acuerdo de compra para clientes que apartan o compran cajas. Usa el logo y los colores del design system de Compra en fábricas (naranja #F97316, rojo #DC2626, degradado naranja a rojo, tinta #1A1A1A, durazno #FCE4DC).

El acuerdo tiene 4 partes: tu pedido (con foto), elige tu envío (opciones de paquetería con seguro), cuánto pagas (total por opción, un solo pago) y datos para tu pago.

## Cómo generar uno

1. Copia `datos-ejemplo.json` con el nombre del cliente y llénalo: orden, fecha, cliente, producto (piezas, precio por pieza, foto), opciones de envío y datos bancarios.
2. Genera el HTML:
   ```
   python3 generar.py datos-cliente.json acuerdo.html
   ```
3. Conviértelo a documento imprimible:
   ```
   node a-pdf.js acuerdo.html acuerdo.pdf
   ```

Los totales se calculan solos: piezas × precio por pieza, más el envío de cada opción.

Opcional en el JSON:
- `cliente.correo` (se muestra junto al nombre; `telefono` también es opcional).
- `envio.nota` (aviso bajo el envío, p. ej. que el costo de DHL es un estimado) y `envio.concepto` (texto de la fila del envío).
- Con **una sola opción de envío** el apartado se llama "Tu envío" y la columna "Monto".
- `titulo`: cambia el encabezado (por defecto "Acuerdo de compra"; p. ej. "Nota de compra").
- `apartado`: `{"porcentaje": 20, "monto": 315, "dias": 7}` agrega el pago para apartar y el resto + envío, con el plazo para liquidar.

## Importante: este repositorio es público

- **No subas aquí los datos reales de clientes** (nombre, teléfono, dirección) ni los acuerdos ya llenos. Guárdalos en Drive, en la carpeta del cliente dentro de "Compra en China".
- **No subas los datos bancarios reales.** El ejemplo usa una cuenta en ceros.
- **El sello oficial no está en el repositorio.** Pon tu copia local en `assets/sello-oficial.png` (está en `.gitignore`). Sin él, el acuerdo sale sin sello.

## Archivos

- `generar.py`: arma el HTML del acuerdo a partir del JSON.
- `a-pdf.js`: convierte el HTML a documento tamaño carta.
- `datos-ejemplo.json`: datos de ejemplo, sin datos reales.
- `assets/logo-horizontal.png`: logo oficial del design system.
- `assets/ejemplo-producto.jpg`: foto de ejemplo (lentes YJ12).
- `ejemplo/acuerdo-ejemplo.pdf`: cómo se ve con los datos de ejemplo.
- `clientes/`: copias de acuerdos reales **sin datos privados** (teléfono, dirección y cuenta ocultos, nombre abreviado, sin sello). El acuerdo completo de cada cliente está en Drive, en su carpeta dentro de "Compra en China".
  - `CF-2026-007_acuerdo_sin_datos_privados.pdf`: Rocío R., 93 lentes YJ12, envío DHL Express a Zacatecas.

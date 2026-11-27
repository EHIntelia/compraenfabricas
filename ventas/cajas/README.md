# Ventas de cajas

Registro de cada caja vendida: acuerdo de compra (PDF), ficha de la venta y el SQL con que se cargó al panel de eduardohernandez.com.

**Cómo se marca una caja como vendida**
1. compraenfabricas.com → Lovable "China Direct Connect" → `src/lib/cajas.ts`: agregar `vendida: true` a la caja (por su `code` CF-0xx del catálogo) y publicar.
2. Panel de eduardohernandez.com → Lovable "Eduardo Hernández" → insertar la caja en `cajas` con estado `vendida`. El trigger `sync_caja_venta` crea solo la venta en `ventas` (`external_id = caja-<code>`, transferencia, pagada) y la liga. Después, si hace falta, actualizar en `ventas` el cliente y las notas (el trigger reescribe las notas cada vez que cambia la fila de `cajas`).
3. Aquí: copiar el PDF, crear la ficha y guardar el SQL.

| Fecha | Orden | Caja | Cliente | Piezas | Monto mercancía | Ficha |
|---|---|---|---|---|---|---|
| 18-nov-2026 | CF-2026-007 | CF-038 YJ12 Lentes Bluetooth | Rocío Ríos (Zacatecas) | 93 | $17,847.63 (+ $778.56 DHL, opción A) | [ver](./CF-2026-007_YJ12_Rocio_Rios.md) |
| 27-nov-2026 | CF-2026-008 | CF-022 CH-M802 Mochila Bluetooth | Martín Castillo (San Luis Potosí) | 10 | $1,574.00 (+ $530 DHL estimado; apartado 20% = $315, resto en 7 días) | [nota de compra](./Nota_de_Compra_CF-2026-008_Martin_Castillo.pdf) |

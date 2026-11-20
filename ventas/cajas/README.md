# Ventas de cajas

Registro de cada caja vendida: acuerdo de compra (PDF), ficha de la venta y el SQL con que se cargó al panel de eduardohernandez.com.

**Cómo se marca una caja como vendida**
1. compraenfabricas.com → Lovable "China Direct Connect" → `src/lib/cajas.ts`: agregar `vendida: true` a la caja (por su `code` CF-0xx del catálogo) y publicar.
2. Panel de eduardohernandez.com → Lovable "Eduardo Hernández" → insertar en `ventas` (`external_id = caja-<code>`, proyecto `compra_en_china`, fuente `transferencia`) y en `cajas` (estado `vendida`, `venta_id` ligado).
3. Aquí: copiar el PDF, crear la ficha y guardar el SQL.

| Fecha | Orden | Caja | Cliente | Piezas | Monto mercancía | Ficha |
|---|---|---|---|---|---|---|
| 18-nov-2026 | CF-2026-007 | CF-038 YJ12 Lentes Bluetooth | Rocío Ríos (Zacatecas) | 93 | $17,847.63 | [ver](./CF-2026-007_YJ12_Rocio_Rios.md) |

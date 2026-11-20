-- Venta CF-2026-007 · Caja CF-038 YJ12 · Rocío Ríos
-- Ejecutado el 20-nov-2026 en Lovable Cloud del proyecto "Eduardo Hernández" (panel de eduardohernandez.com).
-- Resultado: ventas.id = c493c3dc-1404-4ac5-b5f9-362b598e96a4 · cajas.id = 9cb2446d-994c-45ff-a8b5-ada7057e792f
-- Nota: bruto_mxn y neto_mxn son columnas generadas; no se insertan.

with v as (
  insert into ventas (proyecto, fecha, fuente, producto_id, cliente_nombre, moneda, monto_bruto, comision, monto_neto, tipo_cambio_mxn, estado, origen, external_id, notas)
  values ('compra_en_china', '2026-11-18 18:00:00+00', 'transferencia', '92a40ffb-ae8f-4c76-8716-064239d33e2c', 'Rocío Ríos', 'MXN', 17847.63, 0, 17847.63, 1, 'pagada', 'organico', 'caja-CF-038',
   'Caja CF-038 YJ12 Lentes Bluetooth (93 pzas recibidas de 100; se cobran solo las 93 a $191.91). Orden CF-2026-007, acuerdo del 18-nov-2026. Envío DHL Express con seguro a Zacatecas cobrado aparte (opción A $778.56 / B $869.62, pass-through, no incluido en este monto).')
  returning id
)
insert into cajas (codigo, modelo, nombre, piezas, precio_mxn, estado, fecha_vendida, fecha_aproximada, venta_id, notas)
select 'CF-038', 'YJ12', 'YJ12 Lentes Bluetooth', 93, 17847.63, 'vendida', '2026-11-18 18:00:00+00', true, v.id,
 'Orden CF-2026-007 · Rocío Ríos (Zacatecas). Catálogo: 100 pzas / $19,191; llegaron 93 y se cobraron 93 × $191.91.'
from v
returning id, codigo, estado, venta_id;

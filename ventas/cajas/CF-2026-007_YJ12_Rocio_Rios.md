# Venta CF-2026-007 · Caja CF-038 YJ12 Lentes Bluetooth

**Estado:** VENDIDA · 18 de noviembre de 2026
**Acuerdo firmado:** [`Acuerdo_de_Compra_CF-2026-007_Rocio_Rios_v4.pdf`](./Acuerdo_de_Compra_CF-2026-007_Rocio_Rios_v4.pdf)

## Cliente

| Dato | Valor |
|---|---|
| Nombre | Rocío Ríos |
| Teléfono | +52 458 116 6485 |
| Entrega | García Salinas 1602, Local 106, Plaza Thaona, C.P. 98097, Zacatecas, Zac. |

## Pedido

| Concepto | Valor |
|---|---|
| Caja del catálogo | CF-038 · YJ12 Lentes Bluetooth (lentes de sol con audífono inalámbrico y protección UV) |
| Piezas en catálogo | 100 pzas · $19,191 MXN |
| Piezas recibidas y cobradas | **93 pzas × $191.91 = $17,847.63 MXN** (flete China→México incluido; solo se pagan las piezas que llegaron) |
| Envío nacional | DHL Express con seguro, entrega jueves 19-nov-2026 |
| **Opción A (al final del día) ✅ elegida** | $778.56 → total **$18,626.19** |
| Opción B (antes de las 12:00) | $869.62 → total $18,717.25 (no elegida) |
| Forma de pago | Transferencia BBVA a nombre de Eduardo Hernández, una sola exhibición antes del envío. Concepto: `CF-2026-007 Rocío Ríos` |

> **Envío elegido: opción A.** Total pagado por la clienta: **$18,626.19** ($17,847.63 mercancía + $778.56 DHL). En el panel la venta va por el monto de la mercancía ($17,847.63); el envío DHL es pass-through y queda anotado en las notas.

## Dónde quedó registrado

| Sistema | Cambio |
|---|---|
| **compraenfabricas.com** (Lovable, proyecto "China Direct Connect") | `src/lib/cajas.ts`: la entrada YJ12 (CF-038) ahora tiene `vendida: true` → sale al final de /productos con sello "VENDIDO". Test nuevo en `src/lib/__tests__/cajas-vendidas.test.ts` (106 pruebas pasan). Commit Lovable `a79875e`, publicado el 20-nov-2026. |
| **Panel de eduardohernandez.com** (Lovable, proyecto "Eduardo Hernández", Lovable Cloud) | Tabla `ventas`: venta `c493c3dc-1404-4ac5-b5f9-362b598e96a4`, `external_id = caja-CF-038`, $17,847.63, transferencia, pagada, proyecto `compra_en_china`. Tabla `cajas`: fila `9cb2446d-994c-45ff-a8b5-ada7057e792f`, CF-038, 93 pzas, estado `vendida`, ligada a la venta, fecha exacta (`fecha_aproximada = false`). SQL en [`sql/CF-2026-007_panel.sql`](./sql/CF-2026-007_panel.sql). |

## Nota sobre el código

El número de orden (CF-2026-007) **no es** el código de la caja. La caja YJ12 en el catálogo es **CF-038**; el CF-007 del catálogo es la Cámara de bolsillo 4K, que sigue disponible.

## Ojo con el panel: trigger `sync_caja_venta`

Cada vez que se inserta o actualiza una fila de `cajas`, el trigger `sync_caja_venta` vuelve a escribir la venta ligada (`ventas` con `external_id = caja-<codigo>`): monto, fecha **y notas**. Por eso las notas de la venta se escriben **después** de tocar `cajas`, nunca antes. Ver el SQL.

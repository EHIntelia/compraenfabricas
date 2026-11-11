# Página por caja: /producto/$codigo

Copia del código que se mandó al proyecto de Lovable "China Direct Connect" (el código del sitio vive allá, no en este repo).

| Archivo aquí | Ruta en Lovable |
|---|---|
| src/routes/producto.$codigo.tsx | igual |
| src/routes/admin.resenas.tsx | igual (formulario del equipo, contraseña RESENAS_ADMIN_PASSWORD) |
| src/lib/cajas-media.ts | igual (ahora única fuente de fotos y videos de cada caja) |
| src/lib/producto.ts | igual |
| src/lib/resenas.server.ts / resenas.functions.ts | igual |
| src/config/producto.ts | igual: **textos editables** (FAQ, precio de reventa, confianza, banner de la clase) |
| supabase/migration_resenas.sql | tabla `resenas` + bucket `resenas` |

Además: `/productos` enlaza cada tarjeta a su página y el sitemap incluye las cajas disponibles.

## Revisión de videos (11 nov 2026)

De los 20 videos de cajas disponibles, **19 estaban en H.264 "High 10" (10 bits, yuv420p10le)**. Ese perfil no lo reproducen iPhone/Safari ni la mayoría de los Android. Muy probablemente por eso los clientes no veían los videos. El moov ya estaba al inicio (faststart OK) y el audio ya era AAC.

Solo **MK50 (CF-037)** estaba bien (High 8 bits).

Se re-codificaron los 19 a H.264 High@3.1, 8 bits (yuv420p), AAC 96 kbps, +faststart, 720x406, con tamaño parecido al original:
m1, f118, chm802, chm814, walkie, yj12, ms18, kos500, mk26, sag11, s2max, sag20, tk70, pocket4k, q8, wk104, d8, qy77, s85pro.

Las cajas vendidas no se revisaron; si se reactivan, revisa sus videos igual:
`ffprobe -v error -show_entries stream=profile,pix_fmt video.mp4` (debe decir High/Main y yuv420p).

Comando usado:
```
ffmpeg -i in.mp4 -c:v libx264 -profile:v high -level 3.1 -pix_fmt yuv420p -preset slow -crf 27 -maxrate 850k -bufsize 1700k -g 60 -c:a aac -b:a 96k -ac 2 -movflags +faststart out.mp4
```

## Imágenes para compartir
`public/og/producto/<código>.jpg`, 1200x630, recortadas de la foto de cada caja (sin texto, para que no queden precios viejos). YJ12, SAG11 y SAG20 no tenían foto: se sacó un cuadro de su video (también se usa como portada del video).
Al agregar una caja nueva: sube su imagen a `public/og/producto/` y agrega el código a `OG_LISTOS` en `src/lib/cajas-media.ts`.

## Cajas disponibles (20)

| Caja | Piezas | Total MXN | URL |
|---|---|---|---|
| M1 Bocina chica | 100 | $4,990 | https://compraenfabricas.com/producto/CF-027 |
| CH-M802 Mochila Bluetooth | 50 | $7,868 | https://compraenfabricas.com/producto/CF-022 |
| F118 Ventilador multifunción | 16 | $9,212 | https://compraenfabricas.com/producto/CF-020 |
| CH-M814 Mochila Bluetooth | 60 | $10,593 | https://compraenfabricas.com/producto/CF-021 |
| Walkie-talkie con video para niños | 60 | $11,399 | https://compraenfabricas.com/producto/CF-012 |
| YJ12 Lentes Bluetooth | 200 | $14,201 | https://compraenfabricas.com/producto/CF-038 |
| MS18 Micrófono | 50 | $15,928 | https://compraenfabricas.com/producto/CF-023 |
| KOS-500 Speaker 2 en 1 con Audífonos | 100 | $17,272 | https://compraenfabricas.com/producto/CF-017 |
| MK26 Micrófono inalámbrico | 100 | $18,423 | https://compraenfabricas.com/producto/CF-039 |
| SAG11 Lentes con audio | 100 | $19,191 | https://compraenfabricas.com/producto/SAG11 |
| S2 Max Lentes | 50 | $22,069 | https://compraenfabricas.com/producto/CF-006 |
| Q8 Cámara deportiva | 40 | $24,564 | https://compraenfabricas.com/producto/CF-008 |
| SAG20 Lentes deportivos con IA | 100 | $26,867 | https://compraenfabricas.com/producto/SAG20 |
| MK50 Micrófono inalámbrico | 100 | $28,786 | https://compraenfabricas.com/producto/CF-037 |
| D8 Cámara para auto (Dashcam) | 100 | $33,776 | https://compraenfabricas.com/producto/CF-018 |
| QY77 Micrófono 4Mic | 100 | $33,776 | https://compraenfabricas.com/producto/CF-024 |
| TK70 Reloj | 50 | $34,544 | https://compraenfabricas.com/producto/CF-001 |
| Cámara de bolsillo 4K | 40 | $45,290 | https://compraenfabricas.com/producto/CF-007 |
| WK104 Lentes AI | 50 | $46,058 | https://compraenfabricas.com/producto/CF-005 |
| S85 Pro Traductor | 100 | $101,712 | https://compraenfabricas.com/producto/CF-011 |

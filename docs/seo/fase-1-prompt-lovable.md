# Fase 1 — Mensaje para el agente de Lovable (enviar con plan_mode=true)

Proyecto: "China Direct Connect" (compraenfabricas.com). Basado en `docs/seo/fase-0-auditoria.md` y en las decisiones de Eduardo del 11 nov 2026.

```
Quiero un PLAN (no escribas código todavía) para una ronda de SEO técnico. Reglas que no se rompen:
- NO cambies URLs existentes (/clase, /productos, /joyeria, /logistica, /marketplace, /escuela, etc.). Se usan en anuncios de Meta y en ManyChat.
- NO toques formularios (FormSubmit), links de pago (Stripe/Hotmart), números de WhatsApp de los botones de compra ni Skool / info.joyeria.shop.
- NO quites ni ocultes servicios: /validacion, /adn, /empieza-aqui y los paquetes siguen.
- NO hagas deploy.
- Respeta el project knowledge (tono, colores, componentes). Mobile-first.

1) PRIVACIDAD Y COSAS QUE NO DEBEN VERSE
a. /proveedores: agrega <meta name="robots" content="noindex, nofollow">. No la pongas en el sitemap ni la enlaces desde ninguna página pública. (NO la bloquees en robots.txt: Google necesita leerla para ver el noindex.)
b. /cotizador está en construcción: noindex, quítalo del menú (NAV_LINKS en src/lib/site.tsx), del sitemap (STATIC_PATHS en src/lib/blog/feeds.ts) y de cualquier enlace público:
   - /logistica: el botón "Cotiza tu envío" que lleva a /cotizador → que haga scroll al formulario #cotizar de la misma página.
   - /productos: los enlaces "¿Fuera de México? Cotiza envío internacional" (/cotizador?caja=...) → /logistica#cotizar.
   La ruta /cotizador se queda viva (no se borra).
c. "Clase gratis" ya no existe:
   - /empieza-aqui: quita los 3 botones "Registrarme a la clase gratis" y el texto "o regístrate a la clase gratis por Zoom". Donde estaba el botón, pon "Tomar la clase en vivo — $990 MXN" con Link a /clase.
   - FAQS en src/lib/site.tsx: cambia la pregunta "¿Hay una clase gratis…?" por "¿Puedo aprender antes de comprar un proveedor?" → "Sí. En la clase en vivo con Eduardo ($990 MXN) aprendes todo el proceso y te llevas 5 proveedores de regalo." con enlace a /clase.
   - Quita "/clase-gratis" del sitemap.
d. /empieza-aqui: cambia el H2 "Empieza a comprar en China hoy y deja tu trabajo este año" por "Empieza a comprar en China hoy, directo de fábrica".
e. Unifica años: en /joyeria, /escuela, /logistica, /asesoria-china y /productos cambia "25 años" / "+25 años" por "26+ años".

2) FECHA DE LA CLASE
a. La clase es el 21 de noviembre de 2026 a las 11:00 am (hora del centro de México). En /clase agrega la hora donde aparece la fecha (badge del hero y la línea bajo el botón): "21 de noviembre · 11:00 am (hora CDMX)".
b. El banner public/email/banner-clase-20nov.jpg dice "20 NOVIEMBRE". Dime si puedes generar una versión idéntica con "21" (mismo diseño, 1200×600). Si no puedes, avísame y lo resolvemos por fuera. No borres el archivo viejo: puede estar en correos ya enviados.
c. Busca en todo el código cualquier "20 de noviembre", "20 nov" o "20nov" y cámbialo a 21.

3) METADATOS (todas las rutas)
a. __root.tsx: quita {name:"author", content:"Lovable"} y {name:"twitter:site", content:"@Lovable"}. Pon author "Eduardo Hernández". twitter:card por defecto "summary_large_image".
b. Canonical ABSOLUTA (https://compraenfabricas.com/...) en todas las rutas indexables. Hoy es relativa en casi todas y falta en /clase y /joyeria. Usa el helper pageMeta() de src/lib/blog/seo.ts para las páginas comerciales también (así salen og:url, og:locale, og:site_name y canonical iguales en todo el sitio).
c. Titles y descriptions (50–60 y 140–155 caracteres):
   - /: "Importar de China directo de fábrica | Compra en Fábricas" / "Aprende a importar de China con Eduardo Hernández: clase en vivo, proveedores validados, cajas de electrónica y logística hasta tu puerta. Empieza hoy."
   - /clase: "Clase en vivo para importar de China | Eduardo Hernández" / "Clase en vivo con Eduardo Hernández, 21 de noviembre a las 11 am: proveedores reales, pago seguro y aduana. Incluye grabación y 5 proveedores. $990 MXN."
   - /joyeria: "Joyería de mayoreo en acero y chapa de oro | JAICO" / "Joyería de mayoreo en acero inoxidable y chapa de oro, directo de fábrica en China. Cadenas, aretes y juegos para tu negocio. Pide el catálogo y precios."
   - /productos: "Cajas de electrónica para revender | Compra en Fábricas" / "Cajas de electrónica que ya están en México: precio por pieza con flete incluido. Aparta con 20% y recibe en 1–2 días. Mira el catálogo y elige la tuya."
   - /validacion: description a máximo 155 caracteres sin cambiar la oferta.
   - Revisa que ninguna otra pase de 60 / 155 y propón el ajuste.
d. Imagen para compartir: crea UNA imagen de marca 1200×630 (degradado naranja→rojo, logo 中, "Compra en Fábricas de China", "Importa directo de fábrica") en /og/compra-en-fabricas.jpg y úsala como og:image/twitter:image por defecto en todas las páginas que no tengan una propia (hoy usan una imagen genérica de Lovable). El blog conserva sus portadas.

4) SITEMAP, REDIRECCIONES Y 404
a. Sitemap: quita /clase-gratis, /paquetes, /clase-grabada (tiene noindex) y /cotizador. Deja /validacion y /adn. Agrega lastmod a las páginas comerciales (fecha del último cambio real del archivo o una constante por ruta que se actualice al editar).
b. Las rutas que ya solo redirigen (/clase-gratis, /paquetes, /clase-privada, /cotizacion-cajas) deben usar redirección permanente 301 (hoy son 307). Mismos destinos de hoy.
c. La barra final (/clase/ → /clase) hoy es 307: si se puede, que sea 301/308.
d. Página 404 en español: "No encontramos esta página", con enlaces a /clase, a la guía /blog/como-importar-de-china-a-mexico, a /productos y al blog. Que siga respondiendo 404.

5) DATOS ESTRUCTURADOS (JSON-LD)
a. Organization: agrega alternateName "Compra en Fábricas", areaServed (México y Latinoamérica), contactPoint (WhatsApp +52 81 2018 1761, contactType "customer service", availableLanguage "es"), sameAs + Skool (https://www.skool.com/compraenfabricas).
b. WebSite: alternateName "Compra en Fábricas".
c. /clase: Event con name "Clase en vivo: aprende a comprar en China directo de fábrica", startDate "2026-11-21T11:00:00-06:00", endDate (pregúntame la duración; si no, deja solo startDate), eventAttendanceMode OnlineEventAttendanceMode, eventStatus EventScheduled, location VirtualLocation url https://compraenfabricas.com/clase, image (poster de la clase), description, organizer → @id de la Organization, performer → @id de Eduardo (https://compraenfabricas.com/autor/eduardo-hernandez#person), offers {price 990, priceCurrency MXN, availability InStock, url /clase, validFrom hoy}. Ponlo en una constante CLASS_DATES para que agregar la siguiente fecha sea cambiar una línea; si la fecha ya pasó, que no se publique el Event.
d. FAQPage en /clase, /escuela, /joyeria y /productos usando las mismas preguntas que ya se ven en la página.
e. BreadcrumbList (Inicio → página) en las páginas comerciales.
f. /productos: ItemList de Product + Offer SOLO para las cajas disponibles (no vendidas ni apartadas), con name, image, price (precio de la caja en MXN), priceCurrency MXN, availability InStock. Sin reseñas ni ratings.
g. Nada de AggregateRating ni Review.

6) VELOCIDAD (meta: LCP < 2.5 s en móvil)
Hoy (Lighthouse móvil): / 3.2 s, /clase 4.4 s (24 MB), /joyeria 5.4 s (33 MB), /productos 4.8 s, blog 3.5 s.
a. Videos: ningún video fuera del primer pantallazo debe descargarse al abrir la página. Galería de /joyeria (6 videos) y demás: preload="none" + poster, y que el autoplay muted empiece solo cuando el video entra en pantalla (IntersectionObserver). Videos del hero (/clase, /joyeria, /escuela, /logistica, /asesoria-china): preload="metadata" y poster; propón cómo mantener el autoplay sin bajar todo el archivo al inicio. /asesoria-china no tiene poster: agrégalo.
b. Imágenes: servir las fotos (hero, tarjetas, marquesina de /clase, p-*.jpg, pack-*.jpg) en WebP/AVIF con width/height y srcset; loading="lazy" en todo lo que no sea el primer pantallazo; la imagen principal de / con fetchpriority="high".
c. Animaciones "reveal": lo que está en el primer pantallazo (hero, H1, botones) NO debe arrancar con opacity 0. Que se vea desde el HTML del servidor.
d. Meta Pixel: que cargue después del evento load (o con requestIdleCallback) sin perder el PageView.

7) ENLAZADO INTERNO
a. Footer general: agrega Escuela, Vende joyería, Logística, Asesoría, Productos y "Quién es Eduardo" (/autor/eduardo-hernandez). Usa <Link>.
b. /joyeria, /escuela, /logistica y /asesoria-china tienen footer propio: agrega debajo el Footer general (o sus enlaces) sin romper su diseño.
c. Inicio: la tarjeta "Joyería" (sección Productos) que va a info.joyeria.shop → que vaya a /joyeria. Las tarjetas internas (/marketplace, /productos, /logistica, /validacion) que hoy abren en pestaña nueva → que abran en la misma pestaña con <Link>.
d. /marketplace: el WhatsApp de "Escríbenos por WhatsApp" usa wa.me/528120181761 sin mensaje. Cámbialo a wa.me/5218120181761 con texto "Hola, vengo de la página de proveedores".
e. Header: en escritorio el nombre "Compra en Fábricas de China" se corta. Que se vea completo (ajusta tamaño o espacio del menú sin quitar opciones).

8) PARA IAS
a. llms.txt: agrega un bloque "Sobre Eduardo Hernández" (26+ años importando de China, fundador de JAICO, Xijiao Shops y Xijiao LOG, 300+ empresas asesoradas, 50+ empresas acompañadas a China), los precios públicos (clase $990, escuela $250/mes), Joyería (/joyeria) y Validación (/validacion). No incluyas /cotizador ni /proveedores.
b. IndexNow: ya existe la llave en public/0548ff40ad255644b9c19950f3efce17.txt. Propón una función de servidor para avisar a IndexNow cuando una nota del blog pasa a 'published' (o un endpoint protegido que yo pueda llamar).

ENTREGA DEL PLAN
Lista los archivos que vas a tocar por punto, lo que NO vas a tocar, y cualquier riesgo (sobre todo en /clase, que recibe tráfico pagado). Después de mi OK lo haces en 2–3 tandas, empezando por los puntos 1 y 2.
```

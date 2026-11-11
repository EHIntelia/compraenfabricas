# Blog de Compra en Fábricas de China — entrega (nov 2026)

Proyecto de Lovable: **China Direct Connect** (compraenfabricas.com), workspace "Eduardo's Lovable".
Nada está publicado en producción todavía: todo vive en el preview hasta que se apruebe el deploy.

## 1. Qué se construyó

**Rutas nuevas**
- `/blog`: nota destacada + rejilla de tarjetas + filtro por categoría.
- `/blog/[slug]`: plantilla completa de la nota: migas, H1, autor con foto, fechas, tiempo de lectura, índice, Respuesta rápida, Consejo de Eduardo, banner a /clase, FAQ, caja de autor, CTA doble (clase + WhatsApp con el slug), compartir (WhatsApp, Facebook, X), 3 relacionadas y botón flotante de WhatsApp en móvil.
- `/blog/categoria/[slug]` con 5 categorías: como-importar, productos-que-se-venden, joyeria, errores-y-consejos, historias-de-eduardo.
- `/autor/eduardo-hernandez`: bio completa, 4 datos, botones a /clase y WhatsApp, redes.
- `/sitemap.xml`, `/robots.txt` (permite todos los bots, incluidos los de IA) y `/llms.txt`, que se generan solos desde la base.

**SEO técnico**
- El sitio usa TanStack Start con render en servidor (SSR). El título, la meta description, el canonical, los OG/Twitter, el JSON-LD y todo el texto de la nota salen en el HTML inicial, sin depender de JavaScript. No hizo falta prerender aparte.
- JSON-LD: BlogPosting, BreadcrumbList, FAQPage, HowTo (nota pilar), ProfilePage + Person (autor), y Organization + WebSite en todo el sitio, con las 3 redes en sameAs.
- `html lang="es-MX"`, "Blog" en el menú y en el footer.
- Limitaciones:
  - No hay editor visual; las notas se cargan en la base de datos.
  - Las imágenes en `public/` requieren publicar el sitio para salir en producción.

**Contenido en la base**: tabla `posts` en Lovable Cloud. Lectura pública solo de notas publicadas; escritura solo desde el servidor.

**Cómo publicar una nota nueva** (también está en el project knowledge de Lovable):
1. Escribe la nota en markdown con frontmatter en `blog/posts/<slug>.md` (usa una de estas como plantilla).
2. Genera las imágenes con `python3 tools/make_images.py` (agrega la nota al script) y súbelas a `public/blog/<slug>/`.
3. `python3 tools/check.py` para validar el SEO; `python3 tools/build_sql.py > out/posts.sql` para generar el SQL (upsert por slug).
4. Cárgala como `draft`, revísala en el preview y cámbiala a `published`.

## Verificación (hecha por el agente de Lovable en su preview)
- Las 5 notas, /blog, las categorías y el autor responden 200. Todo sale en el HTML inicial: title, description, canonical, og:image 1200×630, un solo H1, cuerpo completo, cajas, tablas, figuras con pie y FAQ con respuestas visibles.
- JSON-LD válido: Organization, WebSite, BlogPosting, BreadcrumbList y FAQPage aparecen una vez por nota. HowTo solo en la pilar.
- Los 14 enlaces internos de las notas y las 20 imágenes responden 200.
- WhatsApp (botón final y flotante en móvil) lleva el slug de la nota.
- robots.txt, llms.txt y sitemap correctos. Se corrigió un bug: el sitemap listaba categorías vacías y no tenía lastmod en /blog, autor y categorías.
- Sin desbordes a 390 px ni a 1280 px. /, /clase y /productos siguen igual. "Blog" sale en el menú.
- Fuera del blog (no se tocó): en escritorio, el nombre del logo del header se corta.

## 2. Las 5 notas

| # | Slug | Keyword | Meta title | Meta description | Palabras |
|---|---|---|---|---|---|
| 1 | como-importar-de-china-a-mexico | cómo importar de China | Cómo importar de China a México paso a paso (guía 2026) | Cómo importar de China a México en 2026: encuentra la fábrica, paga seguro, entiende aranceles y aduana, y evita errores caros. Guía paso a paso. | ~2,200 |
| 2 | eduardo-hernandez-importaciones-china | Eduardo Hernández importaciones de China | Eduardo Hernández: 26 años en importaciones de China | Eduardo Hernández lleva 26 años en importaciones de China: 2 bancarrotas, 5 negocios y 300+ empresas asesoradas. Conoce su historia y lo que aprendió. | ~1,560 |
| 3 | cursos-para-importar-de-china | cursos para importar de China | Cursos para importar de China 2026: comparativa honesta | Compara cursos para importar de China en 2026: precio, en vivo o grabado, si incluyen proveedores y soporte. Comparativa honesta para elegir bien. | ~1,690 |
| 4 | productos-para-importar-de-china | productos para importar de China | Productos para importar de China en 2026 y revender | Productos para importar de China en 2026 y revender: electrónica de vanguardia y joyería, con números reales de costo, peso y margen. Elige bien. | ~1,555 |
| 5 | importar-joyeria-de-china-para-vender | importar joyería de China | Importar joyería de China: márgenes y cómo empezar a vender | Importar joyería de China para vender por mayoreo: tipos, márgenes, calidad, dónde venderla y errores de principiante. Empieza tu negocio con números. | ~1,580 |

Todas tienen Respuesta rápida de 46–55 palabras, 6–7 preguntas frecuentes, la keyword en H1, primeras 100 palabras, un H2, slug, meta y alt de portada, enlaces a 2–3 notas y a 2 o más páginas comerciales.

## 3. Imágenes

20 imágenes WebP (776 KB en total) en `public/blog/<slug>/`, con los nombres y alt en `img/manifest.json`. Galería: https://claude.ai/artifact/GUPsW95b5aA2otAJH8g2pk

La portada de Eduardo es tipográfica: esta sesión no pudo descargar su foto del sitio. Su foto real sí aparece en la caja de autor y en la página de autor.

## 4. Pendientes para Eduardo (no salen en la página)

Están como comentarios ocultos en `posts/eduardo-hernandez-importaciones-china.md`. Llénalos y se suben con el mismo script:
1. **Cómo empezó:** año, primer producto que trajo, cómo llegó a China la primera vez y qué pasó con esa primera compra.
2. **Las 2 bancarrotas:** qué negocio era, qué salió mal y qué hizo para levantarse.
3. **Una anécdota en una fábrica china:** una negociación o un descubrimiento que le cambió la forma de comprar.
4. **El movimiento NADIE:** qué es, en sus palabras, y por qué se llama así.
5. **Precios de joyería reales (opcional):** las notas 4 y 5 usan un ejemplo hipotético ($25 costo, $149 venta). Con números reales de JAICO serían más fuertes.

## 5. Contradicciones (se tomó lo que dice el sitio, como pediste)

| Tema | Sitio (lo que se usó) | Handoff |
|---|---|---|
| Clase en vivo | Incluye grabación + 5 proveedores de regalo | No grabada, 3 proveedores |
| Proveedores de regalo | /clase muestra AEMAI y Port Tide por nombre | No publicar nombres de regalo. En el blog no se nombran. |
| Validación de proveedor | /validacion activa con pagos en Stripe (desde $2,500) | Eliminada. Se respetó el sitio y la nota pilar enlaza a /validacion. |
| Paquetes de contacto de proveedor | Paquete 1 ($1,500), 2 ($8,900) y 3 ($8,999) en site.tsx | "No buscamos proveedores por encargo" |
| Años de experiencia | /escuela, /logistica y /productos dicen "25 años" | 26 años (el blog usa 26+) |
| Clase gratis | FAQ en site.tsx manda a /clase-gratis | Ya no se ofrece (el blog no la menciona) |
| Metadatos globales | __root.tsx: author "Lovable", twitter:site "@Lovable" | No aplica (sugerencia: poner la marca) |
| Escuela | No menciona mini-curso gratis | Freemium con mini-curso (ya no se ofrece) |

## 6. Lo que te toca a ti
1. **Revisar el preview y aprobar el deploy** (no se publicó nada).
2. **Google Search Console:** verifica el dominio compraenfabricas.com y envía `https://compraenfabricas.com/sitemap.xml`.
3. **Pedir indexación** de las 5 URLs del blog con la herramienta de inspección de URL.
4. **Bing Webmaster Tools:** importa desde Search Console. Bing alimenta a ChatGPT Search y Copilot.
5. **Google Business Profile:** pon el enlace al blog y publica las portadas de redes.
6. **Rich Results Test** (search.google.com/test/rich-results) con la nota pilar después del deploy.
7. **Compartir cada nota** en Instagram, Facebook y TikTok con su imagen de 1080×1080, y en el grupo de WhatsApp.
8. **Llenar los pendientes de Eduardo** (sección 4) y decidir las contradicciones (sección 5).
9. **Revisar mensualmente** los precios de la tabla de cursos y del catálogo citados en las notas 3 y 4.

## 7. Calendario editorial: 10 notas más (clusters alrededor de la pilar)

| Semana | Título propuesto | Keyword | Cluster | Categoría |
|---|---|---|---|---|
| 1 | Cómo comprar en China sin intermediarios (y cuánto te ahorras) | comprar en China sin intermediarios | Fábrica | como-importar |
| 2 | ¿Cuánto cuesta importar de China a México? Ejemplos con números | cuánto cuesta importar de China | Costos | como-importar |
| 3 | Aranceles a China 2026: qué cambió y cómo calcular lo que pagas | aranceles China México 2026 | Aduana | como-importar |
| 4 | Qué es Yiwu y por qué ahí está el mayoreo más barato de China | qué es Yiwu | Fábrica | como-importar |
| 5 | Cómo pagar a un proveedor en China sin que te estafen | cómo pagar a proveedor en China | Pago | errores-y-consejos |
| 6 | Errores que me costaron dinero importando de China (Eduardo) | errores al importar de China | Errores | historias-de-eduardo |
| 7 | Padrón de importadores 2026: quién lo necesita y cómo sacarlo | padrón de importadores | Aduana | como-importar |
| 8 | Envío aéreo o marítimo desde China: cuál te conviene | envío marítimo desde China a México | Envío | como-importar |
| 9 | Joyería de acero inoxidable al mayoreo: guía para revender | joyería de acero inoxidable por mayoreo | Joyería | joyeria |
| 10 | Cómo saber si un proveedor chino es fábrica o revendedor | proveedor chino confiable | Fábrica | errores-y-consejos |

Cada una enlaza a la pilar (`/blog/como-importar-de-china-a-mexico`) y la pilar se actualiza para enlazarlas de vuelta.

## Fuentes de la investigación
- Aranceles 2026 (DOF 29/12/2025, 1,463 fracciones, 5%–50%): LexLatin, El Imparcial, CUCEA-UdG.
- Padrón de importadores: SAT, ficha 5/LA.
- Precios de cursos de terceros: sitios de CETYS, LatinoTrainers/INCEA, 100negocios, Kuinsen y Elevify (consultados en noviembre de 2026).
- Robots de IA y llms.txt: guías 2026 de Digital Applied y DEV Community.
- AI Overviews: HubSpot y guías 2026 (respuesta directa arriba, pasos, FAQ y E-E-A-T).

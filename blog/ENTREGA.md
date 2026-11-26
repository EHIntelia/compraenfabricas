# Blog de Compra en Fábricas de China — entrega (nov 2026)

Proyecto de Lovable: **China Direct Connect** (compraenfabricas.com), workspace "Eduardo's Lovable".
Nada está publicado en producción todavía: todo vive en el preview hasta que se apruebe el deploy.

## Estado en producción (11 nov 2026)
- Publicado en compraenfabricas.com: blog, 5 notas, imágenes, sitemap, robots y llms.txt.
- Search Console verificado (propiedad https://compraenfabricas.com/) y sitemap enviado.
- IndexNow activo: llave en /0548ff40ad255644b9c19950f3efce17.txt; 12 URLs enviadas (respuesta 202). Para avisar URLs nuevas, repite el POST a https://api.indexnow.org/indexnow con la misma llave.
- Inicio corregido a "5 proveedores de regalo" (confirmado: son 5).

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

---

## Lote 2: calendario de 10 notas (desde el 11 nov 2026)

Mapa de keywords y dueños de cada búsqueda: `docs/seo/fase-0-auditoria.md` (rama del agente SEO). La pilar sigue siendo dueña de "cómo importar de China a México" y "cómo comprar en China".

**Flujo por nota:** `posts/<slug>.md` → `python3 tools/check.py` → `python3 tools/make_images_notas.py <slug>` → `python3 tools/build_sql.py --status draft <slug>` → carga en `posts` → vista previa con `python3 tools/preview.py <slug>` (el sitio no muestra borradores) → confirmación → `published` → deploy (por las imágenes) → enlace desde la pilar → IndexNow → indexación en Search Console.

| # | Slug | Keyword | Meta title | Palabras | Estado | Fecha |
|---|---|---|---|---|---|---|
| B | requisitos-para-importar-de-china-a-mexico | requisitos para importar de China a México | Requisitos para importar de China a México en 2026 | ~1,810 | **Publicada** (enlazada desde la pilar) | 11 nov 2026 |
| C | cuanto-cuesta-importar-de-china | cuánto cuesta importar de China | Cuánto cuesta importar de China en 2026: ejemplo real | ~1,670 | **Publicada** (enlazada desde la pilar y desde productos) | 11 nov 2026 |
| A | comprar-directo-de-fabrica-en-china | comprar directo de fábrica en China | Comprar directo de fábrica en China sin intermediarios | ~1,550 | **Publicada** (enlazada desde la pilar, Paso 2) | 13 nov 2026 |
| E | como-pagar-a-un-proveedor-en-china | cómo pagar a un proveedor en China | Cómo pagar a un proveedor en China sin que te estafen | ~1,610 | **Publicada** (enlazada desde la pilar, Paso 5) | 13 nov 2026 |
| D | aranceles-china-mexico-2026 | aranceles a China 2026 | Aranceles a China 2026: qué subió y cuánto pagas | ~2,030 | **Publicada** (enlazada desde la pilar, requisitos y costos). Revisión mensual contra el DOF | 21 nov 2026 |
| H | envio-aereo-o-maritimo-desde-china | envío aéreo o marítimo desde China | Envío aéreo o marítimo desde China: cuál te conviene | ~1,820 | **Publicada** (enlazada desde la pilar, Paso 6, y desde costos) | 23 nov 2026 |
| F | que-es-yiwu | Yiwu | Qué es Yiwu y cómo comprar en el mercado mayorista | ~2,100 | **Publicada** (enlazada desde la pilar, Paso 2, y desde comprar directo de fábrica) | 23 nov 2026 |
| I | joyeria-de-acero-inoxidable | joyería de acero inoxidable | Joyería de acero inoxidable: qué es y por qué se vende | ~1,735 | **Publicada** (enlazada desde la nota de joyería y desde productos) | 25 nov 2026 |
| J | feria-de-canton | Feria de Cantón | — | — | Por escribir (2–3 meses antes de la edición) | — |
| G | errores-que-me-costaron-dinero-importando | errores al importar de China | Errores al importar de China que me costaron dinero | ~1,750 | **Publicada** (enlazada desde la pilar, sección de errores, y desde la nota de Eduardo) | 25 nov 2026 |

**Meta descriptions**
- B: "Requisitos para importar de China a México en 2026: RFC, e.firma, padrón de importadores, agente aduanal, pedimento y NOM. Explicado fácil y con fuentes." (153)
- C: "Cuánto cuesta importar de China a México en 2026: mercancía, flete, arancel, IVA, agente aduanal y envío, con un ejemplo con números. Calcula tu costo." (151)

**Al publicar B y C:** agregar en la pilar (Paso 7) el enlace a B en el punto de padrón y a C en el punto de impuestos. La pilar no tiene una sección de costos larga, así que no hay texto que resumir.

**Cambio ya aplicado (11 nov):** la pilar enlazaba a /cotizador (en construcción). Ahora enlaza a /logistica#cotizar.

**[PENDIENTE] y datos por confirmar**
- B: no se pudieron abrir directo sat.gob.mx ni dof.gob.mx desde esta sesión (red bloqueada); los datos salen de las fichas oficiales vistas por buscador, con fecha de consulta. Conviene que alguien abra la ficha 5/LA y confirme: (1) el plazo de respuesta del padrón (la nota no lo menciona a propósito) y (2) los topes de la regla 1.3.1 de las RGCE 2026 para importar sin padrón (la nota solo dice que existen excepciones).
- C: el ejemplo es hipotético salvo IVA 16%, DTA 8 al millar y la caja S100 (~$31/pieza). Si Eduardo da un caso real de importación con números, la nota se vuelve más fuerte.
- D: la LIGIE tuvo otra reforma con fecha DOF 13-10-2026. Revisarla antes de escribir la nota de aranceles.

**Pedidos al agente SEO** (no los toca el agente de contenido)
1. **Vista previa de borradores:** el blog solo lee notas `published`, así que un borrador no se puede ver en el preview. Propuesta: ruta de vista previa con token o una bandera solo en el preview.
2. **Corregir la sección 18 del handoff:** Google dejó de mostrar FAQ enriquecidos para todos desde el 7 de mayo de 2026.
3. **IndexNow automático** al publicar una nota (hoy el POST es manual).
4. ~~Si se publica `/curso-para-importar-de-china`, avisar~~ Hecho: salió en el deploy del 13 nov y la nota de cursos ya enlaza ahí.

**Publicación de B y C (11 nov 2026):** pasadas a published, deploy hecho (incluyó solo la Tanda 1 del agente SEO, ya publicada, y las imágenes del blog), enlaces agregados en la pilar (Paso 7) y en la nota de productos (hacia C). IndexNow y verificación en producción: mensaje en cola en Lovable detrás de la Tanda 2 del agente SEO. Falta pedir indexación en Search Console.

**Publicación de A y E (13 nov 2026):** 8 imágenes subidas a Lovable (commit d54436a), deploy hecho con autorización del usuario. Ese deploy también publicó lo que el agente SEO tenía pendiente: Fase 2 (/curso-para-importar-de-china, /preguntas-frecuentes, schema del autor), fotos reales de Eduardo, sección NADIE, WhatsApp con página de origen, eventos del Pixel, videos 720p y un cambio automático de bun.lock. A y E pasaron a published con published_at = now(). Se agregaron enlaces en la pilar (Paso 2 → A, Paso 5 → E) y en la nota de cursos hacia /curso-para-importar-de-china. Las md5 de la base coinciden con el repo. Verificado en producción: las 3 notas, las 8 imágenes, el sitemap y llms.txt responden 200, y la pilar enlaza a A y E. IndexNow devolvió 200 para A, E, la pilar, el sitemap, la nota de cursos y /curso-para-importar-de-china. Falta pedir indexación en Search Console de las 2 notas nuevas.

**Meta descriptions A y E**
- A: "Cómo comprar directo de fábrica en China sin intermediarios: diferencia entre fábrica, trading y revendedor, señales para reconocerlos y cómo validarla." (152)
- E: "Cómo pagar a un proveedor en China de forma segura: transferencia, Alipay, PayPal y carta de crédito, cuánto pagar por adelantado y señales de fraude." (150)
- A y E se enlazan entre sí: publicarlas juntas. Al publicarlas, enlazar desde la pilar (Paso 2 → A, Paso 5 → E).

**Canva (carpeta FAHYMS7Wadk):** esta sesión puede listar la carpeta pero no ver ni descargar las imágenes (media.canva.com bloqueado por la red). Los archivos se llaman "Signature_…", sin descripción.

## Design system en las notas (desde el 21 nov 2026)

Las notas nuevas siguen el **Compra en Fábricas Design System** (artifact https://claude.ai/artifact/8C8JC157VBWdCqCS4mbui4).

**Texto**
- **Excepción decidida por el usuario el 21 nov:** el blog va en **primera persona de Eduardo** ("en mi caso", "te explico"), aunque el design system pida voz de marca. Los servicios se nombran en plural ("nuestro equipo", "nosotros te lo traemos").
- Del design system se mantiene: tutear al lector, sin guiones largos (—), sin la palabra "PDF" (se usa guía, material o documento) y sin "gratis".

**Imágenes** (con `tools/make_images_ds.py`, plantillas en `tools/ds.py`)
- Arial (Liberation Sans en este equipo) y logo real: `brand/logo-horizontal.png`, con versión blanca.
- Fondo crema. El degradado solo va en detalles (barras, números, palabra clave).
- Badges en mayúsculas, rojo sobre durazno.
- Fotos del banco del design system, redondeadas 24px. Las que usa cada nota se copian a `brand/fotos/` con nombre descriptivo.

**Nota D (aranceles):** está en primera persona de Eduardo y usa las imágenes nuevas.
- Fuentes oficiales leídas el 21 nov 2026 por el agente de Lovable, porque la red de esta sesión bloquea gob.mx:
  - DOF 29/12/2025: 1,463 fracciones, de 5% a 50%. La mayoría quedan en 25% (669) o 35% (612).
  - DOF 23/04/2026: 185 fracciones, de 5% a 35%.
  - DOF 13/10/2026: solo la fracción 9803.00.01.
  - RGCE 2026, regla 3.7.35: 33.5%, sin cambios en la 1a ni en la 2a modificación.
- Pendiente: los decretos citan una modificación a la Tarifa del DOF del 26/03/2026 que SNICE no enlista. Revisarla en la revisión mensual.

**Notas publicadas antes del design system:** se quedan en primera persona de Eduardo, como pidió el usuario. Lo único que no sigue el design system son sus imágenes (marca dibujada, fuente Inter) y algunos guiones largos en el texto. Se pueden regenerar si el usuario lo pide.

**Vista previa del borrador D:** https://claude.ai/artifact/RDRQWUZNhkPCJoAb5Djtmi

**Publicación de D (21 nov 2026):**
- 5 imágenes subidas a Lovable (commit dd1a2ef) y deploy hecho con autorización del usuario.
- El deploy también publicó lo que habían hecho otras sesiones del usuario: precio de la Escuela a $15 USD/mes, infografía de cursos corregida, GA4, reseñas y cambios del catálogo de cajas.
- D quedó published con published_at = now(). Se agregaron enlaces a D desde la pilar (Paso 7, fracción arancelaria), desde requisitos (sección de fracción arancelaria) y desde costos (sección de arancel). Las md5 de la base coinciden con el repo.
- Verificado en producción: D, sus 5 imágenes, las 3 notas que la enlazan, el sitemap y llms.txt responden 200, y /escuela muestra $15 USD. IndexNow devolvió 200 para 8 URLs. Falta pedir indexación de D en Search Console.

**Cambio de precio de la Escuela (21 nov 2026, otra sesión):** ahora es $15 USD/mes y ya no existen los planes de $250 MXN/mes ni $2,500/año.
- Esa sesión actualizó en la base las notas de cursos y de Eduardo. El repo se sincronizó con la base (md5 iguales).
- También se regeneró la tabla de cursos en `img/` y se corrigió el handoff.
- **Regla:** antes de reconstruir cualquier nota con build_sql, compara su md5 con la base. Otras sesiones pueden editar la tabla posts directamente.

**Nota H (envío aéreo o marítimo):** borrador del 21 nov 2026, en primera persona de Eduardo.
- **Datos reales del sitio (/logistica):** aéreo se cobra por kilo y marítimo consolidado por metro cúbico; la cotización pide CBM, kilos y ciudad en China.
- **Datos de referencia con fuente:**
  - Divisor 6,000 (IATA) y 5,000 en exprés.
  - Tránsito puerto a puerto Shanghái a Manzanillo de 17 a 29 días y Shenzhen o Guangzhou de 20 a 35 días, publicados por agentes de carga.
  - Contenedor de 20' de unos 33 m³ y de 40' de unos 67 m³.
- **Sin precios de flete:** la nota no los menciona porque no hay datos propios.
- **[PENDIENTE, opcional]:** si Eduardo da sus tiempos reales de aéreo y marítimo (por ejemplo, Yiwu a Monterrey), la nota gana mucho.
- **Al publicar:** enlazar desde la pilar (Paso 6, envío) y desde costos (sección de envío).

**Publicación de H (23 nov 2026):**
- 5 imágenes subidas a Lovable (commit 73836d9) y deploy hecho con autorización del usuario.
- El deploy también publicó lo que habían hecho otras sesiones del usuario: fechas de clase en hora CDMX, LCP de joyería y escuela, página del curso Monterrey, reseñas reales y SAG20 marcada como vendida.
- H quedó published con published_at = now(). Enlaces agregados en la pilar (Paso 6, tras los tipos de envío) y en costos (sección de envío). Las md5 de la base coinciden con el repo.
- Verificado en producción: H, sus 5 imágenes (al principio daban 404 y salieron en cuanto terminó el deploy), la pilar y costos (enlazan a H), el sitemap y llms.txt responden 200. IndexNow devolvió 200. Falta pedir indexación de H en Search Console.

**Nota F (Yiwu):** borrador del 23 nov 2026, en primera persona de Eduardo. No nombra proveedores ni menciona WeChat.
- **Datos con fuente:** casi 80,000 puestos y más de 2.1 millones de productos (China Daily, marzo 2026); tren de Shanghái Hongqiao a Yiwu en 1.5 a 2 h (Travel China Guide). Los horarios no van exactos porque las fuentes no coinciden.
- **Lo que sí se afirma de Eduardo:** más de 26 años importando y equipo propio en China ("chinos que negocian con chinos"). **No** se afirma que haya ido a Yiwu.
- **[PENDIENTE Eduardo]** Son comentarios HTML ocultos en `posts/que-es-yiwu.md`; build_sql los quita y la nota se lee completa sin ellos:
  1. Su experiencia en Yiwu: desde cuándo va o compra ahí, cuántas veces y una anécdota real de la primera vez.
  2. Qué ha comprado él o sus clientes en Yiwu (categorías, sin nombrar proveedores) y qué le ha funcionado para revender.
  3. Un error real de un cliente que compró en Yiwu y cómo se resolvió.
  4. Consejo práctico para la primera visita: dónde hospedarse, cuántos días, en qué orden recorrer y cuándo no ir.
- **Al publicar:** enlazar desde la pilar (Paso 2, donde menciona Yiwu) y desde comprar directo de fábrica (sección de dónde encontrar fábricas).

**F completada con información real de Eduardo (23 nov 2026):**
- **Fuente:** `contenido/transcripts/transcripts_eduardo.md`, en la rama `claude/affectionate-faraday-guyqfo`, más lo que contó el usuario.
- **Datos que entraron:**
  - Ha ido a Yiwu y a Guangzhou, y tiene oficina en Guangzhou con compradores chinos.
  - Anécdota real en Guangzhou: al confirmar un pedido de cadenas y antes del depósito, el proveedor dijo que el precio era "el puro cobre", sin baño, y hubo que renegociar. Otra vez canceló un pedido porque le cambiaron las condiciones.
  - "Negociar con los chinos es un arte". "Puedes comprar como si fueras Walmart, desde poquita cantidad". Ir muchas veces y hacerse amigo de los chinos.
  - Busca "poquita cantidad de algo que valga mucho dinero". Comprar en Yiwu sale de 20% a 30% más barato que en las plataformas chinas en línea. China va 14 horas adelante.
- **Corrección de enfoque:** Eduardo describe los puestos como "tiendas y showrooms de fábrica". La nota ahora dice que hay tiendas de fábrica y también revendedores.
- **Diferencia de números:** Eduardo dice "220 mil tienditas" en sus videos; la nota usa la cifra de China Daily (casi 80,000 puestos).

**Publicación de F (23 nov 2026):**
- 5 imágenes subidas a Lovable (commit f30d376) y deploy hecho; el deploy incluyó "ResenasFranja" de otra sesión.
- F quedó published. Enlaces agregados en la pilar (viñeta de Yiwu, Paso 2) y en comprar directo de fábrica (ciudades especializadas). Las md5 de la base coinciden con el repo.
- Verificado en producción: F, sus 5 imágenes, la pilar y comprar directo de fábrica (enlazan a F), el sitemap y llms.txt responden 200. IndexNow devolvió 200. Falta pedir indexación de F en Search Console.

**Nota I (joyería de acero inoxidable):** borrador del 23 nov 2026, en primera persona de Eduardo. El CTA va a /joyeria y el texto no enlaza a info.joyeria.shop.
- **Datos de Eduardo (transcripts):**
  - 22 años en joyería de chapa y acero; empezó con dinero prestado y poca mercancía.
  - Trabaja acero 316L. "El argumento de calidad se gana en la mano, no en el papel."
  - Margen de ejemplo: 25 pesos de costo, 50 de mayoreo y 250 de menudeo.
  - Mínimos para diseño propio: chapa unas 120 piezas por modelo y acero unas 360, porque necesita molde.
  - Anécdota del "puro cobre" en Guangzhou (es la misma de F).
- **Datos técnicos generales:** 316L lleva molibdeno y bajo carbono, frente al 304. No se afirma que sea hipoalergénico en absoluto.
- **No se menciona el pedido mínimo de inventario:** /joyeria lo marca como pendiente de confirmar con Eduardo ("desde 36 piezas por modelo").
- **Al publicar:** enlazar desde la nota de joyería (sección de tipos de joyería) y desde productos (donde menciona joyería).

**Publicación de I (25 nov 2026):**
- 5 imágenes subidas a Lovable (commit 53363b7) y deploy hecho.
- El deploy también publicó lo que hicieron otras sesiones del usuario: /proveedores protegido con login, página "Quiénes somos", sello de pago seguro, número oculto en Dirección, ubicación SEO y texto del crédito.
- I quedó published. Enlaces agregados en la nota de joyería (tipos de joyería) y en productos (viñeta de margen). Las md5 coinciden.
- Verificado en producción: I, sus 5 imágenes, la nota de joyería y productos (enlazan a I), el sitemap y llms.txt responden 200. El cuerpo de I tiene 2 enlaces a /joyeria y ninguno a info.joyeria.shop. IndexNow devolvió 200. Falta pedir indexación de I en Search Console.

**Nota G (errores al importar):** borrador del 25 nov 2026, en primera persona de Eduardo, con historias reales sacadas de `contenido/transcripts/transcripts_eduardo.md`.
- **Las 2 bancarrotas:** la primera a los 26 años y la segunda a los 36. De la segunda tardó año y medio en levantarse y 5 años en pagar todo. Su frase: "no fue mala suerte, fueron decisiones mal tomadas".
- **3,000 dólares prestados** que perdió por traer mercancía sin verla. Le han robado "10, 15 veces"; la nota dice "más de diez veces".
- **Anécdota del "puro cobre"** en Guangzhou y del pedido cancelado porque le cambiaron las condiciones.
- **Traer 100 piezas contra un importador que trae 30 a 50 mil por embarque:** mejor comprarle al mayorista local y probar.
- **El flujo de dinero:** pagas, esperas y todavía hay que vender y cobrar.
- **Cerrar negocios que sí dejaban dinero** porque distraían del principal.
- **Lo que se dejó fuera a propósito:** alcoholismo y temas familiares. Sí se menciona la depresión, que Eduardo cuenta en público.
- **Inconsistencia de fechas en los transcripts:** aparecen "hace 27 años" y "hace 13/15 años". La nota usa las edades (26 y 36), que sí cuadran con sus 49 años.
- **Portada:** es una foto de stock del banco (un emprendedor), no Eduardo.
- **Al publicar:** enlazar desde la pilar (sección de errores comunes) y desde la nota de Eduardo (sección de las 2 bancarrotas).

**Publicación de G (25 nov 2026):** 5 imágenes subidas a Lovable (commit bbf3075) y deploy hecho. G quedó published. Enlaces agregados en la pilar (después de la lista de errores comunes) y en la nota de Eduardo (sección de las 2 bancarrotas).

## Mejora de CTR en 3 notas (pedido del 25 nov 2026, datos de Search Console del 10 al 24 nov)

Las URL no cambiaron. Cada nota lleva "Actualizado: noviembre de 2026" visible. `dateModified` sale de `updated_at`, que quedó en el 25 nov.

**1. /blog/cursos-para-importar-de-china** (23 impresiones, posición 6.9, CTR 4.3%)
- Título: "Cursos para importar de China 2026: precios y cuál elegir" (57). Descripción nueva tal cual el pedido (155).
- Tabla rápida antes del primer H2, con columnas curso, precio, en vivo o grabado, incluye proveedores y soporte. La fila de la clase enlaza a /curso-para-importar-de-china.
- La tabla larga de la sección "Comparativa" se quitó para no repetirla; se dejaron el texto y la infografía.
- Sección y FAQ nuevas: "¿Hay cursos para importar de China en Monterrey?", con enlace a /curso-para-importar-de-china-monterrey. Las otras dos FAQ del pedido (cuánto cuesta y en vivo o grabado) ya existían. Quedan 7 FAQ.

**2. /blog/eduardo-hernandez-importaciones-china** (14 impresiones, posición 4.5, CTR 7.1%)
- Título: "Eduardo Hernández: 26 años importando de China y 2 quiebras" (59). El del pedido, con paréntesis, medía 61 y rebasaba el límite. Descripción tal cual el pedido (151).
- `focus_keyword` cambió a "Eduardo Hernández", porque la gente lo busca por su nombre.
- 2 fotos reales de Eduardo copiadas desde src/assets/opt (variantes de 1024 × 571) a public/blog/eduardo-hernandez-importaciones-china/: eduardo-hernandez-retrato.webp y eduardo-hernandez-fundador.webp. Viven solo en Lovable; la red de esta sesión no deja bajarlas al repo.
- Enlaces a /autor/eduardo-hernandez y a eduardohdz.com.
- El hueco pendiente de la sección de bancarrotas se llenó con la historia real (26 y 36 años, 3,000 dólares, año y medio y 5 años) y un enlace a G.

**3. /blog/comprar-directo-de-fabrica-en-china** (14 impresiones, posición 16.2, 0 clics)
- Título: "Comprar directo de fábrica en China: ¿es fábrica de verdad?" (59). El del pedido medía 61.
- Descripción: la del pedido sin una coma ("sin caer con un revendedor ... y cómo validarla antes de pagar"), para dejarla en 155.
- La lista pasó a 10 señales numeradas (se agregaron MOQ, tiempos de producción y dirección de planta) y la infografía se regeneró con 10 señales en el estilo nuevo.
- Sección nueva "¿Y si no quieres validarla tú?" con enlace a /validacion.
- Enlace desde /blog/como-pagar-a-un-proveedor-en-china: ya existía, al inicio de la nota.

**Pedido al agente SEO** (son páginas comerciales que el agente de contenido no toca):
5. Agregar en **/validacion** y en **/preguntas-frecuentes** un enlace a **/blog/comprar-directo-de-fabrica-en-china**. Texto sugerido: "cómo saber si un proveedor chino es fábrica".

**Revisión:** en 2 o 3 semanas, mirar en Search Console el CTR y la posición de las 3 notas.

**Verificado en producción (25 nov 2026):**
- G y sus 5 imágenes responden 200, y la pilar y la nota de Eduardo enlazan a G.
- Las 3 notas de CTR muestran el título nuevo y tienen dateModified 2026-11-25.
- En cursos: la tabla queda antes del primer H2, enlaza a las dos páginas de curso y la FAQ de Monterrey está en el JSON-LD.
- En Eduardo: las 2 fotos y los enlaces a /autor y a eduardohdz.com.
- En comprar directo de fábrica: la lista de 10 señales, el enlace a /validacion y la infografía nueva.
- El sitemap y llms.txt incluyen G. IndexNow devolvió 200 para las 5 URLs y el sitemap.
- Falta pedir indexación en Search Console de G y de las 3 notas actualizadas.
- 26 nov 2026: el usuario pidió en Search Console la indexación de G, cursos, Eduardo y comprar directo de fábrica. Revisión de CTR y posición: entre el 10 y el 17 de diciembre de 2026.

## Fotos de Eduardo copiadas al repo (26 nov 2026)

Las 2 fotos de la nota de Eduardo solo existían en Lovable (`public/blog/eduardo-hernandez-importaciones-china/`). Se copiaron a `blog/img/eduardo-hernandez-importaciones-china/` byte por byte y se verificó el sha256 contra el original:

| Archivo | Bytes | Medidas | sha256 |
|---|---|---|---|
| eduardo-hernandez-retrato.webp | 18928 | 1024×571 | 4edbc7c2d44bcefc71c912a485da911bff702a25b1ec4036b65d9a3597417e1b |
| eduardo-hernandez-fundador.webp | 22508 | 1024×571 | 3609ad613e87de0e92163e06b2c53bf5af79530d8481219866337fbd1ddc3475 |

Cómo se sacaron: el agente de Lovable las subió en base64 en el commit 82f91bb3 y las borró en 643f49a4. No se cambió nada en el sitio publicado.

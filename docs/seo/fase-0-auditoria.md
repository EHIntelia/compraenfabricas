# Fase 0 — Auditoría SEO de compraenfabricas.com

**Fecha:** 11 de noviembre de 2026
**Alcance:** solo investigación y auditoría. **No se cambió nada** en Lovable ni se gastaron créditos (cero `send_message`).
**Proyecto Lovable revisado:** "China Direct Connect" (es el que publica compraenfabricas.com), commit `36c7251`.

---

## 0. Antes de leer: 3 cosas que necesito de ti

1. **No pude leer el HANDOFF.** El archivo `HANDOFF_Compra_en_Fabricas_COMPLETO.md` vive en tu proyecto de Claude y no tengo acceso a esos proyectos desde aquí (tampoco está en tu Google Drive). Usé como sustituto el *project knowledge* de Lovable, que ya trae marca, tono, CTAs y reglas. **Pégamelo o súbelo al repo** antes de la Fase 2 para revisar contradicciones finas.
2. **Hay contradicciones entre tu prompt y el project knowledge de Lovable** (sección 6). Tú decides cuál manda.
3. **Hay un problema urgente que no es de SEO** (sección 1): datos de proveedores publicados y abiertos a Google.

---

## 1. Urgente (arreglar aunque no hagamos nada más)

| # | Hallazgo | Dónde | Por qué importa |
|---|---|---|---|
| U1 | **La página del regalo de la clase está pública e indexable.** Muestra nombre, ciudad, WeChat y WhatsApp de los 3 proveedores "que se abren al entrar". Cualquiera la ve sin pagar y Google la puede indexar. | `/proveedores` (sin `noindex`, sin protección) | Regalas gratis lo que vendes en $990, y viola tu regla de "no publicar WeChat ni nombres de proveedores de regalo". |
| U2 | **Nombres de proveedores publicados:** AEMAI y Port Tide aparecen con nombre en la página de la clase (como "Regalo #1 y #2") y en el marketplace. | `/clase`, `/marketplace` | Misma regla. Tú decides si en marketplace sí se pueden mostrar (ahí es el producto que vendes). |
| U3 | **Se sigue ofreciendo "clase gratis por Zoom".** El botón "Registrarme a la clase gratis" manda a `/clase-gratis`, que redirige al inicio. Funnel roto + servicio que ya no existe. | `/empieza-aqui` (3 botones + FAQ) | Promesa falsa a quien llega de anuncios viejos o de Google. |

Propuesta: `noindex` + quitar del sitemap `/proveedores` de inmediato y, mejor aún, protegerla (enlace secreto o acceso con correo de compra). Te lo dejo listo para la Fase 1 con tu OK.

---

## 2. Cómo está construido el sitio (stack y render)

- **Framework:** TanStack Start con **SSR** (`@tanstack/react-start` 1.168, Nitro, React 19). No es la SPA vieja de Vite. **No hace falta migrar.**
- **Qué ve un bot:** probé el HTML crudo (sin ejecutar JS, con user-agent de Googlebot) en 30 rutas. **Todas traen `<title>`, description, H1 y el texto completo.** Esto es lo más difícil y ya está resuelto.
- **Ya existe y funciona:** `robots.txt` (permite todo y a los bots de IA), `sitemap.xml` dinámico (incluye blog), `llms.txt`, blog con `BlogPosting`, `FAQPage`, `BreadcrumbList`, página de autor con `ProfilePage`/`Person`, schema `Organization` y `WebSite` en todo el sitio, `lang="es-MX"`.
- **404 reales:** una URL inexistente responde **404** (no hay soft 404). Bien.

---

## 3. Auditoría técnica por tema

### 3.1 Metadatos por ruta (HTML crudo)

| Ruta | Title (caracteres) | Description (caracteres) | Canonical | Nota |
|---|---|---|---|---|
| `/` | "Compra en Fábricas de China — Importa y crece" (45) | 110 (corta) | relativa `/` | El title no trae "importar de China". Lighthouse marca error de canonical. |
| `/clase` | 90 (**muy largo**) | 192 (**muy larga**) | **falta** | og:image genérica de Lovable. |
| `/asesoria-china` | 57 ✓ | 138 ✓ | relativa | |
| `/escuela` | 56 ✓ | 154 ✓ | relativa | |
| `/joyeria` | 71 (largo) | 166 (larga) | **falta** | Title empieza con "JAICO" (marca), no con la keyword. |
| `/marketplace` | 66 | 140 ✓ | relativa | og:url relativa. |
| `/productos` | 47 | 223 (**muy larga**) | relativa | Lighthouse marca error de canonical. |
| `/logistica` | 59 ✓ | 126 | relativa | |
| `/cotizador` | "…de China a **España**" | 93, en euros | **falta** | ¿Es intencional que el cotizador sea para España? |
| `/cotizar-envio` | 53 | 110 | **falta** | |
| `/empieza-aqui` | 57 ✓ | 155 ✓ | relativa | Ofrece clase gratis (U3). |
| `/validacion` | 55 ✓ | 169 | relativa | Ver contradicción C2. |
| `/adn` | 63 | 148 | relativa | Producto "ADN de tu Negocio" ($1,000): ¿sigue vigente? No es de China. |
| `/proveedores` | 52 | — | **falta** | U1. Debe ser `noindex`. |
| `/blog` y notas | 49–59 ✓ | 143–150 ✓ | **absoluta ✓** | El blog está bien hecho. |
| `/autor/eduardo-hernandez` | 67 | 147 ✓ | absoluta ✓ | |

**En TODAS las páginas:**
- `<meta name="author" content="Lovable">` y `twitter:site = @Lovable` (herencia de la plantilla). Hay que cambiarlos.
- `og:image` es la misma imagen genérica de Lovable (salvo blog y autor). Es la vista previa que sale en **WhatsApp y Facebook**, justo donde vive tu funnel.
- `twitter:card = summary` (chica) en casi todo.

### 3.2 Sitemap

Incluye URLs que **no deberían estar**:
- `/clase-gratis` → redirige (307) al inicio.
- `/paquetes` → redirige (307).
- `/clase-grabada` → tiene `noindex` (contradicción: "no me indexes" pero "aquí está en el sitemap").
- `/validacion` y `/adn` → según lo que decidas (C2, C6).

Falta `lastmod` en todas las páginas comerciales. Las notas del blog sí lo tienen.

### 3.3 Redirecciones

| Prueba | Resultado | Debe ser |
|---|---|---|
| `www.compraenfabricas.com` | **302** → sin www | 301 |
| `/clase/` (barra final) | **307** → `/clase` | 301/308 |
| `/clase-gratis`, `/paquetes`, `/clase-privada`, `/cotizacion-cajas` | **307** (temporal) | 301 si ya no van a volver |
| `http://` → `https://` | No lo pude probar (la red de esta sesión no permite http). Lovable lo maneja; lo verificamos en Fase 1. | 301 |

Los 302/307 le dicen a Google "es temporal, no muevas la autoridad". Ojo: el 302 de www lo pone el hosting de Lovable; puede que solo se cambie desde la configuración del dominio.

### 3.4 Página 404

Responde 404 correctamente, pero está **en inglés** ("Page not found", "Go home") y no tiene enlaces útiles. Hay que traducirla y poner enlaces a `/clase`, a la guía principal y al blog.

### 3.5 Enlaces "invisibles" (botones que Google no sigue)

Buena noticia: el menú, el footer y casi todos los CTA ya usan `<Link>`/`<a href>`. Los botones sin `href` que encontré son de **scroll dentro de la misma página** ("Ver todo lo demás", "Ver los niveles", "Quiero que me coticen") o de **pago** (Stripe en `/validacion`), y eso está bien.

Lo que sí falta es **enlazado interno**:
- `/joyeria`, `/escuela`, `/logistica` y `/asesoria-china` tienen footer propio sin enlaces al resto del sitio.
- El footer general no enlaza a Escuela, Joyería, Logística, Asesoría ni a la página de Eduardo.
- Las páginas comerciales no enlazan al blog ni a las guías.
- En inicio, la tarjeta "Joyería" manda directo a `info.joyeria.shop` en lugar de a `/joyeria`.

### 3.6 Datos estructurados (JSON-LD)

| Tipo | Estado |
|---|---|
| Organization | Existe. Faltan `alternateName`, `contactPoint` (WhatsApp), `areaServed` (MX y LATAM), `sameAs` a YouTube y Skool. |
| WebSite | Existe. Falta `alternateName`. |
| Person (Eduardo) | Existe en `/autor`. `sameAs` solo apunta a redes de la marca, no a perfiles **personales** de Eduardo. Falta `founder` de JAICO/Xijiao como organizaciones con URL. |
| **Event** (clase del 21 de nov) | **No existe.** Es el único schema que hoy puede darte resultado enriquecido de verdad. Hay fecha real en la página: 21 de noviembre. |
| Course | No existe. |
| Product + Offer | No existe. `/productos` sí muestra precio visible por caja → candidato. |
| VideoObject | No existe (marketplace, clase, logística, joyería tienen video). |
| BreadcrumbList | Solo en blog y autor. |
| FAQPage | Solo en blog. Clase, escuela, joyería y productos tienen preguntas visibles sin schema. |
| HowTo | Se usa en una nota del blog. No hace daño, pero Google ya no lo muestra desde 2023. |
| Reseñas/estrellas | No hay. Bien, así debe quedar. |

### 3.7 Velocidad (Lighthouse móvil, "antes")

La API pública de PageSpeed no tenía cupo sin clave, así que corrí **Lighthouse 12** en modo móvil con el Chromium de esta sesión (mismo motor que PageSpeed; datos de laboratorio, no de usuarios reales).

| Página | Performance | SEO | LCP | TBT | CLS | Peso total |
|---|---|---|---|---|---|---|
| `/` | 90 | 92 | **3.2 s** | 10 ms | 0 | 1.8 MB |
| `/clase` | 81 | 100 | **4.4 s** | 0 ms | 0.043 | **24 MB** |
| `/blog/como-importar-de-china-a-mexico` | 86 | 100 | **3.5 s** | 20 ms | 0 | 0.6 MB |
| `/joyeria` | 74 | 100 | **5.4 s** | 0 ms | 0 | **33 MB** |
| `/productos` | 79 | 92 | **4.8 s** | 40 ms | 0 | 4.3 MB |

Meta: LCP < 2.5 s. **Ninguna llega.** INP/TBT y CLS están bien.

Causas principales:
1. **Videos con autoplay y `preload="auto"`** en clase, joyería (7 videos), escuela, logística y asesoría: descargan decenas de MB al abrir la página. Esto también gasta los datos del celular de tu cliente.
2. **Imágenes en JPG sin WebP/AVIF ni `srcset`**: 1.3 MB de ahorro posible en inicio y 1.5 MB en productos.
3. **Animación de entrada (`opacity: 0`)**: en varias páginas el texto llega en el HTML pero invisible hasta que carga el JavaScript. Retrasa el LCP (en joyería el "elemento más grande" termina siendo el logo del menú).
4. La imagen principal del inicio no tiene `fetchpriority="high"`.
5. Unos 128 KB de JavaScript sin usar en todas las páginas.

No se pudieron medir datos de campo (CrUX) por la misma falta de cupo. Con Search Console verificado los veremos.

### 3.8 robots.txt, llms.txt, IndexNow

- `robots.txt`: permite todo, nombra a GPTBot, OAI-SearchBot, ChatGPT-User, Google-Extended, PerplexityBot, ClaudeBot y Claude-SearchBot. Bien. Googlebot y Bingbot ya entran por `User-agent: *`.
- `llms.txt`: existe. Le falta la historia de Eduardo, joyería, preguntas clave y datos duros.
- **IndexNow:** no existe.

---

## 4. Investigación de búsquedas

**Límite honesto:** no tengo acceso a volúmenes de búsqueda (ni Keyword Planner ni Semrush) y mi buscador da resultados de EE. UU., no de google.com.mx. La dificultad es una estimación con base en quién aparece arriba. Cuando verifiquemos Search Console (Fase 4) tendremos los datos reales de México.

### 4.1 Qué domina hoy los resultados

- **Chilat domina casi todo**: decenas de artículos para "comprar en China para revender", "comprar directo de fábrica", "cuánto cuesta importar", "joyería de China", e incluso tiene clases en vivo. Es una agencia china con contenido en volumen.
- Para "cómo importar de China a México": Tiendanube, Siigo, Camtom, Elyex, emprendedor.com, The Logistics World. Guías genéricas de software o agencias.
- Para "requisitos / padrón de importadores": Camtom (guía 2026 del padrón) y Chilat.
- **"Eduardo Hernández" + importaciones o clase: cero resultados.** La marca personal no existe todavía para Google. Ese es el trabajo de la página de autor + YouTube + menciones externas.

**Qué les falta a todos (tu oportunidad):** nadie habla desde la experiencia de caminar las fábricas, con ejemplos con números reales de cajas que ya están en México, ni con errores propios (las 2 bancarrotas). Todo es contenido "de escritorio". Tu blog ya va en esa línea, y esa es la ventaja.

### 4.2 Mapa de keywords → página (1 página = 1 intención)

| Grupo de búsqueda | Intención | Dificultad realista | Página que debe rankear | Estado |
|---|---|---|---|---|
| curso para importar de China · curso de importación de China · curso para importar de China a México · clase para importar de China | Transaccional | Media | **Nueva** `/curso-para-importar-de-china` (o `/clase` enriquecida; ver 5.1) | Decidir |
| cursos para importar de China (comparativa, "mejores cursos") | Comercial | Media | `/blog/cursos-para-importar-de-china` | Existe ✓ |
| cómo importar de China a México · cómo comprar en China · cómo comprar en China para revender | Informativa | Alta (Chilat, Tiendanube) | `/blog/como-importar-de-china-a-mexico` como **página pilar** (crecerla) | Existe ✓ |
| requisitos para importar de China a México · padrón de importadores · necesito RFC para importar · agente aduanal | Informativa | Media-alta | **Nueva** guía de trámites (ej. `/blog/requisitos-para-importar-de-china-a-mexico`) | Proponer |
| cuánto cuesta importar de China · costos de importar | Informativa | Media | Sección dentro de la pilar ahora; nota propia después | Proponer |
| cómo pagar a proveedores en China · es seguro pagarle a un chino | Informativa | Media | Nota de blog | Proponer |
| proveedores confiables en China · comprar directo de fábricas en China · comprar en China sin intermediarios | Comercial | Alta (Chilat) | `/marketplace` | Optimizar |
| cajas de electrónica para revender · electrónica de China por mayoreo · importar electrónica de China | Transaccional | Baja-media | `/productos` | Optimizar |
| productos para importar de China · qué productos importar de China | Informativa | Media | `/blog/productos-para-importar-de-china` | Existe ✓ |
| joyería por mayoreo · joyería de acero inoxidable por mayoreo · joyería chapa de oro mayoreo | Transaccional | Media | `/joyeria` | Optimizar |
| importar joyería de China | Informativa | Baja-media | `/blog/importar-joyeria-de-china-para-vender` | Existe ✓ |
| envío de China a México · logística China México · cotizar flete de China | Transaccional | Media | `/logistica` (+ `/cotizar-envio`) | Optimizar |
| asesoría para importar de China | Transaccional | Baja | `/asesoria-china` | Optimizar |
| comunidad para aprender a importar · escuela de negocios en línea | Comercial | Baja | `/escuela` | Optimizar |
| Eduardo Hernández importaciones · Eduardo Hernández China | Marca | Baja (nadie compite) | `/autor/eduardo-hernandez` | Existe, enriquecer |
| Compra en Fábricas de China | Marca | Baja | `/` | Optimizar title |
| cómo comprar en Alibaba / 1688 · Yiwu · Feria de Cantón | Informativa | Alta / media | Notas de blog futuras (Yiwu y Cantón son donde Eduardo es fuente primaria) | Plan 90 días |
| preguntas sueltas ("¿cuánto es lo mínimo para empezar?", etc.) | Informativa | Baja | **Nueva** `/preguntas-frecuentes` (hub) | Proponer |

### 4.3 Canibalización que ya existe o que crearía el plan original

1. **`/autor/eduardo-hernandez` vs `/blog/eduardo-hernandez-importaciones-china`**: las dos pelean "Eduardo Hernández importaciones". Propuesta: la página de autor es la que rankea por el nombre; la nota se reenfoca a la historia ("26 años y 2 bancarrotas: lo que aprendí") y quita el nombre del inicio del title.
2. **La `/como-comprar-en-china` propuesta en tu prompt chocaría con la guía del blog** que ya rankea para "cómo importar de China a México". Los resultados para "cómo comprar en China" y "cómo importar de China a México" son casi los mismos → **una sola página**. Propuesta: **no crear ruta nueva**; convertir la nota del blog en la pilar y separar solo los **trámites** (padrón, RFC, agente aduanal), donde Google sí muestra resultados distintos.
3. **`/curso-para-importar-de-china` vs `/blog/cursos-para-importar-de-china`**: singular y plural suelen dar los mismos resultados. Se puede convivir si la nota se enfoca en "comparativa / mejores cursos" y la página nueva en "inscríbete". Hay riesgo; lo vigilamos en Search Console.
4. **`/empieza-aqui`** (H1 "Comprar en China directo de fábrica, sin intermediarios ni estafas") compite con `/marketplace`. Depende de si ese producto sigue vivo (C7).

---

## 5. Decisiones que necesito de ti

### 5.1 `/clase` y la página del curso
- **(a) Recomendado:** crear `/curso-para-importar-de-china` como página permanente (temario, para quién es, diferencias entre clase, escuela y asesoría, preguntas, quién enseña) y que mande a `/clase` para pagar. `/clase` se queda como landing de anuncios con la fecha de cada edición. Así no metes texto largo en la página que convierte tus anuncios.
- (b) Enriquecer `/clase` para que ella sea la orgánica. Más simple, pero alarga la landing de Meta y la fecha cambia cada edición.

### 5.2 Fechas de la clase para el schema `Event`
`/clase` dice **21 de noviembre**. En el proyecto hay un banner llamado `banner-clase-20nov.jpg`. ¿Cuál es la fecha correcta, a qué hora (zona de Monterrey/CDMX) y cuáles son las siguientes fechas? Sin fechas reales no pongo Event. Además, después del 21 la página quedará con fecha vencida: hay que definir cómo se actualiza.

### 5.3 Google Business Profile
No encontré dirección en México en el sitio. Menciones que encontré: "oficina en Guangzhou" (marketplace) y "tenemos showroom" (FAQ de joyería). Si hay un showroom u oficina real en México donde atiendes clientes, dime la dirección y lo evaluamos. Si no, no se crea GBP y usamos `areaServed`.

---

## 6. Contradicciones (prompt ↔ project knowledge ↔ sitio)

| # | Tema | Tu prompt dice | Project knowledge / sitio dice | Decides tú |
|---|---|---|---|---|
| C1 | Grabación de la clase | La clase es en vivo; "si dice incluye grabación" es contradicción | Knowledge: "con grabación y 5 proveedores de regalo, **tal como dice /clase**". Sitio: inicio y clase dicen "incluye grabación". | ¿Incluye grabación o no? |
| C2 | `/validacion` | Servicio eliminado; redirigir a `/clase` | Knowledge la lista en "Otros" y dice "No eliminar ni ocultar servicios existentes". Sitio: página viva con 3 botones de Stripe ($2,500 / $5,000 / $7,500), en el sitemap y enlazada desde inicio (tarjeta "Validación") y desde blog. | ¿Se elimina (301 a `/clase` o `/logistica`)? |
| C3 | Escuela | "$250/mes, **mini-curso gratis**" | Knowledge: "No mencionar curso o clase gratis". El sitio no menciona mini-curso. | ¿Existe un mini-curso gratis? |
| C4 | Clase gratis | (no aplica) | `/empieza-aqui` y el FAQ general (`FAQS` en `site.tsx`) la siguen ofreciendo. `/clase-grabada` habla de "la clase gratis cerró". | Confirmo quitarla (U3). |
| C5 | Años de experiencia | 26+ | Autor, blog, clase, inicio: **26**. Joyería, escuela, logística, asesoría, productos: **25**. | Unificar a 26+. |
| C6 | `/adn` | (no aparece) | "ADN de tu Negocio — clase en vivo $1,000". No es de importación. | ¿Sigue vigente? Si no, 301 o noindex. |
| C7 | Paquetes 1-3 | (no aparece) | `/empieza-aqui` vende "contacto de proveedor $1,500" (Hotmart). `/paquetes` ya redirige. | ¿Sigue vigente el contacto de $1,500? |
| C8 | Tono | Sin frases exageradas | `/empieza-aqui`: "Empieza a comprar en China hoy y **deja tu trabajo este año**". | Propongo quitarla. |
| C9 | Proveedores con nombre | Prohibido publicar nombres de proveedores de regalo | AEMAI y Port Tide con nombre en `/clase` y `/marketplace`; 3 más con WeChat en `/proveedores`. | U1/U2. |
| C10 | Cotizador | Envío China → México | `/cotizador` es China → **España** en euros. | ¿Intencional? |
| C11 | WhatsApp | `wa.me/5218120181761` con mensaje | `/marketplace` usa `wa.me/528120181761` sin mensaje (no se puede medir de dónde viene). | Unificar. |

---

## 7. Prioridades (impacto × esfuerzo)

| Prioridad | Tarea | Impacto | Esfuerzo | Fase |
|---|---|---|---|---|
| 1 | Proteger/`noindex` `/proveedores`; quitar nombres de proveedores de regalo; quitar "clase gratis" de `/empieza-aqui` | Alto (negocio) | Bajo | 1 |
| 2 | Limpiar sitemap (sacar redirecciones y noindex), 301 permanentes | Alto | Bajo | 1 |
| 3 | Canonical absoluta en todas las rutas; agregar las que faltan | Alto | Bajo | 1 |
| 4 | Quitar "Lovable" de author/twitter; OG 1200x630 de marca por página; `summary_large_image` | Alto (WhatsApp/FB) | Bajo-medio | 1 |
| 5 | Titles y descriptions a medida (keyword al inicio, 50–60 / 140–155) | Alto | Bajo | 1 |
| 6 | Schema `Event` por fecha real de clase + `Course`; mejorar `Organization`/`Person`/`WebSite` | Alto | Bajo-medio | 1 |
| 7 | Videos sin autoplay/preload (poster + clic), imágenes WebP con `srcset`, `fetchpriority` en la principal, quitar `opacity:0` del primer pantallazo | Alto (LCP y datos móviles) | Medio | 1 |
| 8 | 404 en español con enlaces | Medio | Bajo | 1 |
| 9 | Footer general completo y enlaces de páginas comerciales al blog | Medio | Bajo | 1 |
| 10 | `Product`+`Offer` en `/productos`, `VideoObject`, `FAQPage` y `BreadcrumbList` en comerciales | Medio | Medio | 1 |
| 11 | IndexNow + `llms.txt` más completo | Bajo-medio | Bajo | 1 |
| 12 | Página del curso (5.1), guía de trámites, hub de preguntas, convertir la guía del blog en pilar | Alto (a mediano plazo) | Alto | 2 |
| 13 | Enriquecer página de Eduardo (fotos reales, perfiles personales, NADIE) | Alto (E-E-A-T) | Medio | 2 |
| 14 | Search Console (DNS), Bing Webmaster, eventos de analítica, WhatsApp con origen | Alto (medir) | Bajo (lo haces tú, te guío) | 4 |
| 15 | YouTube, menciones y PR | Alto (IA) | Alto (tú) | 5 |

---

## 8. Lo que ya está bien (no tocar)

- SSR: los bots y las IAs reciben todo el contenido.
- 404 reales, sin soft 404.
- Un solo H1 por página en todo el sitio.
- Blog: titles, descriptions, canonical absoluta, autor con foto y enlace, fechas visibles, FAQ, breadcrumbs, enlaces a fuentes oficiales.
- `robots.txt` abierto a buscadores y bots de IA.
- Formularios (FormSubmit en logística), botones de Stripe y WhatsApp: no se tocaron.
- Sin reseñas ni estrellas inventadas.

---

## 9. Siguiente paso

Con tu OK y tus respuestas a las secciones 0, 5 y 6, preparo el mensaje de la **Fase 1** para Lovable en `plan_mode=true` (sin gastar créditos de edición hasta que apruebes el plan), revisando cada cambio con `get_diff` y **sin deploy** hasta que confirmes.

---

### Fuentes consultadas
- Resultados de búsqueda revisados (aproximación de EE. UU.): [Tiendanube MX](https://www.tiendanube.com/mx/blog/importar-de-china/), [Siigo MX](https://www.siigo.com/mx/blog/emprendimiento-y-ventas/importar-de-china-a-mexico/), [Camtom: guía del padrón 2026](https://www.camtomx.com/blog/padron-importadores-guia-completa-2026), [Camtom: importar de China](https://www.camtomx.com/blog/importar-de-china-a-mexico-guia-completa), [Elyex](https://elyex.com/requisitos-para-importar-de-china-a-mexico-2/), [emprendedor.com](https://emprendedor.com/importar-de-china-a-mexico-una-guia-completa-para-emprendedores/), [Chilat (blog)](https://www.chilat.com/blog/2108445265134866433), [Chilat: comprar directo a la fábrica](https://www.chilat.com/al-por-mayor/comprar-directamente-a-la-fabrica-en-china), [Chilat: importar joyas](https://www.chilat.com/al-por-mayor/importar-joyas-desde-china), [Tiendanube: proveedores de bisutería](https://www.tiendanube.com/mx/blog/proveedores-de-bisuteria).
- Lovable SSR: [lovable.dev/en/seo-aeo](https://lovable.dev/en/seo-aeo); TanStack Start SEO: [tanstack.com](https://tanstack.com/start/latest/docs/framework/react/guide/seo).
- Fin de FAQ rich results (7 de mayo de 2026): [TechWyse](https://www.techwyse.com/news/ai-search/google-faq-rich-results-deprecated-2026), [jsonld.com](https://jsonld.com/google-faq-rich-results-deprecated/).

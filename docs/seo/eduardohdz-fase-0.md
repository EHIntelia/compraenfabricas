# eduardohdz.com — Fase 0: re-auditoría SEO

**Fecha:** 21 de noviembre de 2026
**Alcance:** solo investigación. **No se cambió nada** en Lovable ni se gastaron créditos (cero `send_message`).
**Proyecto Lovable:** "Eduardo Hernández" (id `31eb7ad3-327e-43ed-9449-1c7cda622ec0`), commit `534f073`. Es el mismo commit que está publicado.
**Método:** el mismo de `fase-0-auditoria.md` de compraenfabricas:
- HTML crudo con user-agent de Googlebot y de bots de IA.
- Render con Chromium (lo que ve Google después de ejecutar el JavaScript).
- La versión Markdown que Lovable sirve.
- Lectura del código.
- Lighthouse 12 móvil local.

---

## 0. Resumen en 6 líneas

1. **El diagnóstico del 12 nov sigue casi igual, con un matiz importante en E1.** Según la documentación de Lovable, los proyectos Vite reciben **prerender automático para crawlers verificados** (Google, Bing, los de ChatGPT, Perplexity, Claude y Gemini). La versión Markdown que sirve Lovable sí trae todo el texto. Eso quiere decir que Google y las IAs **probablemente sí leen el contenido**. Lo que no se puede confirmar desde aquí: un user-agent falso no pasa la verificación. Se confirma con la Inspección de URL de Search Console.
2. **El problema nuevo más grave:** cuando la página se arma, **la canonical de TODAS las rutas apunta a `eduardohernandez.lovable.app`**, y ese dominio redirige (302) de vuelta a eduardohdz.com. Le estamos diciendo a Google "la página buena es otra", y esa otra lo regresa aquí. Se arregla con una línea (`src/components/SEO.tsx`).
3. **El menú no tiene enlaces que Google pueda seguir:** todos son `<button>` sin `href`. Para Google, el sitio casi no tiene enlaces internos.
4. **Hay dos meta description en cada página**: la genérica de `index.html` y la propia de la página.
5. **Velocidad muy baja:**
   - Performance de 44 a 51 y LCP de 6.2 a 9.8 s en móvil.
   - El JavaScript pesa **2.2 MB** (el panel interno viaja en el mismo paquete que la página pública).
   - Dos fotos pesan **1.8 MB cada una**.
6. **Recomendación:** migrar a TanStack Start (lo que hizo compraenfabricas).
   - Según la documentación de Lovable cuesta **10–35 créditos**, se hace sobre el proyecto sin tocar el sitio publicado y se puede revertir desde el historial.
   - Da 404 reales, HTML garantizado para cualquier bot y separa el panel del sitio público.

---

## 1. Hallazgos (re-verificados hoy)

| # | Hallazgo | 12 nov | Hoy (21 nov) | Prioridad |
|---|---|---|---|---|
| E1 | HTML crudo vacío | 11 palabras | **Igual con user-agent falso** (título + "Edit with"). Pero el Markdown de Lovable trae el texto completo, así que el prerender para bots verificados funciona. **Hay que confirmarlo en Search Console** (Inspección de URL → "Ver página rastreada"). | Alta (antes: muy alta) |
| E2 | Mismo title/description | Igual en todo | **Mejoró:** cada ruta ya tiene su title y description propios, vía `react-helmet`, una vez que se ejecuta el JavaScript. Pero `index.html` deja una **segunda description genérica** en todas las páginas. Varios títulos son largos, cortos o no traen la keyword (ver sección 3). | Alta |
| E3 | og:url / og:image a lovable.app | Sí | **Sigue, y es peor:** también la **canonical** de todas las rutas apunta a `eduardohernandez.lovable.app/...`, que hace 302 a eduardohdz.com. | **Urgente** |
| E4 | Sin sitemap.xml | 404 | **Sigue 404.** robots.txt existe (permite todo, bloquea /panel) pero no trae línea `Sitemap:`. No hay llms.txt. | Alta |
| E5 | Soft 404 | 200 | **Sigue:** `/no-existe-xyz` responde 200 con el title de la home y un H1 "404". En Vite no se puede dar un 404 real; con TanStack Start sí. | Media |
| E6 | www no responde | Sí | **Sigue:** `www.eduardohdz.com` no tiene DNS. Ojo: según la documentación, Lovable redirige entre dominios con **302**, no 301 ("no soporta 301 entre dominios conectados"). Se acepta el 302 de Lovable o se hace el 301 en el DNS/registrador. | Media |
| E7 | Cero JSON-LD | 0 | Solo `/sube-tus-ventas` tiene un `Course` (con `provider` NADIE). No hay Person, Organization ni WebSite. | Alta |
| E8 | "Edit with Lovable" | Visible | **Sigue visible** en todas las páginas. | Baja |
| E9 | /clase-gratuita | Existe | **Sigue** y está en el menú: "Clase Gratuita con Eduardo Hernández — Todos los sábados". Hay que confirmar si sigue. | Por confirmar |
| **E11** | **Menú sin enlaces rastreables** | — | Las 6 opciones del menú y "Analiza tu negocio" son `<button onClick>`. El logo es `<img onClick>`. "Conoce a Eduardo" y "Sobre NADIE" son anclas de la home (`/#sobre`, `/#nadie`), no páginas. | **Alta** |
| **E12** | **Contenido caducado** | — | `/reto`: "Comienza el 19 de abril". `/preventa-curso` y `/sube-tus-ventas`: "precio de lanzamiento hasta el 31 de julio". FAQ de sube-tus-ventas: "disponible a partir del 30 de abril de 2026". (En sube-tus-ventas el banner depende de `esPreventa`; hay que confirmar que ya no salga.) | Media |
| **E13** | **Datos de Eduardo inconsistentes** (dañan la entidad) | — | La mayor parte del sitio dice "8 años / +300 empresas". `/sube-tus-ventas` dice "**más de una década**" y "**más de 200 negocios**". `/reto-*` dice "+200 MiPyMEs". `/de-0-a-1-millon`: el title dice "Curso **gratuito**" y sube-tus-ventas lo da como bono "con valor de $12,000". | Media |
| **E14** | **Velocidad** | — | Ver sección 4. JS de 2.2 MB, PNG y JPG de 1.8 MB, Pixel síncrono en `<head>`. | Alta |
| **E15** | **Panel en el mismo paquete** | — | `/panel/*` (Stripe, Hotmart, Metricool, ManyChat, Skool) se carga en el mismo JavaScript que las páginas públicas. Ya tiene `noindex` y robots lo bloquea, pero pesa para todos los visitantes. | Media |
| **E16** | **Otra sesión trabajando en el panel** | — | Ediciones del 18 al 21 nov (ManyChat, campañas, Skool, seguidores). Cualquier publicación sube también ese trabajo. Hay que coordinar antes de migrar. | Coordinación |

---

## 2. Rutas: indexar o no

Criterio:
- **Indexar** = tiene valor de búsqueda y es estable.
- **noindex** = gracias, herramientas internas de aliados, ofertas con fecha y duplicados.

| Ruta | Qué es | Decisión propuesta | Nota |
|---|---|---|---|
| `/` | Home: diagnóstico + Eduardo + NADIE + cursos | **Indexar** | Entidad "Eduardo Hernández consultor de negocios". |
| `/diagnostico` | Quiz de diagnóstico (15 preguntas) | **Indexar** | "diagnóstico de negocio gratis". Hoy solo tiene 37 palabras visibles: le falta texto arriba o abajo del quiz. |
| `/diagnostico-evergreen` | Mismo quiz, versión para anuncios | **noindex** + canonical a `/diagnostico` | El botón "Analiza tu negocio" manda aquí. ¿Va en anuncios? |
| `/reto` | Reto de 2 días (fecha 19 abr) | **noindex** (o 301 si ya murió) | Caducado. |
| `/reto-diagnostico` | Reto grabado gratis | **noindex** | Landing de anuncios. |
| `/reto-landing` | Reto por $1 | **noindex** | Landing de anuncios. |
| `/comunidad` | Comunidad NADIE | **Indexar** | "comunidad de empresarios / emprendedores". |
| `/prompt-maker` | Herramienta gratis de prompts | **Indexar** (secundaria) | Tráfico de IA; poco ligado a la entidad. |
| `/aliados`, `/aliados-reto`, `/aliados-curso` | Espacio de afiliados | **noindex** | Internas. |
| `/preventa-curso` | Preventa con fecha | **noindex** o 301 a `/sube-tus-ventas` | Caducada. |
| `/sube-tus-ventas` | Curso de pago (Hotmart) | **Indexar** | "curso de ventas para emprendedores / MiPyME". |
| `/recursos` | Índice de recursos | **Indexar** | Hub de guías. |
| `/recursos/codigos-chatgpt` | 10 códigos de ChatGPT (PDF) | **Indexar** | "códigos / prompts de ChatGPT para negocios". |
| `/clase-gratuita` | Clase semanal gratis | **Por confirmar** (E9) | Si sigue: indexar. Si no: 301 a `/adn-de-tu-negocio` o a `/diagnostico`. |
| `/asesoria` | Asesoría 1 a 1 | **Indexar** | "asesoría para pymes / consultor de negocios". |
| `/trabaja-conmigo` | Duplicado de /asesoria | **Mantener** (ya tiene canonical a /asesoria); fuera del sitemap | ¿Se usa en anuncios o bio? |
| `/30-preguntas` | Lead magnet (PDF) | **Indexar** | "preguntas para cerrar ventas". |
| `/de-0-a-1-millon` | Curso (¿gratis?) 30 sesiones | **Indexar** | Hay que aclarar si es gratis o bono (E13). |
| `/automatiza` | Servicio de automatización/WhatsApp | **Indexar** | "automatizar WhatsApp para negocio". ¿Sigue vigente? |
| `/adn-de-tu-negocio` | Clase ADN $1,000 | **Indexar** | Event cuando haya fecha real. |
| `/adn-de-tu-negocio-gracias` | Gracias | **noindex** | |
| `/panel/*` | Panel interno | **noindex** + Disallow (ya está) | |
| **Nuevas** `/eduardo-hernandez` (o `/conoce-a-eduardo`) y `/nadie` | Hoy son anclas de la home | **Crear** (Fase 4) | Son las dos páginas más importantes para la entidad. |

---

## 3. Metadatos actuales (render con JavaScript)

| Ruta | Title actual (car.) | Problema |
|---|---|---|
| `/` | Eduardo Hernández — Consultor de Negocios y Crecimiento Empresarial (67) | Largo; está bien que empiece con el nombre. |
| `/diagnostico` | Diagnóstico Empresarial Gratis — Evalúa tu Negocio en 3 Minutos (63) | Dice "3 minutos" y la description dice "15 preguntas"; la home dice "5 minutos". Hay que unificar. |
| `/asesoria` | Asesoría empresarial \| Eduardo Hernández (40) | Corto; falta "para pymes". |
| `/sube-tus-ventas` | Sube tus Ventas en 5 Pasos · Curso para MiPyME · NADIE (54) | Bien. Falta "curso de ventas" al inicio. |
| `/de-0-a-1-millon` | De 0 a 1 Millón — Curso gratuito de Eduardo Hernández (53) | ¿"Gratuito" es correcto? |
| `/automatiza` | Automatiza tu negocio — Sistema de ventas y WhatsApp \| Eduardo Hernández (72) | Largo. |
| `/recursos` | Recursos gratuitos \| Eduardo Hernández (38) | Corto. |
| Todas | + la description genérica de `index.html` duplicada | Hay que quitarla de `index.html`. |
| Todas | canonical y og:url → `eduardohernandez.lovable.app` | Urgente. |
| Todas | og:image → `eduardohernandez.lovable.app/og-image.jpg` | Tiene que ser una imagen de marca 1200×630 en eduardohdz.com. |

La tabla final de **URL → keyword → title → description → schema** va en la Fase 2, cuando se apruebe el mapa de la sección 5.

---

## 4. Lighthouse móvil — "ANTES" (21 nov 2026)

Lighthouse 12, modo móvil, Chromium de la sesión. Son datos de laboratorio, no de usuarios reales. Los JSON están guardados en la sesión.

| Página | Perf | SEO | Accesib. | Buenas prácticas | FCP | **LCP** | TBT | CLS | Peso |
|---|---|---|---|---|---|---|---|---|---|
| `/` | 44 | 100 | 83 | 79 | 4.3 s | **7.4 s** | 820 ms | 0 | **4.8 MB** |
| `/asesoria` | 49 | 92 | 90 | 79 | 4.2 s | **9.8 s** | 630 ms | 0 | 2.3 MB |
| `/diagnostico` | 51 | 100 | 94 | 79 | 4.3 s | **6.9 s** | 610 ms | 0 | 1.0 MB |
| `/sube-tus-ventas` | 48 | 100 | 90 | 79 | 4.1 s | **8.8 s** | 700 ms | 0 | 2.0 MB |
| `/de-0-a-1-millon` | 49 | 100 | 91 | 79 | 4.4 s | **6.2 s** | 630 ms | 0 | 2.1 MB |

El SEO sale en 100 porque Lighthouse ejecuta el JavaScript y no revisa a qué dominio apunta la canonical. No refleja los problemas E3 ni E11.

**Causas principales:**
- `index-*.js` de **2.2 MB**: todo el sitio y el panel van en un solo paquete, sin dividir por ruta.
- `eduardo-portrait.png` de **1.87 MB** (un PNG para una foto) y `nadie-community.jpg` de **1.85 MB**. En WebP con srcset deberían pesar menos de 150 KB.
- El elemento LCP de la home es un fondo decorativo (`results-team.jpg` al 20% de opacidad).
- Meta Pixel (2 IDs: `1837657807608257` y `1251487166845355`) carga en `<head>` antes que la página. Hay que diferirlo con cola, como en compraenfabricas.
- Videos de testimonio en `public/images/*.mp4`: hay que revisar que no se descarguen hasta darles play.

**Meta:** LCP < 2.5 s y Perf ≥ 85 en móvil.

---

## 5. Investigación de búsquedas y mapa (borrador para aprobar)

**Qué se encontró en buscadores** (búsqueda web desde EE. UU.; para México los resultados pueden variar):
- **eduardohdz.com no aparece** ni buscando el dominio. No hay resultados de "NADIE" como movimiento de empresarios. **La entidad hoy no existe para los buscadores.**
- "Eduardo Hernández" está ocupado por muchas personas (políticos, empresarios colombianos, desarrolladores). Como se esperaba, se gana con combinaciones.
- Las búsquedas genéricas ("cómo hacer crecer mi negocio", "asesoría para pymes") las dominan **BBVA, Mercado Pago, DHL** y universidades. Son difíciles a corto plazo. La puerta está en el long-tail con ángulo propio: MiPyME mexicana, WhatsApp, "dueño que hace todo", diagnóstico con resultado inmediato.
- "Diagnóstico de negocio gratis": la competencia son formularios sueltos (Tally, Jotform) y programas de gobierno. **Hay hueco** para una página con texto real + quiz + resultado.
- "Curso de ventas para emprendedores": edX, ed2go y productos de Hotmart. Se puede competir con "curso de ventas para MiPyME / dueños de negocio en México".

**Mapa 1 página = 1 intención (sin chocar con compraenfabricas):**

| Intención / keyword principal | Secundarias | Página | Estado |
|---|---|---|---|
| Eduardo Hernández consultor de negocios | Eduardo Hernández asesor de negocios, Eduardo Hernández NADIE, quién es Eduardo Hernández | `/` (home) + **nueva** `/eduardo-hernandez` | Crear la página de Eduardo |
| movimiento NADIE | NADIE empresarios, comunidad NADIE, "yo no soy nadie" | **nueva** `/nadie` | Crear (texto oficial) |
| comunidad de empresarios / emprendedores México | networking para emprendedores | `/comunidad` | Ajustar |
| diagnóstico de negocio gratis | diagnóstico empresarial gratis, test de mi negocio, evaluar mi negocio | `/diagnostico` | Agregar texto |
| asesoría para pymes en México | consultor de negocios para pymes, asesoría empresarial | `/asesoria` | Ajustar |
| curso de ventas para MiPyME / emprendedores | cómo vender más en mi negocio (curso), sistema de ventas | `/sube-tus-ventas` | Ajustar |
| curso para hacer crecer mi negocio | de 0 a 1 millón, curso de negocios gratis | `/de-0-a-1-millon` | Ajustar |
| clase ADN de tu negocio | identidad / estructura de negocio | `/adn-de-tu-negocio` | Ajustar + Event |
| preguntas para cerrar ventas | preguntas de venta, cierre de ventas | `/30-preguntas` | Ajustar |
| prompts / códigos de ChatGPT para negocios | ChatGPT para emprendedores | `/recursos/codigos-chatgpt` | Ajustar |
| automatizar WhatsApp para mi negocio | chatbot para negocio, responder mensajes | `/automatiza` | Confirmar vigencia |
| **Guías (Fase 4)**: cómo hacer crecer mi negocio · cómo subir mis ventas · cliente ideal · diagnóstico de negocio (qué es) | — | `/recursos/<slug>` o `/guias/<slug>` | Plan |
| **No se ataca aquí:** importar de China, proveedores, curso para importar, joyería de mayoreo | — | → compraenfabricas.com | Enlace cruzado |

Ojo con canibalizar dentro del sitio:
- `/diagnostico` y `/diagnostico-evergreen`: una sola indexable.
- `/sube-tus-ventas`, `/preventa-curso` y `/reto-*`: solo sube-tus-ventas indexa.
- La guía "diagnóstico de negocio" no debe pelear con `/diagnostico`: o se escribe con ángulo informativo ("qué es y cómo hacerlo") o se omite.

---

## 6. Fase 1: opciones y recomendación

| | A. Migrar a TanStack Start (**recomendado**) | B. Quedarse en Vite + prerender de Lovable |
|---|---|---|
| HTML para bots | Garantizado para cualquier bot (SSR) | Solo bots "verificados"; los demás (y los scanners SEO) ven vacío |
| 404 reales | Sí | No (siempre 200) |
| Separar el panel del JS público | Sí (por ruta) | Habría que dividir el código a mano |
| Igual que compraenfabricas | Sí: se reutiliza lo ya hecho (seo-pages, feeds, LazyVideo) | No |
| Costo (doc. Lovable) | **10–35 créditos** para la migración, más las tandas de prueba y ajuste | Menos créditos |
| Riesgo | Librerías que solo funcionan en el navegador (jsPDF del diagnóstico, recharts y framer-motion del panel) pueden romper el render en servidor; se ven como pantalla en blanco en la vista previa. La documentación dice que la base de datos, los webhooks (Stripe, Hotmart, ManyChat) y el login se conservan. | Bajo |
| Reversible | Sí: historial de versiones. El sitio publicado no cambia hasta publicar. | — |

**Cómo se haría (con tu OK):**
1. Pausar o coordinar la otra sesión que edita el panel.
2. `send_message` en **plan_mode** pidiendo a Lovable el plan de migración y la lista de riesgos (sin escribir código).
3. Revisar el plan contigo.
4. Migrar (Lovable pide confirmación con una tarjeta).
5. Probar en la vista previa: las 23 rutas, quiz y PDF, Hotmart, Stripe/ADN, formularios (30 preguntas, reto, comunidad), panel con login y Pixel con 2 IDs.
6. HTML crudo de cada ruta.
7. Pedirte OK para publicar.

**Si eliges B**, la Fase 2 sigue casi igual: canonical, sitemap estático, robots, noindex, schema, enlaces reales en el menú y velocidad. Solo no hay 404 real.

---

## 7. Preguntas para ti (necesito estas respuestas antes de la Fase 1)

1. **URLs en anuncios de Meta y ManyChat:** ¿cuáles se usan hoy? (sospecho `/diagnostico-evergreen`, `/reto-landing`, `/reto-diagnostico`, `/adn-de-tu-negocio`, `/sube-tus-ventas`, `/30-preguntas`, `/comunidad`). Ninguna cambiará sin tu permiso.
2. **/clase-gratuita** ("todos los sábados"): ¿sigue? Si no, ¿a dónde la mandamos?
3. **Redes de NADIE:** ¿siguen vigentes Instagram y TikTok @_nadieofficial, YouTube @nadieofficiall y Facebook nadieofficiall?
4. **Dominio:** ¿dónde está registrado eduardohdz.com (GoDaddy, Namecheap, Cloudflare, Lovable…)? Es para agregar `www`.
5. **Datos que chocan (E13):**
   - ¿Se queda "8 años y +300 empresas" en todo el sitio (y se corrige "más de una década / +200 negocios" de sube-tus-ventas)?
   - ¿"+200 negocios validaron el método" es un dato del curso que se queda?
6. **De 0 a 1 Millón:** ¿es gratis (title) o es un bono con valor de $12,000 (sube-tus-ventas)?
7. **Páginas que quizá ya no se usan:** `/reto`, `/preventa-curso`, `/automatiza`, `/prompt-maker`. ¿Siguen, se ocultan (noindex) o se redirigen?
8. **Opción de la Fase 1:** ¿A (migrar a TanStack Start, recomendado) o B?
9. **La otra sesión del panel:** ¿quién la lleva? Hay que pausarla durante la migración.
10. **Search Console:** ¿ya tienes eduardohdz.com dado de alta? Si sí, una Inspección de URL de `/asesoria` nos confirma qué recibe Google hoy.
11. **Fotos:** ¿me pasas `eduardo-hernandez-asesor-de-negocios.jpg` y las otras 4 de compraenfabricas, o autorizas pedirle a Lovable que las copie?

---

## 8. [PENDIENTE]

- [PENDIENTE: confirmación con Search Console de lo que recibe el Googlebot real]
- [PENDIENTE: lista de URLs en anuncios]
- [PENDIENTE: vigencia de /clase-gratuita, redes de NADIE y páginas de la pregunta 7]
- [PENDIENTE: registrador del dominio]
- [PENDIENTE: fotos nuevas de Eduardo]
- [PENDIENTE: fechas reales de la clase ADN para el schema Event]

---

## 9. Respuestas del usuario (21 nov) y avance de la Fase 1 (23 nov)

**Respuestas:**
- El sitio es solo para darle autoridad a Eduardo; por ahora no se vende nada.
- /clase-gratuita sigue vigente.
- Las redes de NADIE ya no están vigentes: las únicas redes son las de Compra en Fábricas.
- El dominio está en GoDaddy.
- De 0 a 1 Millón es gratis en vivo; las grabaciones están en Skool (15 USD al mes).
- Se migra a TanStack Start.
- Search Console: se agrega como propiedad de dominio en la misma cuenta.

**Decisión sobre noindex** (la dejó el usuario a mi criterio):
- Se ocultan a Google: /reto, /reto-*, /preventa-curso, /aliados*, /diagnostico-evergreen y la página de gracias.
- No se borra ni se redirige ninguna.

**Migración (Lovable, commit `c9f14f3`):**
- Plan aprobado. La migración arrancó a las 18:46 UTC y terminó a las 19:03 UTC.
- Pruebas que reporta Lovable:
  - TypeScript sin errores.
  - SSR: 32 de 32 rutas responden 200.
  - Sin errores al hidratar.
  - Las 7 edge functions siguen en Supabase, sin cambios.
  - 404 real.
  - Pixel con 2 IDs y un PageView por navegación (corrigió un doble conteo).
  - El parámetro `ref` sigue llegando a los links de Hotmart.
  - Panel probado con sesión.
  - Home y /clase-gratuita comparadas con el sitio publicado.
- Revisado en el código:
  - `src/lib/seo.ts` con `SITE_URL = https://eduardohdz.com`.
  - `head()` por ruta.
  - /trabaja-conmigo con canonical a /asesoria.
  - El panel con `ssr: false` y `noindex`.
- Salvedad: `/diagnostico` y `/diagnostico-evergreen` quedaron con `ssr: false`, porque el quiz guarda el avance en el navegador. El servidor manda su title y description, pero no texto. En la Fase 2 hay que agregar texto renderizado en servidor alrededor del quiz.
- [PENDIENTE: la vista previa pide sesión (401), así que el HTML crudo de las 25 rutas se verifica en vivo después de publicar o con capturas del usuario. La captura automática del proyecto mostró "Not found" en la home: hay que revisarlo en el editor antes de publicar.]

### Publicación de la migración (23 nov 2026)

Publicada con OK del usuario (deploy `5abcf320`, commit `c9f14f3`). Antes de publicar se revisó `list_edits`: solo estaba la migración.

**HTML crudo como Googlebot, en vivo:**
- Las 23 rutas públicas responden 200, con 1 title, 1 description y canonical absoluta a `https://eduardohdz.com/...`.
- `/trabaja-conmigo` tiene canonical a `/asesoria`.
- Todas tienen H1 y texto (117 a 1,069 palabras), salvo `/diagnostico` (12 palabras) y `/diagnostico-evergreen` (7), que se arman en el navegador.
- `/panel` y `/panel/login` tienen `noindex, nofollow`.
- `/no-existe-xyz` responde **404**.

**En navegador real:**
- Sin errores de JavaScript.
- El Pixel carga con los 2 IDs. El envío a facebook.com/tr no se ve porque Meta descarta los navegadores automatizados; hay que confirmarlo en "Probar eventos".
- El link de Hotmart conserva `?src=`.
- El login del panel carga.
- El badge "Edit with Lovable" sigue visible.

**Lighthouse móvil, antes → después:**

| Página | Perf | LCP | Peso |
|---|---|---|---|
| `/` | 44 → 58 | 7.4 s → **17.8 s** | 4.7 → 4.3 MB |
| `/asesoria` | 49 → 62 | 9.8 → 7.4 s | 2.3 → 1.9 MB |
| `/diagnostico` | 51 → 77 | 6.9 → 3.3 s | 1.0 → 0.6 MB |
| `/sube-tus-ventas` | 48 → 58 | 8.8 → 6.8 s | 2.0 → 1.2 MB |
| `/de-0-a-1-millon` | 49 → 81 | 6.2 → 2.9 s | 2.0 → 1.6 MB |

El LCP de la home empeoró porque ahora el elemento LCP es `eduardo-portrait.png` (1.8 MB); antes era un fondo decorativo. Se corrige en la Fase 2 con WebP y srcset (también `nadie-community.jpg`, de 1.8 MB).

---

## 10. Fase 2 publicada (23 nov 2026)

**Commits:**
- Tanda 1 (SEO técnico): `b3bf041`.
- Tanda 2 (velocidad): `9788743`, costó 11.1 créditos.
- Deploy `6cafee57`, con OK del usuario. Antes se revisó `list_edits`: solo estaban estas dos tandas.

**Verificación en vivo:**
- `/sitemap.xml` responde 200 `application/xml`, con 13 URLs y lastmod.
- `/robots.txt` responde 200 `text/plain`:
  - `*` y GPTBot, OAI-SearchBot, ChatGPT-User, Google-Extended, PerplexityBot, ClaudeBot, Claude-SearchBot, Bingbot y Googlebot con `Allow: /`;
  - `Disallow: /panel`;
  - línea `Sitemap:`.
- `/llms.txt` responde 200 `text/plain`, con el texto acordado.
- `/asesoria/` → 301 → `/asesoria`; la query string se conserva.
- 13 rutas indexables con su title y description nuevos, canonical propia, H1 y texto.
- `/diagnostico` ya trae en el HTML del servidor 152 palabras (antes 12), con su H1 y la sección "¿Qué mide el diagnóstico de negocio?".
- 9 rutas con `noindex, follow`.
- El panel conserva `noindex, nofollow`.
- La 404 está en español, con status 404 y `noindex`. Detalle menor: trae 2 `<title>` (el de la raíz y el de la página); se corrige en la siguiente tanda.
- El menú y el footer tienen `<a href>` reales (10 rutas internas enlazadas desde la home).
- 22 imágenes WebP en la home y precarga con `fetchPriority="high"` para la imagen del hero.
- Navegador real:
  - sin errores de JavaScript;
  - Hotmart conserva `src`;
  - el Pixel deja el stub en fila y carga fbevents con los 2 IDs;
  - el quiz recorre las 15 preguntas hasta "Analizando tu negocio".

**Lighthouse móvil (Fase 0 → migración → Fase 2):**

| Página | Perf | LCP | Peso |
|---|---|---|---|
| `/` | 44 → 58 → **82** | 7.4 → 17.8 → **3.3 s** | 4.7 → 4.3 → **0.7 MB** |
| `/asesoria` | 49 → 62 → **82** | 9.8 → 7.4 → **3.5 s** | 2.3 → 1.9 → **0.6 MB** |
| `/diagnostico` | 51 → 77 → **79** | 6.9 → 3.3 → **4.0 s** | 1.0 → 0.6 → 0.6 MB |
| `/sube-tus-ventas` | 48 → 58 → **81** | 8.8 → 6.8 → **3.1 s** | 2.0 → 1.2 → **0.7 MB** |
| `/de-0-a-1-millon` | 49 → 81 → **83** | 6.2 → 2.9 → **3.0 s** | 2.0 → 1.6 → 1.6 MB |

**Pendiente de velocidad** (todavía sin llegar a la meta de 2.5 s):
- En la home, el LCP es el fondo decorativo `results-team-960.webp` (TTFB 0.76 s y carga 1.4 s). Opciones: un fondo más chico o borroso, o un degradado en CSS.
- `/diagnostico` subió a 4.0 s porque ahora monta el quiz en el cliente.
- `/asesoria` tiene SEO 92 por un texto de enlace genérico.

**"Edit with Lovable":** no se quita desde el código. Se oculta en los ajustes de publicación del proyecto (requiere plan Pro o superior).

---

## 11. Fase 3 publicada: entidad y JSON-LD (23 nov 2026)

**Commits y deploy:**
- Fase 3: `c02a5ac`.
- Corrección del Skool: `28b0bc0`, 0.6 créditos.
- Deploy `69dcf5bf`, con OK del usuario. También subieron los 3 cambios del panel de la otra sesión del usuario (Tareas, videos IB y grupos), aprobados por el usuario.

**Qué quedó (todo en el HTML del servidor, en `src/lib/schema.ts`):**
- **Grafo global en todas las páginas:**
  - **Person** `https://eduardohdz.com/#person`:
    - jobTitle "Consultor de negocios" y description con los datos verificados;
    - image `/images/eduardo-foto-profesional.jpg`;
    - knowsAbout;
    - affiliation con JAICO, Xijiao Shops, Xijiao LOG y Compra en Fábricas (con founder → Person);
    - memberOf → NADIE;
    - sameAs: el autor en compraenfabricas, Skool `emprende-importando-4690` y las redes de Compra en Fábricas.
  - **Organization NADIE** `#nadie`, con el texto oficial, el slogan y founder → Person. Sin sameAs, porque sus redes ya no están vigentes.
  - **WebSite** `#website`: name "Eduardo Hernández", con alternateName.
- **Home:** ProfilePage con mainEntity → Person.
- **BreadcrumbList** en las 11 páginas indexables internas.
- **Course:**
  - `/sube-tus-ventas`: precio 7,900 MXN, igual al visible, calculado con `getPrecioActual()`;
  - `/de-0-a-1-millon`: gratis.
- **FAQPage** en `/sube-tus-ventas` (9 preguntas), generado desde el mismo arreglo que pinta la página (`src/content/sube-tus-ventas-faqs`).
- **Event** listo en `src/lib/class-dates.ts` (`CLASS_DATES`), hoy vacío: no sale ningún Event hasta que haya una fecha real de ADN o de la clase gratuita.
- **`/adn-de-tu-negocio`** con noindex y fuera del sitemap y de `llms.txt`, porque muestra texto "Placeholder" en "Qué vas a aprender". [PENDIENTE: los 5 puntos reales.]
- **La 404** tiene un solo `<title>`.

**Verificación en vivo:**
- 15 rutas revisadas: JSON válido, sin duplicados, 1 title por página.
- Sitemap con 12 URLs.
- `llms.txt` con el Skool correcto.
- El resto de las rutas sin cambios (status, H1 y texto).

**Para la sesión de compraenfabricas** (se le dio el texto al usuario): cambiar el `@id` del Person a `https://eduardohdz.com/#person`, dejar `url` en el autor de compraenfabricas y agregar `https://eduardohdz.com/` al sameAs.

---

## 12. Fase 4 publicada: contenido de entidad (24 nov 2026)

**Commit y deploy:**
- Commit `a3e7b66`, 5.3 créditos.
- Deploy `4b82f5e7`, con OK del usuario. También subió el rediseño del panel de la otra sesión del usuario (`db6e7ce`), aprobado por el usuario.

**Qué quedó:**
- **`/eduardo-hernandez`** ("Quién es Eduardo Hernández"):
  - respuesta directa arriba;
  - historia en corto, con enlace a la nota completa en compraenfabricas;
  - 6 números, 4 negocios, NADIE y "Cómo te puedo ayudar";
  - bloque "¿Quieres importar de China?" → compraenfabricas.com, y la cita;
  - 3 fotos reales de Eduardo en WebP;
  - schema ProfilePage + BreadcrumbList;
  - og:image `/img/eduardo-hernandez-og.jpg`: la foto profesional recortada a 1200×630, sin texto, revisada.
- **`/nadie`** ("Qué es NADIE"): logo, texto oficial, filosofía, cita y "Cómo ser parte". Sin fotos de banco ni redes. Schema AboutPage + BreadcrumbList.
- **Schema:**
  - la home pasa a WebPage (about → Person);
  - el Person tiene `mainEntityOfPage` → `/eduardo-hernandez`;
  - la url de NADIE es `/nadie`.
- **Navegación:**
  - el menú lleva a las dos páginas nuevas;
  - el footer tiene los enlaces "Eduardo Hernández" y "NADIE", y "¿Quieres importar de China? Visita Compra en Fábricas →".
- **Home:**
  - se quitaron las redes de NADIE (ya no están vigentes);
  - "Sé parte de nosotros" → `/comunidad` (antes `#`);
  - "Xijiao Logistics" → "Xijiao LOG";
  - enlaces "Conoce su historia →" y "Qué es NADIE →".
- **`/sube-tus-ventas`:** "más de una década" → "8 años en consultoría".
- **Sitemap** con 14 URLs, y `llms.txt` con las dos páginas nuevas.

**Verificación en vivo:**
- `/eduardo-hernandez`: 200, 464 palabras, title, description y canonical correctos, H1 "Quién es Eduardo Hernández", JSON-LD válido.
- `/nadie`: 200, 207 palabras, H1 "Qué es NADIE", JSON-LD válido.
- La home ya trae WebPage.
- En ninguna página quedan redes de NADIE ni "Xijiao Logistics".
- El enlace a compraenfabricas.com aparece en todas las páginas, desde el footer.

**Plan de guías:** `docs/seo/eduardohdz-plan-guias.md`.

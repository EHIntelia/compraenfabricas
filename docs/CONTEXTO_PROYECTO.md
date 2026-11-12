# Compra en Fábricas de China — Contexto del proyecto

**Para quién es:** cualquier persona o IA que entre nueva al proyecto.
**Actualizado:** 12 de noviembre de 2026.
**Documento interno.** Incluye estrategia que no se dice en público (sección 2). No se copia al sitio ni al project knowledge de Lovable.

> **Regla de oro:** si este documento y el sitio compraenfabricas.com no coinciden, **manda el sitio**. Precios, productos y condiciones se confirman ahí.

Documentos relacionados en este repo (`EHIntelia/compraenfabricas`):
- `HANDOFF_Compra_en_Fabricas_COMPLETO.md`: documento maestro de marca, productos y funnel.
- `blog/ENTREGA.md`: cómo se construyó y se publica el blog.
- `docs/seo/fase-0-auditoria.md`: auditoría SEO completa, mapa de keywords y prioridades.
- `docs/seo/fase-1-prompt-lovable.md`: lo que se le pidió a Lovable en la ronda de SEO técnico.
- `docs/seo/prompt-10-notas.md`: instrucciones para las siguientes 10 notas del blog.

---

## 1. Qué es

**Compra en Fábricas de China** (compraenfabricas.com) es la marca de educación de **Eduardo Hernández**: enseña a emprendedores de México y Latinoamérica a comprar directo de fábricas en China, sin intermediarios.

- **Eduardo:** 49 años, 26+ años importando de China, 5 negocios funcionando, 300+ empresas asesoradas en los últimos 8 años, 50+ empresas acompañadas a comprar en China, 2 bancarrotas de las que se levantó. Fundador de **JAICO (Jaico Jewels)**, **Xijiao Shops** y **Xijiao LOG**, y del movimiento **NADIE**.
- **Equipo propio en China:** "chinos que negocian con chinos".
- **Promesa:** te enseñamos todo el proceso; si quieres que lo hagamos por ti, también se puede. "Si puedes hacerlo solo, hazlo solo. Nosotros estamos para acelerarte, no para amarrarte."
- **Marca distinta** a la marca personal de Eduardo (negro + rojo #A30E1A). Esta usa naranja #F97316, rojo #DC2626 y el degradado naranja → rojo, con el carácter 中 como ícono.

## 2. El objetivo real del negocio (interno, no se dice en público)

El fin último es que la gente **compre joyería al mayoreo y la revenda** (JAICO / Xijiao Shops): mejor margen, mucha rotación y envío barato. El contenido enseña importación en general (electrónica, etc.) y **siembra la joyería de forma natural**: como ejemplo, como "lo que mejor se vende", con números. Nunca como pitch directo.

## 3. Qué se vende (según el sitio, nov 2026)

| Producto | Precio | Página | Nota |
|---|---|---|---|
| **Clase en vivo con Eduardo** | $990 MXN | /clase | CTA principal. **21 de noviembre de 2026, 11:00 am hora CDMX, dura 1 h 30 min.** Incluye grabación, material, plantillas y 5 proveedores de regalo. Pago por Stripe. |
| Escuela de Negocios (Skool) | $250 MXN/mes o $2,500/año | /escuela | Cursos grabados, Zooms en vivo y comunidad. |
| Joyería al mayoreo (JAICO) | Variable | /joyeria → info.joyeria.shop | Producto estrella real. |
| Cajas de electrónica | Desde ~$3,000 MXN | /productos y /producto/<código> | Ya en México. Se apartan con 20%, llegan en 1–2 días hábiles. |
| Proveedores de tecnología | — | /marketplace | AEMAI y Port Tide, con videos. |
| Validación de proveedor | Desde $2,500 MXN | /validacion | Activa, con Stripe. No se elimina. |
| Paquetes de contacto de proveedor | $1,500 / $8,900 / $8,999 + comisiones | /empieza-aqui | P1 por Hotmart. |
| Asesoría 1 a 1 | 4 niveles, $2,500 a $100,000 | /asesoria-china | Por WhatsApp. |
| Logística ("que lo traigan por mí") | Cotización | /logistica | Para quien **ya tiene** proveedor. No se buscan proveedores por encargo. |
| Clase ADN de tu Negocio | $1,000 MXN | /adn | Del ecosistema. Se queda. |

- **Ya NO existe** clase ni curso gratis. No se menciona en ningún lado.
- **/cotizador** (envíos internacionales) está **en construcción**: oculto a Google y fuera del menú.
- **/proveedores** es la página del regalo de la clase: oculta a Google (`noindex`) y no se enlaza nunca.
- **WhatsApp único:** wa.me/5218120181761.

## 4. Cómo hablamos (aplica a todo: sitio, blog, anuncios, mensajes)

- Español mexicano informal, "lenguaje de banqueta". Nada corporativo ni de coach.
- Palabras simples. Si un término técnico es obligatorio (Incoterms, pedimento, NOM), se explica en una línea.
- Estructura: **dolor → autoridad de Eduardo → solución**.
- Autoridad sin soberbia: años, negocios y asesorados sí. Facturación o "el mejor del mundo", nunca.
- Enemigo común: el sistema de intermediarios, nunca personas ni empresas.
- **Prohibido inventar** testimonios, reseñas, clientes, cifras o precios de fábrica. Si falta un dato: `[PENDIENTE: …]`.
- **No se publica:** WeChat, contactos de proveedores de regalo o de logística, nombres del equipo, acuerdos con clientes.
- Siempre "**26+ años**".
- Excepción SEO: en títulos y encabezados se usan las palabras que la gente busca ("proveedores en China", "importar"), aunque en el texto se prefiera la versión simple.

## 5. Funnel

Anuncio de Meta → WhatsApp (ManyChat) o landing → clase de $990 o Escuela → seguimiento por WhatsApp → joyería, cajas, logística o asesoría.

**Nuevo canal (nov 2026):** blog y SEO orgánico (Google y respuestas de IA como ChatGPT, Gemini y Perplexity) → clase / WhatsApp / joyería.

## 6. El sitio por dentro

- **Lovable**, proyecto **"China Direct Connect"** (id `72afffe6-8b0f-4aea-a6a4-8c41fab24fd9`), workspace "Eduardo's Lovable". El código vive en Lovable y **no está conectado a GitHub**. Este repo guarda el blog en markdown y la documentación.
- **Stack:** TanStack Start con render en servidor (SSR), React 19, Tailwind, Lovable Cloud (Supabase). Google y las IAs reciben el HTML completo.
- **Base de datos:** tabla `posts` (blog) y tabla `resenas` (reseñas reales, vacía; solo se ven las aprobadas).
- **Archivos clave:**

| Qué | Dónde |
|---|---|
| Menú, footer, links de Skool, joyería y WhatsApp | `src/lib/site.tsx` |
| **Fecha de la clase** (una línea por fecha) | `src/lib/clase-fechas.ts` → `CLASS_DATES` |
| Titles, descriptions y schema de páginas comerciales | `src/lib/seo-pages.ts` |
| Helpers de SEO, schema Organization/WebSite/Person | `src/lib/blog/seo.ts` |
| Sitemap, robots.txt, llms.txt y fechas de actualización | `src/lib/blog/feeds.ts` (`STATIC_PATHS`, `PAGE_LASTMOD`) |
| Videos (clip ligero arriba, video completo al dar play) | `src/components/LazyVideo.tsx` |
| Redirección de barra final (301) | `src/server.ts` |
| Aviso a buscadores (IndexNow) | `src/lib/indexnow.ts` y `POST /api/public/indexnow` |
| Panel de reseñas (con contraseña) | `/admin/resenas` |

- **Formularios:** FormSubmit (logística). **Pagos:** Stripe (clase y validación) y Hotmart (Paquete 1).
- **Medición:** Meta Pixel en todo el sitio (carga después de la página, sin perder eventos). Google Search Console y Bing Webmaster Tools verificados.

### Reglas para trabajar en Lovable
- Los cambios se piden por mensaje al agente de Lovable y **gastan créditos**. Cambios grandes: primero en modo plan.
- **No cambiar URLs** que se usan en anuncios o en ManyChat (/clase, /productos, /joyeria, /logistica, /marketplace, /escuela). Si hiciera falta, redirección 301.
- **No tocar** formularios, links de Stripe y Hotmart, WhatsApp de compra, Skool ni info.joyeria.shop sin permiso.
- **No quitar ni ocultar servicios** sin aprobación de Eduardo.
- **No publicar (deploy) sin OK.** Ojo: cada publicación sube **todo** lo que haya en el proyecto, incluido el trabajo de otras sesiones. Antes de publicar, revisar el historial de cambios (`list_edits`).
- **Hay más de una sesión trabajando en paralelo** (SEO técnico, blog, páginas de producto). Coordinar quién toca qué.

## 7. Lo que se hizo en SEO (11–12 nov 2026)

### Fase 0 — Auditoría
Hallazgos principales (detalle en `docs/seo/fase-0-auditoria.md`):
- El SSR ya funcionaba, y las páginas inexistentes ya respondían 404.
- Problemas: metadatos con "Lovable", canonical relativa o faltante, una imagen genérica de Lovable para compartir, sitemap con páginas que redirigían, redirecciones temporales, 404 en inglés, sin schema Event, páginas muy pesadas por videos, "clase gratis" todavía ofrecida y la página del regalo de la clase abierta a Google.
- **Competencia:** Chilat domina casi todas las búsquedas. **"Eduardo Hernández" no aparecía en ninguna búsqueda de importación:** hay que construir la marca como entidad.

### Fase 1 — SEO técnico (todo publicado)
- **Tanda 1:** `noindex` en /proveedores y /cotizador, fuera "clase gratis", "26+ años" en todo el sitio, hora de la clase en /clase y banner de correo nuevo (`/email/banner-clase-21nov.jpg`).
- **Tanda 2:**
  - Metadatos nuevos con autor Eduardo Hernández, canonical absoluta e imagen de marca 1200×630 (`/og/compra-en-fabricas.jpg`).
  - Titles y descriptions a medida.
  - Sitemap limpio con fechas, redirecciones 301 y 404 en español.
  - Schema: Event de la clase, FAQ, migas, lista de productos y Organization completa.
  - La fecha de la clase sale de un solo lugar y desaparece sola cuando pasa.
- **Tanda 3:**
  - Videos e imágenes que solo cargan cuando se ven, y fotos en WebP.
  - Lo de arriba visible desde el primer momento.
  - Pixel diferido sin perder eventos.
  - Footer y enlaces internos completos, `llms.txt` ampliado e IndexNow por endpoint.
- **Clips:** los videos de arriba de 6 páginas ahora arrancan con un clip de ~1.5 MB sin sonido. El video completo (65–203 MB) solo se baja al dar "Ver video completo".
- **En proceso:** convertir esos 6 videos completos a H.264 para que se reproduzcan en todos los celulares y pesen menos.

### Velocidad en celular (Lighthouse, sitio en vivo)

| Página | LCP antes → después | Peso antes → después |
|---|---|---|
| Inicio | 3.2 s → **2.3 s** | 1.8 MB → 0.4 MB |
| /productos | 4.8 s → **2.6 s** | 4.3 MB → 0.5 MB |
| /clase | 4.4 s → 3.1 s | 24 MB → 22 MB* |
| /joyeria | 5.4 s → 3.8 s | 33 MB → 25 MB* |

\*Medido antes de los clips. Con los clips, clase y joyería deben bajar mucho; falta volver a medir.

Meta: LCP menor a 2.5 s. La nota de SEO de Lighthouse está en 100 en las páginas principales.

## 8. Blog

- **Notas publicadas (5):**
  - Pilar: `como-importar-de-china-a-mexico`.
  - `eduardo-hernandez-importaciones-china`.
  - `cursos-para-importar-de-china`.
  - `productos-para-importar-de-china`.
  - `importar-joyeria-de-china-para-vender`.
- **Flujo:** markdown en `blog/posts/<slug>.md` → `tools/check.py` → imágenes → SQL → borrador → publicada. Después: IndexNow y solicitar indexación en Search Console.
- **Siguientes 10 notas:** en `docs/seo/prompt-10-notas.md`, ya entregado a quien escribe el blog. Ajustes clave para que las notas no se peleen en Google:
  - Una sola nota para "comprar directo de fábrica / fábrica vs. revendedor".
  - Una guía completa de requisitos (padrón, RFC, agente aduanal).
  - Joyería de acero con ángulo informativo, para no competir con /joyeria.
  - Una nota nueva sobre la Feria de Cantón.
- **Reglas de las notas:**
  - Las notas no ponen la fecha de la clase, para que no caduquen.
  - No enlazan /cotizador ni /proveedores.
  - Nunca nombran a los 3 proveedores de Yiwu.

## 9. Decisiones tomadas

1. **El sitio manda** sobre el handoff cuando no coinciden.
2. **5 proveedores de regalo** en la clase; la clase **incluye grabación**.
3. Validación, ADN y Paquetes **siguen vivos**.
4. No hay clase ni curso gratis.
5. Se permiten todos los bots de IA en robots.txt.
6. **Ruta nueva propuesta:** `/curso-para-importar-de-china`, para rankear la búsqueda "curso para importar de China". `/clase` se queda como landing de anuncios con la fecha de cada edición.
   - No se usa /clase para SEO por dos razones: alargarla puede bajar la conversión de la pauta, y su fecha caduca.
   - Aprobada por Eduardo. Se construye en la Fase 2.
7. **No crear `/como-comprar-en-china`:** la guía pilar del blog ya cubre esa búsqueda.
8. **Google Business Profile:** no se usa oficina virtual (Google suspende esos perfiles). Opción en evaluación: perfil de **JAICO** (no de Compra en Fábricas) en el showroom de San Pedro Garza García, que atiende con cita.

## 10. Pendientes

**Para el equipo**
- [ ] Revisar el banner nuevo de correo (`/email/banner-clase-21nov.jpg`) y usarlo en los siguientes envíos.
- [ ] Crear el secreto `INDEXNOW_ADMIN_TOKEN` en Lovable (Ajustes → Secretos). Sirve para avisar a Bing de cada nota nueva; ChatGPT busca con el índice de Bing.
- [ ] Confirmar la dirección exacta del showroom, si tiene letrero de JAICO y si alguien recibe ahí. Con eso se prepara el perfil de Google.
- [ ] Mandar las historias reales de Eduardo para su nota: cómo empezó, las 2 bancarrotas, una anécdota en fábrica y qué es NADIE.
- [ ] Decidir quién coordina las sesiones que trabajan en paralelo en Lovable.
- [ ] Actualizar el árbol de ManyChat: 5 proveedores e incluye grabación.

**SEO (siguientes fases)**
- [ ] Terminar y publicar la conversión a H.264; volver a medir velocidad de /clase y /joyeria.
- [ ] Revisar /clase y /productos en la prueba de resultados enriquecidos de Google.
- [ ] **Fase 2:** página `/curso-para-importar-de-china`, hub `/preguntas-frecuentes`, convertir la nota pilar en guía principal, enriquecer la página de Eduardo (fotos reales, perfiles personales, NADIE).
- [ ] **Fase 3:** perfil de Google de JAICO, si califica.
- [ ] **Fase 4:** eventos de analítica (clic a WhatsApp, a la clase, a joyería y a Skool), WhatsApp con mensaje de origen en las páginas comerciales y tabla de posiciones por keyword.
- [ ] **Fase 5 (fuera del sitio, lo hace Eduardo):**
  - YouTube con títulos y descripciones optimizados; es la fuente que más citan las IAs.
  - Perfiles consistentes en todas las redes.
  - Entrevistas en medios y podcasts, y menciones de la marca en otros sitios.

## 11. Links

- Sitio: https://compraenfabricas.com · Blog: /blog · Autor: /autor/eduardo-hernandez
- Sitemap: /sitemap.xml · Robots: /robots.txt · Resumen para IAs: /llms.txt
- Joyería: https://info.joyeria.shop · Escuela: https://www.skool.com/compraenfabricas
- Redes: Instagram y TikTok @compraenfabricasdechina · Facebook (id 61591427343713)
- WhatsApp: wa.me/5218120181761
- Lovable: https://lovable.dev/projects/72afffe6-8b0f-4aea-a6a4-8c41fab24fd9

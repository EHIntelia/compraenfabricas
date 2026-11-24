# eduardohdz.com — Entrega del SEO integral

**Periodo:** 21 al 24 de noviembre de 2026
**Proyecto Lovable:** "Eduardo Hernández" (id `31eb7ad3-327e-43ed-9449-1c7cda622ec0`)
**Detalle por fase:**
- Fase 0 con bitácora de las Fases 1 a 4: `docs/seo/eduardohdz-fase-0.md`.
- Fase 5 y plan fuera del sitio: `docs/seo/eduardohdz-fase-5.md`.
- Plan de guías: `docs/seo/eduardohdz-plan-guias.md`.

---

## 1. Resumen

eduardohdz.com pasó de ser una página que Google y las IAs veían casi vacía a ser la "casa" de la entidad **Eduardo Hernández, consultor de negocios y fundador de NADIE**:

- **HTML completo para cualquier bot.** Se migró a TanStack Start con render en servidor (SSR).
- **Cada página tiene:**
  - su title, description y canonical a `https://eduardohdz.com`;
  - H1 y texto;
  - su schema.
- **Una sola ficha de Eduardo** (`https://eduardohdz.com/#person`) en todas las páginas, con su página de perfil (`/eduardo-hernandez`) y la de NADIE (`/nadie`).
- **Sitemap, robots, llms.txt, 404 real, 301 en la barra final y noindex** donde corresponde.
- **Velocidad:** la home bajó de 4.7 MB a 0.7 MB y de 44 a 82 en rendimiento móvil.
- **Medición:**
  - Search Console y Bing verificados;
  - GA4 `G-BMKRPT12Z6` con 7 eventos;
  - IndexNow activo.

No se cambiaron URLs, pagos (Hotmart y Stripe), formularios, el quiz ni el panel interno, más allá de lo necesario para SSR y medición. Cada publicación se hizo con el OK del usuario y revisando antes `list_edits`.

---

## 2. Cambios por fase (antes → después)

| Fase | Antes | Después | Publicado |
|---|---|---|---|
| **0. Auditoría** | HTML con 11 palabras; canonical a lovable.app; sin sitemap; soft 404; menú con botones; 0 schema; LCP 6–10 s | Informe y mapa de keywords | 21 nov |
| **1. Migración SSR** | Vite (SPA) | TanStack Start con SSR; panel solo en el cliente (`ssr:false`); edge functions intactas; 404 real | 23 nov |
| **2. SEO técnico** | Títulos genéricos, description duplicada, sin sitemap, menú no rastreable, fotos de 1.8 MB | Metadatos por página, noindex en 9 páginas, sitemap/robots/llms, 301, enlaces reales, footer, texto en /diagnostico, 404 en español, WebP + srcset, Pixel diferido | 23 nov |
| **3. Entidad** | 0 JSON-LD (salvo un Course incompleto) | Person `#person`, Organization NADIE, WebSite, BreadcrumbList, Course ×2, FAQPage, Event preparado (`CLASS_DATES`); /adn-de-tu-negocio con noindex porque tiene texto de relleno | 23 nov |
| **4. Contenido** | "Conoce a Eduardo" y "NADIE" eran anclas de la home; redes de NADIE caducadas; "Sé parte" sin destino | `/eduardo-hernandez` (ProfilePage) y `/nadie` (AboutPage); enlaces cruzados con compraenfabricas; datos unificados ("Xijiao LOG", "8 años"); plan de 4 guías | 24 nov |
| **5. Medición** | Sin Search Console, Bing ni GA4 | GSC (propiedad de dominio por DNS) + sitemap; Bing importado; GA4 con 7 eventos; IndexNow (14 URLs avisadas) | 24 nov |

---

## 3. Tabla de páginas

| URL | Keyword principal | Title | Schema | Índice |
|---|---|---|---|---|
| `/` | Eduardo Hernández consultor de negocios | Eduardo Hernández, consultor de negocios y fundador de NADIE | WebPage (+ grafo global) | Sí |
| `/eduardo-hernandez` | quién es Eduardo Hernández / Eduardo Hernández NADIE | Quién es Eduardo Hernández: historia, negocios y NADIE | ProfilePage, BreadcrumbList | Sí |
| `/nadie` | movimiento NADIE | Qué es el movimiento NADIE, fundado por Eduardo Hernández | AboutPage, BreadcrumbList | Sí |
| `/diagnostico` | diagnóstico de negocio gratis | Diagnóstico de negocio gratis: 15 preguntas para tu empresa | BreadcrumbList | Sí |
| `/asesoria` | asesoría para pymes en México | Asesoría para pymes en México con Eduardo Hernández | BreadcrumbList | Sí |
| `/sube-tus-ventas` | curso de ventas para MiPyME | Curso de ventas para MiPyME: Sube tus Ventas en 5 Pasos | Course, FAQPage, BreadcrumbList | Sí |
| `/de-0-a-1-millon` | curso gratis para hacer crecer tu negocio | De 0 a 1 Millón: curso gratis para hacer crecer tu negocio | Course, BreadcrumbList | Sí |
| `/comunidad` | comunidad de empresarios | Comunidad de empresarios NADIE \| Eduardo Hernández | BreadcrumbList | Sí |
| `/clase-gratuita` | clase gratuita para emprendedores | Clase gratuita para emprendedores con Eduardo Hernández | BreadcrumbList (+ Event cuando haya fecha) | Sí |
| `/30-preguntas` | preguntas para cerrar ventas | 30 preguntas para cerrar ventas: PDF gratis \| NADIE | BreadcrumbList | Sí |
| `/recursos` | recursos para hacer crecer tu negocio | Recursos gratis para hacer crecer tu negocio \| E. Hernández | BreadcrumbList | Sí |
| `/recursos/codigos-chatgpt` | códigos de ChatGPT para negocios | Códigos de ChatGPT para negocios: 10 comandos gratis | BreadcrumbList | Sí |
| `/prompt-maker` | mejorador de prompts | Mejorador de prompts gratis para ChatGPT \| Eduardo Hernández | BreadcrumbList | Sí |
| `/automatiza` | automatizar WhatsApp para negocio | Automatiza tu negocio: WhatsApp que vende las 24 horas | BreadcrumbList | Sí |
| `/adn-de-tu-negocio` | clase ADN de tu negocio | ADN de tu Negocio: clase en vivo con Eduardo Hernández | (Event cuando haya fecha) | **noindex** hasta quitar el relleno |
| `/trabaja-conmigo` | — | (igual que /asesoria) | — | canonical → /asesoria |
| `/diagnostico-evergreen`, `/reto`, `/reto-diagnostico`, `/reto-landing`, `/aliados`, `/aliados-reto`, `/aliados-curso`, `/preventa-curso`, `/adn-de-tu-negocio-gracias` | — | (sin cambios) | — | noindex, follow |
| `/panel/*` | — | Panel interno | — | noindex, nofollow + Disallow |

Las descriptions están en el código (`src/routes/*.tsx`) y en la sección 3 de `eduardohdz-fase-0.md`. Todas miden entre 140 y 155 caracteres.

**Sin chocar con compraenfabricas:** eduardohdz.com no ataca búsquedas de importación. Enlaza a compraenfabricas.com desde el footer y desde `/eduardo-hernandez`.

---

## 4. Lighthouse móvil (antes → después)

| Página | Perf | LCP | Peso |
|---|---|---|---|
| `/` | 44 → **82** | 7.4 → **3.3 s** | 4.7 → **0.7 MB** |
| `/asesoria` | 49 → **82** | 9.8 → **3.5 s** | 2.3 → **0.6 MB** |
| `/diagnostico` | 51 → **79** | 6.9 → **4.0 s** | 1.0 → **0.6 MB** |
| `/sube-tus-ventas` | 48 → **81** | 8.8 → **3.1 s** | 2.0 → **0.7 MB** |
| `/de-0-a-1-millon` | 49 → **83** | 6.2 → **3.0 s** | 2.0 → 1.6 MB |

**Pendiente:** todavía no se llega a LCP < 2.5 s.
- **Home:** el LCP es el fondo decorativo del hero; se puede aligerar o cambiar por un degradado.
- **`/diagnostico`:** el quiz se monta en el cliente.

---

## 5. Medición

- **Search Console:** propiedad de dominio `eduardohdz.com` (TXT en GoDaddy; **no borrar**) y sitemap enviado.
- **Bing Webmaster Tools:** importado desde GSC.
- **GA4 `G-BMKRPT12Z6`:**
  - "Cambios de página según el historial" está desactivado; el sitio manda sus propios `page_view`.
  - Probado en vivo: un `page_view` por página, `clic_curso`, `clic_whatsapp`, `begin_checkout` (valor 7,900 en Sube tus Ventas) y `diagnostico_iniciado`.
  - Eventos totales: `page_view`, `diagnostico_iniciado`, `diagnostico_terminado`, `clic_whatsapp`, `clic_curso`, `begin_checkout` y `generate_lead`. Ninguno lleva datos personales.
- **Meta Pixel:** intacto, con sus 2 IDs; ahora carga diferido.
- **IndexNow:** llave `39ad97afec30c14ce2be6916ba563acf`; las 14 URLs se enviaron el 24 nov (respuesta 202).

---

## 6. [PENDIENTE] y preguntas abiertas

- [PENDIENTE: los 5 puntos reales de "Qué vas a aprender" de la clase ADN. Con eso se quita el noindex de `/adn-de-tu-negocio`.]
- [PENDIENTE: fechas reales de la clase ADN y de la clase gratuita, que se cargan en `src/lib/class-dates.ts` → Event.]
- [PENDIENTE: las 5 fotos nuevas de Eduardo (`eduardo-hernandez-*.jpg`) para `/eduardo-hernandez`.]
- [PENDIENTE: historias reales de Eduardo (cómo empezó, las 2 bancarrotas, qué es NADIE para él).]
- [PENDIENTE: ejemplos reales y permiso de usar las hojas de trabajo, para las 4 guías.]
- [PENDIENTE: confirmar "8 años en consultoría / +300 empresas" como dato único. Ya está así en todo el sitio.]
- [PENDIENTE: velocidad, para llegar a LCP < 2.5 s (ver sección 4).]
- [PENDIENTE: el link de la tarjeta Skool del panel interno sigue apuntando a skool.com/compraenfabricas, porque es otra comunidad. Confirmar si está bien.]

---

## 7. Lo que le toca al usuario

| # | Qué | Estado |
|---|---|---|
| 1 | Search Console: propiedad de dominio + sitemap | ✅ Hecho |
| 2 | Bing Webmaster Tools: importar desde GSC | ✅ Hecho |
| 3 | GA4: propiedad nueva + ID + desactivar historial | ✅ Hecho |
| 4 | Search Console: "Solicitar indexación" de /, /eduardo-hernandez, /nadie, /diagnostico y /asesoria | Pendiente |
| 5 | `www.eduardohdz.com`: conectarlo en Lovable (Project settings → Domains, con redirect a la raíz) y crear en GoDaddy el registro que indique Lovable. Lovable redirige con 302, no 301 | Pendiente |
| 6 | compraenfabricas (otra sesión): cambiar el `@id` del Person a `https://eduardohdz.com/#person` y agregar `https://eduardohdz.com/` a su sameAs | Pendiente |
| 7 | Ocultar "Edit with Lovable" en los ajustes de publicación (requiere plan Pro o superior) | Pendiente |
| 8 | Confirmar el Pixel en Meta → Probar eventos, y GA4 en Informes → Tiempo real | Pendiente |
| 9 | En GA4, marcar como eventos clave: `diagnostico_terminado`, `clic_whatsapp`, `begin_checkout` y `generate_lead` (aparecen en Administrar → Eventos cuando ya hay datos, 24–48 h) | Pendiente |
| 10 | Fuera del sitio: bio y foto iguales en todos lados, video 1 "Quién soy y qué es NADIE", correos a medios (`eduardohdz-fase-5.md`) | Pendiente |

---

## 8. Mantenimiento

- **Cuando cambie el contenido real de una página:** actualizar su línea en `PAGE_LASTMOD` (`src/lib/feeds.ts`) y avisar por IndexNow.
- **Cuando haya fecha de clase:** agregarla a `CLASS_DATES` (`src/lib/class-dates.ts`). El Event sale solo y desaparece cuando pasa.
- **Página nueva indexable:** agregarla a `STATIC_PATHS`, a `PAGE_LASTMOD` y a `/llms.txt`, con `seoHead()` y su BreadcrumbList.
- **Perfil social nuevo de Eduardo:** agregarlo a `SAME_AS` (`src/lib/schema.ts`).
- **Antes de cada publicación:** revisar `list_edits`, porque hay otra sesión que trabaja en el panel.

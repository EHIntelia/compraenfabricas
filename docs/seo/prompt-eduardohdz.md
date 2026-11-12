# PROMPT — SEO integral de eduardohdz.com (sitio oficial de Eduardo Hernández)

Pegar completo en una sesión nueva de Claude Code con acceso al conector de Lovable y a este repo (`EHIntelia/compraenfabricas`).

```
ROL
Eres un consultor SEO senior (técnico, de contenido, de entidad y GEO/AEO para buscadores con IA) y desarrollador front-end. Tu trabajo es dejar eduardohdz.com lista para que Google, ChatGPT, Gemini, Perplexity y los AI Overviews entiendan quién es Eduardo Hernández y lo citen, sin pagar anuncios.

CONTEXTO OBLIGATORIO (léelo antes de proponer nada)
1. En el repo EHIntelia/compraenfabricas:
   - docs/CONTEXTO_PROYECTO.md: quién es Eduardo, sus negocios, tono y reglas.
   - docs/seo/eduardohdz-propuesta.md: diagnóstico del 12 nov 2026 y la estrategia acordada.
   - docs/seo/fase-0-auditoria.md: cómo se auditó compraenfabricas.com; usa el mismo método.
2. Lovable:
   - Proyecto "Eduardo Hernández" (id 31eb7ad3-327e-43ed-9449-1c7cda622ec0), workspace "Eduardo's Lovable". Es el que publica eduardohdz.com.
   - El proyecto hermano "China Direct Connect" (id 72afffe6-8b0f-4aea-a6a4-8c41fab24fd9) publica compraenfabricas.com. NO lo toques desde esta sesión; solo léelo como referencia de cómo quedó el SEO técnico (src/lib/seo-pages.ts, src/lib/blog/seo.ts, src/lib/blog/feeds.ts, src/components/LazyVideo.tsx).
3. Lee el código del proyecto, sus rutas, componentes y project knowledge antes de proponer cambios.

QUÉ ES EDUARDOHDZ.COM (estrategia acordada)
- Es la "casa" de la PERSONA: Eduardo Hernández, consultor de negocios y fundador del movimiento NADIE. Aquí viven el diagnóstico de negocio, los cursos "De 0 a 1 millón" y "Sube tus ventas", la asesoría, la clase ADN de tu Negocio, la comunidad y los recursos.
- compraenfabricas.com es la marca de IMPORTACIÓN DE CHINA. Los dos sitios no compiten: eduardohdz.com no ataca búsquedas de importación (enlaza a compraenfabricas para eso), y compraenfabricas no ataca consultoría general.
- Meta: que exista UNA entidad "Eduardo Hernández" con dos frentes, conectados por schema (sameAs/@id) y enlaces cruzados.
- "Eduardo Hernández" es un nombre muy común. Se gana con combinaciones ("Eduardo Hernández NADIE", "Eduardo Hernández consultor de negocios", "Eduardo Hernández importaciones China") y con señales consistentes: misma foto, misma bio y mismos datos.

DATOS VERIFICADOS DE EDUARDO (no inventes otros)
- 49 años. 26+ años importando de China. 8 años en consultoría. 300+ empresas y emprendedores asesorados. 50+ empresas acompañadas a comprar en China. 5 negocios funcionando. 2 bancarrotas de las que se levantó.
- Fundador de JAICO (Jaico Jewels), Xijiao Shops, Xijiao LOG y del movimiento NADIE.
- Redes: Eduardo NO tiene redes personales. Las de Compra en Fábricas son Instagram y TikTok @compraenfabricasdechina, y Facebook id 61591427343713. Las de NADIE son Instagram y TikTok @_nadieofficial, YouTube @nadieofficiall y Facebook nadieofficiall; confirma con el usuario que siguen vigentes.
- NADIE (texto oficial): "NADIE es un movimiento de empresarios que buscan construir negocios más sólidos, rentables y con visión a largo plazo. Empresarios que comparten experiencias reales, aprendizajes y estrategias que ya han aplicado en sus propios negocios. Aquí el conocimiento se construye entre todos. La cara del movimiento no está en quien da la asesoría. La verdadera fuerza está en la comunidad de empresarios que lo hacen posible." Frase: "Yo no soy nadie, solo quiero ayudarte a hacer crecer tu negocio y que ganes más dinero." — Eduardo Hernández.
- Fotos reales de Eduardo: en el proyecto China Direct Connect hay 5 nuevas (eduardo-hernandez-*.jpg, incluida eduardo-hernandez-asesor-de-negocios.jpg, guardada para este sitio). Pide al usuario los archivos si no puedes copiarlos entre proyectos.

DIAGNÓSTICO YA HECHO (12 nov 2026) — vuelve a verificar, puede haber cambiado
- E1: el sitio es Vite (SPA vieja de Lovable). Con user-agent de Googlebot, el HTML trae 11 palabras (título + "Edit with Lovable"): sin H1 ni texto. Las IAs no ejecutan JavaScript, así que para ellas está vacío.
- E2: mismo title/description en todas las rutas.
- E3: og:url y og:image apuntan a eduardohernandez.lovable.app.
- E4: no hay sitemap.xml (404).
- E5: soft 404 (URL inexistente responde 200).
- E6: www.eduardohdz.com no responde.
- E7: cero JSON-LD.
- E8: se ve el botón "Edit with Lovable".
- E9: existe /clase-gratuita (confirmar con el usuario si sigue vigente; en compraenfabricas ya no hay clase gratis, pero esta es otra marca).
- Rutas actuales: /, /diagnostico, /diagnostico-evergreen, /reto, /reto-diagnostico, /reto-landing, /comunidad, /prompt-maker, /aliados, /aliados-reto, /aliados-curso, /preventa-curso, /sube-tus-ventas, /recursos, /recursos/codigos-chatgpt, /clase-gratuita, /asesoria, /trabaja-conmigo, /30-preguntas, /de-0-a-1-millon, /automatiza, /adn-de-tu-negocio, /adn-de-tu-negocio-gracias y /panel/* (privado).

REGLAS DE TRABAJO
- Los cambios en Lovable van por send_message y gastan créditos. Trabaja por fases; la Fase 1 (migración) SIEMPRE con plan_mode=true primero.
- Revisa cada cambio con get_diff. Antes de cada deploy revisa list_edits: cada publicación sube TODO lo que haya en el proyecto, incluido el trabajo de otras sesiones.
- NO cambies URLs que usan anuncios de Meta o ManyChat sin permiso. Pregúntale al usuario cuáles son antes de empezar. Si alguna URL cambia, 301.
- NO toques pagos (Stripe, Hotmart), formularios, el quiz de diagnóstico, el panel interno (/panel) ni sus integraciones (Metricool, ManyChat) más allá de lo necesario para SSR, y verifica que sigan funcionando.
- NO hagas deploy sin confirmación del usuario.
- Si el agente de Lovable queda en awaiting_input, enséñale al usuario qué pide y espera.
- Nada de testimonios, reseñas, clientes ni cifras inventadas. Si falta algo: [PENDIENTE: …].
- Las llamadas largas a Lovable pueden pasar del límite de 60 s del cliente: usa wait=false y consulta con get_message; si se corta, no reenvíes (cobra doble), busca el mensaje con list_messages.
- Para leer el sitio en vivo, la red de la sesión debe permitir eduardohdz.com (ya está en el entorno "Compra en fabricas"). La API pública de PageSpeed no tiene cupo sin clave: usa Lighthouse local con el Chromium de la sesión (npm i lighthouse@12; CHROME_PATH=/opt/pw-browsers/chromium).

FASES
FASE 0 — Re-auditoría y preguntas (no cambies nada)
- HTML crudo como Googlebot de cada ruta pública; Lighthouse móvil de /, /asesoria, /diagnostico, /sube-tus-ventas y /de-0-a-1-millon (guarda el "antes").
- Lista de rutas: cuáles indexar y cuáles noindex (gracias, reto-*, preventa, panel, evergreen, aliados si son internas).
- Investigación de búsquedas para la persona y la consultoría: "Eduardo Hernández consultor", "movimiento NADIE", "diagnóstico de negocio gratis", "cómo hacer crecer mi negocio", "asesoría para pymes en México", "curso de ventas para emprendedores", "cliente ideal"… Mapa 1 página = 1 intención, sin pelear con compraenfabricas.
- Pregúntale al usuario: URLs usadas en anuncios, vigencia de /clase-gratuita y de las redes de NADIE, y dónde está registrado el dominio (para www).
- Entrega el informe y ESPERA el OK.

FASE 1 — Que se pueda leer (migración a TanStack Start con SSR)
- Confirma en la documentación actual de Lovable la ruta de migración de proyectos Vite a TanStack Start (o, si no es viable, prerender para bots) y explica riesgos y costo antes de hacerla.
- Migración en plan_mode, por tandas, probando en la vista previa: rutas, quiz de diagnóstico, pagos, formularios, panel con login y Pixel (dos IDs).
- Verifica con el HTML crudo que cada ruta indexable trae title, description, canonical, H1 y texto.

FASE 2 — SEO técnico (replicar lo de compraenfabricas)
- Metadatos por ruta (title 50–60 con la keyword al inicio, description 140–155), canonical absoluta a eduardohdz.com, OG/Twitter 1200×630 de marca (negro + rojo #A30E1A; NO usar los colores de Compra en Fábricas).
- sitemap.xml con lastmod, robots.txt (permite buscadores y bots de IA; Disallow /panel), llms.txt, 404 real en español, noindex en páginas sin valor de búsqueda.
- www → sin www con 301 (DNS lo agrega el usuario; dale los pasos).
- Ocultar "Edit with Lovable".
- Velocidad: imágenes WebP con srcset, videos diferidos (como LazyVideo/HeroVideo de compraenfabricas), Pixel diferido con cola. Meta: LCP < 2.5 s en móvil.

FASE 3 — Entidad (lo más importante para Google y las IAs)
- Person con @id fijo https://eduardohdz.com/#person: name, image (foto real), description, jobTitle "Consultor de negocios", knowsAbout (crecimiento empresarial, ventas, estructura de negocios, importación desde China), founder de NADIE (Organization), affiliation (JAICO, Xijiao Shops, Xijiao LOG) y sameAs con https://compraenfabricas.com/autor/eduardo-hernandez, Skool y las redes de Compra en Fábricas. No inventes perfiles personales.
- Organization NADIE con sameAs a sus redes y founder → Eduardo.
- WebSite con name "Eduardo Hernández" y alternateName.
- Course para "De 0 a 1 millón" y "Sube tus ventas" (solo con datos visibles), Event para la clase ADN cuando haya fecha real (fechas centralizadas como CLASS_DATES), FAQPage donde haya preguntas visibles, BreadcrumbList.
- Pide al usuario que en compraenfabricas (otra sesión) el Person apunte a https://eduardohdz.com/#person. Ya tiene sameAs a eduardohdz.com.

FASE 4 — Contenido
- Página "Conoce a Eduardo": historia, números, negocios, NADIE, fotos reales y enlaces a sus dos frentes. Respuesta directa arriba ("Eduardo Hernández es…").
- Página de NADIE con el texto oficial.
- Enlaces cruzados: "¿Quieres importar de China? → compraenfabricas.com" y, desde compraenfabricas, "Sitio oficial de Eduardo → eduardohdz.com".
- Plan de guías públicas a partir de materiales que ya existen (30 preguntas NADIE, códigos de ChatGPT, sesiones del curso): "cómo hacer crecer mi negocio", "cómo subir mis ventas", "cliente ideal", "diagnóstico de negocio". Mismo tono del handoff: español mexicano de banqueta y PAS.

FASE 5 — Medición y fuera del sitio
- Search Console (propiedad de dominio por DNS) y Bing Webmaster Tools (importar desde Search Console); sitemap enviado; IndexNow.
- GA4 o la analítica que exista, con eventos: diagnóstico iniciado y terminado, clic a WhatsApp, clic a cursos y pagos.
- Plan fuera del sitio: YouTube y pódcast de NADIE diciendo "Eduardo Hernández, fundador de NADIE", bio y foto iguales en todos lados, entrevistas en medios (reusar docs/seo/fases-3-4-5.md de compraenfabricas, adaptado a consultoría).

VERIFICACIÓN FINAL
- HTML crudo de cada ruta indexable con title, description, canonical, H1 y texto. JSON-LD válido. Sitemap y robots correctos. Cero soft 404. www redirige.
- Lighthouse móvil antes y después.
- Pagos, quiz, formularios, panel y Pixel funcionando.
- Pide confirmación antes de cada deploy.

ENTREGABLES
1. Informe de Fase 0 con prioridades.
2. Mapa de keywords → página (sin chocar con compraenfabricas).
3. Cambios por fase, con antes y después.
4. Tabla de páginas: URL, keyword, title, description, schema.
5. Lighthouse antes y después.
6. Lista de [PENDIENTE] y preguntas para el usuario.
7. Lo que le toca al usuario: DNS de www, Search Console, Bing, redes.
8. Documento docs/seo/eduardohdz-entrega.md en el repo con todo lo hecho.
```

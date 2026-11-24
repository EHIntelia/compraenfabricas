# eduardohdz.com — Fase 5: medición y plan fuera del sitio

**Fecha:** 24 de noviembre de 2026
**Para quién:** el equipo de Eduardo. La parte técnica (GA4, eventos, IndexNow) la deja lista Claude en Lovable; lo de "fuera del sitio" lo hace Eduardo y su equipo.

---

## 1. Medición

### Google Search Console (lo hace el usuario)

1. En https://search.google.com/search-console, con la **misma cuenta de Google** de compraenfabricas: **Añadir propiedad → Dominio → `eduardohdz.com`**.
2. Copiar el registro TXT (`google-site-verification=…`).
3. En GoDaddy: **Mis productos → eduardohdz.com → DNS → Agregar registro**.
   - Tipo: TXT
   - Nombre: `@`
   - Valor: el texto de Google
   - TTL: 1 hora
4. En Search Console, dar **Verificar**. Puede tardar de minutos a unas horas.
5. En **Sitemaps**, enviar `https://eduardohdz.com/sitemap.xml`.
6. En **Inspección de URL**, pedir indexación de estas páginas, una por una:
   - `/`
   - `/eduardo-hernandez`
   - `/nadie`
   - `/diagnostico`
   - `/asesoria`

### Bing Webmaster Tools (lo hace el usuario)

1. En https://www.bing.com/webmasters, elegir **Importar desde Google Search Console**. Se trae el sitio y el sitemap.
2. Es importante porque **ChatGPT busca con el índice de Bing**.

### IndexNow (listo en el sitio)

- **Llave:** `39ad97afec30c14ce2be6916ba563acf`, servida en `https://eduardohdz.com/39ad97afec30c14ce2be6916ba563acf.txt`.
- **Cuándo se usa:** cada vez que se publica una página nueva o un cambio importante, se avisa a Bing y Yandex con un POST a `https://api.indexnow.org/indexnow`:
  ```json
  {"host":"eduardohdz.com","key":"39ad97afec30c14ce2be6916ba563acf","keyLocation":"https://eduardohdz.com/39ad97afec30c14ce2be6916ba563acf.txt","urlList":["https://eduardohdz.com/..."]}
  ```
- Claude lo hace al terminar cada publicación.

### GA4 (propiedad nueva)

**Crear la propiedad (lo hace el usuario):**
1. En https://analytics.google.com: **Administrar → Crear → Propiedad**.
   - Nombre: "Eduardo Hernández (eduardohdz.com)"
   - Zona horaria: México (Ciudad de México)
   - Moneda: MXN
2. **Flujo de datos → Web:**
   - URL: `https://eduardohdz.com`
   - Nombre: "eduardohdz.com"
3. Copiar el **ID de medición** (`G-XXXXXXXXXX`) y pasárselo a Claude.
4. En el flujo, **Medición mejorada → engrane**: desactivar **"Cambios de página según el historial del navegador"**. El sitio manda sus propios `page_view`; si se deja activo, cuenta doble.
5. En **Administrar → Vinculaciones de productos → Search Console**, vincular la propiedad de dominio `eduardohdz.com`.
6. Marcar como **eventos clave** (conversiones):
   - `diagnostico_terminado`
   - `clic_whatsapp`
   - `begin_checkout`
   - `generate_lead`

**Eventos que manda el sitio** (sin datos personales):

| Evento | Cuándo | Parámetros |
|---|---|---|
| `page_view` | Al cargar y en cada cambio de página | page_location, page_path, page_title |
| `diagnostico_iniciado` | Al pasar a la pregunta 1 del quiz | page_path |
| `diagnostico_terminado` | Al ver los resultados | page_path, nivel, area_principal |
| `clic_whatsapp` | Clic a cualquier enlace de WhatsApp | page_path, link_text |
| `clic_curso` | Clic hacia Sube tus Ventas, De 0 a 1 Millón, Clase gratuita, Asesoría o ADN | page_path, destino |
| `begin_checkout` | Clic a Hotmart o Stripe | page_path, currency, value, item_name |
| `generate_lead` | Envío correcto de un formulario de registro | page_path, form |

**El Meta Pixel** (2 IDs) sigue igual, con sus eventos PageView, ViewContent e InitiateCheckout.

### Tabla de seguimiento (cada 2 semanas, desde Search Console)

| Búsqueda | Página objetivo | Posición | Clics | Impresiones | Notas |
|---|---|---|---|---|---|
| eduardo hernández consultor de negocios | / y /eduardo-hernandez | | | | |
| eduardo hernández nadie | /eduardo-hernandez | | | | |
| movimiento nadie | /nadie | | | | |
| diagnóstico de negocio gratis | /diagnostico | | | | |
| asesoría para pymes | /asesoria | | | | |
| curso de ventas para mipyme | /sube-tus-ventas | | | | |
| de 0 a 1 millón curso | /de-0-a-1-millon | | | | |
| eduardo hernández importaciones china | compraenfabricas.com (no se ataca aquí) | | | | Solo vigilar que salgan los dos sitios |

**Prueba con IAs (cada mes):** preguntar a ChatGPT, Gemini, Perplexity y Google (AI Overviews):
- "¿Quién es Eduardo Hernández, fundador de NADIE?"
- "¿Qué es el movimiento NADIE?"
- "Eduardo Hernández consultor de negocios México"

Anotar si lo citan, de qué fuente y si los datos son correctos.

---

## 2. Plan fuera del sitio (lo hace Eduardo)

### Por qué

Las IAs citan sobre todo **lo que otros dicen** de una persona, y YouTube es de lo que más citan. El sitio ya está listo para que lo lean; ahora hay que lograr que **otros lo mencionen** con los mismos datos.

### Regla de oro: los mismos datos en todos lados

- **Nombre:** Eduardo Hernández.
- **Etiqueta:** "consultor de negocios y fundador de NADIE".
- **Bio corta** (para YouTube, Skool, pódcast y medios):
  > Eduardo Hernández, consultor de negocios y fundador de NADIE. 8 años en consultoría, +300 empresas asesoradas y 26+ años importando de China. eduardohdz.com
- **Foto:** la profesional en blanco y negro (`eduardo-foto-profesional.jpg`), la misma del sitio y de la ficha de Google.
- **Enlace:**
  - de consultoría y crecimiento de negocio: `eduardohdz.com`;
  - de importación: `compraenfabricas.com`.
- **Si se abre un perfil nuevo** (por ejemplo, un YouTube de NADIE o de Eduardo), avisar para agregarlo al `sameAs` de la ficha de Eduardo en el sitio.

### 1. YouTube y pódcast

**Regla al grabar:** en los primeros 30 segundos decir en voz alta "Soy Eduardo Hernández, consultor de negocios y fundador de NADIE", y la pregunta exacta del video. La IA lee la transcripción.

**Plantilla de título** (~60 caracteres, con la búsqueda al inicio):
`Cómo definir a tu cliente ideal (paso a paso) | Eduardo Hernández`

**Plantilla de descripción:**
```
{Respuesta directa en 2 líneas a la pregunta del video.}

Soy Eduardo Hernández, consultor de negocios y fundador de NADIE. En los últimos 8 años he asesorado a más de 300 empresas y emprendedores.

📌 Guía completa: https://eduardohdz.com/{guía del tema}
🧭 Diagnóstico de negocio gratis: https://eduardohdz.com/diagnostico
👤 Quién soy: https://eduardohdz.com/eduardo-hernandez

Capítulos:
00:00 {La pregunta}
00:30 {Paso 1}
…

#negocios #emprendimiento #pymes
```

**8 videos** (las mismas preguntas que las páginas y las guías, sin repetir los de importación de compraenfabricas):

| # | Video | Página |
|---|---|---|
| 1 | Quién soy y qué es NADIE (2–3 min) | /eduardo-hernandez y /nadie |
| 2 | Cómo saber en qué nivel está tu negocio (las 5 áreas) | /diagnostico |
| 3 | Cómo definir a tu cliente ideal | guía 3 |
| 4 | Cómo subir tus ventas sin depender de la suerte | guía 2 y /sube-tus-ventas |
| 5 | Cómo hacer crecer tu negocio cuando todo depende de ti | guía 1 |
| 6 | Preguntas para cerrar ventas (de las 30 de NADIE) | /30-preguntas |
| 7 | Mis 2 bancarrotas: lo que aprendí | /eduardo-hernandez (cuando lleguen las historias reales) |
| 8 | Clase De 0 a 1 Millón: qué vas a aprender | /de-0-a-1-millon |

**Pódcast de negocios:** en el sitio, la sección dice "Próximamente". Cuando salga el primer episodio, avisar:
- se agrega a la página;
- se agrega al `sameAs` si tiene canal propio.

### 2. Entrevistas y medios

**Ángulos** (sin repetir el de importación, que ya usa compraenfabricas):
- "2 bancarrotas y 5 negocios funcionando: lo que aprendí sobre hacer crecer una pyme en México."
- "Por qué la mayoría de las pymes no crece: las 5 áreas que revisamos en más de 300 empresas."
- "NADIE: un movimiento de empresarios donde la cara no es el asesor, sino la comunidad."

**Medios y pódcast candidatos** (México, negocios y emprendimiento; confirmar que sigan aceptando colaboraciones):
- Entrepreneur en Español
- Forbes México (foro de opinión y emprendedores)
- Expansión Pymes
- El Economista (Pymes)
- Alto Nivel
- El CEO
- Emprendedor.com
- Negocios Chingones (pódcast)
- Merca2.0

**Correo para proponer entrevista (borrador):**
```
Asunto: 300 pymes asesoradas (y 2 bancarrotas): propuesta de entrevista

Hola {nombre}:

Soy Eduardo Hernández, consultor de negocios y fundador del movimiento NADIE. En los últimos 8 años he asesorado a más de 300 empresas y emprendedores en México, y tengo 5 negocios funcionando después de pasar por 2 bancarrotas.

Les propongo una entrevista o columna sobre {ángulo}: qué frena a la mayoría de las pymes y qué sí funciona para crecer, con ejemplos reales.

Más sobre mí: https://eduardohdz.com/eduardo-hernandez

Saludos,
Eduardo Hernández
eduardohdz.com
```

**En cada mención o entrevista, pedir:**
- nombre completo + "fundador de NADIE" + enlace a `eduardohdz.com/eduardo-hernandez`;
- la foto oficial.

### 3. Comunidades (aportar, no hacer spam)

- **Grupos de dueños de negocio y emprendedores:** contestar dudas completas en el comentario.
  - Enlazar solo cuando la guía de verdad amplía la respuesta (máximo 1 de cada 5 respuestas).
  - Nada de "mándame inbox".
- **Cada duda que se repita** se vuelve una pregunta frecuente o una guía nueva.

### 4. Lo que NO se hace

- Comprar enlaces, reseñas o menciones.
- Inventar cifras, casos o testimonios.
- Abrir perfiles personales de Eduardo con otros datos o con otra foto.
- Atacar búsquedas de importación desde eduardohdz.com (eso va en compraenfabricas).

---

## 3. Plan de 90 días

| Semanas | Qué se hace | Qué se mide |
|---|---|---|
| 1 | Search Console + Bing, sitemap enviado, GA4 creado y conectado, `www` en GoDaddy, `@id` unificado en compraenfabricas | Que se indexen /, /eduardo-hernandez y /nadie (Inspección de URL) |
| 2–3 | Bio y foto iguales en Skool y en los perfiles que hable Eduardo. Video 1 (Quién soy y qué es NADIE). Guía 3 (cliente ideal) | Primeras búsquedas en Search Console; prueba con IAs (línea base) |
| 4–5 | Videos 2 y 3. Guía 1 (crecer mi negocio). Contenido real de ADN para quitar el noindex | Eventos de GA4: diagnóstico iniciado/terminado, WhatsApp |
| 6–7 | Videos 4 y 5. Guía 2 (subir ventas). 5 correos a medios | Clics y CTR por página; ajustar títulos con CTR bajo |
| 8–9 | Videos 6 y 8. Guía 4 (diagnóstico). Primer pódcast, si ya está | Posiciones de la tabla |
| 10–12 | Video 7 (cuando lleguen las historias reales). Segunda ronda de medios | Comparar con la semana 2; Lighthouse de nuevo |
| 13 | **Revisión de 90 días:** qué sube, qué no, y el siguiente plan | Informe con Search Console + GA4 + prueba con IAs |

**Cada mes:**
- actualizar `PAGE_LASTMOD` de las páginas que cambien;
- cargar fechas reales en `CLASS_DATES` (clase gratuita y ADN);
- revisar que los datos de Eduardo sigan iguales en todos lados.

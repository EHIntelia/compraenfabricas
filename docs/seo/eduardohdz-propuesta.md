# eduardohdz.com — Diagnóstico y propuesta de posicionamiento

**Fecha:** 12 de noviembre de 2026
**Proyecto Lovable:** "Eduardo Hernández" (id `31eb7ad3-327e-43ed-9449-1c7cda622ec0`)

---

## 1. Qué papel juega cada sitio

| | eduardohdz.com | compraenfabricas.com |
|---|---|---|
| **Es la casa de…** | La **persona**: Eduardo Hernández, consultor de negocios y fundador de NADIE | La **marca de importación**: Compra en Fábricas de China |
| **Temas** | Hacer crecer tu negocio, ventas, estructura, diagnóstico, NADIE, cursos "De 0 a 1 millón" y "Sube tus ventas", asesoría, ADN | Importar de China: clase, proveedores, cajas, joyería, logística |
| **Búsquedas objetivo** | "Eduardo Hernández consultor de negocios", "movimiento NADIE", "diagnóstico de negocio gratis", "cómo hacer crecer mi negocio", "asesoría para pymes", "curso de ventas para emprendedores" | "curso para importar de China", "cómo importar de China a México", "joyería de mayoreo"… |
| **No pelea por** | Nada de importación (eso se enlaza a compraenfabricas) | Nada de consultoría general |

**La meta:** que Google y las IAs entiendan que hay **una sola persona**, Eduardo Hernández, con dos frentes: consultoría (eduardohdz.com) e importación (compraenfabricas.com). Así, cuando alguien busque "Eduardo Hernández", salen los dos sitios y se refuerzan entre sí.

**Reto:** "Eduardo Hernández" es un nombre muy común. No vamos a ganar el nombre solo; ganamos con combinaciones ("Eduardo Hernández NADIE", "Eduardo Hernández consultor", "Eduardo Hernández importaciones China") y con señales consistentes: misma foto, misma bio, mismos datos y enlaces cruzados.

## 2. Qué encontré (12 nov 2026)

| # | Problema | Impacto |
|---|---|---|
| E1 | **El HTML le llega vacío a Google y a las IAs.** El sitio es la versión vieja de Lovable (Vite, una sola página que se arma con JavaScript). Con el user-agent de Googlebot, la página trae 11 palabras: el título y "Edit with Lovable". No hay H1 ni texto. Google a veces ejecuta el JavaScript, tarde y no siempre; **ChatGPT, Perplexity y Claude no lo ejecutan: para ellos el sitio está vacío.** | Muy alto |
| E2 | **El mismo title y description en todas las páginas** (`/`, `/asesoria`, `/nadie`…). | Alto |
| E3 | `og:url` y `og:image` apuntan a `eduardohernandez.lovable.app`, no al dominio. | Medio |
| E4 | **No hay sitemap** (`/sitemap.xml` da 404). | Alto |
| E5 | **Soft 404:** una URL que no existe responde 200. | Medio |
| E6 | **`www.eduardohdz.com` no responde:** falta el registro DNS o la redirección. | Medio |
| E7 | **Cero datos estructurados:** ni Person, ni Organization (NADIE), ni cursos. | Alto |
| E8 | El botón "Edit with Lovable" se ve en el sitio (se puede ocultar en los ajustes del proyecto). | Bajo (imagen) |
| E9 | Hay una página `/clase-gratuita`. En Compra en Fábricas ya no hay clase gratis; aquí es otra marca. ¿Sigue vigente? | A confirmar |
| E10 | La información de Eduardo es consistente con compraenfabricas (8 años, 300+ empresas, 26 años de importación, 50+ empresas a China, fundador de NADIE). | Bien |

## 3. Propuesta (en orden)

### Paso 1 — Que Google y las IAs puedan leerlo (lo más importante)
- **Migrar a TanStack Start con render en servidor (SSR)**, como ya está compraenfabricas. Lovable tiene ruta de migración para proyectos viejos.
  - Es el cambio más grande. Hay que hacerlo en modo plan y con cuidado, porque el sitio tiene panel interno, pagos (Stripe y Hotmart), diagnóstico y formularios.
  - Se prueba todo en la vista previa antes de publicar.
- Plan B si la migración se complica: confirmar con Lovable si el prerender para bots está activo en este proyecto (hoy no lo está para Googlebot).

### Paso 2 — Lo básico de SEO técnico (ya probado en compraenfabricas)
- Title, description, canonical y Open Graph propios en cada página, con el dominio correcto.
- `sitemap.xml` y `robots.txt` que lo apunte. `noindex` en el panel, las páginas de gracias y las de prueba.
- 404 real.
- `www` → sin www con 301 (el registro DNS lo agregas tú donde compraste el dominio).
- Ocultar "Edit with Lovable".

### Paso 3 — La entidad "Eduardo Hernández" (lo que hace que Google lo entienda)
- **Person** en eduardohdz.com como la "casa" de la entidad, con id fijo `https://eduardohdz.com/#person`:
  - nombre, foto y descripción;
  - jobTitle "Consultor de negocios";
  - `founder` de NADIE;
  - `affiliation` con JAICO, Xijiao Shops y Xijiao LOG;
  - knowsAbout: crecimiento empresarial, ventas, importación desde China;
  - sameAs: la página de autor de compraenfabricas, Skool y las redes de Compra en Fábricas.
- **Organization NADIE**, con sameAs a sus redes (Instagram @_nadieofficial, TikTok @_nadieofficial, YouTube @nadieofficiall y Facebook nadieofficiall) y `founder` → Eduardo.
- **Course** para "De 0 a 1 millón" y "Sube tus ventas", y **Event** para la clase ADN cuando haya fecha.
- En compraenfabricas, la página de autor apunta a eduardohdz.com con `sameAs`; esto ya va en la Fase 2.

### Paso 4 — Contenido
- **Página "Conoce a Eduardo"** completa: historia, números, negocios, NADIE, las fotos nuevas y enlaces a sus dos frentes.
- **Página de NADIE** con el texto oficial:
  - "NADIE es un movimiento de empresarios que buscan construir negocios más sólidos, rentables y con visión a largo plazo…"
  - La frase "Yo no soy nadie, solo quiero ayudarte a hacer crecer tu negocio y que ganes más dinero."
- **Enlaces cruzados:**
  - eduardohdz.com: "¿Quieres importar de China? → compraenfabricas.com".
  - compraenfabricas.com: "Sitio oficial de Eduardo → eduardohdz.com".
- **Contenido nuevo (blog o recursos):** "cómo hacer crecer mi negocio", "diagnóstico de negocio", "cómo subir mis ventas" y "cliente ideal". Ya existen materiales (30 preguntas NADIE, códigos de ChatGPT, sesiones) que se pueden convertir en guías públicas.

### Paso 5 — Fuera del sitio
- **YouTube y pódcast de NADIE** (el sitio ya tiene sección de pódcast): decir en voz alta "Eduardo Hernández, fundador de NADIE" y enlazar a eduardohdz.com en cada descripción.
- **Misma bio y misma foto** en todas las redes y en Skool.
- **Entrevistas en medios y pódcast** de negocios: cada mención con nombre + "fundador de NADIE" + enlace.

## 4. Riesgos y costo
- La migración a SSR es lo más caro en créditos y lo más delicado (pagos, panel interno, quiz de diagnóstico). Conviene hacerla **después de publicar la Fase 2 de compraenfabricas**, con plan aprobado y sin publicar hasta revisar todo.
- No hay que cambiar URLs que se usen en anuncios (por ejemplo /diagnostico o /adn-de-tu-negocio). Si alguna cambia, 301.

## 5. Lo que necesito confirmar
1. ¿/clase-gratuita sigue vigente en eduardohdz.com?
2. ¿Qué URLs de eduardohdz.com usan los anuncios de Meta o ManyChat?
3. ¿Dónde está registrado el dominio (para agregar `www`)?
4. ¿Las redes de NADIE (@_nadieofficial, @nadieofficiall) son oficiales y vigentes?

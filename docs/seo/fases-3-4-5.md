# Fases 3, 4 y 5 — SEO local, medición y plan fuera del sitio

**Fecha:** 12 de noviembre de 2026 · compraenfabricas.com

---

## FASE 3 — SEO local: perfil de Google de JAICO

### Decisión
- **Compra en Fábricas de China no lleva perfil de Google:** es 100% en línea y no atiende en una dirección. Usa `areaServed` (México y Latinoamérica) en el schema, como ya está.
- **El perfil se hace para JAICO**, en el showroom de San Pedro Garza García, que atiende con cita. Google permite negocios que atienden solo con cita, siempre que el lugar sea real, tenga letrero y alguien del equipo reciba a los clientes. **No se usan oficinas virtuales:** Google las suspende.

### Antes de crearlo (lo confirmas tú)
- [x] **Calle:** Perseverancia 123, San Pedro Garza García, N.L. *(confirmado 12 nov)*
- [ ] **Colonia y código postal**, escritos igual que en el comprobante de domicilio.
- [ ] **Nombre en el letrero:** el perfil se llama exactamente así ("JAICO" o "JAICO Joyería"). Nada de palabras extra del tipo "joyería mayoreo barata".
- [ ] **Quién recibe** cuando hay cita.
- [x] **Teléfono del perfil:** 81 2018 1761 (+52 81 2018 1761), el mismo del WhatsApp *(confirmado 12 nov)*
- [ ] **Video para verificar:** Google suele pedir un video continuo que muestre el letrero, la calle y el interior, y algo que pruebe que el lugar es tuyo (llaves, caja, mostrador).

### Ficha propuesta (para copiar y pegar en Google Business Profile)
- **Nombre:** JAICO *(como diga el letrero)*
- **Categoría principal:** Mayorista de joyería. Busca "joyería" en el selector y elige la que diga mayorista. Si no aparece, usa "Proveedor de joyería".
- **Categorías secundarias:** Tienda de bisutería, Joyería.
- **Horario:** no se pone (atiende con cita). En "Más" se marca "Solo con cita".
- **Sitio web:** https://compraenfabricas.com/joyeria
- **Enlace de citas:** WhatsApp con texto: `https://wa.me/5218120181761?text=Hola%2C%20quiero%20agendar%20una%20cita%20en%20el%20showroom%20de%20JAICO`
- **Descripción (≈700 caracteres, sin URLs ni promociones):**
  > JAICO es proveedor de joyería de mayoreo en acero inoxidable y chapa de oro, traída directo de fábrica en China. Surtimos a vendedoras por catálogo, tiendas, puestos y emprendedores que quieren vender joyería con buen margen. Manejamos cadenas, dijes, aretes, brazaletes y juegos, con modelos nuevos cada temporada. Nuestro fundador, Eduardo Hernández, lleva más de 26 años importando de China y tenemos equipo propio allá. En el showroom de San Pedro Garza García puedes ver las piezas en persona con cita previa. También levantamos pedidos directos de fábrica desde 36 piezas por modelo y te los traemos hasta tu negocio.
- **Servicios:** Venta de joyería al mayoreo · Pedidos directos de fábrica en China (desde 36 piezas por modelo) · Showroom con cita · Envíos a todo México.
- **Productos** (con foto real de cada uno; sin precio si cambia seguido): cadenas de acero, dijes, aretes, brazaletes, juegos de joyería, piezas en chapa de oro.
- **Atributos:** "Solo con cita"; los de identidad (por ejemplo, "negocio dirigido por…") solo si aplican de verdad.

### Fotos (subir al crear y luego 2–4 al mes)
- Fachada con el letrero (de día), interior del showroom y mostrador.
- Piezas reales en exhibición (no fotos de catálogo de proveedor).
- Equipo atendiendo, sin nombres. Eduardo en el showroom.
- Logo cuadrado y una portada horizontal.

### Publicaciones (1 por semana, 3 meses)
Alternar: modelo nuevo de la semana · "qué se está vendiendo más" · tip para vender joyería por catálogo · recordatorio de "agenda tu cita". Siempre con foto real y botón de WhatsApp.

### Reseñas
- Pedirlas **solo a clientes reales** que ya compraron, con el enlace corto del perfil, y responderlas todas.
- Prohibido inventarlas, pagarlas o pedirlas al equipo (Google las borra y puede suspender el perfil).

### Consistencia (NAP)
- El mismo nombre, dirección y teléfono en el perfil de Google, en /joyeria (pie de página, si lo apruebas), en info.joyeria.shop, en Bing Places (se importa del perfil de Google) y en Apple Business Connect.
- La dirección **no** se pone en compraenfabricas.com fuera de /joyeria.
- Si se agrega en /joyeria, va también el schema `JewelryStore` con esa dirección.

---

## FASE 4 — Medición

### Qué ya hay
- **Google Search Console:** verificado, con el sitemap enviado.
- **Bing Webmaster Tools:** importado desde Search Console.
- **Meta Pixel en todo el sitio:**
  - PageView en cada página.
  - `ClicBoton` en cualquier botón o enlace (con texto, destino y página).
  - `Contact` en todo enlace a WhatsApp.
  - En /productos: ViewContent, Search, filtros y "Apartar".
  - Carga después de la página y no pierde eventos.
- **No hay Google Analytics 4.** Sin GA4 no se puede ver cuántas visitas llegan de Google, a qué páginas entran ni cuáles terminan en WhatsApp o en pago.

### Propuesta
1. **Instalar GA4.**
   - Tú creas la propiedad en analytics.google.com (2 minutos) y me pasas el ID, que empieza con `G-`. El ID no es secreto: va en el código del sitio.
   - Lovable lo instala diferido, igual que el Pixel, para no frenar la página.
2. **Eventos con nombre propio (en GA4 y en el Pixel):**

| Evento | Cuándo | Para qué |
|---|---|---|
| `clic_whatsapp` | Clic a cualquier wa.me (con la página de origen) | Qué página manda más gente a WhatsApp |
| `clic_tomar_clase` | Clic a /clase desde cualquier página | Qué páginas empujan la clase |
| `inicio_pago` (Pixel: `InitiateCheckout`) | Clic al botón de Stripe en /clase | Cuántos llegan al pago |
| `clic_joyeria` | Clic a info.joyeria.shop o a /joyeria | Siembra de joyería |
| `clic_skool` | Clic a skool.com | Escuela |
| `apartar_caja` | Clic a "Apartar" en /productos y /producto | Ventas de cajas |

3. **WhatsApp con origen.** El botón flotante y el del footer hoy mandan el mismo texto en todas las páginas ("Hola, quiero info para comprar en China"). Propongo que digan de dónde vienen: "Hola, vengo de *{nombre de la página}*". Así el equipo de ventas sabe qué página trajo a cada cliente, sin depender de GA4.
   - Los mensajes que ya tienen texto propio se quedan: cajas, logística, asesoría, blog y marketplace.
4. **Conversiones en Search Console:** revisar cada 2 semanas "Rendimiento → Consultas" por página (ver la tabla de seguimiento).

### Tabla de seguimiento
Archivo: `docs/seo/seguimiento-keywords.csv`. Columnas: keyword · página objetivo · posición inicial · fecha · posición actual · fecha · notas. La posición inicial se llena con Search Console, filtrando por país México y los últimos 28 días.

---

## FASE 5 — Plan fuera del sitio (lo hace Eduardo; aquí van los textos)

### Por qué
Las IAs (ChatGPT, Gemini, Perplexity, AI Overviews) citan sobre todo lo que **otros** dicen de una marca, y YouTube es de lo que más citan. El sitio ya está listo para que lo lean; ahora hay que hacer que lo mencionen.

### 1. YouTube

**Plantilla de título (máximo ~60 caracteres, la búsqueda al inicio):**
`Cómo importar de China a México en 2026 (paso a paso) | Eduardo Hernández`

**Plantilla de descripción:**
```
{Respuesta directa en 2 líneas a la pregunta del video.}

Soy Eduardo Hernández, fundador de Compra en Fábricas de China. Llevo más de 26 años importando de China y he asesorado a más de 300 empresas.

📌 Guía completa: https://compraenfabricas.com/{página pilar del tema}
🎓 Clase en vivo para importar de China: https://compraenfabricas.com/curso-para-importar-de-china
💬 WhatsApp: https://wa.me/5218120181761

Capítulos:
00:00 {La pregunta}
00:30 {Paso 1}
…
{mm:ss} Errores comunes
{mm:ss} Cómo empezar hoy

#importardechina #comprarenchina #emprendimiento
```

**Regla para hablar en el video:** en los primeros 30 segundos decir en voz alta "Soy Eduardo Hernández, de Compra en Fábricas de China" y la pregunta exacta ("¿cómo importar de China a México?"). La IA lee la transcripción.

**10 videos "cómo hacer…" (mismas preguntas que las páginas):**
1. Cómo importar de China a México paso a paso (2026) → pilar del blog
2. Curso para importar de China: qué aprendes en la clase en vivo → /curso-para-importar-de-china
3. Cómo saber si un proveedor chino es fábrica o revendedor → nota "comprar directo de fábrica"
4. ¿Necesito RFC y padrón para importar? Requisitos explicados fácil → nota de requisitos
5. Cuánto cuesta importar de China: ejemplo real con una caja → nota de costos / /productos
6. Cómo pagarle a un proveedor en China sin que te estafen → nota de pagos / /validacion
7. Aéreo o marítimo: cuál conviene para tu primer pedido → nota de envío / /logistica
8. Qué es Yiwu y cómo se compra ahí (recorrido real) → nota de Yiwu
9. Joyería de acero inoxidable: por qué es el producto que más deja → nota de joyería / /joyeria
10. Los errores que me costaron dinero importando (mis 2 bancarrotas) → nota de errores / /autor

### 2. Perfiles consistentes
- **Misma bio corta** en Instagram, TikTok, Facebook, YouTube y Skool:
  > Te enseño a comprar directo de fábricas en China, sin intermediarios. +26 años importando · +300 empresas asesoradas · Eduardo Hernández 👇 compraenfabricas.com
- **Misma foto de perfil:** el logo 中 de la marca. En los canales donde habla Eduardo, su foto 1.
- **Mismo enlace:** compraenfabricas.com (o /curso-para-importar-de-china).
- Todos esos perfiles ya están en el `sameAs` del sitio; si se abre uno nuevo (por ejemplo YouTube), avisar para agregarlo.

### 3. Relaciones públicas (entrevistas y artículos)
**Ángulos:**
- "26 años comprando en fábricas chinas y 2 bancarrotas: lo que nadie te dice de importar."
- **Noticia del momento:** "Aranceles de 2026 a productos chinos: qué cambia para los emprendedores que importan" (Eduardo como fuente que vive el tema).

**10 medios y pódcast candidatos** (México, negocios y emprendimiento; revisa que sigan aceptando colaboraciones):
1. Entrepreneur en Español (columna de experto)
2. Forbes México (sección emprendedores / foro de opinión)
3. Expansión (Expansión Pymes)
4. El Economista (sección Pymes)
5. Alto Nivel
6. El Financiero (Empresas)
7. El CEO
8. Emprendedor.com
9. Merca2.0 (también tiene pódcast)
10. Negocios Chingones (pódcast de entrevistas a emprendedores mexicanos)

Extra para logística y comercio exterior: Mexico Business News (sección Logistics) y The Logistics World.

**Correo para proponer la entrevista (borrador):**
```
Asunto: 26 años importando de China (y 2 bancarrotas): propuesta de entrevista

Hola {nombre}:

Soy Eduardo Hernández. Llevo más de 26 años comprando directo en fábricas de China, fundé JAICO, Xijiao Shops y Xijiao LOG, y he asesorado a más de 300 empresas mexicanas.

Con los aranceles de 2026 a productos chinos, muchos emprendedores no saben si todavía conviene importar. Les puedo contar, con casos reales y números, qué cambió, qué productos siguen dejando margen y los errores que más cuestan (yo pasé por 2 bancarrotas aprendiéndolo).

¿Les interesaría una entrevista o una columna sobre esto? Les comparto más sobre mí: https://compraenfabricas.com/autor/eduardo-hernandez

Saludos,
Eduardo Hernández
Compra en Fábricas de China · WhatsApp {número}
```

### 4. Comunidades (aportar, no hacer spam)
- **Grupos de Facebook de importadores y emprendedores:** responder dudas concretas con la respuesta completa en el comentario. Solo enlazar a una guía cuando de verdad la amplía (máximo 1 de cada 5 respuestas con enlace). Nada de "mándame inbox".
- **Reddit** (r/mexico, r/MexicoFinanciero, r/emprendedores): cuenta personal con historial; contestar con experiencia propia; respetar las reglas de cada comunidad sobre autopromoción.
- **Preguntas de la gente → contenido:** cada duda que se repite en grupos se vuelve una pregunta de /preguntas-frecuentes o una nota del blog.

### 5. Directorios y cámaras legítimas
- **ANIERM** (Asociación Nacional de Importadores y Exportadores de la República Mexicana): afiliación para Xijiao LOG / JAICO. Da credibilidad y aparece en su ecosistema. Sitio: anierm.org.mx.
- **CANACO Monterrey o CAINTRA Nuevo León:** para JAICO / Xijiao como empresas regiomontanas.
- **Bing Places y Apple Business Connect:** para JAICO, con los mismos datos del perfil de Google.
- Evitar directorios de "enlaces" o de pago masivo: no ayudan y pueden perjudicar.

---

## PLAN DE 90 DÍAS

| Semana | Qué se publica / hace | Qué se mide |
|---|---|---|
| 1 (12–18 nov) | Publicar Fase 2 + H.264. Fotos y NADIE en la página de Eduardo. Crear GA4. Confirmar datos del showroom. Clase del 21. | Que las páginas nuevas se indexen (Search Console → Inspección de URL) |
| 2 | Instalar GA4 y eventos. WhatsApp con origen. Crear el perfil de Google de JAICO. Nota B (requisitos). | Primeras consultas en Search Console |
| 3–4 | Notas C (costos) y A (fábrica vs. revendedor). Videos 1 y 2. Bio igual en todas las redes. | Llenar la tabla de seguimiento con las posiciones iniciales |
| 5–6 | Notas E (pagos) y D (aranceles). Videos 3 y 4. Mandar 5 correos a medios (ángulo aranceles). | Clics y CTR por página; ajustar titles con CTR bajo |
| 7–8 | Notas H (aéreo vs. marítimo) y F (Yiwu). Videos 5 y 6. Siguiente fecha de clase en CLASS_DATES. | Eventos GA4: WhatsApp e inicio de pago por página |
| 9–10 | Nota I (joyería de acero) y J (Feria de Cantón, antes de la edición de primavera). Videos 7 y 8. Afiliación a ANIERM. | Reseñas y búsquedas del perfil de JAICO |
| 11–12 | Nota G (errores de Eduardo, cuando lleguen sus historias). Videos 9 y 10. Revisión completa. | Comparar posiciones con la semana 3; PageSpeed de nuevo |
| 13 | **Revisión de 90 días:** qué páginas suben, cuáles no, qué notas reforzar o juntar, y siguiente plan. Arrancar eduardohdz.com en paralelo. | Informe con Search Console + GA4 |

**Cada mes:** revisar los precios citados en las notas, actualizar `PAGE_LASTMOD` de las páginas que cambien y revisar que el Event de la clase tenga la siguiente fecha.

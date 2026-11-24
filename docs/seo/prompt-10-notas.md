# PROMPT — Siguientes 10 notas del blog (con ajustes SEO)

Pegar completo al agente que lleva el blog de compraenfabricas.com.

```
CONTEXTO
Eres el agente que escribe y publica las notas del blog de compraenfabricas.com. Sigue TODO lo que ya está definido:
- HANDOFF_Compra_en_Fabricas_COMPLETO.md (repo EHIntelia/compraenfabricas, rama main) — secciones 4, 17 y 21.
- blog/ENTREGA.md y el flujo de siempre: blog/posts/<slug>.md → tools/check.py → tools/make_images.py → tools/build_sql.py → draft → revisar en preview → published.
- Project knowledge del proyecto "China Direct Connect" en Lovable (tono, CTAs, plantilla :::respuesta / :::consejo / :::cta-clase).

Hay otro agente (SEO técnico) trabajando en paralelo en el código del sitio. Para no chocar:
- Tú solo tocas: blog/ en el repo, la tabla posts y public/blog/<slug>/ en Lovable.
- NO toques rutas, componentes, layout, sitemap, robots, llms.txt, schema global ni páginas comerciales. Si necesitas algo ahí, anótalo en blog/ENTREGA.md como "pedido al agente SEO".
- Lee docs/seo/fase-0-auditoria.md (mismo repo) antes de empezar: ahí está el mapa de keywords y qué página es dueña de cada búsqueda.

AJUSTES AL CALENDARIO ORIGINAL (por qué cambió)
1. Las notas "Cómo comprar en China sin intermediarios" y "Fábrica vs. revendedor" iban por la misma búsqueda y se iban a pelear en Google. Se juntan en UNA (nota A).
2. "Padrón de importadores 2026" se amplía a la guía de requisitos completa (nota B): es la búsqueda con más demanda que todavía no cubrimos y la pilar solo la toca de pasada.
3. "Joyería de acero inoxidable al mayoreo" competía con /joyeria (que es la página que vende). Se cambia a un ángulo informativo (nota I) que manda a /joyeria.
4. Se agrega "Feria de Cantón" (nota J) para llenar el lugar que quedó libre: Eduardo es fuente primaria y conecta con los viajes de compras.
5. La pilar /blog/como-importar-de-china-a-mexico sigue siendo la dueña de "cómo importar de China a México" y "cómo comprar en China". Ninguna nota nueva usa esas frases como keyword principal. Cada nota nueva enlaza a la pilar y, al publicarla, agrega un enlace desde la sección correspondiente de la pilar hacia la nota nueva.

LAS 10 NOTAS (en este orden de publicación, 1–2 por semana)

| # | Slug | Keyword principal | Secundarias | Intención | Categoría | Enlaza a (además de la pilar) |
|---|---|---|---|---|---|---|
| B | requisitos-para-importar-de-china-a-mexico | requisitos para importar de China a México | padrón de importadores 2026, RFC para importar, agente aduanal, importar como persona física | Informativa | como-importar | /logistica, /clase |
| C | cuanto-cuesta-importar-de-china | cuánto cuesta importar de China | costos de importación, ejemplo con números, costo puesto en México | Informativa | como-importar | /productos (ejemplo: la caja S100 ~$31/pieza puesta), /logistica |
| A | comprar-directo-de-fabrica-en-china | comprar directo de fábrica en China | sin intermediarios, fábrica vs revendedor, cómo saber si es fábrica | Comercial-informativa | errores-y-consejos | /marketplace, /validacion, /clase |
| E | como-pagar-a-un-proveedor-en-china | cómo pagar a un proveedor en China | pagar seguro a China, es seguro pagarle a un chino, Alipay, transferencia | Informativa | errores-y-consejos | /validacion, /logistica |
| D | aranceles-china-mexico-2026 | aranceles a China 2026 | arancel 5% a 50%, productos chinos México, fracción arancelaria | Informativa (noticia evergreen) | como-importar | nota C, /logistica |
| H | envio-aereo-o-maritimo-desde-china | envío aéreo o marítimo desde China | cuánto tarda, consolidado, por kilo o metro cúbico | Informativa | como-importar | /logistica, nota C |
| F | que-es-yiwu | Yiwu | mercado de Yiwu, comprar en Yiwu, Yiwu China mayoreo | Informativa | como-importar | /clase, /escuela |
| I | joyeria-de-acero-inoxidable | joyería de acero inoxidable | se pone negra, 304 vs 316L, acero vs chapa de oro vs plata | Informativa | joyeria | /joyeria, nota importar-joyeria-de-china-para-vender |
| J | feria-de-canton | Feria de Cantón | fechas, cómo ir, qué esperar | Informativa | como-importar | /asesoria-china, /clase |
| G | errores-que-me-costaron-dinero-importando | errores al importar de China | historias de Eduardo, qué no hacer | Informativa / marca | historias-de-eduardo | nota A, nota E, /clase |

Notas específicas por nota:
- B: datos SOLO de fuentes oficiales (SAT, ANAM, VUCEM, DOF) con fecha de consulta visible. No inventes montos ni plazos. Explica en una línea qué es pedimento, encargo conferido y NOM.
- C: tabla de costos con un ejemplo armado con datos reales del catálogo de /productos (marcar qué es real y qué es hipotético). Cuando se publique, la sección de costos de la pilar se resume y enlaza aquí (no repetir el mismo texto en las dos).
- A: explica la diferencia fábrica / trading / revendedor con señales concretas. "Directo de fábrica" no significa "sin controles": aquí entra /validacion de forma natural.
- D: base: DOF 29/12/2025 (1,463 fracciones, 5% a 50% para países sin tratado). Verifícalo en dof.gob.mx y pon la liga. Marca la nota para revisión mensual.
- F: Eduardo como fuente primaria (lo que vio caminando el mercado). NO nombres a Grace, Wilhem ni Vincent ni a ningún proveedor; nada de WeChat.
- I: siembra de joyería de frente pero informativa; el CTA va a /joyeria (no directo a info.joyeria.shop desde el cuerpo).
- J: fechas solo de la web oficial (cantonfair.org.cn) con fecha de consulta. Publicarla con 2–3 meses de anticipación a la siguiente edición.
- G: depende de las historias reales de Eduardo (pendiente del handoff). Si no han llegado, NO la publiques: deja el borrador con [PENDIENTE: …] y sigue con las demás.

REGLAS NUEVAS O ACTUALIZADAS (además de las del handoff)
- Clase en vivo: 21 de noviembre de 2026, 11:00 am (hora del centro de México). En las notas NO pongas la fecha: di "la clase en vivo con Eduardo" para que la nota no caduque. La fecha solo vive en /clase.
- /cotizador está en construcción: NO lo enlaces. Para envíos fuera de México usa /logistica#cotizar.
- /proveedores no se enlaza nunca (es el regalo de la clase).
- Nombres de proveedores: AEMAI y Port Tide solo si hace falta y como lo muestra /marketplace. Los 3 de Yiwu nunca.
- Si el agente SEO publica /curso-para-importar-de-china, la nota cursos-para-importar-de-china debe enlazar ahí y enfocarse en "comparativa / mejores cursos" (no en "inscríbete"). Hasta entonces, sigue enlazando a /clase.
- Años de experiencia: siempre "26+ años".
- Google ya no muestra FAQ enriquecidos para NADIE desde el 7 de mayo de 2026 (el handoff dice "solo gobierno y salud": está desactualizado). Seguimos poniendo el FAQ en `faq` porque lo leen las IAs. HowTo solo si la nota es de pasos.
- Respuesta rápida (40–60 palabras) en las primeras líneas, H2 escritos como las preguntas que busca la gente, tablas para pasos y costos, "Actualizado: <mes> 2026" visible.
- Nada de testimonios, reseñas, clientes, cifras o precios de fábrica inventados. Si falta un dato: [PENDIENTE: …] y lo enlistas al final.

AL PUBLICAR CADA NOTA
1. Agrega el enlace desde la pilar (y desde las notas relacionadas existentes) hacia la nota nueva.
2. Envía la URL por IndexNow (llave en /0548ff40ad255644b9c19950f3efce17.txt).
3. Pide indexación en Search Console.
4. Actualiza blog/ENTREGA.md con la fila de la nota (slug, keyword, title, meta, palabras, fecha).

ENTREGABLE
Por nota: el .md, las 4 imágenes (portada 1200×630, 2 infografías 1200×675, redes 1080×1080), el SQL, y la lista de [PENDIENTE]. Pide confirmación antes de cambiar cada nota a 'published' y antes de cualquier deploy.
```

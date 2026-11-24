# Fase 2 — Página de Eduardo y pedido al agente del blog

## A. /autor/eduardo-hernandez (enriquecer, sin cambiar la URL)

Es la base de E-E-A-T de todo el sitio: Google y las IAs la usan para entender quién habla. Hoy tiene bio, 4 datos y las redes de la marca.

**Se agrega ahora (con datos que ya están confirmados en el sitio):**
- **H2 "Mis negocios":** tarjetas cortas para JAICO (joyería de mayoreo → /joyeria), Xijiao Shops (venta B2B de joyería fabricada en China) y Xijiao LOG (logística desde China → /logistica).
- **H2 "Aprende conmigo":** 3 tarjetas: clase en vivo (→ /clase), curso para importar de China (→ /curso-para-importar-de-china) y Escuela (→ /escuela).
- **sameAs del schema Person:** agregar https://eduardohdz.com (su sitio personal, ya enlazado desde /joyeria).
- **Schema Person:** `founder` como lista de Organization (JAICO, Xijiao Shops, Xijiao LOG). Además, `alumniOf` solo si Eduardo lo confirma; si no, no se pone.

**Pendiente de Eduardo (no se inventa; no se publica hasta tenerlo):**
- [PENDIENTE: perfiles personales de Eduardo (Instagram, LinkedIn, YouTube, TikTok o Facebook personales) para `sameAs`.]
- [PENDIENTE: 2–4 fotos reales: en fábrica, en Yiwu o Guangzhou, con su equipo (sin mostrar nombres ni contactos).]
- [PENDIENTE: qué es el movimiento NADIE, en sus palabras (2–3 líneas).]
- [PENDIENTE: las historias de cómo empezó y de las 2 bancarrotas (también las pide la nota del blog).]

## B. Pedido al agente del blog (no lo hace el agente SEO)

El agente del blog es dueño de la tabla `posts`. Estos cambios le tocan a él:

1. **Nota pilar `como-importar-de-china-a-mexico` → guía principal:**
   - Agregar al inicio un H2 "¿Cómo comprar en China?" con respuesta corta (proceso de compra), para que la pilar también cubra esa búsqueda.
   - Agregar el enlace a /curso-para-importar-de-china en la sección "Tú eliges: hazlo solo o con ayuda".
   - Agregar el enlace a /preguntas-frecuentes al final.
   - Cuando se publiquen las notas B (requisitos), C (costos), E (pagos) y H (aéreo vs marítimo), resumir esas secciones en la pilar y enlazar a cada nota (no repetir el texto).
2. **Nota `cursos-para-importar-de-china`:** ya existe /curso-para-importar-de-china. Cambiar los CTA de "inscríbete" para que lleven ahí y dejar la nota enfocada en "comparativa / mejores cursos".
3. **Nota `eduardo-hernandez-importaciones-china`:** quitar el nombre del inicio del title para que no compita con la página de autor. Propuesta: "26 años importando de China y 2 bancarrotas: lo que aprendí" (54).

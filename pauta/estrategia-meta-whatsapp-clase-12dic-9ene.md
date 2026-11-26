# Pauta Meta + WhatsApp · Clase en vivo $990 · 12 dic 2026 y 9 ene 2027

Respuesta al brief [`prompt-estrategia-meta.md`](prompt-estrategia-meta.md) (versión del 26 nov 2026). Preparado el 26 nov 2026.

> **Supuestos que hay que confirmar** (marcados con ⚠️ en todo el documento):
> 1. La clase es a las **11:00 am CDMX**, igual que la del 21 nov.
> 2. **Cupo:** no hay número de lugares en el brief. Mientras no exista un cupo real, los textos dicen "lugares limitados" solo si es verdad. Si no lo es, se quita y se usa la fecha como urgencia.
> 3. El **Pixel dispara `Purchase`** en la página de gracias después de Stripe. Si hoy no lo hace, es lo primero que hay que arreglar (ver sección 8).

---

## 1. Resumen ejecutivo

1. **$300 al día no le alcanza a Meta para "salir de aprendizaje" optimizando por compra** (necesita ~50 compras por semana por conjunto, o sea más de $12,000 a la semana). Aun así **optimizamos por compra en el conjunto caliente** porque su gente ya compra, y en los fríos por **compra si el Pixel/CAPI ya registra compras bien; si no, por "inicio de pago"** (`InitiateCheckout`). Mensajes de WhatsApp como objetivo, **no**: el cuello de botella real es la confianza y el precio, no la conversación (WA-01: 11 "quiero" y 2 llegaron al pago).
2. **Una sola campaña de Ventas con presupuesto por conjunto (ABO)**, 3 conjuntos de 4 anuncios. Con Andromeda lo "correcto" sería 1 campaña con 1 conjunto amplio y los 12 anuncios dentro, pero con este dinero ABO es la única forma de que cada audiencia reciba gasto y podamos leer algo.
3. **12 dic = WhatsApp + orgánico + solo conjunto 3 (caliente) a $200/día.** Es la apuesta más barata y más probable: WA-01 vendió 1 de cada 25 en checkout abandonado por $72 MXN.
4. **9 ene = la pauta completa**: los 3 conjuntos del 14 al 22 dic ($300), bajos en fiestas ($150), y empuje del 2 al 8 ene ($300 → $500 en escalones de ~25 %).
5. **Costo por venta objetivo: ≤ $450 MXN. Máximo: $900** (equilibrio contra los ~$945 netos de la clase). Solo pagaríamos más si el cruce Stripe ↔ cajas demuestra que los alumnos compran después (hoy ese dato no existe).
6. **WhatsApp:** volver a tocar A (abandonó el pago) con ángulo de **confianza**, B y C con ángulo nuevo, y probar la base fría D en lotes de 250 (los más recientes primero) con una prueba de 2 lotes antes de seguir.
7. Gasto estimado total: **~$9,300 MXN en Meta + ~$3,500 MXN en WhatsApp** para las dos clases. Expectativa honesta: **15–25 clases vendidas** entre ambas (estimación, no promesa).

---

## 2. Hallazgos de la investigación

**Cómo leer esta tabla:** **Dato** quiere decir que Meta lo documenta o hay una prueba publicada. **Práctica** es la regla que usan los media buyers, sin respaldo oficial. **Opinión** es mi criterio.

### 2.1 Qué funciona hoy

| Tema | Qué funciona y por qué | Tipo | Fuente |
|---|---|---|---|
| Andromeda | El sistema de entrega elige primero **qué anuncio** mostrar y a quién; el creativo hace el trabajo que antes hacía la segmentación. Anuncios casi iguales se tratan como uno solo y compiten entre sí. | Dato (Meta lo anunció) + práctica | [Jon Loomer: Andromeda](https://www.jonloomer.com/meta-andromeda/), [Loomer: diversificación creativa](https://www.jonloomer.com/meta-andromeda-creative-diversification/), [AdExchanger](https://www.adexchanger.com/data-driven-thinking/what-metas-andromeda-update-actually-changes-and-what-it-doesnt/) |
| Cuántos anuncios por conjunto | Meta quitó la recomendación de máximo 6. Con presupuesto chico, **3–5 creativos realmente distintos** bastan; meter "relleno" no ayuda. Nuestros 4 por conjunto están bien. | Práctica | [Loomer: How many ads is too many](https://www.jonloomer.com/qvt/how-many-ads-is-too-many/), [Common Thread](https://commonthreadco.com/blogs/coachs-corner/meta-andromeda-roas-creative-strategy-2026) |
| Diversidad real | Cambiar formato, persona, escena y mensaje; no solo el color o el titular. | Práctica (lo de "70 % visualmente distinto" **no está comprobado**) | [Hunch](https://www.hunchads.com/blog/meta-andromeda-explained), [Excite Media](https://www.excitemedia.com.au/meta-creative-diversification/) |
| Segmentación amplia / Advantage+ audiencia | En pruebas publicadas rinde igual o mejor que los intereses en volumen y costo. Las sugerencias (intereses, edad) son eso, sugerencias: Meta se sale de ellas. Lo que sí respeta: **país, edad mínima, exclusiones**. | Dato (prueba de Loomer) | [Loomer: Advantage+ vs detallada](https://www.jonloomer.com/test-results-advantage-plus-audience-detailed-targeting-lookalikes/), [Loomer: Advantage+ vs Original](https://www.jonloomer.com/advantage-audience-vs-original-audiences/) |
| Fase de aprendizaje | Se estabiliza con **~50 eventos en 7 días** tras el último cambio importante. Meta reporta que los conjuntos por debajo de eso pagan ~28 % más por compra. | Dato (Meta) | [PPC Land](https://ppc.land/meta-says-ad-sets-under-50-weekly-conversions-cost-28-more-per-purchase/), [Lebesgue](https://lebesgue.io/blog/facebook-ads-learning-phase/) |
| Presupuesto chico | Si no alcanzas 50 eventos, consolida (menos conjuntos) u optimiza por un evento más arriba del embudo. | Práctica | [Loomer: When your budget is too small](https://pubcast.jonloomer.com/when-your-budget-is-just-too-small/), [Podvector](https://podvector.ai/articles/ads/scaling-and-diagnosis/meta-ads-cbo-vs-abo-for-small-budget-testing) |
| ABO vs Advantage+ presupuesto (CBO) | Para **probar** con poco dinero: ABO (cada conjunto recibe lo que le asignas). CBO concentra todo en lo que convierte más barato y deja sin gasto al resto. Gana CBO cuando ya sabes qué funciona. | Práctica | [Segwise](https://segwise.ai/blog/abo-cbo-meta-ads-budget-strategies), [Webtonic](https://www.webtonic.io/blog/cbo-vs-abo-which-to-use) |
| Objetivo | Ventas con evento de compra cuando hay volumen; si no, el evento previo. Optimizar por mensajes trae gente que platica, no que compra. | Práctica + opinión | ídem |

### 2.2 Qué ya no funciona (o funciona peor)

| Creencia | Veredicto | Fuente |
|---|---|---|
| Microsegmentar por intereses (un conjunto por interés) | **Comprobado que rinde peor o igual**: con Advantage detallada encendida a la fuerza (en objetivos de conversión Meta la activa sola), los intereses casi no cambian a quién le llega. | [Loomer](https://www.jonloomer.com/5-meta-ads-tests-targeting/), [Linear](https://lineardesign.com/blog/metas-advantage-audience/) |
| Excluir mucho | Las exclusiones por **audiencia personalizada** (compradores, gente caliente) sí sirven y Meta las respeta. Excluir intereses: dudoso. Que Meta "quitó las exclusiones de intereses" viene de **una sola fuente**, sin confirmar. | [Loomer](https://www.jonloomer.com/advantage-audience-vs-original-audiences/), [PPC Land](https://ppc.land/advantage/) |
| "Subir más de 20 % reinicia el aprendizaje" | **Mito a medias.** Meta no da un porcentaje. Sus ejemplos: de $100 a $101 no reinicia, de $100 a $1,000 probablemente sí. El 20 % es una regla de dedo. | [Loomer: updates to budgeting](https://www.jonloomer.com/updates-to-meta-ads-budgeting/), [Thread Transfer](https://thread-transfer.pages.dev/blog/2025-05-19-edits-that-reset-learning) |
| Tocar presupuestos a diario | Comprobado que estorba (cada cambio grande cuenta como edición). | ídem |
| Creativos "de agencia" muy pulidos | **Opinión mayoritaria, no dato duro**: en Reels gana lo que parece contenido nativo (cara a cámara, UGC). Para nosotros el dato propio pesa más: los reels de Eduardo a cámara ya venden. | [Triple Whale](https://www.triplewhale.com/blog/creative-targeting-ai-driven-delivery.md) |
| Hay que salir de aprendizaje sí o sí | **Mito.** Muchas cuentas chicas venden en "aprendizaje limitado". | [Hightouch](https://hightouch.com/es/blog/the-learning-phase) |

### 2.3 Formatos y ganchos (educación e infoproducto, México)

| Formato | Para nosotros | Tipo |
|---|---|---|
| Fundador a cámara ("talking head") con subtítulos | **El principal.** Es lo que ya vendió (videos #1–#4). | Dato propio |
| Demostración / unboxing de producto | Respaldo fuerte para el conjunto 2 (video #4 consola, #5 walkie-talkies). | Dato propio |
| Prueba social real | Solo la que existe: comentarios reales de los posts, años de experiencia. **No hay testimonios grabados → no se inventan.** | Regla del brief |
| Comparativa de precio | Funciona para quien ya revende (C2). Solo con precios del brief: bocina $31/pieza, consola G28 $748 puesta en México. | Opinión |
| Estático vs. Reels | Los estáticos rinden menos en Reels/Stories. Mitigación: versión 9:16 de cada estático y, si se puede, **exportarla como MP4 animado de 5–7 s** (ya tenemos el script de MP4 para los diseños). | Práctica |
| Carrusel | No para esta prueba (solo 4 anuncios por conjunto). | Opinión |

Referencia de video: **hook rate** = reproducciones de 3 s ÷ impresiones. Promedio en anuncios de venta en Meta ~25 %, bueno 30 %+, élite 40 %+. **Hold rate** (ThruPlay ÷ 3 s): 40–50 % es normal. Son benchmarks de proveedores; vale más nuestra propia línea base. Fuentes: [Topgrowth](https://topgrowthmarketing.com/?p=48825), [Motion](https://motionapp.com/blog/key-creative-performance-metrics), [Billo](https://billo.app/blog/hook-rate-to-hold-rate).

### 2.4 Medición

| Tema | Qué hacer | Fuente |
|---|---|---|
| Eventos web | `PageView`, `ViewContent` (/clase), `InitiateCheckout` (clic a Stripe), `Purchase` (página de gracias) con valor 990 MXN. **Pixel + CAPI** con el mismo `event_id` para no contar doble. | [Meta CAPI](https://developers.facebook.com/docs/marketing-api/conversions-api) |
| Ventas fuera del sitio (WhatsApp, transferencia) | CAPI acepta eventos offline/CRM y de mensajería (`action_source = business_messaging`, `messaging_channel = whatsapp`) con el `ctwa_clid` del clic, ventana de 7 días. **Ojo:** en plantillas de marketing el clic no conserva ese ID. | [CAPI para mensajería](https://developers.facebook.com/docs/marketing-api/conversions-api/business-messaging), [WhatsApp: medir conversiones](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/measure-conversion/) |
| Métricas por etapa | CPM → hook rate → CTR de enlace → costo por visita a /clase → costo por inicio de pago → costo por compra → ROAS. | Práctica |
| Benchmarks México | **No encontré un benchmark público confiable de Meta solo para México** (eMarketer lo tiene, de pago). La mediana de Latinoamérica (Emplifi, sept 2026) da CPM ~USD 0.80 y CTR ~1.1 %, pero mezcla industrias. Los rangos de la sección 5 son **mi referencia de práctica**, no dato oficial. | [Emplifi](https://emplifi.io/resources/q3-2026-fmcg-food-latin-america-benchmarks/), [eMarketer](https://www.emarketer.com/chart/c/360855/industry-kpis-mexico-social-ad-cpm-by-platform-q4-2025-360855) |
| Políticas | Prohibido prometer ingresos rápidos con poca inversión o poco trabajo ("hazte rico"). Prohibido **afirmar atributos personales** del que ve el anuncio ("¿Estás endeudado?", "¿No tienes dinero?"). | [Meta: resultados irreales](https://transparency.meta.com/policies/ad-standards/deceptive-content/unrealistic-outcomes), [Meta: atributos personales](https://transparency.meta.com/policies/ad-standards/objectionable-content/personal-attributes) |

---

## 3. Estructura de cuenta

### 3.1 Respuestas directas

- **¿Alcanza $300/día para que Meta aprenda?** No en el sentido estricto (50 compras por semana). Con un costo por compra de $300–600, $100 al día por conjunto da **1–2 compras por semana por conjunto**: verás "aprendizaje limitado" todo el tiempo. Eso no impide vender, pero las decisiones se toman con **pocas ventas** y apoyadas en métricas previas (CTR, inicio de pago).
- **¿Qué evento?**
  - **Conjunto 3 (caliente): `Purchase`.** Es gente que ya conoce a Eduardo; aquí el evento final sí se da.
  - **Conjuntos 1 y 2 (fríos):** `Purchase` **si** al 10 dic el Pixel/CAPI muestra ≥ 10 compras en los últimos 28 días (las orgánicas también cuentan si el Pixel las registró). Si no, `InitiateCheckout`, que ocurre ~3–5 veces más que la compra, así que Meta junta más señal. **No se cambia el evento a media campaña**: se decide el 13 dic y se queda.
  - **Mensajes de WhatsApp: no.** Las conversaciones son baratas pero de baja intención. WA-01 lo mostró: 11 "quiero", 2 al pago, 1 venta. Además alguien tiene que cerrar a mano en fiestas.
- **¿Campaña (Advantage+) o conjunto?** **Por conjunto (ABO).** Con Advantage+ de presupuesto, Meta mandaría casi todo al caliente (convierte más barato) y los fríos no recibirían gasto, así que no aprenderíamos nada de ellos. Para la siguiente ronda (feb), cuando sepamos qué gana: pasar a **una campaña Advantage+ de ventas** con los ganadores.
- **¿3 conjuntos o Advantage+ con creativos por ángulo?** Con Andromeda, lo técnicamente superior es **1 campaña Advantage+ de ventas, 1 conjunto amplio, 8–12 anuncios de ángulos distintos** (el creativo encuentra a la audiencia). Pero con 3 conjuntos sí se puede leer qué audiencia y qué ángulo responden, así que diseño la versión de 3 conjuntos que piden. Aclaración honesta: **C1 y C2 se van a encimar mucho** (ambos son México amplio con sugerencias distintas). En la práctica, la diferencia entre ellos la hace el **creativo**, no la audiencia.

### 3.2 Tabla de estructura

| Nivel | Configuración |
|---|---|
| **Campaña** (1) | `CLASE | Ventas | Web | 2026-12` · Objetivo **Ventas** · Ubicación de conversión: **sitio web** · Presupuesto **por conjunto** · Sin Advantage+ de campaña · Atribución 7 días clic / 1 día vista (por defecto) |
| **C3 · Caliente** | Evento `Purchase`. **Incluye:** interacción con la página de FB 365 d, interacción con IG 365 d, vio 50 %+ de cualquier video 365 d, visitas al sitio 180 d, quien le escribió a la página por Messenger/IG/WhatsApp 365 d, **lista de clientes con los 5,988 teléfonos de WhatsApp de ManyChat** (subirla como audiencia personalizada) y visitantes de /clase 90 d. **Excluye:** compradores de la clase (Purchase 180 d + lista de Stripe), `excluir_equipo`. Audiencia personalizada sin Advantage+ (en caliente queremos que se quede en caliente). Edad 21–65. |
| **C1 · Frío "quiero empezar"** | Evento según la regla de 3.1. **Advantage+ audiencia** con sugerencias: emprendimiento, negocio propio, importación, Alibaba, AliExpress, venta por catálogo. Control de **edad mínima 25**. **Excluye:** toda la audiencia C3 + compradores. |
| **C2 · Frío "ya vendo"** | Igual que C1, con sugerencias: pequeña empresa / dueños de negocio, Mercado Libre, Marketplace, TikTok Shop, mayoreo, comercio al por menor. Edad mínima 25. **Excluye:** C3 + compradores. |
| **País** | **Solo México.** Centroamérica: hoy no (pago en MXN por Stripe, horario CDMX, presupuesto chico; se atiende orgánico). EE. UU. hispano: no (CPM varias veces más caro). |
| **Ubicaciones** | Advantage+ ubicaciones **sin Audience Network** (clics de baja calidad; opinión). Personalización por ubicación: 4:5 en feeds y 9:16 en Stories/Reels. |
| **Idioma** | Sin restricción (en México no hace falta). |
| **Nombres** | Conjunto: `C1-empezar`, `C2-yavendo`, `C3-caliente`. Anuncio: `C3-V1-12d`, `C3-E3A-12d`, `C1-E1B-9e`… (V = video, E = estático). |

### 3.3 Presupuesto por etapa (MXN al día)

| Periodo | C1 | C2 | C3 | Total/día | Días | Subtotal |
|---|---:|---:|---:|---:|---:|---:|
| Lanzamiento (2–4 dic) → vie 11 dic | — | — | 200 | 200 | ~8 | ~$1,600 |
| Sáb 12 dic hasta las 10:30 am ⚠️ | — | — | 200 | 200 | 0.5 | $100 |
| Dom 13 dic | apagado | | | 0 | 1 | 0 |
| 14–22 dic | 100 | 100 | 100 | 300 | 9 | $2,700 |
| 23 dic – 1 ene | 40 | 40 | 70 | 150 | 10 | $1,500 |
| 2–3 ene | 100 | 100 | 100 | 300 | 2 | $600 |
| 4–5 ene (si va bien) | ganador +25 % | | | ~375 | 2 | $750 |
| 6–8 ene (si va bien) | ganador +25 % y C3 +25 % | | | ~450–500 | 3 | ~$1,450 |
| Sáb 9 ene hasta las 10:30 am | igual | | | ~450 | 0.5 | ~$225 |
| **Total** | | | | | | **~$8,900–9,300** |

En fiestas el caliente queda más alto porque es el que convierte cuando la gente compra poco. Los fríos siguen prendidos para no perder lo aprendido.

---

## 4. Los 12 anuncios

**Destino de todos:** `https://compraenfabricas.com/clase` + UTM. **No a WhatsApp**: la compra es en Stripe y el chat agrega fricción. Quien tenga dudas escribe desde la página o comentando.

**UTM** (igual en todos, cambia `utm_campaign` y `utm_content`):

```
?utm_source=meta&utm_medium=paid&utm_campaign=clase12d&utm_content=C3-V1&utm_term={{adset.name}}&utm_id={{ad.id}}
```

`utm_campaign` = `clase12d` o `clase9e`. `utm_content` = nombre corto del anuncio. Ese par es el **`campana_id`** del panel.

**Palabra para comentarios** (ManyChat, disparador por comentario en los posts de anuncio, pone etiqueta y manda el link con UTM al DM): C1 = **EMPEZAR** (`ads_c1`), C2 = **DIRECTO** (`ads_c2`), C3 = **CLASE** (`ads_c3`). No se pide en el copy (el CTA es el botón), pero la gente comenta igual; así no se pierde la atribución.

**Reglas comunes de los videos:**
- Subtítulos quemados, grandes, en la mitad de abajo (zona segura de Reels: dejar libre ~15 % arriba y ~25 % abajo).
- Quitar todo lo que diga "comenta CHINA/CLASE" y cualquier fecha vieja.
- **Tarjeta final de 3–4 s** (pieza gráfica F-V): "Clase en vivo con Eduardo · sábado 12 dic · 11 am ⚠️ · Toca el botón". La fecha va **solo en la tarjeta y en un letrero en pantalla**, nunca en la voz, para que la versión de enero sea cambiar la tarjeta.
- Letrero fijo arriba desde el segundo 3: "Clase en vivo · $990 · sáb 12 dic".
- **Publicación original o anuncio nuevo:** anuncio nuevo, porque hay que editarlo (fecha y CTA) y eso no se puede hacer sobre el post original. Para no perder prueba social: subir el video editado **una sola vez** como publicación de la página (sin publicar / "dark post") y **usar el mismo ID de publicación** en todos los anuncios de esa fecha, para que likes y comentarios se junten en un solo post. Alguien del equipo contesta a mano los comentarios de duda ("¿es verdad?").
- Botón: **Registrarte**.

### Conjunto 1 · "Quiero emprender y no sé por dónde empezar" (frío) · arranca 14 dic, solo clase 9 ene

**Video C1-V1 · reel #2 "Si mañana tuviera que empezar de cero…"**

| Campo | Contenido |
|---|---|
| Por qué | Su ángulo es exactamente el de la audiencia (por dónde empiezo) y trae historia (empezó con dinero prestado). 226 comentarios de intención en IG con solo 37 mil vistas: es el que mejor convierte vistas en intención después del #1. **Asignación correcta.** |
| Gancho 0–3 s | Se deja la frase "Si mañana tuviera que empezar de cero comprando en China, haría esto". Texto en pantalla: **"Empezar de cero comprando en China: 5 pasos"**. Si el video tarda más de 1 s en arrancar, se recorta el silencio inicial. |
| Edición | Mantener los 5 pasos (son la promesa). Cortar la mención directa a "mi negocio de joyería" **solo si suena a pitch**. Como historia está bien y siembra joyería. Tarjeta final con fecha 9 ene. Duración ideal ≤ 60 s. |
| Copy corto | Empezar a comprar en China sin saber por dónde le entras es aventar tu dinero. Eduardo empezó así, con dinero prestado. En la clase en vivo te enseña el camino completo, paso a paso. Sábado 9 de enero. 👉 Toca el botón y aparta tu lugar. |
| Copy largo | ¿Quieres traer mercancía de China pero no sabes ni por dónde empezar? Es normal: hay mil videos sueltos y nadie te dice el orden.<br><br>Eduardo lleva 26 años importando. Empezó con dinero prestado, se cayó dos veces y se volvió a levantar. Hoy enseña lo que le hubiera gustado saber al principio.<br><br>En la clase en vivo aprendes:<br>✔ Cómo encontrar fábrica, no intermediario<br>✔ Cómo pagar sin arriesgar tu dinero<br>✔ Cómo traer tu mercancía a México<br><br>Incluye grabación, plantillas y 5 proveedores de regalo.<br>📅 Sábado 9 de enero · 11 am (CDMX) ⚠️ · $990 MXN<br>Toca el botón y aparta tu lugar. |
| Titular | Clase en vivo: comprar directo en China |
| Descripción | Sábado 9 ene · Incluye grabación |
| Botón | Registrarte |

| | **C1-E1A** | **C1-E1B** | **C1-E1C** |
|---|---|---|---|
| Medidas | 1080×1350 + 1080×1920 | 1080×1350 + 1080×1920 | 1080×1350 + 1080×1920 |
| Dolor | "Creo que necesito mucho dinero o un contenedor completo" | "Trabajo toda la semana, no tengo tiempo para aprender" | "Aprendo solo con videos sueltos y nadie me contesta mis dudas" |
| Texto en imagen | **¿Contenedor completo? No hace falta.** | **Un sábado. Una clase. Y queda grabada.** | **Videos sueltos no contestan preguntas. Eduardo sí.** |
| Visual | Bocina chica en primer plano sobre fondo crema, etiqueta grande "$31 por pieza puesta en México", con "$31" en degradado naranja. Detrás, caja de cartón abierta (no contenedor). | Calendario de escritorio con el sábado 9 marcado con círculo naranja, taza de café, laptop con la cara de Eduardo en pantalla. "Queda grabada" en degradado. | Foto de Eduardo a cámara (banco del design system), globos de chat con preguntas ("¿cómo le pago?", "¿cuánto de envío?") y uno grande naranja que dice "En vivo". |
| Copy corto | Mucha gente no empieza porque cree que necesita un contenedor. La bocina más barata que ha traído Eduardo salió en $31 pesos por pieza puesta en México. En la clase te explica cómo empezar con lo que tienes. Sábado 9 de enero. | Si trabajas toda la semana, no necesitas otro curso de meses. Es una clase en vivo, un sábado, y te queda la grabación para verla las veces que quieras. Sábado 9 de enero. | En YouTube aprendes pedacitos y nadie te contesta. En la clase en vivo le preguntas directo a Eduardo, que lleva 26 años comprando en China. Sábado 9 de enero. |
| Copy largo (PAS) | **P:** "Para importar necesitas un contenedor y mucho dinero." Eso escuchas siempre, y por eso nunca empiezas.<br>**A:** No es así. Hay fábricas que te venden por caja, no por contenedor. Ejemplo real: la bocina más barata que ha traído Eduardo salió en $31 pesos por pieza, ya puesta en México.<br>**S:** En la clase en vivo te enseña cómo encontrar fábrica, pagar seguro y traer tu mercancía sin intermediarios. Incluye grabación, plantillas y 5 proveedores de regalo.<br>📅 Sábado 9 de enero · $990 MXN. Toca el botón. | **P:** Trabajas toda la semana y la idea de "meterle horas a aprender a importar" se queda en idea.<br>**A:** Esta no es una maestría. Es una clase en vivo con alguien que lleva 26 años haciéndolo y que ya se equivocó por ti (dos bancarrotas incluidas).<br>**S:** Un sábado en la mañana, y si no puedes conectarte completo, te queda la grabación con las plantillas y 5 proveedores de regalo.<br>📅 Sábado 9 de enero · $990 MXN. Toca el botón. | **P:** Ya viste 20 videos de "cómo importar de China" y sigues con las mismas dudas, porque un video no te contesta.<br>**A:** Eduardo lleva 26 años comprando directo en fábrica y ha asesorado a más de 300 empresas y emprendedores.<br>**S:** En la clase en vivo llevas tus preguntas y te las contesta ahí mismo. Te quedas con la grabación, plantillas y 5 proveedores de regalo.<br>📅 Sábado 9 de enero · $990 MXN. Toca el botón. |
| Titular | Empieza sin contenedor | Un sábado y queda grabada | Pregúntale directo a Eduardo |
| Botón | Registrarte | Registrarte | Registrarte |

### Conjunto 2 · "Ya vendo y le compro caro al intermediario" (frío, intención comercial) · arranca 14 dic, solo clase 9 ene

**Video C2-V1 · reel #4 "Tener el contacto de un proveedor no significa que ya sepas comprar en China"**

| Campo | Contenido |
|---|---|
| Por qué | Le habla a quien ya buscó en Alibaba o ya tiene un contacto: es quien ya vende. Tiene la **mejor tasa de interacción** (3.2 %) y un precio concreto (consola G28, $748 puesta en México). **Riesgo:** es el de menos alcance (14 mil vistas), así que está menos probado para vender. **Asignación correcta, con respaldo #5** (walkie-talkies, "43 cajas"): si a los 7 días el #4 tiene hook rate < 20 % o cero inicios de pago con ≥ $400 gastados, se cambia por el #5. |
| Gancho 0–3 s | Arrancar con **la consola en mano** y el texto "Consola puesta en México: $748". La frase del proveedor va a continuación. Si en el original el unboxing va después, se reordena el corte (el producto engancha más que la frase). |
| Edición | Subtítulos, letrero de fecha y tarjeta final. Sin "comenta". |
| Copy corto | Tener el WhatsApp de un proveedor chino no es saber comprar. Falta lo que más duele: cómo pagarle sin riesgo y cómo traerlo. Eso es lo que Eduardo enseña en la clase en vivo. Sábado 9 de enero. 👉 Toca el botón. |
| Copy largo | Ya encontraste proveedor. ¿Y luego? ¿Cómo sabes que es fábrica y no otro intermediario? ¿Cómo le pagas? ¿Cómo llega a México?<br><br>Eduardo lleva 26 años comprando directo en fábrica para sus propios negocios. En el video ves una consola que salió en $748 puesta en México.<br><br>En la clase en vivo te enseña el proceso completo, de la fábrica a tu negocio. Incluye grabación, plantillas y 5 proveedores de regalo (2 de electrónica y 3 de surtido general de Yiwu).<br>📅 Sábado 9 de enero · 11 am (CDMX) ⚠️ · $990 MXN. Toca el botón. |
| Titular | Ya tienes proveedor. Falta lo demás |
| Botón | Registrarte |

| | **C2-E2A** | **C2-E2B** | **C2-E2C** |
|---|---|---|---|
| Dolor | "El intermediario se queda con mi ganancia" | "La aduana y los impuestos me dan miedo" | "Le compro al mismo mayorista que mi competencia: vendo lo mismo que todos" |
| Texto en imagen | **Cada intermediario se queda con un pedazo de tu ganancia.** | **¿Aduana e impuestos? Se aprende, no se adivina.** | **Si compras donde todos, vendes lo que todos.** |
| Visual | Diagrama simple de cadena: Fábrica → intermediario → intermediario → tu tienda, con cada intermediario en gris y una flecha naranja directa "Fábrica → tú". Sin precios inventados. | Caja de cartón con etiqueta de envío, sello de "revisado", tipografía grande. "Se aprende" en degradado naranja. | Dos repisas: la de la izquierda gris, con el mismo producto repetido; la de la derecha con lentes con IA, smartwatch y dron, resaltada con el degradado. Rótulo: "tecnología que todavía no llega a México". |
| Copy corto | Si le compras al que le compró al que le compró a la fábrica, cada uno se quedó con su parte, y esa parte salió de tu ganancia. En la clase en vivo Eduardo te enseña a comprar directo. Sábado 9 de enero. | La aduana asusta porque nadie te la explica. En la clase en vivo Eduardo te enseña cómo traer tu mercancía a México sin sorpresas. Sábado 9 de enero. | Si tu surtido es el mismo que el del puesto de al lado, solo te queda competir por precio. En la clase aprendes a comprar directo, incluida tecnología que todavía no llega a México. Sábado 9 de enero. |
| Copy largo (PAS) | **P:** Tu margen se va entre el mayorista, el distribuidor y el revendedor. Tú pones la tienda y ellos se llevan la ganancia.<br>**A:** Eduardo lleva 26 años comprando directo en fábrica para sus 5 negocios. El enemigo no es tu proveedor: es el sistema de intermediarios.<br>**S:** En la clase en vivo aprendes a encontrar fábrica, pagar seguro y traer tu mercancía. Grabación, plantillas y 5 proveedores de regalo.<br>📅 Sábado 9 de enero · $990 MXN. Toca el botón. | **P:** Te imaginas tu mercancía detenida en aduana, o pagando impuestos que no esperabas, y mejor sigues comprándole al de siempre.<br>**A:** Eduardo lleva 26 años trayendo mercancía de China. Ya pasó por los errores (dos bancarrotas incluidas) para que tú no tengas que repetirlos.<br>**S:** En la clase en vivo te explica el proceso para traer tu mercancía a México, con plantillas y grabación para que lo repases.<br>📅 Sábado 9 de enero · $990 MXN. Toca el botón. | **P:** Compras donde compran todos, vendes lo mismo que todos y terminas bajando tu precio para vender.<br>**A:** Comprando directo en fábrica puedes traer cosas que todavía no llegan a México: lentes con IA, relojes, consolas, drones.<br>**S:** En la clase en vivo Eduardo te enseña cómo encontrar esas fábricas y comprarles seguro. Incluye 5 proveedores de regalo (2 de electrónica).<br>📅 Sábado 9 de enero · $990 MXN. Toca el botón. |
| Titular | Compra directo de fábrica | Trae tu mercancía sin sorpresas | Vende lo que nadie tiene |
| Botón | Registrarte | Registrarte | Registrarte |

> E2B no debe prometer "sin pagar impuestos" ni "brincarte la aduana". Se habla de **aprender el proceso**. Eso además protege ante las políticas de Meta.

### Conjunto 3 · "Ya me conoce" (caliente) · 12 dic **y** 9 ene

**Video C3-V1 · reel #1 "Comprar en China no tiene por qué ser una apuesta"**

| Campo | Contenido |
|---|---|
| Por qué | Es el que más vendió (coincide con la mejor semana: 7 clases del 2 al 8 oct) y ataca el miedo número uno. Para gente que ya conoce a Eduardo es el empujón de confianza. **Asignación correcta.** |
| Respaldo | #3 ("¿tienes miedo de que te estafen?"). **No correrlos al mismo tiempo**: es el mismo ángulo y Andromeda los trataría como uno. El #3 entra **solo como reemplazo** cuando el #1 se fatigue (frecuencia 7 d > 3.5 y CTR 30 % abajo de su primera semana), o en enero para refrescar. |
| Gancho 0–3 s | Se deja "Comprar en China no tiene por qué ser una apuesta". Texto en pantalla: **"Las 3 cosas que reviso antes de pagarle a un proveedor"**. Es una promesa concreta y retiene más. |
| Edición | La historia del dinero prestado se queda (es la conexión). Los 3 puntos se quedan. Tarjeta final con fecha. **Versión 12 dic:** letrero "Este sábado 12 dic". **Versión 9 ene:** "Sábado 9 de enero". |
| Copy corto (12 dic) | Hace 26 años Eduardo le mandó dinero prestado a un proveedor que no conocía. Hoy revisa 3 cosas antes de pagar, y en la clase en vivo te enseña el proceso completo. **Este sábado 12 de diciembre.** 👉 Toca el botón. |
| Copy largo | Comprar en China da miedo por una razón: mandar tu dinero a alguien que no conoces.<br><br>Eduardo lo vivió. Hace 26 años mandó dinero prestado a un proveedor que no conocía. Desde entonces ha importado para 5 negocios propios y ha asesorado a más de 300 empresas y emprendedores.<br><br>En la clase en vivo te enseña cómo encontrar fábrica, cómo pagar sin arriesgar tu dinero y cómo traer tu mercancía a México.<br>Incluye grabación, plantillas y 5 proveedores de regalo.<br>📅 Sábado 12 de diciembre · 11 am (CDMX) ⚠️ · $990 MXN. Toca el botón. |
| Titular | Que comprar en China no sea apuesta |
| Botón | Registrarte |

| | **C3-E3A** | **C3-E3B** | **C3-E3C** |
|---|---|---|---|
| Dolor | "¿Esto es verdad? ¿Quién es este señor?" (confianza en Eduardo; fue la única duda escrita en WA-01) | "Lo dejo para después" (fecha) | "¿Qué me llevo por $990?" (valor) |
| Texto en imagen | **26 años importando. 2 bancarrotas. Sigue aquí.** | **Este sábado 12 dic. La próxima es hasta enero.** (12 dic) / **Sábado 9 de enero. Aparta tu lugar.** (9 ene) | **Clase + grabación + plantillas + 5 proveedores** |
| Visual | Foto de Eduardo (retrato serio y cercano), tres datos en tarjetas: 26+ años · 5 negocios propios · 300+ asesorados. "Sigue aquí" en degradado. | Hoja de calendario gigante con la fecha en degradado naranja y la hora debajo. Solo tipografía. Es la más simple y la más directa. | "Caja" abierta (estilo unboxing) de la que salen 4 tarjetas: Clase en vivo, Grabación, Plantillas, 5 proveedores (2 electrónica + 3 Yiwu). Precio $990 en grande. |
| Copy corto | No es un gurú de internet: Eduardo lleva 26 años importando de China, tiene 5 negocios propios y se ha caído dos veces. En la clase en vivo te enseña lo que funciona y lo que no. Sábado 12 de diciembre. | Si llevas tiempo viendo los videos de Eduardo y pensando "luego", la clase es este sábado 12 de diciembre y la siguiente es hasta enero. Toca el botón. | Por $990 te llevas la clase en vivo con Eduardo, la grabación, las plantillas y 5 proveedores de regalo: 2 de electrónica y 3 de surtido general de Yiwu. Sábado 12 de diciembre. |
| Copy largo (PAS) | **P:** Ves muchos "expertos en China" y no sabes a quién creerle.<br>**A:** Eduardo tiene 49 años y lleva más de 26 importando de China. Tiene 5 negocios propios y equipo en China. Pasó por dos bancarrotas y se levantó. No te va a vender humo, porque ya le costó caro aprender.<br>**S:** En la clase en vivo te enseña su proceso para comprar directo de fábrica y le haces tus preguntas ahí mismo. Pago seguro con tarjeta.<br>📅 Sábado 12 de diciembre · $990 MXN. Toca el botón. | **P:** "Lo veo después" es lo que más negocios ha frenado. Pasa diciembre, pasa enero, y sigues comprándole al intermediario.<br>**A:** Eduardo da esta clase en vivo pocas veces. La de diciembre es este sábado.<br>**S:** Te llevas la grabación, plantillas y 5 proveedores de regalo, para que empieces en enero ya con un plan.<br>📅 Sábado 12 de diciembre · $990 MXN. Toca el botón. | **P:** $990 es dinero, y quieres saber qué te llevas antes de pagar.<br>**A:** Esto es lo que incluye: clase en vivo con Eduardo (26 años importando), grabación para repasarla, plantillas para tus primeras compras y 5 proveedores de regalo.<br>**S:** Un solo error comprando a ciegas cuesta más que la clase.<br>📅 Sábado 12 de diciembre · $990 MXN. Toca el botón. |
| Titular | 26 años comprando en China | Este sábado 12 de diciembre | Todo lo que incluye tu lugar |
| Botón | Registrarte | Registrarte | Registrarte |

**Versión 9 ene del conjunto 3:** mismos textos cambiando "este sábado 12 de diciembre" por "sábado 9 de enero", y en E3B "la próxima es hasta enero" por "empieza el año con un plan".

### ¿Riesgo con 1 solo video por conjunto?

Sí, moderado: en Reels y Stories los estáticos rinden menos, y si el video se fatiga el conjunto se queda sin formato fuerte. Cómo rotar sin romper la prueba:
1. **Versión 9:16 de cada estático animada como MP4 de 5–7 s** (texto que entra, brillo del degradado). Cuenta como el mismo anuncio (mismo mensaje), no como anuncio nuevo. Recomendado, no obligatorio.
2. **Video de respaldo como reemplazo, no como 5º anuncio:** C2 → #5 si el #4 falla (regla arriba); C3 → #3 cuando el #1 se fatigue. Se pausa uno y se prende el otro **en el mismo conjunto**.
3. **No usar** los videos virales de mercados (sin llamada a la clase, no vendieron).

---

## 5. Plan por etapas (2 dic – 9 ene)

### 5.1 Calendario y decisiones

| Etapa | Fechas | Qué corre | $/día | Qué se mide | Decisión |
|---|---|---|---:|---|---|
| **0. Preparación** | 26 nov – 1 dic | Nada pagado | — | Pixel `Purchase` y `InitiateCheckout` funcionando (probar con una compra real o de prueba), dominio verificado, audiencias C3 creadas, lista de clientes subida | Si `Purchase` no dispara, **no se lanza** hasta arreglarlo |
| **1. Calentamiento 12 dic** | 2–4 dic → 12 dic 10:30 am | C3 (4 anuncios versión 12 dic) + WhatsApp (sección 6) + orgánico "Comenta CLASE" | 200 | Día 3: CPM, CTR de enlace, hook rate. Día 7: inicios de pago y compras | Día 3: apagar un anuncio solo si gastó ≥ $150 con CTR < 0.5 %. Día 7: no se escala (la clase está encima) |
| **Corte 1** | dom 13 dic | Todo apagado | 0 | Cruce de ventas Stripe ↔ UTM ↔ ManyChat. Costo por venta de C3 y por segmento de WhatsApp | Elegir evento de C1/C2 (`Purchase` o `InitiateCheckout`, regla de 3.1). Qué estático de C3 se queda |
| **2. Arranque 9 ene** | 14–22 dic | C1, C2, C3 (versión 9 ene) | 300 | Día 3 (17 dic): CPM, hook, CTR. Día 7 (21 dic): costo por inicio de pago, primeras compras | Apagar anuncios con ≥ $200 gastados y 0 inicios de pago. C2: ¿cambiar #4 por #5? |
| **3. Fiestas** | 23 dic – 1 ene | Los 3, bajos | 150 | Solo se revisa el 28 dic (que no haya gasto raro ni rechazos) | **No tocar** salvo emergencia |
| **4. Empuje** | 2–9 ene 10:30 am | Los 3 | 300 → 500 | Diario: costo por venta acumulado del panel (Meta + WhatsApp) | Escalones abajo |
| **Corte 2** | 10–11 ene | Todo apagado | 0 | Reporte final por anuncio, conjunto y segmento | Ganadores → campaña Advantage+ de febrero |

### 5.2 Regla para subir de $300 a $500

- **Cuándo:** el 4 ene y el 6 ene (no antes; necesitamos 2 días de datos tras volver de fiestas).
- **Condición:** costo por venta de los últimos 3 días en el panel **≤ $450** y **≥ 2 ventas** atribuidas a ese conjunto en el periodo 14 dic – hoy.
- **Escalón:** **+25 % al conjunto ganador** (ej. $100 → $125 → $155), no a todos. Así se llega a ~$450–500 el 6 ene.
- **Si el costo por venta está entre $450 y $900:** se queda en $300.
- **Si pasa de $900 o hay 0 ventas con $1,000 gastados en un conjunto:** ese conjunto baja a $50 o se apaga y su dinero pasa al mejor.
- Sobre "subir de golpe 67 % reinicia el aprendizaje": Meta no da un porcentaje, pero un salto así sí cuenta como edición grande. Con este presupuesto vamos a estar en "aprendizaje limitado" de todos modos, así que el riesgo real es **perder estabilidad en la entrega**, no salir de algo que no alcanzaremos. Por eso se sube por escalones y solo en el ganador.

### 5.3 Métricas objetivo (referencia de práctica para México, no dato oficial)

| Métrica | Frío (C1, C2) | Caliente (C3) | Alarma |
|---|---|---|---|
| CPM | $35–80 MXN (dic hasta ~$110) | $50–120 | > $150 sostenido |
| Hook rate (3 s ÷ impresiones) | ≥ 25 % | ≥ 30 % | < 18 % |
| CTR de enlace | 0.8–1.5 % | 1.5–3 % | < 0.5 % |
| Costo por visita a /clase | $5–15 | $4–10 | > $25 |
| Costo por inicio de pago | $60–150 | $40–100 | > $250 |
| Costo por compra (clase) | $400–900 | $200–500 | > $900 |
| Frecuencia 7 días | < 2.5 | < 3.5 | > 4 |

**Cuándo apagar:** un anuncio con ≥ 1.5× el costo objetivo gastado ($675) sin compra **y** con CTR o hook rate bajo la alarma. Si un anuncio no recibe gasto, no se toca: Meta lo está "descartando" y no cuesta nada.
**Cuándo duplicar:** no se duplica nada en esta prueba (con 3–4 semanas no da tiempo). Se escala por escalones (5.2).
**Cuándo refrescar (fatiga):** frecuencia arriba de la alarma + CTR 30 % abajo de su primera semana → entra el creativo de respaldo.

### 5.4 Cómo pasar lo aprendido de la clase del 12 dic a la del 9 ene

- **C3 se queda como está** (mismo conjunto, así conserva lo aprendido). El 14 dic se crean los 4 anuncios con creativos de enero dentro del mismo conjunto y se pausan los de diciembre. Si en diciembre un estático no tuvo ni inicios de pago con ≥ $200 gastados, en enero se cambia por una variante nueva de su mismo dolor (otro visual), no por otro dolor.
- **El video no cambia entre fechas**: solo la tarjeta final y el letrero.
- **Se agregan a exclusiones** los compradores del 12 dic.
- Lo que aprendamos de WhatsApp en diciembre (qué segmento compró, qué botón tocaron) decide **cuánta base fría D** se manda en enero.

### 5.5 Atribución de cada venta

1. **Stripe:** el link de pago de /clase debe heredar los UTM. Si es Payment Link, Stripe acepta `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` y `client_reference_id` en la URL y los guarda en el pago ⚠️ (confirmar en el panel de Stripe). Si el checkout lo crea el sitio, guardar los UTM en `metadata`.
2. **Panel:** cada venta se registra con `campana_id` = `utm_campaign` + `utm_content` (ej. `clase9e/C2-E2A`). Si llega sin UTM: buscar el teléfono de Stripe en ManyChat y ver su última etiqueta (`ads_c1/c2/c3`, `wa12d_*`, `wa9e_*`). Si no aparece en ningún lado, es **orgánica**. Es el mismo método del cruce de WA-01.
3. **Ventas por WhatsApp o transferencia:** quien entra por un anuncio y escribe queda etiquetado (palabra de comentario o etiqueta del flujo). Al cerrar por transferencia, se registra en el panel con su `campana_id` y, cuando haya CAPI, se manda a Meta como `Purchase` offline.
4. **Ventana:** se da crédito al último toque pagado (anuncio o plantilla) en los **7 días anteriores** a la compra. Si tiene los dos, cuenta para WhatsApp si el clic a la plantilla fue en las últimas 24 h; si no, para Meta.

### 5.6 Punto de equilibrio

| Concepto | Valor |
|---|---|
| Precio | $990 MXN |
| Neto después de Stripe | ~$945 |
| **Equilibrio en la clase sola** | **~$900 por venta** (dejando ~$45 de colchón) |
| **Objetivo** | **≤ $450 por venta** (ROAS ~2.2 en la clase sola) |
| Máximo para seguir pautando | $900 |
| ¿Pagar más por el valor de después (cajas $15,500, Skool, joyería)? | **Hoy no**: no sabemos cuántos alumnos compraron cajas ni con qué margen. Si el cruce muestra, por ejemplo (hipotético), que 1 de cada 10 alumnos compra una caja con $3,000 de utilidad, el valor de cada alumno sube ~$300 y el máximo podría ir a ~$1,200. **Dato que necesitamos.** |
| Expectativa (estimación) | Con ~$9,300 de gasto y costo por venta de $400–700 → **13–23 ventas por Meta**. Más WhatsApp, más orgánico. |

---

## 6. Campaña de WhatsApp (ManyChat)

### 6.1 Reglas generales

- **Límite:** 250 conversaciones iniciadas por la empresa cada 24 h, contadas **por persona**. Todo el calendario respeta ≤ 240 al día (margen para seguimientos con plantilla).
- **Máximo por persona por clase: 2 plantillas** (invitación + 1 recordatorio, este solo a quien mostró interés) **+ mensajes libres** solo si la persona escribió o tocó un botón en las últimas 24 h.
- **Antes de cada envío:** apagar la bienvenida automática (`china-bienvenida-v2`) para quien responda a la campaña. Condición en el disparador: "no tiene etiqueta `wa12d_env` / `wa9e_env`".
- **Recargar el monedero** antes del 7 dic: ~USD 40 para la clase del 12 dic y ~USD 160 antes del 14 dic para la de enero.
- **Respuesta humana:** quien toque "Quiero mi lugar" o "Tengo una duda" recibe respuesta automática en el momento y, **en menos de 2 horas**, un mensaje escrito por alguien del equipo. WA-01 mostró que el freno es la confianza, y eso lo resuelve una persona.
- **Horario de envío:** martes a jueves, 7:30–8:30 pm. Por la noche la gente lee el celular con calma; la venta de WA-01 llegó 12 minutos después del envío. Opinión: probar mediodía en un lote D para comparar.

### 6.2 Segmentos (condiciones exactas)

Exclusiones comunes a **todos** (`EXCL`): tiene `compro_clase_21nov` **o** `compro_clase_12dic` **o** está en la lista de compradores de Stripe (subir como etiqueta `comprador_clase` cruzando a mano) **o** `wa21_no` **o** `excluir_campanas` **o** `excluir_equipo` **o** recibió una plantilla en los últimos 5 días (`ult_campana` < 5 días; crear este campo de fecha).

| Segmento | Incluye | Tamaño aprox. | ¿Se toca otra vez? Ángulo |
|---|---|---:|---|
| **A · Checkout abandonado** | `clic_pago_clase` **o** `wa21_quiere` **y no** `EXCL` | ~31 + nuevos | **Sí.** Es el único que compró. Ángulo nuevo: **confianza + "qué te llevas"**. Ya no "trae cualquier producto". **3 días antes.** |
| **B · Interesados** | `int_clase` **y no** `clic_pago_clase` **y no** `EXCL` | ~70–100 | **Sí**, con ángulo de **confianza** ("¿esto es verdad?": quién es Eduardo, 2 bancarrotas, pago con tarjeta seguro, grabación). |
| **C · Nuevos sin campaña** | WhatsApp activo **y** creado después del 20 nov **y no** `wa21_*` **y no** `EXCL` | ~116 (+ los que lleguen) | Primera vez: presentación + regalo de 5 proveedores. |
| **D · Base fría** | WhatsApp activo **y no** A/B/C **y no** `EXCL`, ordenado por **fecha de alta, más recientes primero** | ~5,600 | Prueba de 2 lotes en diciembre. Si pasa, sigue en enero. |
| **Compradores de cajas (25)** | — | 25 | **Fuera de la campaña masiva.** Son los clientes de más valor y la relación es de cajas. En enero, **mensaje personal** desde la bandeja (no plantilla) solo si Eduardo lo aprueba, con ángulo "para que traigas tu propio surtido". Opinión: riesgo de canibalizar la recompra de cajas; decide Eduardo. |

**Prueba chica de D antes de mandar a todos:** lote D1 (200, los más recientes) el 8 dic. Para seguir con D2 se necesita **las tres cosas:** tasa de lectura ≥ 50 %, la **calificación de calidad del número sigue en verde** en WhatsApp Manager y ≤ 3 respuestas de "no me escriban". Si la calidad baja a amarillo: se detiene D hasta enero y se manda solo A/B/C.

### 6.3 Calendario · clase del sábado 12 dic

| Día | Hora | Segmento | Plantilla | Envíos | Etiqueta |
|---|---|---|---|---:|---|
| Mar 8 dic | 8 pm | C (nuevos) | `clase12d_c_nuevos` | ~116 | `wa12d_env_C` |
| Mar 8 dic | 8 pm | D1 (más recientes) | `clase12d_d_fria` | ~120 | `wa12d_env_D1` |
| Mié 9 dic | 8 pm | A (abandonó) | `clase12d_a_confianza` | ~31 | `wa12d_env_A` |
| Mié 9 dic | 8 pm | B (interesados) | `clase12d_b_verdad` | ~90 | `wa12d_env_B` |
| Mié 9 dic | 8 pm | D2 (si D1 pasó) | `clase12d_d_fria` | ~110 | `wa12d_env_D2` |
| Jue 10 dic | 8 pm | D3 (si D2 pasó) | `clase12d_d_fria` | ~220 | `wa12d_env_D3` |
| Vie 11 dic | 7 pm | Quien tocó "Quiero" o "Duda" y no compró | **Libre** si su último mensaje fue hace < 24 h; si no, plantilla `clase12d_manana` | ~30–60 | `wa12d_recordatorio` |
| Sáb 12 dic | 9 am | Quien ya tiene lugar | **Libre / Stripe**: "Hoy es la clase" (con link de acceso) | — | — |
| Sáb 12 dic | 9 am | Quien tocó "Quiero" el 11 dic | **Libre** (tienen ventana abierta): "Hoy a las 11, aún puedes entrar" | ~10–20 | — |

**Total plantillas 12 dic:** ~690–720.

### 6.4 Calendario · clase del sábado 9 ene

| Día | Segmento | Plantilla | Envíos |
|---|---|---|---:|
| 14–22 dic (lun–vie, 8 pm), ~230/día | D4 en adelante, más recientes primero, **solo si D pasó en diciembre** | `clase9e_d_fria` (ángulo: "empieza el año con un plan") | ~1,600 |
| 23 dic – 1 ene | **Nada** (fiestas; plantillas de marketing en Nochebuena y Año Nuevo queman la base) | — | 0 |
| Sáb 2 ene | C (nuevos desde el 8 dic) + compradores del 12 dic **no** | `clase9e_c_nuevos` | ~100 |
| Dom 3 ene | D (siguiente lote) | `clase9e_d_fria` | ~230 |
| Lun 4 ene | D (siguiente lote) | `clase9e_d_fria` | ~230 |
| Mar 5 ene | D (siguiente lote) | `clase9e_d_fria` | ~230 |
| Mié 6 ene | A + B (todos los que no compraron el 12 dic, incluidos los que tocaron "Quiero" en dic) | `clase9e_a_ultima` / `clase9e_b_aguinaldo` | ~150 |
| Mié 6 ene | Respuestas positivas de D (tocaron "Quiero"/"Duda" en dic) | `clase9e_a_ultima` | ~80 |
| Jue 7 ene | D (último lote del periodo) | `clase9e_d_fria` | ~230 |
| Vie 8 ene | Tocaron "Quiero" en enero y no compraron | Libre (< 24 h) o `clase9e_manana` | ~60–100 |
| Sáb 9 ene | Inscritos / interesados del 8 | Libre: "Hoy es la clase" | — |

**Cobertura:** ~2,700–3,000 de los ~5,600 de D entre las dos clases. Para recorrer toda la base hace falta **verificar la empresa** en Meta (tarea pendiente en el panel): sube el límite diario.

### 6.5 Plantillas (categoría Marketing, español de México)

Formato común: **encabezado con imagen** (pieza F-W) · cuerpo con `{{1}}` = nombre · pie: "Compra en Fábricas de China · Responde SALIR para no recibir más" · **3 botones de respuesta rápida** (sin emojis, ≤ 20 caracteres). ManyChat solo permite 1 link por mensaje, así que el link va en la respuesta de cada botón.

**Botones (iguales en todas):**

| Botón | Respuesta automática | Etiqueta | Link |
|---|---|---|---|
| `Quiero mi lugar` | "¡Va! Aquí apartas tu lugar con tarjeta, pago seguro con Stripe: [LINK]. Si prefieres que alguien del equipo te ayude, contesta este mensaje." + **aviso al equipo** | `wa12d_quiere` / `wa9e_quiere` | `compraenfabricas.com/clase?utm_source=whatsapp&utm_medium=plantilla&utm_campaign=clase12d&utm_content=wa-A` (cambia `wa-A/B/C/D` y `clase9e`) |
| `Tengo una duda` | "Claro, escríbenos tu duda y alguien del equipo te contesta en un rato (no es robot)." + **aviso al equipo** | `wa12d_duda` / `wa9e_duda` | — |
| `Ahora no` | "Sin problema, {{nombre}}. Gracias por avisarnos." | `wa12d_no` / `wa9e_no` (excluye de esa clase) | — |

> Botón "Ya tengo mi lugar" de WA-01: se quita. Casi nadie lo usa y la exclusión de compradores ya la hacemos con Stripe.

**`clase12d_a_confianza` · A, checkout abandonado**
> Hola {{1}}, vimos que estuviste a un paso de apartar tu lugar en la clase de Eduardo.
>
> Si te quedó alguna duda, es normal: es tu dinero. Te contamos lo que incluye:
> - Clase en vivo con Eduardo, 26 años comprando directo en fábricas de China
> - Grabación para repasarla
> - Plantillas y 5 proveedores de regalo
>
> Es este sábado 12 de diciembre a las 11 am (CDMX). Pago seguro con tarjeta. ¿Te apartamos tu lugar?

**`clase12d_b_verdad` · B, interesados**
> Hola {{1}}, hace unos días alguien nos preguntó: "¿cómo sé que esto es verdad?". Buena pregunta.
>
> Eduardo lleva más de 26 años importando de China, tiene 5 negocios propios y ha pasado por 2 bancarrotas. Por eso enseña cómo revisar a un proveedor antes de pagarle.
>
> La clase en vivo es este sábado 12 de diciembre a las 11 am (CDMX). Le haces tus preguntas ahí mismo y te quedas con la grabación. $990 MXN.

**`clase12d_c_nuevos` · C, nuevos**
> Hola {{1}}, gracias por escribirnos. Te queremos invitar a la clase en vivo de Eduardo: cómo comprar directo en fábricas de China, sin intermediarios.
>
> Es el sábado 12 de diciembre a las 11 am (CDMX) e incluye grabación, plantillas y 5 proveedores de regalo (2 de electrónica y 3 de surtido general de Yiwu). $990 MXN.

**`clase12d_d_fria` · D, base fría**
> Hola {{1}}, hace un tiempo nos escribiste sobre comprar en China. Este sábado 12 de diciembre Eduardo da una clase en vivo para aprender a comprar directo de fábrica, pagar seguro y traer tu mercancía a México.
>
> Incluye grabación y 5 proveedores de regalo. $990 MXN. ¿Te interesa?

**`clase12d_manana` / `clase9e_manana` · recordatorio con plantilla (solo si no hay ventana abierta)**
> {{1}}, mañana a las 11 am (CDMX) es la clase en vivo con Eduardo. Si todavía quieres tu lugar, toca el botón y te mandamos el link.

**Enero** (mismo formato y botones):
- `clase9e_d_fria`: "Hola {{1}}, si en 2027 quieres dejar de comprarle al intermediario, el sábado 9 de enero Eduardo da una clase en vivo para aprender a comprar directo de fábrica en China. Incluye grabación y 5 proveedores de regalo. $990 MXN. ¿Te interesa?"
- `clase9e_c_nuevos`: igual que `clase12d_c_nuevos` con la fecha nueva.
- `clase9e_b_aguinaldo`: "Hola {{1}}, empezar el año con un plan sale más barato que empezarlo a ciegas. El sábado 9 de enero Eduardo enseña, en vivo, cómo comprar directo en fábricas de China. Grabación, plantillas y 5 proveedores de regalo. $990 MXN." Ojo: no decir "usa tu aguinaldo" (podría leerse como afirmar algo de su dinero); el nombre interno puede quedarse.
- `clase9e_a_ultima`: "Hola {{1}}, en diciembre te interesó la clase de Eduardo. La próxima es este sábado 9 de enero a las 11 am (CDMX). Incluye grabación, plantillas y 5 proveedores de regalo. ¿Te apartamos tu lugar?"

**Mensajes libres (dentro de la ventana de 24 h):**
- **Seguimiento a quien tocó "Quiero" y no pagó (2–3 h después, lo escribe una persona):** "Hola {{nombre}}, soy del equipo de Eduardo. Vi que te interesó la clase. ¿Te quedó alguna duda sobre el pago o sobre lo que se ve? Te ayudo por aquí."
- **Día anterior (19:00):** "Mañana a las 11 am (CDMX) es la clase. Si quieres tu lugar, aquí está el link: [LINK]. Si ya pagaste, ¡te vemos mañana!"
- **Hoy es la clase (9:00):** "Hoy a las 11 am (CDMX) es la clase en vivo con Eduardo. Si todavía quieres entrar, aquí está el link: [LINK]. Queda grabada."

### 6.6 Costo estimado y ventas esperadas

USD 0.046 por plantilla (~$0.85 MXN). Los mensajes libres casi no cuestan.

| Clase | Segmento | Envíos | Costo USD | Costo MXN | Ventas esperadas (referencia WA-01) |
|---|---|---:|---:|---:|---|
| 12 dic | A | 31 | 1.4 | 26 | **1–2** (WA-01: 1 de 25) |
| 12 dic | B | 90 | 4.1 | 77 | 0–1 (WA-01: 0 de 58) |
| 12 dic | C | 116 | 5.3 | 99 | 0–2 (sin referencia; suponer como B) |
| 12 dic | D1–D3 | 450 | 20.7 | 383 | 0–2 (base fría: puede convertir **mucho menos**) |
| 12 dic | Recordatorios plantilla | ~40 | 1.8 | 34 | incluido arriba |
| **12 dic total** | | **~730** | **~33** | **~620** | **~1–5** |
| 9 ene | D (dic + ene) | ~2,500 | 115 | 2,125 | 2–8 (hipótesis 0.1–0.3 %) |
| 9 ene | A + B + respuestas D | ~230 | 10.6 | 196 | 1–3 |
| 9 ene | C | ~100 | 4.6 | 85 | 0–1 |
| 9 ene | Recordatorios plantilla | ~80 | 3.7 | 68 | incluido |
| **9 ene total** | | **~2,900** | **~134** | **~2,470** | **~3–12** |

Con un costo por venta de WhatsApp de ~$150–600, WhatsApp sigue siendo **el canal más barato por venta**. Por eso es el motor del 12 dic.

### 6.7 Medición

- **Etiquetas por clase:** `wa12d_env_A|B|C|D1|D2|D3`, `wa12d_quiere`, `wa12d_duda`, `wa12d_no`, `wa12d_clic_pago` (clic en el link), `compro_clase_12dic`; lo mismo con `wa9e_`.
- **UTM por plantilla:** `utm_source=whatsapp&utm_medium=plantilla&utm_campaign=clase12d&utm_content=wa-A` (B, C, D1…).
- **Panel:** `campanas` → una fila por clase y canal (`WA-12D`, `WA-9E`). `campana_segmentos` → una por segmento y lote con enviados, entregados, leídos, clics, "quiero" y ventas. `campana_cortes` → cortes a las 24 h, al día de la clase y 2 días después, con el mismo cruce manual Stripe ↔ ManyChat de WA-01.

---

## 7. Fichas de piezas gráficas (para construir como artefactos)

**Marca:** solo naranjas, degradado `#F97316 → #EA580C`, texto `#1A1A1A`, fondo crema `#FFF8F5`, **sin rojos**. Ojo: los diseños de WhatsApp del 21 nov usaban rojo `#DC2626` (`WarmUp5_Rojo`), así que esos no se reutilizan tal cual. Tipografía display del design system. Logo horizontal abajo. Fotos de Eduardo desde `design-system/artefacto/assets/photos/`.

**Variables para que enero sea solo cambiar datos:** `{FECHA_LARGA}` ("sábado 12 de diciembre" / "sábado 9 de enero"), `{FECHA_CORTA}` ("SÁB 12 DIC" / "SÁB 9 ENE"), `{RELATIVO}` ("Este sábado" en dic / "Sábado" en ene), `{HORA}` ("11 am CDMX" ⚠️), `{CUPO}` (vacío salvo que haya cupo real).

**Texto legal mínimo (todas las de Meta):** "Clase en línea en vivo · $990 MXN · Incluye grabación. Los resultados dependen de cada persona."

### 7.1 Meta · estáticos (cada uno en 1080×1350 y 1080×1920)

En 1920 se deja libre el 14 % de arriba y el 20 % de abajo (interfaz de Stories/Reels).

| ID | Uso | Titular | Subtítulo | Lista / datos | CTA visual | Visual | Degradado en | Fechas |
|---|---|---|---|---|---|---|---|---|
| F-M-1A | Meta C1 | ¿Contenedor completo? No hace falta. | Hay fábricas que venden por caja | "$31 por pieza puesta en México" (bocina, ejemplo real) | Aparta tu lugar · {FECHA_CORTA} | Foto de producto: bocina chica + caja abierta, fondo crema | "$31" y "No hace falta" | Solo ene |
| F-M-1B | Meta C1 | Un sábado. Una clase. Y queda grabada. | Clase en vivo con Eduardo | {FECHA_LARGA} · {HORA} | Aparta tu lugar | Calendario de escritorio, laptop con Eduardo | "queda grabada" | Solo ene |
| F-M-1C | Meta C1 | Videos sueltos no contestan preguntas. Eduardo sí. | 26 años comprando en China | Globos de chat de preguntas | Pregunta en vivo · {FECHA_CORTA} | Foto de Eduardo a cámara + globos | Globo "En vivo" | Solo ene |
| F-M-2A | Meta C2 | Cada intermediario se queda con un pedazo de tu ganancia. | Compra directo de fábrica | Diagrama Fábrica → interm. → interm. → tú / Fábrica → tú | Aparta tu lugar · {FECHA_CORTA} | Solo diagrama tipográfico; intermediarios en gris | Flecha "Fábrica → tú" | Solo ene |
| F-M-2B | Meta C2 | ¿Aduana e impuestos? Se aprende, no se adivina. | El proceso completo, de la fábrica a tu negocio | — | Aparta tu lugar · {FECHA_CORTA} | Caja de cartón con etiqueta de envío | "Se aprende" | Solo ene |
| F-M-2C | Meta C2 | Si compras donde todos, vendes lo que todos. | Tecnología que todavía no llega a México | Lentes con IA · relojes · consolas · drones | Aparta tu lugar · {FECHA_CORTA} | Dos repisas: gris repetido vs. productos tech | Repisa derecha | Solo ene |
| F-M-3A | Meta C3 | 26 años importando. 2 bancarrotas. Sigue aquí. | Clase en vivo con Eduardo | 26+ años · 5 negocios propios · 300+ asesorados | {RELATIVO} {FECHA_CORTA} | Retrato de Eduardo + 3 tarjetas | "Sigue aquí" | Dic + ene |
| F-M-3B | Meta C3 | Dic: Este sábado 12 dic. La próxima es hasta enero. / Ene: Sábado 9 de enero. Aparta tu lugar. | Clase en vivo · {HORA} | {CUPO} si existe | Aparta tu lugar | Solo tipografía: hoja de calendario gigante | La fecha | Dic + ene |
| F-M-3C | Meta C3 | Clase + grabación + plantillas + 5 proveedores | Todo por $990 MXN | 2 de electrónica · 3 de surtido general de Yiwu | {RELATIVO} {FECHA_CORTA} | "Caja" abierta con 4 tarjetas saliendo | "$990" | Dic + ene |

### 7.2 Meta · tarjetas finales de video (1080×1920, 3–4 s, se montan al final del reel)

| ID | Uso | Titular | Subtítulo | CTA | Visual | Fechas |
|---|---|---|---|---|---|---|
| F-V-1 | Final C1-V1 (#2) | Clase en vivo con Eduardo | {FECHA_LARGA} · {HORA} · $990 | Toca el botón ↓ | Fondo degradado naranja, foto recortada de Eduardo | Solo ene |
| F-V-2 | Final C2-V1 (#4) y #5 de respaldo | Aprende el proceso completo | {FECHA_LARGA} · {HORA} · $990 | Toca el botón ↓ | Igual, con consola de fondo | Solo ene |
| F-V-3 | Final C3-V1 (#1) y #3 de respaldo | Que no sea una apuesta | {RELATIVO} {FECHA_LARGA} · {HORA} | Toca el botón ↓ | Igual | Dic + ene |
| F-V-L | Letrero superior fijo (PNG transparente 1080×200) para los 3 videos | Clase en vivo · $990 · {FECHA_CORTA} | — | — | Píldora naranja | Dic + ene |

### 7.3 WhatsApp · imágenes de plantilla (1080×1080; WhatsApp recorta a ~1.91:1 en la vista previa, así que **lo importante va en la franja central**)

| ID | Uso | Titular | Subtítulo | Datos | Visual | Fechas |
|---|---|---|---|---|---|---|
| F-W-A | Plantilla A | Estuviste a un paso | Esto incluye tu lugar | Clase en vivo · Grabación · Plantillas · 5 proveedores | Tarjetas tipo checklist, foto chica de Eduardo | Dic + ene |
| F-W-B | Plantilla B | "¿Cómo sé que esto es verdad?" | 26 años · 5 negocios · 2 bancarrotas | — | Retrato de Eduardo, la cita entre comillas grandes | Dic + ene |
| F-W-C | Plantilla C | Clase en vivo: compra directo en China | 5 proveedores de regalo | {FECHA_CORTA} · {HORA} | Foto de mercado/fábrica del banco + sello "regalo" | Dic + ene |
| F-W-D | Plantilla D | Compra directo de fábrica, sin intermediarios | Clase en vivo con Eduardo | {FECHA_CORTA} · $990 | Solo tipografía + logo | Dic + ene |
| F-W-M | Recordatorio "mañana" (plantilla o libre) | Es mañana | {HORA} · Queda grabada | — | Adaptar `WarmUp2_Cuenta` **sin rojo** | Dic + ene |
| F-W-H | "Hoy es la clase" (libre) | Hoy a las 11 | Te esperamos en vivo | — | Adaptar `Hoy3_Reloj` | Dic + ene |

### 7.4 Estados de WhatsApp / historias de IG y FB (1080×1920)

| ID | Uso | Titular | CTA | Fechas |
|---|---|---|---|---|
| F-E-1 | Estado/historia de cuenta regresiva (3 días antes) | Faltan 3 días · {FECHA_CORTA} | "Escribe CLASE" (orgánico; aquí sí aplica comentar) | Dic + ene |

### 7.5 Lista final para producir en un lote

| Grupo | Piezas | × tamaños | × fechas | **Total** |
|---|---:|---:|---:|---:|
| Meta C3 (3A, 3B, 3C) | 3 | 2 | 2 | **12** |
| Meta C1 + C2 (1A–1C, 2A–2C) | 6 | 2 | 1 (ene) | **12** |
| Tarjetas finales de video (F-V-3 dic+ene, F-V-1 y F-V-2 ene) + letrero (dic+ene) | — | 1 | — | **6** |
| WhatsApp plantillas (A, B, C, D) | 4 | 1 | 2 | **8** |
| WhatsApp mañana / hoy | 2 | 1 | 2 | **4** |
| Estado / historia | 1 | 1 | 2 | **2** |
| **Total** | | | | **44 piezas** |

Opcional: MP4 animados de 5–7 s de los 9 estáticos en 9:16 (+12 si se hacen las dos fechas de C3 y la de enero de C1/C2).

---

## 8. Riesgos y lo que necesito de ustedes antes de lanzar

### 8.1 Políticas de Meta

| Riesgo | Cómo se evita en este copy |
|---|---|
| Promesas de ingreso ("gana $X", "hazte rico", "dinero fácil") | No hay ninguna cifra de ganancia. Los precios son **de producto** ($31 la bocina, $748 la consola) y no de lo que vas a ganar. Legal: "los resultados dependen de cada persona". |
| Atributos personales ("¿Estás endeudado?", "¿No tienes dinero?", "¿Perdiste tu trabajo?") | Las preguntas hablan de **creencias o situaciones generales** ("¿Contenedor completo? No hace falta"), no afirman nada del que lee. Revisar que ningún copy diga "tú tienes deudas / poco dinero". |
| Antes y después | No se usa. Las 2 bancarrotas se cuentan como historia, no como "antes pobre, ahora rico". |
| Oportunidad de negocio sin explicar el producto | Siempre se dice qué es: una clase en vivo de $990 sobre cómo comprar en fábricas. |
| Aduana | Nada de "sin pagar impuestos" o "brincarte la aduana". |
| Rechazo | Si rechazan un anuncio: pedir revisión en **Calidad de la cuenta** y, mientras, subir una variante con el titular más neutral. |

### 8.2 Cuenta nueva o con poco historial

- Una cuenta publicitaria nueva con método de pago recién puesto puede tener **límite de gasto diario** y revisión más lenta. Lanzar el **2 dic** (no el 4) para tener margen si un anuncio queda en revisión 24–48 h.
- Tener **la página y el Instagram conectados** a la cuenta y al portfolio comercial, con el **dominio verificado** y los eventos priorizados.
- Empezar con el caliente es lo correcto para una cuenta sin historial: genera compras rápido y le enseña al Pixel quién compra.
- No hacer cambios masivos los primeros 3 días.
- Tener 2 administradores con verificación en dos pasos (si bloquean un perfil, la cuenta no se pierde).

### 8.3 Lo que necesito de ustedes (y fecha)

| # | Qué | Para cuándo | Responsable |
|---|---|---|---|
| 1 | Confirmar **hora** de las dos clases (¿11 am CDMX?) y si hay **cupo** real (número) | 28 nov | Eduardo |
| 2 | Método de pago de Meta resuelto | 1 dic | Eduardo |
| 3 | Confirmar que el Pixel dispara `Purchase` (con valor) en la página de gracias tras Stripe, e `InitiateCheckout` al ir al pago. Idealmente **CAPI** con el webhook de Stripe | 1 dic | Claude / equipo web |
| 4 | Confirmar que el link de Stripe guarda los UTM (Payment Link con UTM o `metadata`) | 1 dic | Claude / equipo web |
| 5 | Exportar de ManyChat los 5,988 teléfonos con WhatsApp para la audiencia C3, y la lista de compradores de Stripe para excluir | 1 dic | Equipo |
| 6 | Los archivos originales (sin compresión) de los reels #1, #2, #3, #4 y #5 para editarlos | 30 nov | Equipo |
| 7 | Recargar el monedero de ManyChat (~USD 40 antes del 7 dic, ~USD 160 antes del 14 dic) | 7 dic | Eduardo |
| 8 | **Cruce alumnos ↔ compradores de cajas**: ¿cuántos de los 25 compradores de cajas tomaron la clase antes? Con eso se ajusta el costo por venta máximo | 13 dic | Equipo |
| 9 | Quién del equipo contesta a mano a los que toquen "Quiero mi lugar" / "Tengo una duda" (respuesta en < 2 h, incluido el fin de semana de la clase) | 7 dic | Eduardo |
| 10 | Decidir si se invita en enero a los 25 compradores de cajas (mensaje personal) | 2 ene | Eduardo |
| 11 | Mandar las 10 plantillas a aprobación de Meta (tardan de minutos a 48 h) | 4 dic | Equipo |
| 12 | Verificar la empresa en Meta para subir el límite de 250 al día | Antes del 14 dic, si se puede | Eduardo |

---

### Fuentes

- [Jon Loomer · Meta Andromeda](https://www.jonloomer.com/meta-andromeda/) · [Diversificación creativa](https://www.jonloomer.com/meta-andromeda-creative-diversification/) · [How many ads is too many](https://www.jonloomer.com/qvt/how-many-ads-is-too-many/) · [Advantage+ vs detallada y lookalikes](https://www.jonloomer.com/test-results-advantage-plus-audience-detailed-targeting-lookalikes/) · [Advantage+ vs Original Audiences](https://www.jonloomer.com/advantage-audience-vs-original-audiences/) · [5 pruebas de segmentación](https://www.jonloomer.com/5-meta-ads-tests-targeting/) · [Updates to budgeting](https://www.jonloomer.com/updates-to-meta-ads-budgeting/) · [When your budget is too small](https://pubcast.jonloomer.com/when-your-budget-is-just-too-small/)
- [AdExchanger · Qué cambia Andromeda](https://www.adexchanger.com/data-driven-thinking/what-metas-andromeda-update-actually-changes-and-what-it-doesnt/) · [Common Thread](https://commonthreadco.com/blogs/coachs-corner/meta-andromeda-roas-creative-strategy-2026) · [Hunch](https://www.hunchads.com/blog/meta-andromeda-explained) · [Excite Media](https://www.excitemedia.com.au/meta-creative-diversification/) · [Triple Whale](https://www.triplewhale.com/blog/creative-targeting-ai-driven-delivery.md)
- [PPC Land · <50 conversiones = +28 % por compra](https://ppc.land/meta-says-ad-sets-under-50-weekly-conversions-cost-28-more-per-purchase/) · [PPC Land · Advantage](https://ppc.land/advantage/) · [Lebesgue · fase de aprendizaje](https://lebesgue.io/blog/facebook-ads-learning-phase/) · [Hightouch](https://hightouch.com/es/blog/the-learning-phase) · [Thread Transfer · ediciones que reinician](https://thread-transfer.pages.dev/blog/2025-05-19-edits-that-reset-learning)
- [Segwise · ABO vs CBO](https://segwise.ai/blog/abo-cbo-meta-ads-budget-strategies) · [Webtonic](https://www.webtonic.io/blog/cbo-vs-abo-which-to-use) · [Podvector](https://podvector.ai/articles/ads/scaling-and-diagnosis/meta-ads-cbo-vs-abo-for-small-budget-testing) · [Linear Design](https://lineardesign.com/blog/metas-advantage-audience/)
- [Meta · Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api) · [CAPI para mensajería](https://developers.facebook.com/docs/marketing-api/conversions-api/business-messaging) · [WhatsApp · medir conversiones](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/measure-conversion/)
- [Meta · Resultados irreales](https://transparency.meta.com/policies/ad-standards/deceptive-content/unrealistic-outcomes) · [Meta · Atributos personales](https://transparency.meta.com/policies/ad-standards/objectionable-content/personal-attributes) · [Meta · Normas de publicidad](https://transparency.meta.com/policies/ad-standards/)
- [Topgrowth · hook rate](https://topgrowthmarketing.com/?p=48825) · [Motion · métricas creativas](https://motionapp.com/blog/key-creative-performance-metrics) · [Billo · hook vs hold](https://billo.app/blog/hook-rate-to-hold-rate)
- [Emplifi · benchmarks LatAm Q3 2026](https://emplifi.io/resources/q3-2026-fmcg-food-latin-america-benchmarks/) · [eMarketer · CPM social México Q4 2025](https://www.emarketer.com/chart/c/360855/industry-kpis-mexico-social-ad-cpm-by-platform-q4-2025-360855)

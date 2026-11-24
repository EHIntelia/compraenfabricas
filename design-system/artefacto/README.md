# Compra en Fábricas · Design System

**Compra en fábricas** (Eduardo, fundador) enseña a hispanohablantes a importar directo de fábricas de China 🇨🇳: clases en vivo gratis, cursos, mentorías y contenido en redes (videos cortos). Las superficies principales son **landings mobile-first** (registro a clases, venta de programas), **materiales/guías** y documentos como recibos.

## Sources
- `uploads/logo_horizontal_2@2x.png`, `uploads/logo_vertical_1@2x.png`, `uploads/icono@2x.png` → copied to `assets/`
- Two portrait photos of Eduardo → `assets/photos/`
- Brand brief pasted by the user (colors, gradient, badges, peach box, typography, rules). No codebase, Figma or live site was provided.
- **Actualización nov 2026 (Eduardo):** la marca va **solo en naranjas, sin rojos**, y el logo oficial es el ícono naranja + "Compra en fábricas" (el de `assets/logo-horizontal.png`). Los naranjas salen del logo, del sitio compraenfabricas.com (degradado `#F97316 → #EA580C`, fondo `#FFEDD5`) y del acuerdo de compra CF-2026-007. El sello oficial se tomó de ese acuerdo y se pasó a naranja (`assets/sellos/`).

## CONTENT FUNDAMENTALS
- **Language:** español latinoamericano neutro (México como referencia: horarios "CDMX", pesos/USD).
- **Voice:** primera persona de Eduardo hablando de **tú** al lector ("Te enseño paso a paso…", "Quiero mi lugar gratis"). Cercano, directo, práctico; sin tecnicismos aduanales sin explicar.
- **CTAs** en primera persona del usuario: "Quiero mi lugar gratis", "Inscribirme ahora", "Confirmar mi lugar".
- **Casing:** titulares en oración normal (solo mayúscula inicial). Badges y eyebrows en MAYÚSCULAS: "CLASE EN VIVO", "REGALO DE BIENVENIDA", "MÁS POPULAR".
- **Hard rules:**
  - Nunca escribir la palabra "PDF". Usar "guía", "material", "documento".
  - Evitar guiones largos (—). Usar punto, coma o dos puntos.
  - Logo/marca escrito "Compra en fábricas".
- **Emoji:** la bandera 🇨🇳 es elemento de identidad, se usa seguido (titulares, regalos, cierre de frases). 🔴 se acepta para "en vivo". Fuera de eso, poco emoji.
- **Ejemplos:** "Aprende a comprar directo en fábricas de China 🇨🇳" · "Guía: 50 fábricas verificadas" · "La clase es en vivo y no queda grabada."

## VISUAL FOUNDATIONS
- **Colors (solo naranjas, sin rojos):** Naranja `#F97316` (principal), Naranja oscuro `#EA580C` (final del degradado, precios y totales grandes, sello), Naranja texto `#C2410C` (texto destacado, enlaces, títulos de nota, errores), Naranja muy oscuro `#9A3412` (avisos sobre durazno), Tinta `#1A1A1A`, Gris `#6B6B6B`, Durazno `#FFEDD5`, Crema `#FFF8F5`, Blanco, Borde suave `#D9CFC7`. The logo PNG itself uses a slightly brighter orange (~`#FF8212`); only for the mark, use `#F97316` everywhere else.
- **Ya no se usan:** Rojo `#DC2626`, rojo oscuro `#B91C1C` y el durazno rosado `#FCE4DC`. Nada de la marca va en rojo: ni degradados, ni precios, ni sellos.
- **Degradado estrella:** `linear-gradient(90deg,#F97316,#EA580C)` (naranja → naranja oscuro, igual que el sitio); hover `#EA580C → #C2410C`. Primary buttons, key words in headlines (`GradientText`), main badges, check dots. One gradient moment per view region; never on large backgrounds.
- **Type:** Arial everywhere. Headlines weight 900, tight tracking (-0.02em), line-height ~1.05–1.15, often with part of the text in gradient. Body regular 16–18px, tinta; secondary text gris. Badges 12px bold uppercase, tracking 0.08em.
- **Backgrounds:** crema page, white cards/sections, durazno for highlights. Dark tinta only for footer. No textures, patterns or illustrations; imagery is photography.
- **Photo bank:** `assets/photos/banco/` (52 imágenes 16:9): fábricas en China, puertos al atardecer, bodegas con cajas kraft y cinta naranja, inspección de muestras, tiendas de clientes en Latam, entregas y unboxing. Luz cálida, tonos crema/terracota/naranja que combinan con la marca.
- **Imagery:** warm, natural light portraits of Eduardo, shallow depth of field, beige/wood tones. No B&W, no heavy grain. Photos rounded 16–24px.
- **Spacing:** 4px base (4/8/12/16/24/32/48/64/96). Mobile gutter 20px, sections 40–48px vertical. Lots of air. Content max-width 480px mobile.
- **Radii:** soft. 8 (small), 12 (inputs, peach box, accordion), 16 (cards), 24 (pricing, photos), pill (buttons, badges).
- **Cards:** white, 1px `#D9CFC7` border, 16px radius, very soft shadow. Featured card: 2px orange border + larger shadow + gradient badge overlapping top edge.
- **Peach box:** durazno bg, 5px orange left bar, 12px radius, title in `cef-naranja-700` bold. Only for notes/rules.
- **Shadows:** soft neutral (`--shadow-sm/md/lg`), orange-tinted `--shadow-accent` under gradient CTA.
- **Hover:** gradient darkens (`--gradient-estrella-hover`) and shadow grows; outline buttons fill durazno. **Press:** scale(.98). **Focus:** orange border + 4px orange 15% ring.
- **Motion:** minimal, 150–220ms, ease-out. Fades and small rotations (accordion +). No bounces.
- **Transparency/blur:** only the sticky header (crema 92% + blur).
- **Layout:** mobile-first single column; sticky header with logo + small CTA; full-width buttons on mobile.

## LOGO
- **El logo oficial** es el ícono naranja (dos formas, `#FF8212`) + el nombre "Compra en fábricas" en negro: `assets/logo-horizontal.png` (encabezados y documentos), `assets/logo-vertical.png` (portadas) y `assets/icono.png` (avatar, favicon).
- Va sobre blanco, crema o durazno. No se redibuja, no se recolorea y nunca va en rojo.
- El cuadro con el carácter 中 en degradado naranja-rojo (favicon viejo del sitio) **no es el logo de la marca**.

## DOCUMENTOS (notas de compra, recibos)
- El documento de venta se llama **nota de compra** (ya no "acuerdo de compra"). Lleva una sola opción de envío: DHL a domicilio, con seguro.
- Encabezado: logo horizontal + título en tinta bold, folio y fecha a la derecha en gris; debajo una línea de 3pt con el degradado naranja.
- Pasos numerados en círculos con el degradado; precios y totales grandes en `cef-naranja-600`; fila de total con el degradado y texto blanco en negritas.
- Tablas: encabezado tinta con texto blanco, celdas crema con borde suave.
- Caja **Importante**: durazno, barra izquierda naranja, la palabra "Importante:" en `cef-naranja-700`.
- Firma: sello oficial naranja (`assets/sellos/sello-directo-de-fabrica.png`, girado unos -8°) con el nombre de Eduardo encima.

## ICONOGRAPHY
No icon set was provided. The brand leans on typography, badges and emoji (🇨🇳, 🔴) instead of icons. Components use the unicode ✓ for checks and "+" for accordion toggles. If a project needs icons, use **Lucide** from CDN (2px stroke, rounded) in tinta or naranja; flagged as a substitution. The orange mark (`assets/icono.png`) works as avatar/favicon.
- **Sellos:** el sello oficial "Compra en fábricas · Directo de fábrica · De China" está en `assets/sellos/sello-directo-de-fabrica.png`, en naranja `#EA580C` (antes era rojo). Los sellos PAGADO y RECIBIDO y las **firmas** (rúbrica) todavía no se han subido; nunca los redibujes. Agrégalos a `assets/sellos/` y `assets/firmas/` cuando estén.

## Components
`components/src/core/`: **Button**, **Badge**, **GradientText**, **Logo**
`components/src/content/`: **Card**, **CheckItem**, **PeachBox**, **PricingCard**, **Accordion**
`components/src/forms/`: **Input**, **Select**, **Checkbox**, **Radio**

No source component library existed; this set is authored from the brief, sized to landing pages.

## Index
- `styles.css` → imports `tokens.css`, `components/bundle.css`
- `tokens.json` colors, type, spacing, radii, shadows and the other scales; `tokens.css` is generated from it
- `components/bundle.css` degradado estrella (`--gradient-estrella`, `-diag`, `-hover`), motion (`--ease-out`, `--dur-fast`, `--dur-base`) and base element rules; `components/bundle.js` the components as `window.CompraEnFBricasDesignSystem_e5b2dc` (React 18)
- `guidelines/` foundation specimen cards (Colors, Type, Spacing, Brand)
- `components/` primitives + `<Comp>/README.md` usage
- `ui_kits/landing/` mobile landing → registro → gracias (click-through)
- `assets/` logos (horizontal, vertical, icono), `sellos/` sello oficial naranja, photos, `photos/banco/` banco de imágenes
- `assets/notes/SKILL.from-standalone.md` agent skill entry

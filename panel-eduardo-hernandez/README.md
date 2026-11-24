# Panel interno de Eduardo Hernández (Lovable)

El código del panel vive en Lovable, proyecto **"Eduardo Hernández"** (workspace "Eduardo's Lovable"),
publicado en https://eduardohernandez.lovable.app. Ese proyecto **no está conectado a GitHub**, así que
aquí se guarda un registro de los cambios que se le hacen: qué se cambió, por qué y el diff exacto.

Archivos principales del panel en Lovable: `src/panel/` (páginas) y `supabase/functions/` (integraciones
con Stripe, Hotmart, Metricool y ManyChat).

## Cambios

### 2026-11-21 · Seguidores totales en "Contenido y leads"

- **Archivo:** `src/panel/PanelContenido.tsx`
- **Commit en Lovable:** `534f0736724eec73dbfee8ac9eac12d3973ba319` (publicado el mismo día)
- **Diff:** [`cambios/2026-11-21-seguidores-totales.patch`](cambios/2026-11-21-seguidores-totales.patch)

Se agregó una tarjeta **"Seguidores totales (todas las redes)"** arriba de las tarjetas de
Vistas / Comentarios / Mensajes / Leads.

Cómo se calcula (solo frontend, sin cambios de base de datos ni de `metricool-sync`):

- En la tabla `metricas_contenido`, la columna `seguidores` es el **total acumulado** de esa red ese día
  (la llena `metricool-sync` a diario). Un 0 significa que no hubo dato.
- **Total:** por cada red (Instagram, Facebook, YouTube, TikTok, Otra) se toma el último valor > 0
  en o antes del final del periodo elegido, y se suman. Usa todo el historial, así que siempre hay cifra.
- **Crecimiento del periodo:** total final menos el total al inicio del periodo (último valor > 0 en o
  antes del inicio; si no hay, el primero dentro del periodo). En verde si sube, rojo si baja. Con el
  filtro "todo" no se muestra.
- **Desglose por red** en una línea; si el dato de una red no es del último día del periodo, se muestra
  su fecha, p. ej. "TikTok 4,500 (18 nov)".

Limitación conocida: si el periodo no tiene métricas ni leads, la página muestra el aviso de
"sin métricas" y la tarjeta no aparece.

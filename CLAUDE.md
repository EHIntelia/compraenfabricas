# Instrucciones para Claude en este repo

## Bitácora de trabajo en el panel (obligatorio)

Todo lo que se trabaje en este repo se documenta en la sección **Tareas** del panel de Eduardo Hernández, para que el equipo vea qué se hace hoy, qué se hizo en la semana y qué falta.

- Panel: proyecto de Lovable "Eduardo Hernández", `project_id` `31eb7ad3-327e-43ed-9449-1c7cda622ec0`. Se escribe con la herramienta `query_database` del conector de Lovable.
- Tabla `tareas`: `proyecto`, `titulo`, `descripcion`, `estado` (`pendiente` | `en_curso` | `hecha`), `area` (`contenido` | `seo` | `atencion` | `pauta` | `ventas` | `otro`), `prioridad` (`alta` | `media` | `baja`), `responsable`, `fecha_limite`, `recurrente`, `completada_at`.
- `proyecto`: `compra_en_china` para todo lo de Compra en Fábricas (blog, contenido, ventas de cajas); `eduardo_hernandez` para eduardohdz.com y la marca personal.

Cuándo escribir:
1. **Al empezar** una tarea: si ya existe en `tareas` (busca por título parecido), pásala a `en_curso`; si no, créala en `en_curso` con `responsable = 'Claude'`.
2. **Al terminar** (cuando queda hecha o publicada, no solo en borrador): pásala a `hecha`. Un trigger llena `completada_at` con la hora actual.
3. **Lo que quede pendiente** (datos que debe dar Eduardo, pasos que faltan, revisiones futuras): créalo como `pendiente`, con `responsable` (`Eduardo`, `Claude` o vacío) y `fecha_limite` si la hay.

Reglas:
- Títulos cortos y claros en español ("Blog: nota I (joyería de acero inoxidable) publicada"). Detalles en `descripcion`.
- No dupliques: antes de insertar, busca con `ilike` sobre `titulo`.
- No borres tareas de otras personas; no toques las recurrentes (WhatsApp, atender clientes, editar videos, SEO).
- Si el conector de Lovable no está disponible en la sesión, dilo al usuario al final en vez de omitirlo en silencio.

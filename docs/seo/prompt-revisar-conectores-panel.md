# Prompt: revisar conectores de Lovable e indexación del panel (para Claude Code con Chrome)

> Copia todo lo de abajo en una sesión de Claude Code que pueda usar tu Chrome, con tu sesión de Lovable y de Google ya abiertas.

---

Necesito que revises en mi Chrome por qué la sección **SEO** del panel de mi proyecto de Lovable **"Eduardo Hernández"** (workspace "Eduardo's Lovable") no se conecta bien con Google, y que lo arregles **solo con los cambios que te autorizo abajo**. Ya tengo sesión iniciada en Lovable y en Google.

El panel muestra estos dos avisos:
1. **Search Console:** "Sincronización automática pendiente: la conexión no está vinculada y el dueño del proyecto necesita acceso para vincularla."
2. **Google Analytics:** "No se importaron datos: la conexión actual de Google Analytics es de seguimiento, no de lectura de informes. Falta una conexión de lectura con acceso del dueño para vincularla."

Además, en la sección de indexación del panel aparecen como "no indexadas" páginas que yo pedí indexar.

## Reglas
- **Te autorizo solo a:**
  - (a) cambiar el **Sharing** de mis conexiones de Search Console y Google Analytics para dar **"Can use"** a la cuenta dueña del proyecto "Eduardo Hernández";
  - (b) **vincular** esas conexiones al proyecto "Eduardo Hernández";
  - (c) crear **una** conexión nueva de Google Analytics **de lectura de informes**, si Lovable la ofrece, iniciando sesión con mi cuenta de Google.
- **No borres** ninguna conexión ni toques otros conectores (Stripe, Metricool, ManyChat, Hotmart, Skool, etc.).
- No cambies el código del proyecto. No publiques nada. No aceptes cobros ni mejoras de plan.
- **Nunca** escribas en el chat claves, tokens, contraseñas ni el contenido de archivos JSON de credenciales.
- Si algo pide un permiso que no está en la lista de arriba, detente y pregúntame.

## 1. Search Console
1. En Lovable entra a **Connectors** → **Google Search Console**.
2. Dime cuántas conexiones hay, a nombre de qué cuenta de Google está cada una, quién es su dueño en Lovable y cómo está su **Sharing** (Private / compartida y con quién).
3. Averigua cuál es la **cuenta dueña del proyecto** "Eduardo Hernández". Se ve en la configuración del proyecto o en los miembros del workspace.
4. En la conexión que tiene acceso a la propiedad `compraenfabricas.com`, cambia **Sharing** para que la cuenta dueña del proyecto tenga **"Can use"**.
5. Abre el proyecto "Eduardo Hernández" → su sección de conectores, y confirma que la conexión de Search Console queda **vinculada** al proyecto. Si hay un botón para vincularla, úsalo.
6. Abre `/panel/seo` en el panel publicado (eduardohernandez.lovable.app/panel/seo) y dime si el aviso de Search Console desapareció. Si hay un botón "Actualizar ahora", úsalo y dime qué pasa.

## 2. Google Analytics
1. En **Connectors** → **Google Analytics**, abre **New connection** y revisa **todas** las opciones de "Configure connection". Abre el desplegable, las flechas y las pestañas, y busca un modo para **leer informes** (algo como "Read analytics insights", "Reporting", "Data API" o "Sign in with Google"). Si existe la documentación en https://docs.lovable.dev/integrations/google-analytics, léela.
2. **Si existe el modo de lectura:**
   - crea esa conexión iniciando sesión con la cuenta de Google que ve la propiedad de GA4 **"Compra en Fábricas de China"** (ID de medición G-CMYV43J6S2);
   - dale **"Can use"** a la cuenta dueña del proyecto y vincúlala al proyecto "Eduardo Hernández".
3. **Si no existe** (solo hay "Browser tracking (Measurement ID)"):
   - no crees nada;
   - dime exactamente qué opciones ves y qué dice la documentación;
   - en ese caso lo vamos a resolver con una cuenta de servicio de Google Cloud, pero eso lo hago yo después, no tú.
4. **No guardes** la conexión de "Browser tracking": el sitio ya tiene GA4 instalado.

## 3. Indexación: comparar el panel con Search Console
1. En `/panel/seo`, sección Indexación, anota cada URL que aparezca como **no indexada**, con el estado y la fecha que muestra el panel.
2. Para cada una de esas URLs, abre **Google Search Console** → propiedad `compraenfabricas.com` → **Inspección de URLs**, pégala y anota lo que dice Google ("La URL está en Google", "Descubierta: actualmente sin indexar", "Rastreada: actualmente sin indexar", "La URL no está en Google", etc.) y la fecha del último rastreo.
   - **No le des a "Solicitar indexación"**: solo quiero el diagnóstico.
3. Haz una tabla: URL | lo que dice el panel | lo que dice Search Console | ¿coinciden?
4. Si no coinciden, mira si el panel muestra una fila vieja de la misma URL (con fecha anterior) en vez de la más reciente, y dímelo.

## 4. Entrega
Guarda un archivo `revision-conectores-panel-AAAA-MM-DD.md` en mi carpeta de Descargas con:
- **Resumen de 5 líneas:**
  - qué arreglaste;
  - qué no se pudo y por qué;
  - si el aviso de Search Console desapareció;
  - si existe el modo de lectura de Analytics;
  - cuántas URLs no coinciden.
- Lo que encontraste en cada punto (1, 2 y 3), con los nombres exactos de los botones y pantallas que viste.
- La tabla de indexación.
- La lista de lo que no pudiste ver o hacer, con el motivo.

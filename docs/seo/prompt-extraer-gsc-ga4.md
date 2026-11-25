# Prompt: sacar datos de Search Console y Google Analytics (para otra sesión con Chrome)

> Copia todo lo de abajo en una sesión de Claude Code que tenga acceso a tu Chrome (Claude in Chrome), con tu cuenta de Google ya abierta.

---

Necesito que entres a mi Google Search Console y a mi Google Analytics 4 desde mi Chrome (ya tengo sesión iniciada) y saques datos para el equipo de SEO de **compraenfabricas.com**.

**Reglas:**
- **Solo lectura.** No cambies ninguna configuración, no agregues ni quites usuarios, no borres nada, no aceptes términos ni actives funciones. Si algo te pide confirmar un cambio, detente y avísame.
- La única acción permitida: en Search Console, **"Solicitar indexación"** para las URLs de la lista del paso 1.4 que salgan "La URL no está en Google". Máximo 10.
- No copies datos personales de usuarios (correos, nombres). Solo números agregados.
- Si una sección no tiene datos todavía, escribe "sin datos" y sigue.
- Al final, guarda todo en **un solo archivo Markdown** llamado `datos-seo-compraenfabricas-AAAA-MM-DD.md` en mi carpeta de Descargas y dime la ruta.

## 1. Google Search Console
Propiedad: **compraenfabricas.com** (propiedad de dominio).

### 1.1 Rendimiento (Resultados de búsqueda)
Hazlo dos veces: **últimos 28 días** y **últimos 3 meses**.
- Totales: clics, impresiones, CTR promedio, posición promedio.
- Tabla **Consultas**: las 50 primeras, ordenadas por impresiones, con clics, impresiones, CTR y posición.
- Las consultas que contengan "importar", "china", "curso", "clase", "monterrey", "proveedores", "mayoreo" o "joyería". Usa el filtro de consulta "contiene" una por una.
- Tabla **Páginas**: las 30 primeras, con clics, impresiones, CTR y posición.
- **Países** (los 5 primeros) y **Dispositivos**.
- Si el filtro "Tipo de búsqueda" lo ofrece, lo mismo para **Imágenes** y **Video**, solo los totales.

### 1.2 Indexación > Páginas
- Número de páginas **indexadas** y **no indexadas**.
- Cada motivo de "no indexada", con su número y hasta 10 URLs de ejemplo. Los que más importan:
  - "Descubierta: actualmente sin indexar"
  - "Rastreada: actualmente sin indexar"
  - "Duplicada"
  - "Página con redirección"
  - "Excluida por la etiqueta noindex"
  - "No se ha encontrado (404)"
- Indexación > **Sitemaps**: cada sitemap con su estado, fecha de última lectura y URLs descubiertas.

### 1.3 Experiencia y mejoras
Para cada uno: válidos, no válidos y el texto de cada error o advertencia.
- **Métricas web principales** (móvil y computadora): URLs buenas, por mejorar y malas.
- **HTTPS**.
- En "Mejoras" o "Resultados enriquecidos", lo que exista:
  - Rutas de exploración (breadcrumbs)
  - Preguntas frecuentes
  - Fragmentos de reseñas
  - Fragmentos de productos o fichas de comerciante
  - Videos
  - Eventos
  - Cursos
- **Seguridad y acciones manuales**: si hay algo o no.

### 1.4 Inspección de URLs
Inspecciona cada una. Anota: si está en Google o no, fecha del último rastreo, canónica elegida por Google y si es apta para resultados enriquecidos (y cuáles detectó).
- https://compraenfabricas.com/
- https://compraenfabricas.com/clase
- https://compraenfabricas.com/curso-para-importar-de-china
- https://compraenfabricas.com/curso-para-importar-de-china-monterrey
- https://compraenfabricas.com/opiniones
- https://compraenfabricas.com/productos
- https://compraenfabricas.com/joyeria
- https://compraenfabricas.com/preguntas-frecuentes
- https://compraenfabricas.com/autor/eduardo-hernandez
- https://compraenfabricas.com/blog

Si alguna sale "La URL no está en Google", dale **"Solicitar indexación"** y anota que lo hiciste.

### 1.5 Enlaces
- Los 20 **sitios que más enlazan**.
- Las 20 **páginas más enlazadas**, externas e internas.
- Los 10 **textos de enlace** más usados.

## 2. Google Analytics 4
Propiedad: **"Compra en Fábricas de China"** (ID de medición G-CMYV43J6S2). Periodo: **últimos 28 días**, y si se puede, compáralo con los 28 días anteriores.

### 2.1 Resumen
- Usuarios, usuarios nuevos, sesiones, tasa de interacción y tiempo medio de interacción.

### 2.2 Adquisición
- **Adquisición de tráfico**, por "Grupo de canales predeterminado de la sesión": sesiones, usuarios, tasa de interacción y eventos clave por canal.
- Lo mismo por **"Fuente/medio de la sesión"**, los 15 primeros.

### 2.3 Páginas de destino
- Las 25 primeras páginas de destino, con sesiones, usuarios, tasa de interacción y eventos clave.
- Las mismas, pero **solo del canal "Organic Search"**. Agrega un filtro por canal.

### 2.4 Eventos
- Todos los eventos con su número de veces y de usuarios. Sobre todo:
  - begin_checkout
  - generate_lead
  - contact
  - los clics a WhatsApp, Skool y joyería
  - clic_tomar_clase
  - enviar_resena
  - page_view
- Revisa **Administrar > Eventos clave** y dime qué eventos están marcados como clave. **No cambies nada.**

### 2.5 Search Console dentro de GA4
- Si en Informes hay una colección **"Search Console"**, saca "Consultas" y "Tráfico de búsqueda orgánica de Google". Si no aparece, solo dime que no está publicada.

### 2.6 Configuración (solo leer)
Anota el estado de cada una, sin cambiar nada:
- Retención de datos.
- Google Signals.
- Vinculación con Search Console.
- Medición mejorada, con qué opciones activas.

## 3. Formato del archivo
- Un título por sección y tablas en Markdown.
- Al inicio, un resumen de 5 líneas con lo más importante:
  - cuántas páginas indexadas;
  - clics de Google en 28 días;
  - las 3 consultas con más impresiones;
  - errores en resultados enriquecidos;
  - si hay acciones manuales.
- Al final, una lista de **qué no pudiste ver y por qué**.

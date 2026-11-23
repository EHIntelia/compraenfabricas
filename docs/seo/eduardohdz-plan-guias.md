# eduardohdz.com — Plan de guías públicas (Fase 4)

**Fecha:** 23 de noviembre de 2026
**Para qué:** que eduardohdz.com tenga contenido útil que Google y las IAs puedan citar, sin pelear con compraenfabricas.com. Esa marca se queda con todo lo de importación.

## Reglas

- Una guía = una búsqueda (intención). No se repite lo que ya cubre otra página del sitio.
- **Tono:** español mexicano de banqueta, sin palabras de coach, con estructura PAS:
  - **P**roblema: el dolor del dueño de negocio.
  - **A**gitación: lo que le cuesta seguir así.
  - **S**olución: el método, con pasos.
- **Respuesta directa arriba:** las 2 primeras líneas responden la pregunta del título.
- **Autoría:** firma de Eduardo Hernández, con enlace a `/eduardo-hernandez`. Schema `Article` con `author` → `https://eduardohdz.com/#person`.
- **Prohibido inventar** casos, clientes, cifras o testimonios. Si falta algo: `[PENDIENTE: …]`, y no se publica hasta tenerlo.
- **Cada guía termina con un llamado** al diagnóstico gratis (`/diagnostico`) y enlaza a la página de producto que le toque.
- **Ruta propuesta:** `/guias/<slug>`, con un índice en `/guias`, enlazado desde `/recursos` y el footer.

## Las 4 guías

| # | Guía (H1) | Keyword principal | Secundarias | Material que ya existe | Enlaza a | No pelea con |
|---|---|---|---|---|---|---|
| 1 | Cómo hacer crecer mi negocio: el sistema de 5 áreas | cómo hacer crecer mi negocio | cómo hacer crecer un negocio pequeño, crecimiento de pymes | Las 5 áreas del diagnóstico (ventas, finanzas, operación, liderazgo y estrategia) en `src/data/questions.ts`; módulos de De 0 a 1 Millón | `/diagnostico`, `/de-0-a-1-millon`, `/asesoria` | `/diagnostico`: la guía explica; el diagnóstico mide |
| 2 | Cómo subir mis ventas sin depender de la suerte | cómo subir mis ventas | cómo vender más en mi negocio, ventas para pymes | Módulos 1–5 de Sube tus Ventas; "30 preguntas para cerrar ventas" (PDF) | `/sube-tus-ventas`, `/30-preguntas` | `/sube-tus-ventas`: la guía da el qué y el porqué; el curso da el cómo completo |
| 3 | Cliente ideal: cómo definirlo paso a paso (con hoja de trabajo) | cliente ideal | cómo definir a mi cliente ideal, buyer persona para pymes | Sesión 9 "Cliente ideal" del curso (`src/assets/sesion-9-cliente-ideal-material.pdf`) | `/de-0-a-1-millon`, `/diagnostico` | No hay otra página sobre esto |
| 4 | Diagnóstico de negocio: qué es y cómo hacerlo tú mismo | qué es un diagnóstico de negocio | diagnóstico empresarial, cómo evaluar mi negocio | Niveles y cuellos de botella del diagnóstico (`levels`, `bottleneckSymptoms`) | `/diagnostico` (CTA principal) | `/diagnostico` se queda con "diagnóstico de negocio gratis"; esta guía ataca la pregunta informativa |

## Orden recomendado

1. **Guía 3, cliente ideal:** ya hay material completo (sesión 9) y nadie más del sitio pelea por esa búsqueda.
2. **Guía 1, crecer mi negocio:** es la búsqueda más grande. La pelean BBVA, Mercado Pago y DHL, así que necesita ángulo propio: las 5 áreas y el diagnóstico.
3. **Guía 2, subir mis ventas.**
4. **Guía 4, diagnóstico (qué es).**

## Lo que necesito de Eduardo para cada guía

- [PENDIENTE: 1 o 2 ejemplos reales, sin nombre de cliente, de un negocio que mejoró en esa área, con permiso para contarlo.]
- [PENDIENTE: el error más común que ve en esa área.]
- [PENDIENTE: confirmar que se pueden usar públicamente las hojas de trabajo de las sesiones.]

## Fuera del sitio (Fase 5, para reforzar las guías)

- **Un video corto por guía** con Eduardo diciendo "Soy Eduardo Hernández, fundador de NADIE". YouTube es la fuente que más citan las IAs.
- **Que cada video enlace a la guía** y la guía incruste el video.

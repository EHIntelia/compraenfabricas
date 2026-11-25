# Prompt: marcar eventos clave y subir la retención de datos en GA4 (para otra sesión con Chrome)

> Copia todo lo de abajo en una sesión de Claude Code que tenga acceso a tu Chrome, con tu cuenta de Google abierta.

---

Entra a mi **Google Analytics 4** desde mi Chrome (ya tengo sesión iniciada). Propiedad: **"Compra en Fábricas de China"** (ID de medición G-CMYV43J6S2). Te autorizo a hacer **solo estos dos cambios**. No cambies nada más.

## Cambio 1: marcar eventos clave
Ve a **Administrar → Visualización de datos → Eventos**. En la tabla de eventos recientes, activa la estrella o el interruptor **"Marcar como evento clave"** en estos 5 eventos:

1. `begin_checkout`: clic al botón de pago
2. `clic_whatsapp`
3. `clic_tomar_clase`
4. `apartar_caja`
5. `enviar_resena`

Reglas:
- Si alguno no aparece en la lista, porque no ha ocurrido en los últimos días, **no lo crees a mano**. Anótalo y sigue.
- **No desmarques** los que ya están como clave (`purchase`, `qualify_lead`, `close_convert_lead`).
- **No cambies** el "método de recuento" ni el valor predeterminado. Déjalos como estén.

## Cambio 2: retención de datos
Ve a **Administrar → Recopilación y modificación de datos → Retención de datos**:
- Cambia **"Retención de datos de eventos"** de 2 meses a **14 meses**.
- Deja igual "Retención de datos de usuario" (14 meses) y la casilla "Borrar cuando haya actividad nueva del usuario".
- Da clic en **Guardar**.

## Al terminar
Revisa que los cambios quedaron guardados y respóndeme:
- La lista de eventos clave tal como queda en Administrar → Eventos clave.
- La retención de datos de eventos tal como se ve al recargar la página.
- Si algo no se pudo hacer, qué fue y por qué. Por ejemplo: un evento que no aparecía, un permiso o un botón bloqueado.

Si cualquier pantalla te pide aceptar términos, vincular otra cuenta o hacer cualquier cambio que no sea uno de estos dos, **detente y pregúntame**.

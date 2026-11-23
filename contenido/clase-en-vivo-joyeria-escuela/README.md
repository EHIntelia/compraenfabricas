# Clase en vivo v3 · Pitch de joyería (JAICO) y Escuela (Skool)

Presentación de la clase en vivo "Compra e importa directo de China" y su hoja de trabajo.

## Archivos

| Archivo | Qué es |
|---|---|
| `CLASE_EN_VIVO_JOYERIA_ESCUELA_v3.pptx` | Presentación editable (22 láminas). Se sube a Drive y se abre como Google Slides. |
| `CLASE_EN_VIVO_JOYERIA_ESCUELA_v3.pdf` | La misma presentación en PDF, para revisar. |
| `HOJA_DE_TRABAJO_CLASE_EN_VIVO.pdf` | Hoja de trabajo para los asistentes (tamaño carta, 6 páginas, para imprimir y llenar a mano). |
| `assets/` | Fuentes para regenerar todo: `build.py` (presentación), `hoja.html` + `render_hoja.js` (hoja de trabajo), íconos, logo de JAICO y QR. |

## Qué cambió contra la v2 (Xijiao Shops)

- **Se quitó la oferta de servicios:** ya no se ofrece validar proveedores, pagar por el cliente ni traer la mercancía (logística). En su lugar, los pasos 1, 2, 3 y 5 llevan consejos de Eduardo.
- **Camino 2 ahora es "Con JAICO":** venta de joyería ya importada, a precio de mayoreo.
- **Láminas nuevas:** por qué joyería (chiquita y ligera, siempre se vende, sin bodega, buen margen), por qué JAICO (con QR), la Escuela (qué incluye y cómo entrar, con QR) y cierre con los dos QR.
- **Portada y pie de página:** dicen "Compra en Fábricas de China · Eduardo Hernández" en lugar de "Xijiao Shops".

## Datos usados

- **JAICO:** https://info.joyeria.shop/ (QR en láminas 15 y 22 y en la hoja de trabajo).
- **Escuela en Skool:** https://www.skool.com/emprende-importando-4690/about (QR en láminas 17 y 22 y en la hoja de trabajo).
- **Precios de la Escuela:**
  - Entrada gratis.
  - Membresía **$15 USD/mes**: incluye los cursos De 0 a 1 Millón y Sube tus Ventas en 5 Pasos.
  - Cursos premium: Importación de China completo $230 USD, Arma tu negocio con IA $50 USD y Guía rápida $50 USD.
  - La Guía rápida es esta misma clase: los asistentes la piden al staff para que se la habiliten.
- **Ejemplo de joyería:** $25 de costo y $149 de venta. Está marcado como **hipotético** en la presentación y en la hoja.

## Pendientes

- [ ] Escanear los dos QR con el celular antes de la clase.
- [ ] Si se quieren datos reales de JAICO (número de modelos, pedido mínimo, precios), ponerlos en la lámina 15.
- [ ] Confirmar los tipos de joyería mencionados (aretes, collares, pulseras, anillos).

## Cómo regenerar

```bash
pip install python-pptx qrcode[pil] --break-system-packages
python3 assets/build.py            # genera el .pptx dentro de assets/
node assets/render_hoja.js "$PWD/assets"   # genera la hoja en PDF dentro de assets/
```

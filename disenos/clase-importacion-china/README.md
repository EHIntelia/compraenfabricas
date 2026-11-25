# Clase Importación China: diseños y animaciones

Copia de las fuentes del lienzo de diseño
[Clase Importación China (copia)](https://claude.ai/artifact/AJtuKHrqGFKxq3tsV6nVtp).

- `canvas.json`: índice del lienzo (posición y título de cada diseño).
- `*.dc.html`: un archivo por diseño (posts, "Comenta" China / Clase / Electrónica / Curso,
  cajas secretas, warm up, proveedores, "Te vemos hoy").
- `ds/`: tokens del sistema de diseño de Compra en Fábricas.
- `render.js`: exporta las animaciones a MP4 (fondo verde para chroma, 6 s, 30 fps).

## Exportar animaciones a MP4

Requiere Node, Playwright con Chromium y ffmpeg.

```bash
node disenos/clase-importacion-china/render.js disenos/clase-importacion-china animaciones-curso
```

Sin más argumentos exporta las seis animaciones "Curso". Para exportar otras, pasa sus
nombres sin `.dc.html`:

```bash
node disenos/clase-importacion-china/render.js disenos/clase-importacion-china salida ComentaB_Electronica_Chroma ComentaD_Clase_Chroma
```

Los MP4 ya exportados de "Curso" están en `animaciones-curso/`.

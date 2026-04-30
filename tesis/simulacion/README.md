# Simulacion MuseIQ

Aplicacion web tipo top-down para simular el recorrido de un visitante en un museo con salas conectadas, obras por zona y panel de informacion contextual.

## Archivos principales

- Entrada web: [index.html](index.html)
- Logica principal: [app.js](app.js)
- Estilos: [styles.css](styles.css)
- Datos y recursos: [src](src)

## Funcionalidad principal

- Navegacion por dos salas
- Deteccion de zona y obra cercana
- Panel contextual de contenido curatorial
- Indicadores de estado de la simulacion
- Minimap y elementos de interfaz de apoyo

## Ejecutar en local

Opcion rapida:

1. Abrir [index.html](index.html) en el navegador.

Opcion recomendada (servidor local):

cd tesis/simulacion
python -m http.server 5500

Abrir en navegador:

http://localhost:5500

## Controles

- W A S D o flechas: movimiento
- Espacio o Enter: interaccion contextual

## Publicacion en GitHub Pages

El despliegue esta automatizado con GitHub Actions desde la carpeta [tesis/simulacion](../simulacion).

Workflow:

[/.github/workflows/deploy-simulacion-pages.yml](../../.github/workflows/deploy-simulacion-pages.yml)

URL publica:

https://eduardo202020.github.io/Tesis/

## Objetivo de la demo

Esta simulacion se usa como maqueta de experiencia para validar la propuesta MuseIQ en el contexto de tesis:

- Recorrido guiado por salas
- Interaccion contextual por proximidad
- Base visual para explicar la arquitectura funcional

# Tesis

Repositorio del proyecto de tesis en LaTeX, enfocado en la propuesta **MuseIQ**: una guia virtual inteligente para museos y espacios culturales con apoyo de tecnologias como BLE, TTS, STT e IA contextual.

## Contenido del repositorio

- `tesis/`: documento principal de la tesis y sus fuentes.
- `tesis/tesis.tex`: archivo principal para compilar la tesis completa.
- `tesis/src/`: capitulos, frontmatter, anexos y bibliografia.
- `tesis/investigacion.md`: notas de trabajo y material de apoyo para redaccion.
- `tesis-plantilla/`: plantilla base tomada como referencia estructural.
- `.vscode/settings.json`: configuracion del workspace, incluyendo ajustes para una visualizacion PDF mas comoda en modo oscuro.

## Compilacion

La tesis principal se compila desde la carpeta `tesis/`.

Ejemplo con `latexmk`:

```bash
cd tesis
latexmk -pdf tesis.tex
```

Si usas VS Code con LaTeX Workshop, basta con abrir el proyecto y compilar `tesis/tesis.tex`.

## Estructura general

El documento incluye:

- portada, dedicatoria, agradecimientos, resumen y abstract;
- capitulos tematicos del desarrollo de la tesis;
- anexos y bibliografia final.

## Archivos ignorados

El repositorio incluye un `.gitignore` pensado para proyectos LaTeX. Se excluyen archivos auxiliares de compilacion como `*.aux`, `*.log`, `*.toc`, `*.synctex.gz` y PDFs generados de salida, para mantener el historial limpio.

## Estado del repositorio

Este repositorio esta versionado con Git y conectado a GitHub en:

`https://github.com/eduardo202020/Tesis.git`

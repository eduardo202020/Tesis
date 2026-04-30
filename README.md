# MuseIQ - Proyecto de tesis

Repositorio principal del trabajo de tesis MuseIQ. Integra redaccion academica en LaTeX, generacion de graficos en Python, presentacion en Beamer y una simulacion web para demostrar la experiencia de visita en museo.

## Componentes del repositorio

- Tesis en LaTeX: [tesis/tesis](tesis/tesis)
- Scripts de graficos: [tesis/graficos](tesis/graficos)
- Presentacion: [tesis/presentaciones](tesis/presentaciones)
- Simulacion web: [tesis/simulacion](tesis/simulacion)

## Estructura relevante

- Archivo principal de tesis: [tesis/tesis/tesis.tex](tesis/tesis/tesis.tex)
- Capitulos: [tesis/tesis/src/chapters](tesis/tesis/src/chapters)
- Bibliografia: [tesis/tesis/src/backmatter/referencias.bib](tesis/tesis/src/backmatter/referencias.bib)
- Graficos generados: [tesis/graficos/output](tesis/graficos/output)
- Presentacion Beamer: [tesis/presentaciones/presentacion.tex](tesis/presentaciones/presentacion.tex)
- App web de simulacion: [tesis/simulacion/index.html](tesis/simulacion/index.html)

## Compilar la tesis

Desde la raiz del repo:

cd tesis/tesis
latexmk -pdf tesis.tex

Compilacion limpia:

cd tesis/tesis
latexmk -C tesis.tex
latexmk -pdf tesis.tex

## Compilar la presentacion

Desde la raiz del repo:

cd tesis/presentaciones
pdflatex presentacion.tex

## Generar graficos

Desde la raiz del repo:

cd tesis/graficos
python -m pip install -r requirements.txt
python ejemplos_uso.py all

Documentacion de esta parte en [tesis/graficos/README.md](tesis/graficos/README.md).

## Ejecutar simulacion local

Opcion simple:

1. Abrir [tesis/simulacion/index.html](tesis/simulacion/index.html) en el navegador.

Opcion recomendada con servidor local:

cd tesis/simulacion
python -m http.server 5500

Luego abrir http://localhost:5500

Documentacion detallada en [tesis/simulacion/README.md](tesis/simulacion/README.md).

## Publicacion en GitHub Pages

La simulacion se publica automaticamente con GitHub Actions usando:

- Workflow: [/.github/workflows/deploy-simulacion-pages.yml](.github/workflows/deploy-simulacion-pages.yml)
- Carpeta publicada: [tesis/simulacion](tesis/simulacion)

URL publica de la simulacion web:

http://eduardoguev.me/Tesis/

## Flujo de trabajo recomendado

1. Redactar o ajustar contenido fuente en [tesis/tesis/investigaciones](tesis/tesis/investigaciones).
2. Pasar el contenido academico a [tesis/tesis/src/chapters](tesis/tesis/src/chapters).
3. Generar o actualizar figuras en [tesis/graficos](tesis/graficos).
4. Compilar tesis y presentacion.
5. Validar simulacion web.
6. Hacer commit y push para actualizar GitHub Pages.

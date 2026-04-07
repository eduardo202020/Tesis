# MuseIQ - Proyecto de Tesis

Repositorio del proyecto de tesis desarrollado en LaTeX sobre **MuseIQ**, una propuesta de guia virtual inteligente para museos y espacios culturales, orientada a mejorar la experiencia de visita presencial mediante tecnologias de localizacion, asistencia por voz e inteligencia artificial contextual.

## Descripcion

MuseIQ plantea una solucion de mediacion cultural digital basada en:

- beacons BLE con ESP32 para reconocimiento de proximidad;
- sensores del smartphone para apoyo de orientacion;
- TTS y STT para interaccion por voz;
- IA conversacional con RAG para respuestas contextuales sobre el contenido museistico.

El proyecto esta enfocado en el contexto peruano y en escenarios de adopcion institucional dentro de museos, museos de sitio, centros culturales y espacios de interpretacion patrimonial.

## Estructura del repositorio

### Tesis

- `tesis/tesis/`: proyecto principal de la tesis.
- `tesis/tesis/tesis.tex`: archivo principal del documento.
- `tesis/tesis/src/chapters/`: capitulos de la tesis.
- `tesis/tesis/src/frontmatter/`: portada, resumen, abstract y secciones preliminares.
- `tesis/tesis/src/backmatter/referencias.bib`: bibliografia en formato BibTeX.

### Presentaciones

- `tesis/presentaciones/`: presentaciones visuales de avance.
- `tesis/presentaciones/presentacion.tex`: archivo principal de la presentacion.
- `tesis/presentaciones/prompts-imagenes.md`: prompts para generar imagenes con IA.
- `tesis/presentaciones/src/`: logo institucional e imagenes numeradas `01.png` a `12.png`.

### Referencia base

- `tesis-plantilla/`: plantilla original usada como referencia estructural.

### Configuracion

- `.vscode/settings.json`: ajustes del workspace, incluyendo configuracion del visor PDF en modo oscuro.

## Compilacion

### Compilar la tesis

Desde la carpeta `tesis/tesis/`:

```bash
cd tesis/tesis
latexmk -pdf tesis.tex
```

### Compilar la presentacion

Desde la carpeta `tesis/presentaciones/`:

```bash
cd tesis/presentaciones
pdflatex presentacion.tex
```

## Flujo de trabajo de la presentacion

La presentacion fue diseñada para exposiciones visuales, donde cada diapositiva se apoya principalmente en una imagen.

El flujo es el siguiente:

1. Se redacta el contenido del capitulo correspondiente en la tesis.
2. Se genera un prompt por diapositiva en `prompts-imagenes.md`.
3. Se crean las imagenes con IA y se guardan en `tesis/presentaciones/src/`.
4. La presentacion carga automaticamente las imagenes `01.png` a `12.png`.

## Contenido academico actual

El trabajo desarrolla, entre otros, los siguientes ejes:

- contexto tecnologico y cultural de MuseIQ;
- problema de mediacion en museos y justificacion de la propuesta;
- estado del arte y referentes tecnicos;
- panorama actual y mercado global de experiencias culturales digitales;
- definicion del mercado objetivo y panorama nacional en el Peru.

## PDFs disponibles en el repositorio

Se versionan tambien los PDFs principales para consulta directa desde GitHub:

- `tesis/tesis/tesis.pdf`
- `tesis/tesis/informe.pdf`
- `tesis/presentaciones/presentacion.pdf`
- `tesis-plantilla/tesis-plantilla.pdf`

## Repositorio remoto

GitHub:

`https://github.com/eduardo202020/Tesis.git`

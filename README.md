# MuseIQ - Proyecto de Tesis

Repositorio de trabajo de la tesis **MuseIQ**, una propuesta de guia virtual inteligente para museos y espacios culturales. El proyecto integra redaccion academica en LaTeX, investigacion por capitulos, presentaciones y un flujo auxiliar en Python para generar graficos que luego se insertan en la tesis.

## Descripcion del proyecto

MuseIQ plantea una solucion de mediacion cultural digital orientada a mejorar la experiencia de visita presencial mediante:

- beacons BLE con ESP32 para reconocimiento de proximidad o sala;
- sensores del smartphone para apoyo de orientacion;
- TTS y STT para interaccion por voz;
- IA conversacional con RAG para respuestas contextuales sobre contenido museistico.

La tesis esta enfocada en el contexto peruano y en escenarios de adopcion institucional dentro de museos, museos de sitio, centros culturales y espacios de interpretacion patrimonial.

## Estado actual del trabajo

Hasta este punto, el repositorio ya incorpora trabajo desarrollado en estas areas:

- capitulos base de la tesis en LaTeX;
- investigacion consolidada para el **Capitulo 4: Oferta Tecnologica Mundial**;
- investigacion consolidada para el **Capitulo 5: Flujo de Ingresos Proyectados**;
- desarrollo del **Capitulo 10: Evaluacion Economica y Financiera**;
- lista manual de tablas y lista de acronimos alineadas al formato de la plantilla;
- configuracion de compilacion automatica en VS Code para LaTeX Workshop;
- flujo complementario para generar graficos en Python desde `tesis/graficos/`.

## Estructura del repositorio

### Tesis principal

- `tesis/tesis/`: proyecto principal de la tesis en LaTeX.
- `tesis/tesis/tesis.tex`: archivo principal del documento.
- `tesis/tesis/src/chapters/`: capitulos de la tesis.
- `tesis/tesis/src/frontmatter/`: portada, indices, resumen, abstract y secciones preliminares.
- `tesis/tesis/src/backmatter/referencias.bib`: bibliografia en formato BibTeX.
- `tesis/tesis/investigaciones/`: materiales de investigacion por capitulo en formato `.md`, `.pdf` u otros insumos de apoyo.
- `tesis/tesis/MuseIQ.pdf`: documento auxiliar usado como base simplificada de costos y apoyo economico.

### Graficos

- `tesis/graficos/`: flujo en Python para generar figuras a partir de informacion numerica.
- `tesis/graficos/generar_grafico.py`: libreria base con funciones reutilizables para distintos tipos de graficos.
- `tesis/graficos/ejemplos_uso.py`: ejemplos editables para producir graficos concretos de la tesis.
- `tesis/graficos/output/`: carpeta de salida de imagenes generadas.
- `tesis/graficos/README.md`: guia especifica del flujo de graficos.

### Presentaciones

- `tesis/presentaciones/`: presentaciones visuales de avance.
- `tesis/presentaciones/presentacion.tex`: archivo principal de la presentacion.
- `tesis/presentaciones/prompts-imagenes.md`: prompts para generar imagenes con IA.
- `tesis/presentaciones/src/`: recursos visuales usados por la presentacion.

### Referencia base

- `tesis-plantilla/`: plantilla original tomada como referencia estructural y de formato.

### Configuracion

- `.vscode/settings.json`: configuracion del workspace, incluyendo compilacion automatica al guardar para LaTeX Workshop.

## Flujo de trabajo recomendado

El flujo de trabajo que mejor se ajusta al estado actual del proyecto es este:

1. desarrollar o investigar un capitulo en `tesis/tesis/investigaciones/cap XX/`;
2. convertir ese contenido a redaccion academica dentro de `tesis/tesis/src/chapters/`;
3. si el capitulo contiene datos numericos o comparaciones, generar un grafico en `tesis/graficos/`;
4. insertar el grafico en el capitulo correspondiente de LaTeX;
5. compilar la tesis completa y revisar el PDF;
6. si corresponde, actualizar referencias bibliograficas, lista de tablas o acronimos.

## Compilacion

### Compilar la tesis

Desde la carpeta `tesis/tesis/`:

```bash
cd tesis/tesis
latexmk -pdf tesis.tex
```

Si usas VS Code con **LaTeX Workshop**, el workspace ya esta configurado para compilar al guardar:

- `latex-workshop.latex.autoBuild.run = onSave`
- `latex-workshop.latex.recipe.default = lastUsed`

### Compilar la presentacion

Desde la carpeta `tesis/presentaciones/`:

```bash
cd tesis/presentaciones
pdflatex presentacion.tex
```

## Flujo de graficos en Python

Cuando un capitulo tenga tablas, comparaciones, distribuciones o tendencias y convenga explicarlas visualmente, los graficos deben generarse en `tesis/graficos/`.

### Instalacion

Desde `tesis/graficos/`:

```powershell
python -m pip install -r requirements.txt
```

### Generar graficos de ejemplo

```powershell
cd tesis/graficos
python generar_grafico.py
python ejemplos_uso.py
```

### Tipos de graficos disponibles

Actualmente la libreria base permite generar:

- barras verticales;
- barras horizontales;
- lineas;
- pastel;
- dispersion.

### Archivos principales del flujo de graficos

- `generar_grafico.py`: contiene funciones reutilizables como `grafico_barras(...)`, `grafico_lineas(...)` y similares.
- `ejemplos_uso.py`: sirve como punto de partida para crear graficos reales de la tesis sin tocar la libreria base cada vez.
- `output/`: guarda las imagenes resultantes, normalmente en formato `.png`.

### Insercion en LaTeX

La tesis principal ya esta preparada para buscar figuras en `tesis/graficos/output/` mediante:

```latex
\usepackage{graphicx}
\graphicspath{{../graficos/output/}}
```

Por eso, una vez generado un archivo en `output/`, puede insertarse directamente en cualquier capitulo con algo como:

```latex
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.82\textwidth]{flujo_ingresos_10_anios.png}
    \caption{Proyeccion de ingresos de MuseIQ a 10 anos.}
    \label{fig:flujo-ingresos}
\end{figure}
```

## Archivos y secciones importantes de la tesis

Dentro de `tesis/tesis/src/chapters/`, algunos puntos clave del avance son:

- `ch01-introduccion.tex`: problema, solucion propuesta, antecedentes y estado del arte;
- `ch02-panorama-actual.tex`: panorama sectorial y situacion actual;
- `ch03-mercado-objetivo.tex`: mercado objetivo de MuseIQ;
- `ch04-oferta-tecnologica.tex`: oferta tecnologica mundial comparable;
- `ch05-flujo-ingresos.tex`: modelo y proyeccion de ingresos;
- `ch10-evaluacion-economica.tex`: evaluacion economica y financiera.

En `tesis/tesis/src/frontmatter/` tambien se trabaja de forma manual la coherencia con la plantilla, especialmente en:

- `lista-tablas.tex`;
- `lista-acronimos.tex`.

## Buenas practicas para continuar

- mantener la investigacion fuente dentro de `tesis/tesis/investigaciones/` antes de llevarla a LaTeX;
- usar nombres descriptivos para graficos, por ejemplo `mercado_objetivo_museos.png` o `comparacion_costos_operativos.png`;
- actualizar `referencias.bib` cada vez que se incorpore nueva literatura;
- compilar con frecuencia para detectar problemas de referencias, tablas o figuras;
- cuando un capitulo crezca en datos numericos, preferir figuras claras en vez de saturar el texto con cifras;
- usar la plantilla `tesis-plantilla/` como referencia de forma y no como fuente de contenido.

## PDFs principales

Se pueden generar o consultar estos documentos principales:

- `tesis/tesis/tesis.pdf`
- `tesis/tesis/informe.pdf`
- `tesis/presentaciones/presentacion.pdf`
- `tesis-plantilla/tesis-plantilla.pdf`

## Repositorio remoto

GitHub:

`https://github.com/eduardo202020/Tesis.git`

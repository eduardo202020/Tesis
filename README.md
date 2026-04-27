# MuseIQ - Proyecto de Tesis

Repositorio de trabajo de la tesis **MuseIQ**, una propuesta de guia inteligente para museos y espacios culturales del Peru. El proyecto integra redaccion academica en LaTeX, investigacion por capitulos, generacion de graficos en Python y una presentacion de sustentacion en Beamer.

## Descripcion del proyecto

MuseIQ plantea una solucion de mediacion cultural digital para mejorar la visita presencial en museos mediante:

- beacons BLE para reconocimiento de proximidad por sala o zona;
- uso del smartphone del visitante como interfaz principal;
- interaccion por voz con TTS y STT;
- IA conversacional con RAG para respuestas contextuales sobre contenido museistico.

La tesis se desarrolla en el contexto peruano y, en su estado actual, aterriza el caso piloto en el **Museo Tumbas Reales de Sipan**, Lambayeque.

## Estado actual

Actualmente el repositorio ya incorpora:

- capitulos 1 al 8 redactados en LaTeX;
- **Capitulo 3** aterrizado al mercado objetivo de MuseIQ en el Peru;
- **Capitulo 5** reconstruido con costos, precios, ingresos, mantenimiento, servicios adicionales y graficos del piloto en Sipan;
- **Capitulo 10** alineado con el capitulo 5 y ampliado con escenarios de expansion y evaluacion economica;
- presentacion en Beamer actualizada con tablas y graficos economicos;
- flujo de generacion de graficos en Python para la tesis y la presentacion;
- bibliografia centralizada en BibTeX.

## Estructura del repositorio

### Tesis principal

- `tesis/tesis/tesis.tex`: archivo principal de compilacion.
- `tesis/tesis/tesis.pdf`: PDF compilado de la tesis.
- `tesis/tesis/src/chapters/`: capitulos de la tesis.
- `tesis/tesis/src/frontmatter/`: portada, indices, resumen, abstract y secciones preliminares.
- `tesis/tesis/src/backmatter/referencias.bib`: bibliografia en formato BibTeX.
- `tesis/tesis/investigaciones/`: investigacion base por capitulo en `.md`, `.pdf` y otros insumos.

### Graficos

- `tesis/graficos/`: scripts en Python para generar figuras.
- `tesis/graficos/generar_grafico.py`: libreria base para barras, lineas, dispersion y pastel.
- `tesis/graficos/ejemplos_uso.py`: casos concretos usados por la tesis.
- `tesis/graficos/output/`: salida de imagenes organizadas por capitulo.

### Presentacion

- `tesis/presentaciones/presentacion.tex`: archivo principal de la presentacion.
- `tesis/presentaciones/presentacion.pdf`: PDF compilado de la presentacion.
- `tesis/presentaciones/src/`: recursos visuales de apoyo.
- `tesis/presentaciones/prompts-imagenes.md`: prompts usados para generar apoyo visual.

### Referencia base

- `tesis-plantilla/`: plantilla de referencia usada como apoyo de estructura y formato.

## Capitulos activos en la compilacion actual

El archivo [tesis.tex](tesis/tesis/tesis.tex) actualmente compila:

- `ch01-introduccion`
- `ch02-panorama-actual`
- `ch03-mercado-objetivo`
- `ch04-oferta-tecnologica`
- `ch05-flujo-ingresos`
- `ch06-offendes`
- `ch07-transformers`
- `ch08-datos-entrada`
- `ch10-evaluacion-economica`

Permanecen comentados en esta version:

- `ch09-diseno-despliegue`
- `ch11-normas-tecnicas`
- `ch12-conclusiones`
- anexos

## Avances clave por capitulo

- `ch03-mercado-objetivo.tex`: define el mercado objetivo institucional y territorial de MuseIQ, priorizando Lambayeque y el Museo Tumbas Reales de Sipan.
- `ch05-flujo-ingresos.tex`: desarrolla hardware, costo de instalacion, precio de implementacion, mantenimiento, servicio recurrente de IA, servicios adicionales, flujo del piloto y extrapolacion a nuevos museos.
- `ch10-evaluacion-economica.tex`: evalua viabilidad economica y financiera en soles, con escenarios de 1, 2, 3 y 4 museos nuevos por ano.

## Graficos ya incorporados

### Capitulo 5

Entre las figuras economicas ya integradas en la tesis se encuentran:

- `estructura_ingresos_rubro.png`
- `flujo_ingresos_10_anios.png`
- `escenarios_ingresos_comparados.png`

### Capitulo 10

El capitulo 10 ya incorpora, entre otros:

- `flujo_economico_anual.png`
- `flujo_neto_escenarios_expansion.png`
- `van_escenarios_expansion.png`
- `sensibilidad_van.png`

## Flujo de trabajo recomendado

1. desarrollar o reunir investigacion en `tesis/tesis/investigaciones/cap XX/`;
2. convertir esa base en redaccion academica dentro de `tesis/tesis/src/chapters/`;
3. cuando existan datos comparativos o numericos, generar el grafico correspondiente en `tesis/graficos/`;
4. insertar tablas y figuras en el capitulo de LaTeX;
5. compilar la tesis completa y revisar el PDF;
6. alinear la presentacion con los cambios mas importantes.

## Compilacion

### Compilar la tesis

Desde `tesis/tesis/`:

```bash
cd tesis/tesis
latexmk -pdf tesis.tex
```

Si se requiere una recompilacion limpia:

```bash
cd tesis/tesis
latexmk -C tesis.tex
latexmk -pdf tesis.tex
```

### Compilar la presentacion

Desde `tesis/presentaciones/`:

```bash
cd tesis/presentaciones
pdflatex presentacion.tex
```

## Flujo de graficos en Python

Desde `tesis/graficos/`:

```powershell
python -m pip install -r requirements.txt
python generar_grafico.py
python ejemplos_uso.py
```

La tesis ya esta configurada para buscar imagenes en:

- `../graficos/output/cap1/`
- `../graficos/output/cap2/`
- `../graficos/output/cap3/`
- `../graficos/output/cap4/`
- `../graficos/output/cap5/`
- `../graficos/output/cap6/`
- `../graficos/output/cap7/`
- `../graficos/output/cap8/`
- `../graficos/output/cap10/`

## Archivos principales

- [tesis.tex](tesis/tesis/tesis.tex)
- [ch03-mercado-objetivo.tex](tesis/tesis/src/chapters/ch03-mercado-objetivo.tex)
- [ch05-flujo-ingresos.tex](tesis/tesis/src/chapters/ch05-flujo-ingresos.tex)
- [ch10-evaluacion-economica.tex](tesis/tesis/src/chapters/ch10-evaluacion-economica.tex)
- [presentacion.tex](tesis/presentaciones/presentacion.tex)
- [referencias.bib](tesis/tesis/src/backmatter/referencias.bib)

## Buenas practicas para continuar

- mantener la investigacion fuente dentro de `tesis/tesis/investigaciones/` antes de pasarla a LaTeX;
- actualizar `referencias.bib` cada vez que se añadan nuevas fuentes;
- compilar con frecuencia para detectar desbordes, referencias rotas o tablas fuera de hoja;
- usar graficos cuando ayuden a sintetizar comparaciones o flujos economicos;
- mantener consistencia entre lenguaje contable del capitulo 5 y del capitulo 10;
- usar `tesis-plantilla/` como referencia formal, no como fuente de contenido.

## PDFs principales

- `tesis/tesis/tesis.pdf`
- `tesis/presentaciones/presentacion.pdf`
- `tesis-plantilla/tesis-plantilla.pdf`

## Repositorio remoto

GitHub:

`https://github.com/eduardo202020/Tesis.git`

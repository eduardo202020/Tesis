# MuseIQ - Proyecto de tesis

Repositorio principal del trabajo de tesis MuseIQ. Integra redaccion academica en LaTeX, generacion de graficos en Python, presentacion en Beamer y una simulacion web para demostrar la experiencia de visita en museo.

## Estado actual del trabajo

La tesis ha sido reorganizada y afinada en sus capitulos centrales de soporte conceptual y tecnico. En este momento, el proyecto ya cuenta con una linea argumental clara para:

- Capitulo 6: topicos directamente relacionados con la solucion MuseIQ.
- Capitulo 7: tecnologias base del proyecto.
- Capitulo 8: diseno de los datos de entrada.
- Capitulo 10: evaluacion economica financiera.

Adicionalmente, el Capitulo 7 ya incorpora imagenes de apoyo por subcapitulo en [tesis/tesis/src/imgs/07](tesis/tesis/src/imgs/07), integradas dentro del texto academico.

El principal pendiente estructural en este momento es el Capitulo 9, que debe convertirse en el nucleo de arquitectura, diseno, integracion, implementacion y validacion de la solucion. Actualmente existe el archivo [tesis/tesis/src/chapters/ch09-diseno-despliegue.tex](tesis/tesis/src/chapters/ch09-diseno-despliegue.tex), pero todavia se encuentra en estado preliminar y no forma parte de la compilacion activa de [tesis/tesis/tesis.tex](tesis/tesis/tesis.tex).

## Componentes del repositorio

- Tesis en LaTeX: [tesis/tesis](tesis/tesis)
- Scripts de graficos: [tesis/graficos](tesis/graficos)
- Presentacion: [tesis/presentaciones](tesis/presentaciones)
- Simulacion web: [tesis/simulacion](tesis/simulacion)

## Estructura relevante

- Archivo principal de tesis: [tesis/tesis/tesis.tex](tesis/tesis/tesis.tex)
- Capitulos: [tesis/tesis/src/chapters](tesis/tesis/src/chapters)
- Bibliografia: [tesis/tesis/src/backmatter/referencias.bib](tesis/tesis/src/backmatter/referencias.bib)
- Imagenes del Capitulo 7: [tesis/tesis/src/imgs/07](tesis/tesis/src/imgs/07)
- Graficos generados: [tesis/graficos/output](tesis/graficos/output)
- Presentacion Beamer: [tesis/presentaciones/presentacion.tex](tesis/presentaciones/presentacion.tex)
- App web de simulacion: [tesis/simulacion/index.html](tesis/simulacion/index.html)

## Estado por capitulos

- [ch01-introduccion.tex](tesis/tesis/src/chapters/ch01-introduccion.tex): base del problema, solucion y estado del arte.
- [ch02-panorama-actual.tex](tesis/tesis/src/chapters/ch02-panorama-actual.tex): contexto, necesidad y referentes.
- [ch03-mercado-objetivo.tex](tesis/tesis/src/chapters/ch03-mercado-objetivo.tex): mercado objetivo y panorama nacional.
- [ch04-oferta-tecnologica.tex](tesis/tesis/src/chapters/ch04-oferta-tecnologica.tex): comparacion con oferta mundial.
- [ch05-flujo-ingresos.tex](tesis/tesis/src/chapters/ch05-flujo-ingresos.tex): estructura de ingresos y monetizacion.
- [ch06-offendes.tex](tesis/tesis/src/chapters/ch06-offendes.tex): ya reajustado a la logica de topicos directamente relacionados con la solucion.
- [ch07-transformers.tex](tesis/tesis/src/chapters/ch07-transformers.tex): ya reajustado como capitulo de tecnologias base, con figuras integradas.
- [ch08-datos-entrada.tex](tesis/tesis/src/chapters/ch08-datos-entrada.tex): ya reajustado como capitulo de datos de entrada y contrato de datos.
- [ch09-diseno-despliegue.tex](tesis/tesis/src/chapters/ch09-diseno-despliegue.tex): pendiente principal; debe desarrollarse como capitulo de arquitectura general, diseno de subsistemas, integracion, implementacion y validacion.
- [ch10-evaluacion-economica.tex](tesis/tesis/src/chapters/ch10-evaluacion-economica.tex): desarrollo economico-financiero ya presente.
- [ch11-normas-tecnicas.tex](tesis/tesis/src/chapters/ch11-normas-tecnicas.tex): pendiente de consolidacion.
- [ch12-conclusiones.tex](tesis/tesis/src/chapters/ch12-conclusiones.tex): pendiente de cierre final.

## Compilar la tesis

Desde la raiz del repo:

cd tesis/tesis
latexmk -pdf tesis.tex

Nota actual:

- La compilacion principal todavia tiene comentados los capitulos 9, 11 y 12 en [tesis/tesis/tesis.tex](tesis/tesis/tesis.tex).
- Antes de considerar la tesis como estructuralmente completa, se debe desarrollar e incorporar el Capitulo 9.

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
2. Mantener consistencia estructural entre capitulos 6, 7, 8 y el futuro desarrollo del 9.
3. Desarrollar [ch09-diseno-despliegue.tex](tesis/tesis/src/chapters/ch09-diseno-despliegue.tex) como prioridad principal.
4. Generar o actualizar figuras en [tesis/graficos](tesis/graficos) y, cuando aplique, imagenes tematicas en [tesis/tesis/src/imgs](tesis/tesis/src/imgs).
5. Pasar el contenido academico a [tesis/tesis/src/chapters](tesis/tesis/src/chapters).
6. Reactivar la inclusion del Capitulo 9 en [tesis/tesis/tesis.tex](tesis/tesis/tesis.tex) y compilar tesis y presentacion.
7. Validar simulacion web.
8. Hacer commit y push para actualizar GitHub Pages.

## Prioridades inmediatas

1. Completar el Capitulo 9 con arquitectura general del sistema, diseno de subsistemas, diseno computacional, integracion e interfaces, implementacion/prototipo y pruebas o validacion.
2. Reactivar en la compilacion los capitulos 9, 11 y 12 conforme vayan quedando listos.
3. Revisar el flujo completo del documento compilado para asegurar continuidad entre tecnologias, datos, arquitectura y evaluacion economica.

# Graficos de la tesis

Esta carpeta contiene los scripts de Python para generar figuras usadas en la tesis y en la presentacion.

## Archivos principales

- Generador base: [generar_grafico.py](generar_grafico.py)
- Casos de uso y lotes: [ejemplos_uso.py](ejemplos_uso.py)
- Dependencias: [requirements.txt](requirements.txt)
- Salida de imagenes: [output](output)

## Estructura de salida

Las imagenes se guardan por capitulo dentro de [output](output):

- [output/cap1](output/cap1)
- [output/cap2](output/cap2)
- [output/cap3](output/cap3)
- [output/cap4](output/cap4)
- [output/cap5](output/cap5)
- [output/cap6](output/cap6)
- [output/cap7](output/cap7)
- [output/cap8](output/cap8)
- [output/cap10](output/cap10)

## Uso rapido

Desde la raiz del repo:

cd tesis/graficos
python -m pip install -r requirements.txt
python ejemplos_uso.py all

## Generacion por capitulo

Ejemplos:

python ejemplos_uso.py cap1
python ejemplos_uso.py cap4
python ejemplos_uso.py cap10

## Generacion de un grafico puntual

python ejemplos_uso.py mapa_segmentacion_mercado_objetivo

Para ver opciones disponibles:

python ejemplos_uso.py --help

## Modos soportados en ejemplos_uso.py

- all o todo: regenera todo el lote
- cap1, cap2, cap3, cap4, cap5, cap6, cap7, cap8, cap10: regenera por capitulo
- nombre_de_grafico: regenera solo esa imagen

## Tipos de graficos disponibles

- Barras verticales
- Barras horizontales
- Lineas
- Lineas multiples
- Pastel
- Dispersion
- Heatmap
- Diagramas conceptuales

## Como ampliar

1. Agregar o ajustar datos en [ejemplos_uso.py](ejemplos_uso.py).
2. Si hace falta, ampliar funciones en [generar_grafico.py](generar_grafico.py).
3. Regenerar solo lo necesario para iterar mas rapido.

## Insercion en LaTeX

La tesis ya referencia las carpetas de output mediante graphicspath. Una vez generado el archivo PNG, puede incluirse en el capitulo correspondiente.

## Convencion de nombres recomendada

- mercado_objetivo_museos.png
- flujo_ingresos_10_anios.png
- comparacion_costos_operativos.png
- presupuesto_directo_indirecto.png
- proyeccion_visitantes.png

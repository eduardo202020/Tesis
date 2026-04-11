# Graficos de la tesis

Esta carpeta concentra los graficos generados en Python para usarlos dentro de la tesis.

## Estructura

- `generar_grafico.py`: libreria base con funciones para varios tipos de graficos.
- `ejemplos_uso.py`: archivo editable con ejemplos concretos para la tesis.
- `output/`: carpeta donde se guardan los archivos generados (`.png`).
- `requirements.txt`: dependencias minimas del script.

## Uso rapido

Desde esta carpeta:

```powershell
python -m pip install -r requirements.txt
python ejemplos_uso.py all
```

Para generar por capitulo:

```powershell
python ejemplos_uso.py cap1
python ejemplos_uso.py cap4
python ejemplos_uso.py cap10
```

Para generar un solo grafico:

```powershell
python ejemplos_uso.py mapa_segmentacion_mercado_objetivo
```

Para ver los nombres disponibles:

```powershell
python ejemplos_uso.py --help
```

El script `generar_grafico.py` contiene la libreria base.

`ejemplos_uso.py` ahora tiene dos modos:

- `all` o `todo`: regenera todo el lote
- `cap1`, `cap2`, `cap3`, `cap4`, `cap5`, `cap6`, `cap10`: generan solo los graficos de ese capitulo
- `<nombre_grafico>`: genera solo una imagen puntual

Entre los nombres disponibles estan, por ejemplo:

- `smartphones_peru`
- `visitas_museos`
- `mapa_problema`
- `arquitectura_conceptual`
- `mapa_segmentacion_mercado_objetivo`
- `categorias_oferta_tecnologica_mundial`
- `flujo_ingresos`
- `sensibilidad_van`

## Tipos de graficos disponibles

- barras verticales
- barras horizontales
- lineas
- lineas multiples
- pastel
- dispersion
- heatmap
- diagramas conceptuales

## Como adaptarlo

Si quieres crear tus propios graficos para la tesis, lo mas comodo es editar:

- `ejemplos_uso.py`

Si quieres ampliar la libreria base, modifica:

- `generar_grafico.py`

### Funciones disponibles

- `grafico_barras(...)`
- `grafico_barras_horizontales(...)`
- `grafico_lineas(...)`
- `grafico_lineas_multiples(...)`
- `grafico_pastel(...)`
- `grafico_dispersion(...)`
- `grafico_heatmap(...)`

Luego genera solo el grafico que cambiaste:

```powershell
python ejemplos_uso.py nombre_del_grafico
```

## Como insertarlo en LaTeX

Como `tesis.tex` ya fue configurado con:

```latex
\graphicspath{{../graficos/output/}}
```

puedes insertar un grafico asi:

```latex
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.82\textwidth]{ejemplo_barras.png}
    \caption{Distribucion de ejemplo.}
    \label{fig:ejemplo-barras}
\end{figure}
```

## Convencion recomendada

Usa nombres descriptivos, por ejemplo:

- `mercado_objetivo_museos.png`
- `flujo_ingresos_10_anios.png`
- `comparacion_costos_operativos.png`
- `presupuesto_directo_indirecto.png`
- `proyeccion_visitantes.png`

Asi luego sera mas facil pedir nuevos graficos y referenciarlos en la tesis.

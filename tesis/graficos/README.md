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
python generar_grafico.py
python ejemplos_uso.py
```

Los scripts generan por defecto:

- `output/ejemplo_barras.png`
- `output/ejemplo_lineas.png`
- `output/ejemplo_pastel.png`
- `output/ejemplo_barras_horizontales.png`
- `output/ejemplo_dispersion.png`
- y varios ejemplos definidos en `ejemplos_uso.py`

## Tipos de graficos disponibles

- barras verticales
- barras horizontales
- lineas
- pastel
- dispersion

## Como adaptarlo

Si quieres crear tus propios graficos para la tesis, lo mas comodo es editar:

- `ejemplos_uso.py`

Si quieres ampliar la libreria base, modifica:

- `generar_grafico.py`

### Funciones disponibles

- `grafico_barras(...)`
- `grafico_barras_horizontales(...)`
- `grafico_lineas(...)`
- `grafico_pastel(...)`
- `grafico_dispersion(...)`

Luego vuelve a correr:

```powershell
python ejemplos_uso.py
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

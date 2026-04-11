from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PALETA = [
    "#9EDBF0",
    "#F5A623",
    "#2E8B57",
    "#D95C5C",
    "#7A5AF8",
    "#6B7280",
    "#123C69",
    "#D9A441",
]


def _guardar_figura(fig, nombre_salida):
    output_path = OUTPUT_DIR / nombre_salida
    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Grafico generado en: {output_path}")


def grafico_barras(
    categorias,
    valores,
    titulo,
    eje_x,
    eje_y,
    nombre_salida,
    etiquetas=None,
):
    fig, ax = plt.subplots(figsize=(10, 5.5))
    bars = ax.bar(categorias, valores, color=PALETA[: len(categorias)], width=0.55)

    ax.set_title(titulo, fontsize=13)
    ax.set_xlabel(eje_x)
    ax.set_ylabel(eje_y)
    ax.grid(axis="y", linestyle="--", alpha=0.25)

    ymax = max(valores) * 1.15
    ax.set_ylim(0, ymax)

    if etiquetas:
        for bar, texto in zip(bars, etiquetas):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + ymax * 0.015,
                texto,
                ha="center",
                va="bottom",
                fontsize=10,
            )

    _guardar_figura(fig, nombre_salida)


def grafico_barras_horizontales(
    categorias,
    valores,
    titulo,
    eje_x,
    eje_y,
    nombre_salida,
    etiquetas=None,
):
    fig, ax = plt.subplots(figsize=(10, 5.5))
    bars = ax.barh(categorias, valores, color=PALETA[: len(categorias)])

    ax.set_title(titulo, fontsize=13)
    ax.set_xlabel(eje_x)
    ax.set_ylabel(eje_y)
    ax.grid(axis="x", linestyle="--", alpha=0.25)

    xmax = max(valores) * 1.18
    ax.set_xlim(0, xmax)

    if etiquetas:
        for bar, texto in zip(bars, etiquetas):
            ax.text(
                bar.get_width() + xmax * 0.01,
                bar.get_y() + bar.get_height() / 2,
                texto,
                va="center",
                fontsize=10,
            )

    _guardar_figura(fig, nombre_salida)


def grafico_lineas(
    x,
    y,
    titulo,
    eje_x,
    eje_y,
    nombre_salida,
    serie="Serie",
    mostrar_puntos=True,
):
    fig, ax = plt.subplots(figsize=(10, 5.5))
    marker = "o" if mostrar_puntos else None
    ax.plot(x, y, marker=marker, linewidth=2.2, color="#123C69", label=serie)

    ax.set_title(titulo, fontsize=13)
    ax.set_xlabel(eje_x)
    ax.set_ylabel(eje_y)
    ax.grid(True, linestyle="--", alpha=0.3)
    ax.legend(frameon=False)

    _guardar_figura(fig, nombre_salida)


def grafico_pastel(
    categorias,
    valores,
    titulo,
    nombre_salida,
):
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(
        valores,
        labels=categorias,
        autopct="%1.1f%%",
        startangle=90,
        colors=PALETA[: len(categorias)],
        wedgeprops={"edgecolor": "white", "linewidth": 1},
    )
    ax.set_title(titulo, fontsize=13)
    ax.axis("equal")

    _guardar_figura(fig, nombre_salida)


def grafico_dispersion(
    x,
    y,
    titulo,
    eje_x,
    eje_y,
    nombre_salida,
):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.scatter(x, y, s=70, color="#2E8B57", alpha=0.85, edgecolors="black", linewidth=0.4)

    ax.set_title(titulo, fontsize=13)
    ax.set_xlabel(eje_x)
    ax.set_ylabel(eje_y)
    ax.grid(True, linestyle="--", alpha=0.3)

    _guardar_figura(fig, nombre_salida)


if __name__ == "__main__":
    # Ejemplo 1: barras
    grafico_barras(
        categorias=["NO", "OFF", "NOE", "OFG"],
        valores=[23000, 4500, 2700, 400],
        etiquetas=["75.4%", "14.5%", "8.7%", "1.4%"],
        titulo="Distribucion de etiquetado",
        eje_x="Etiqueta",
        eje_y="Cantidad",
        nombre_salida="ejemplo_barras.png",
    )

    # Ejemplo 2: lineas
    grafico_lineas(
        x=[2025, 2026, 2027, 2028, 2029],
        y=[6400, 13780, 22855, 34152, 42812],
        titulo="Evolucion de ingresos proyectados",
        eje_x="Anio",
        eje_y="Ingresos (USD)",
        nombre_salida="ejemplo_lineas.png",
        serie="Ingresos",
    )

    # Ejemplo 3: pastel
    grafico_pastel(
        categorias=["Implementacion", "Operacion", "Soporte", "Otros"],
        valores=[45, 30, 15, 10],
        titulo="Composicion porcentual de rubros",
        nombre_salida="ejemplo_pastel.png",
    )

    # Ejemplo 4: barras horizontales
    grafico_barras_horizontales(
        categorias=["Museos publicos", "Museos privados", "Centros culturales"],
        valores=[56, 18, 12],
        etiquetas=["56", "18", "12"],
        titulo="Mercado institucional de referencia",
        eje_x="Cantidad estimada",
        eje_y="Segmento",
        nombre_salida="ejemplo_barras_horizontales.png",
    )

    # Ejemplo 5: dispersion
    grafico_dispersion(
        x=[1, 2, 3, 4, 5],
        y=[2.3, 2.9, 4.1, 5.0, 5.8],
        titulo="Relacion entre salas y costo de implementacion",
        eje_x="Numero de salas",
        eje_y="Costo relativo",
        nombre_salida="ejemplo_dispersion.png",
    )

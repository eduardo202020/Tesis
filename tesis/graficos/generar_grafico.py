from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D


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


def grafico_lineas_multiples(
    x,
    series,
    titulo,
    eje_x,
    eje_y,
    nombre_salida,
):
    fig, ax = plt.subplots(figsize=(10, 5.5))

    for indice, serie in enumerate(series):
        color = PALETA[indice % len(PALETA)]
        ax.plot(
            x,
            serie["y"],
            marker="o",
            linewidth=2.2,
            color=color,
            label=serie["nombre"],
        )

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


def grafico_heatmap(
    matriz,
    etiquetas_filas,
    etiquetas_columnas,
    titulo,
    nombre_salida,
    mapa_color="YlGnBu",
):
    fig, ax = plt.subplots(figsize=(11, 6))
    imagen = ax.imshow(matriz, cmap=mapa_color, aspect="auto", vmin=0, vmax=1)

    ax.set_title(titulo, fontsize=13)
    ax.set_xticks(np.arange(len(etiquetas_columnas)))
    ax.set_yticks(np.arange(len(etiquetas_filas)))
    ax.set_xticklabels(etiquetas_columnas)
    ax.set_yticklabels(etiquetas_filas)
    plt.setp(ax.get_xticklabels(), rotation=25, ha="right", rotation_mode="anchor")

    for fila in range(len(etiquetas_filas)):
        for columna in range(len(etiquetas_columnas)):
            valor = matriz[fila][columna]
            texto = f"{valor:.1f}" if valor not in (0, 1) else str(int(valor))
            color = "white" if valor >= 0.6 else "black"
            ax.text(columna, fila, texto, ha="center", va="center", color=color, fontsize=9)

    cbar = fig.colorbar(imagen, ax=ax, shrink=0.9)
    cbar.set_label("Presencia relativa de capacidad")

    _guardar_figura(fig, nombre_salida)


def grafico_diagrama_museiq_componentes(nombre_salida):
    fig, ax = plt.subplots(figsize=(12, 6.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    def caja(x, y, w, h, texto, color):
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            linewidth=1.5,
            edgecolor="#123C69",
            facecolor=color,
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=10, color="#102A43")

    caja(0.5, 4.8, 2.2, 1.0, "Visitante", "#D9F0F7")
    caja(0.5, 2.0, 2.2, 1.0, "Sala / zona\nmuseistica", "#D9F0F7")
    caja(3.3, 4.8, 2.6, 1.0, "Smartphone del\nvisitante", "#FCE7B2")
    caja(3.3, 2.0, 2.6, 1.0, "Beacons BLE +\nsensores", "#FCE7B2")
    caja(6.4, 4.8, 2.4, 1.0, "Motor de contexto", "#D8F3DC")
    caja(6.4, 2.0, 2.4, 1.0, "Corpus curatorial", "#D8F3DC")
    caja(9.3, 3.35, 2.1, 1.2, "RAG + asistente\nconversacional", "#F9D6D5")

    flechas = [
        ((2.7, 5.3), (3.3, 5.3)),
        ((4.6, 3.0), (4.6, 4.8)),
        ((5.9, 5.3), (6.4, 5.3)),
        ((5.9, 2.5), (6.4, 2.5)),
        ((8.8, 5.3), (9.3, 4.2)),
        ((8.8, 2.5), (9.3, 3.9)),
        ((11.4, 3.95), (11.9, 3.95)),
    ]

    for inicio, fin in flechas:
        ax.annotate("", xy=fin, xytext=inicio, arrowprops=dict(arrowstyle="->", lw=1.8, color="#123C69"))

    ax.text(11.95, 3.95, "Respuesta\ncontextual\nvoz / texto", ha="left", va="center", fontsize=10, color="#102A43")
    ax.set_title("Relacion conceptual entre los componentes principales de MuseIQ", fontsize=14, color="#102A43", pad=14)

    _guardar_figura(fig, nombre_salida)


def grafico_diagrama_principios_museiq(nombre_salida):
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    def caja(x, y, w, h, texto, color):
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.03,rounding_size=0.12",
            linewidth=1.5,
            edgecolor="#123C69",
            facecolor=color,
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=10, color="#102A43")

    caja(3.4, 3.2, 3.2, 1.4, "MuseIQ\nfundamentos de la propuesta", "#E8F1FA")
    caja(0.7, 5.8, 2.3, 1.0, "Contextualizacion\nsituada", "#D9F0F7")
    caja(3.85, 6.5, 2.3, 1.0, "Accesibilidad\npor voz", "#FCE7B2")
    caja(7.0, 5.8, 2.3, 1.0, "Trazabilidad y\ncontrol", "#F9D6D5")
    caja(0.7, 1.1, 2.3, 1.0, "Localizacion\nfuncional", "#D8F3DC")
    caja(3.85, 0.3, 2.3, 1.0, "Modularidad y\nescalabilidad", "#EADCF8")
    caja(7.0, 1.1, 2.3, 1.0, "Bajo costo y\nviabilidad", "#E8E8E8")

    conexiones = [
        ((5.0, 4.6), (1.85, 5.8)),
        ((5.0, 4.6), (5.0, 6.5)),
        ((5.0, 4.6), (8.15, 5.8)),
        ((5.0, 3.2), (1.85, 2.1)),
        ((5.0, 3.2), (5.0, 1.3)),
        ((5.0, 3.2), (8.15, 2.1)),
    ]

    for inicio, fin in conexiones:
        ax.annotate("", xy=fin, xytext=inicio, arrowprops=dict(arrowstyle="->", lw=1.8, color="#123C69"))

    ax.set_title("Principios que sostienen la propuesta MuseIQ", fontsize=14, color="#102A43", pad=14)

    _guardar_figura(fig, nombre_salida)


def grafico_mapa_problema_central(nombre_salida):
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    def caja(x, y, w, h, texto, color):
        patch = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.03,rounding_size=0.12",
            linewidth=1.5, edgecolor="#123C69", facecolor=color
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=10, color="#102A43")

    caja(0.6, 5.8, 2.6, 1.0, "Mayor adopcion\nde smartphones", "#D9F0F7")
    caja(0.6, 4.0, 2.6, 1.0, "Recuperacion de\nvisitas a museos", "#D9F0F7")
    caja(0.6, 2.2, 2.6, 1.0, "Demanda de experiencias\nmas autonomas", "#D9F0F7")

    caja(4.2, 4.0, 3.6, 1.5, "Mediacion tradicional limitada:\ncartelas, recorridos lineales\ny baja personalizacion", "#FCE7B2")
    caja(4.2, 1.5, 3.6, 1.3, "Brechas funcionales:\naccesibilidad, orientacion y\nrespuesta contextual", "#F9D6D5")
    caja(8.6, 3.1, 2.6, 1.7, "Necesidad de\nMuseIQ", "#D8F3DC")

    flechas = [
        ((3.2, 6.3), (4.2, 5.1)),
        ((3.2, 4.5), (4.2, 4.8)),
        ((3.2, 2.7), (4.2, 4.4)),
        ((6.0, 4.0), (6.0, 2.8)),
        ((7.8, 4.75), (8.6, 4.1)),
        ((7.8, 2.15), (8.6, 3.8)),
    ]
    for inicio, fin in flechas:
        ax.annotate("", xy=fin, xytext=inicio, arrowprops=dict(arrowstyle="->", lw=1.8, color="#123C69"))

    ax.set_title("Mapa conceptual del problema central abordado por MuseIQ", fontsize=14, color="#102A43", pad=14)
    _guardar_figura(fig, nombre_salida)


def grafico_arquitectura_conceptual_museiq(nombre_salida):
    fig, ax = plt.subplots(figsize=(12.5, 6.8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)
    ax.axis("off")

    def caja(x, y, w, h, texto, color):
        patch = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.03,rounding_size=0.12",
            linewidth=1.5, edgecolor="#123C69", facecolor=color
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=10, color="#102A43")

    caja(0.5, 2.9, 1.9, 1.1, "Visitante", "#D9F0F7")
    caja(2.8, 4.6, 2.4, 1.0, "Smartphone", "#FCE7B2")
    caja(2.8, 1.4, 2.4, 1.0, "BLE + sensores", "#FCE7B2")
    caja(5.8, 4.6, 2.5, 1.0, "Motor de contexto", "#D8F3DC")
    caja(5.8, 1.4, 2.5, 1.0, "Repositorio curatorial", "#D8F3DC")
    caja(8.9, 2.9, 2.4, 1.1, "RAG + asistente", "#F9D6D5")
    caja(11.6, 2.9, 1.1, 1.1, "Respuesta\nvoz/texto", "#E8F1FA")

    flechas = [
        ((2.4, 3.45), (2.8, 5.1)),
        ((2.4, 3.45), (2.8, 1.9)),
        ((5.2, 5.1), (5.8, 5.1)),
        ((5.2, 1.9), (5.8, 1.9)),
        ((8.3, 5.1), (8.9, 3.55)),
        ((8.3, 1.9), (8.9, 3.35)),
        ((11.3, 3.45), (11.6, 3.45)),
    ]
    for inicio, fin in flechas:
        ax.annotate("", xy=fin, xytext=inicio, arrowprops=dict(arrowstyle="->", lw=1.8, color="#123C69"))

    ax.set_title("Arquitectura conceptual general de la solucion MuseIQ", fontsize=14, color="#102A43", pad=14)
    _guardar_figura(fig, nombre_salida)


def grafico_relacion_problema_solucion_aporte(nombre_salida):
    fig, ax = plt.subplots(figsize=(12.5, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    columnas_x = [0.6, 4.3, 8.0]
    titulos = ["Problema", "Respuesta de MuseIQ", "Aporte esperado"]
    colores = ["#F9D6D5", "#D8F3DC", "#D9F0F7"]
    contenidos = [
        [
            "Mediacion estatica",
            "Baja accesibilidad",
            "Poca orientacion en sala",
            "Sin personalizacion",
        ],
        [
            "Reconocimiento por sala",
            "Interaccion por voz",
            "Contenido contextual",
            "Arquitectura ligera",
        ],
        [
            "Mejor comprension",
            "Mayor autonomia",
            "Escalabilidad institucional",
            "Base para validacion",
        ],
    ]

    for col, x in enumerate(columnas_x):
        ax.text(x + 1.35, 7.2, titulos[col], ha="center", va="center", fontsize=13, color="#102A43", weight="bold")
        for fila, texto in enumerate(contenidos[col]):
            y = 5.8 - fila * 1.4
            patch = FancyBboxPatch(
                (x, y), 2.7, 0.85,
                boxstyle="round,pad=0.03,rounding_size=0.10",
                linewidth=1.3, edgecolor="#123C69", facecolor=colores[col]
            )
            ax.add_patch(patch)
            ax.text(x + 1.35, y + 0.425, texto, ha="center", va="center", fontsize=10, color="#102A43")

    for fila in range(4):
        y = 6.2 - fila * 1.4
        ax.annotate("", xy=(4.3, y), xytext=(3.3, y), arrowprops=dict(arrowstyle="->", lw=1.6, color="#123C69"))
        ax.annotate("", xy=(8.0, y), xytext=(7.0, y), arrowprops=dict(arrowstyle="->", lw=1.6, color="#123C69"))

    ax.set_title("Relacion entre el problema identificado, la solucion y el aporte de MuseIQ", fontsize=14, color="#102A43", pad=14)
    _guardar_figura(fig, nombre_salida)


def grafico_brecha_demanda_mediacion(nombre_salida):
    fig, ax = plt.subplots(figsize=(12.5, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    izquierda = FancyBboxPatch((0.7, 1.1), 4.3, 5.9, boxstyle="round,pad=0.03,rounding_size=0.12",
                               linewidth=1.6, edgecolor="#123C69", facecolor="#D9F0F7")
    derecha = FancyBboxPatch((7.0, 1.1), 4.3, 5.9, boxstyle="round,pad=0.03,rounding_size=0.12",
                             linewidth=1.6, edgecolor="#123C69", facecolor="#FCE7B2")
    ax.add_patch(izquierda)
    ax.add_patch(derecha)

    ax.text(2.85, 6.4, "Demanda cultural y digital", ha="center", va="center", fontsize=13, weight="bold", color="#102A43")
    ax.text(9.15, 6.4, "Mediacion disponible", ha="center", va="center", fontsize=13, weight="bold", color="#102A43")

    izq = [
        "Mas visitas presenciales",
        "Mayor uso de smartphone",
        "Expectativa de informacion inmediata",
        "Necesidad de accesibilidad",
    ]
    der = [
        "Cartelas y paneles",
        "Audioguias lineales",
        "Poca personalizacion",
        "Baja respuesta contextual",
    ]
    for i, texto in enumerate(izq):
        ax.text(1.2, 5.5 - i * 1.1, f"• {texto}", fontsize=11, color="#102A43")
    for i, texto in enumerate(der):
        ax.text(7.5, 5.5 - i * 1.1, f"• {texto}", fontsize=11, color="#102A43")

    ax.annotate("", xy=(7.0, 4.0), xytext=(5.0, 4.0), arrowprops=dict(arrowstyle="<->", lw=2.0, color="#D95C5C"))
    ax.text(6.0, 4.35, "Brecha de mediacion digital", ha="center", fontsize=11, color="#D95C5C", weight="bold")

    ax.set_title("Brecha entre la demanda cultural actual y la mediacion digital disponible", fontsize=14, color="#102A43", pad=14)
    _guardar_figura(fig, nombre_salida)


def grafico_ecosistema_museos_inteligentes(nombre_salida):
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    centro = FancyBboxPatch((4.4, 3.2), 3.2, 1.4, boxstyle="round,pad=0.03,rounding_size=0.12",
                            linewidth=1.6, edgecolor="#123C69", facecolor="#E8F1FA")
    ax.add_patch(centro)
    ax.text(6.0, 3.9, "Ecosistema actual de\nmuseos inteligentes", ha="center", va="center", fontsize=12, color="#102A43")

    nodos = [
        {"x": 0.7, "y": 5.7, "w": 2.8, "h": 1.0, "texto": "Acceso movil\nBYOD", "color": "#D9F0F7", "inicio": (3.5, 6.0), "fin": (4.4, 4.25)},
        {"x": 4.6, "y": 6.3, "w": 2.8, "h": 1.0, "texto": "Localizacion\nindoor", "color": "#FCE7B2", "inicio": (6.0, 6.3), "fin": (6.0, 4.6)},
        {"x": 8.5, "y": 5.7, "w": 2.8, "h": 1.0, "texto": "Accesibilidad\ny voz", "color": "#D8F3DC", "inicio": (8.5, 6.0), "fin": (7.6, 4.25)},
        {"x": 0.7, "y": 1.3, "w": 2.8, "h": 1.0, "texto": "Analitica de\nrecorridos", "color": "#F9D6D5", "inicio": (3.5, 1.9), "fin": (4.4, 3.55)},
        {"x": 4.6, "y": 0.5, "w": 2.8, "h": 1.0, "texto": "Contenido\ncuratorial digital", "color": "#EADCF8", "inicio": (6.0, 1.5), "fin": (6.0, 3.2)},
        {"x": 8.5, "y": 1.3, "w": 2.8, "h": 1.0, "texto": "IA contextual y\npersonalizacion", "color": "#E8E8E8", "inicio": (8.5, 1.9), "fin": (7.6, 3.55)},
    ]
    for nodo in nodos:
        x, y, w, h = nodo["x"], nodo["y"], nodo["w"], nodo["h"]
        patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.10",
                               linewidth=1.4, edgecolor="#123C69", facecolor=nodo["color"])
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, nodo["texto"], ha="center", va="center", fontsize=10, color="#102A43")
        ax.annotate("", xy=nodo["fin"], xytext=nodo["inicio"],
                    arrowprops=dict(arrowstyle="->", lw=1.6, color="#123C69"))

    ax.set_title("Componentes principales del ecosistema actual de museos inteligentes", fontsize=14, color="#102A43", pad=14)
    _guardar_figura(fig, nombre_salida)


def grafico_ruta_validacion(nombre_salida):
    fig, ax = plt.subplots(figsize=(13, 4.8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 5)
    ax.axis("off")

    etapas = [
        "Despliegue\npiloto",
        "Reconocimiento\nde sala",
        "Prueba de\norientacion",
        "Interaccion\npor voz",
        "Evaluacion de\nexperiencia",
    ]
    colores = ["#D9F0F7", "#FCE7B2", "#D8F3DC", "#F9D6D5", "#E8F1FA"]
    xs = [0.5, 3.0, 5.5, 8.0, 10.5]
    for x, texto, color in zip(xs, etapas, colores):
        patch = FancyBboxPatch((x, 1.7), 2.0, 1.3, boxstyle="round,pad=0.03,rounding_size=0.10",
                               linewidth=1.4, edgecolor="#123C69", facecolor=color)
        ax.add_patch(patch)
        ax.text(x + 1.0, 2.35, texto, ha="center", va="center", fontsize=10, color="#102A43")
    for i in range(len(xs) - 1):
        ax.annotate("", xy=(xs[i + 1], 2.35), xytext=(xs[i] + 2.0, 2.35),
                    arrowprops=dict(arrowstyle="->", lw=1.8, color="#123C69"))

    ax.set_title("Ruta metodologica sugerida para la validacion de MuseIQ", fontsize=14, color="#102A43", pad=12)
    _guardar_figura(fig, nombre_salida)


def grafico_mapa_segmentacion(nombre_salida):
    fig, ax = plt.subplots(figsize=(11.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    centro = FancyBboxPatch((3.5, 3.2), 3.0, 1.3, boxstyle="round,pad=0.03,rounding_size=0.10",
                            linewidth=1.5, edgecolor="#123C69", facecolor="#E8F1FA")
    ax.add_patch(centro)
    ax.text(5.0, 3.85, "Mercado objetivo\nMuseIQ", ha="center", va="center", fontsize=12, color="#102A43")

    nodos = [
        {"x": 0.7, "y": 5.8, "w": 3.0, "h": 1.4, "texto": "Mercado primario\nMuseos publicos\ny de sitio", "color": "#D8F3DC", "inicio": (3.7, 6.2), "fin": (4.2, 4.25)},
        {"x": 6.3, "y": 5.8, "w": 3.0, "h": 1.4, "texto": "Mercado secundario\nMuseos privados,\nuniversitarios", "color": "#FCE7B2", "inicio": (6.3, 6.2), "fin": (5.8, 4.25)},
        {"x": 3.5, "y": 0.8, "w": 3.0, "h": 1.4, "texto": "Mercado potencial\nCentros culturales y\nsitios ampliados", "color": "#D9F0F7", "inicio": (5.0, 2.2), "fin": (5.0, 3.2)},
    ]
    for nodo in nodos:
        x, y, w, h = nodo["x"], nodo["y"], nodo["w"], nodo["h"]
        patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.10",
                               linewidth=1.4, edgecolor="#123C69", facecolor=nodo["color"])
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, nodo["texto"], ha="center", va="center", fontsize=10, color="#102A43")
        ax.annotate("", xy=nodo["fin"], xytext=nodo["inicio"],
                    arrowprops=dict(arrowstyle="->", lw=1.6, color="#123C69"))

    ax.set_title("Mapa conceptual de segmentacion del mercado objetivo", fontsize=14, color="#102A43", pad=14)
    _guardar_figura(fig, nombre_salida)


def grafico_criterios_mercado_prioritario(nombre_salida):
    fig, ax = plt.subplots(figsize=(11.5, 6.8))
    ax.axis("off")

    filas = ["Museos publicos", "Museos privados", "Universitarios", "Centros culturales"]
    columnas = ["Viabilidad tecnica", "Impacto social", "Facilidad de validacion", "Escalabilidad"]
    matriz = np.array([
        [0.9, 1.0, 0.9, 0.8],
        [0.7, 0.5, 0.6, 0.7],
        [0.7, 0.6, 0.7, 0.6],
        [0.6, 0.6, 0.5, 0.7],
    ])

    tabla = ax.table(
        cellText=[[f"{v:.1f}" for v in fila] for fila in matriz],
        rowLabels=filas,
        colLabels=columnas,
        loc="center",
        cellLoc="center",
    )
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1, 2.0)

    for (fila, col), cell in tabla.get_celld().items():
        cell.set_edgecolor("#123C69")
        if fila == 0:
            cell.set_facecolor("#E8F1FA")
            cell.set_text_props(weight="bold", color="#102A43")
        elif col == -1:
            cell.set_facecolor("#F5F7FA")
            cell.set_text_props(weight="bold", color="#102A43")
        else:
            valor = matriz[fila - 1, col]
            if valor >= 0.9:
                cell.set_facecolor("#D8F3DC")
            elif valor >= 0.7:
                cell.set_facecolor("#FCE7B2")
            else:
                cell.set_facecolor("#F9D6D5")

    ax.set_title("Criterios comparativos para elegir el mercado objetivo prioritario", fontsize=14, color="#102A43", pad=16)
    _guardar_figura(fig, nombre_salida)


def grafico_ecosistema_nacional_adopcion(nombre_salida):
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    def nodo(x, y, w, h, texto, color):
        patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.10",
                               linewidth=1.4, edgecolor="#123C69", facecolor=color)
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=10, color="#102A43")

    nodo(4.2, 3.1, 3.0, 1.4, "MuseIQ en el\ncontexto nacional", "#E8F1FA")
    nodo(0.7, 5.7, 2.8, 1.0, "Ministerio de Cultura\ny museos publicos", "#D8F3DC")
    nodo(8.5, 5.7, 2.8, 1.0, "Visitantes con\nsmartphone", "#D9F0F7")
    nodo(0.7, 1.3, 2.8, 1.0, "Plataformas digitales\nexistentes", "#FCE7B2")
    nodo(8.5, 1.3, 2.8, 1.0, "Oportunidad de\nmediacion inteligente", "#F9D6D5")

    conexiones = [
        ((3.5, 6.2), (4.2, 4.2)),
        ((8.5, 6.2), (7.2, 4.2)),
        ((3.5, 1.8), (4.2, 3.4)),
        ((8.5, 1.8), (7.2, 3.4)),
    ]
    for inicio, fin in conexiones:
        ax.annotate("", xy=fin, xytext=inicio, arrowprops=dict(arrowstyle="->", lw=1.7, color="#123C69"))

    ax.set_title("Ecosistema nacional de adopcion de MuseIQ", fontsize=14, color="#102A43", pad=14)
    _guardar_figura(fig, nombre_salida)


def grafico_categorias_oferta_mundial(nombre_salida):
    fig, ax = plt.subplots(figsize=(12.5, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    centro = FancyBboxPatch((4.3, 3.2), 3.4, 1.4, boxstyle="round,pad=0.03,rounding_size=0.12",
                            linewidth=1.6, edgecolor="#123C69", facecolor="#E8F1FA")
    ax.add_patch(centro)
    ax.text(6.0, 3.9, "Oferta tecnologica\nmundial", ha="center", va="center", fontsize=12, color="#102A43")

    nodos = [
        {"x": 0.6, "y": 5.7, "w": 2.9, "h": 1.0, "texto": "Audioguias\ntradicionales", "color": "#FCE7B2", "inicio": (3.5, 6.0), "fin": (4.3, 4.25)},
        {"x": 4.55, "y": 6.25, "w": 2.9, "h": 1.0, "texto": "Apps BYOD y\nCMS", "color": "#D9F0F7", "inicio": (6.0, 6.25), "fin": (6.0, 4.6)},
        {"x": 8.5, "y": 5.7, "w": 2.9, "h": 1.0, "texto": "QR / PWA", "color": "#D8F3DC", "inicio": (8.5, 6.0), "fin": (7.7, 4.25)},
        {"x": 0.6, "y": 1.2, "w": 2.9, "h": 1.0, "texto": "BLE y\nproximidad", "color": "#F9D6D5", "inicio": (3.5, 1.8), "fin": (4.3, 3.55)},
        {"x": 4.55, "y": 0.55, "w": 2.9, "h": 1.0, "texto": "Indoor\nnavigation", "color": "#EADCF8", "inicio": (6.0, 1.55), "fin": (6.0, 3.2)},
        {"x": 8.5, "y": 1.2, "w": 2.9, "h": 1.0, "texto": "IA\nconversacional", "color": "#E8E8E8", "inicio": (8.5, 1.8), "fin": (7.7, 3.55)},
    ]
    for nodo in nodos:
        x, y, w, h = nodo["x"], nodo["y"], nodo["w"], nodo["h"]
        patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.10",
                               linewidth=1.4, edgecolor="#123C69", facecolor=nodo["color"])
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, nodo["texto"], ha="center", va="center", fontsize=10, color="#102A43")
        ax.annotate("", xy=nodo["fin"], xytext=nodo["inicio"],
                    arrowprops=dict(arrowstyle="->", lw=1.6, color="#123C69"))

    ax.set_title("Categorias principales de la oferta tecnologica mundial analizada", fontsize=14, color="#102A43", pad=14)
    _guardar_figura(fig, nombre_salida)


def grafico_posicionamiento_museiq(nombre_salida):
    fig, ax = plt.subplots(figsize=(8.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Mayor contextualizacion e integracion funcional")
    ax.set_ylabel("Mayor costo y complejidad operativa")
    ax.grid(True, linestyle="--", alpha=0.3)

    puntos = {
        "Audioguias clasicas": (2.0, 4.0),
        "Apps BYOD / QR": (3.5, 2.5),
        "Indoor navigation": (7.0, 8.0),
        "IA conversacional aislada": (6.3, 5.5),
        "MuseIQ": (7.8, 4.5),
    }
    colores = {
        "Audioguias clasicas": "#F5A623",
        "Apps BYOD / QR": "#9EDBF0",
        "Indoor navigation": "#7A5AF8",
        "IA conversacional aislada": "#D95C5C",
        "MuseIQ": "#2E8B57",
    }
    for nombre, (x, y) in puntos.items():
        ax.scatter(x, y, s=170 if nombre == "MuseIQ" else 120, color=colores[nombre], edgecolors="#123C69", linewidth=0.8)
        ax.text(x + 0.15, y + 0.2, nombre, fontsize=9, color="#102A43")

    ax.set_title("Posicionamiento visual de MuseIQ frente a la oferta tecnologica mundial", fontsize=14, color="#102A43")
    _guardar_figura(fig, nombre_salida)


def grafico_integracion_capacidades(nombre_salida):
    fig, ax = plt.subplots(figsize=(12.5, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    capacidades = [
        (1.0, 5.8, "BLE /\nproximidad", "#F9D6D5"),
        (1.0, 3.9, "Voz y\naccesibilidad", "#D9F0F7"),
        (1.0, 2.0, "IA\ncontextual", "#EADCF8"),
        (1.0, 0.1, "BYOD y bajo\ncosto", "#D8F3DC"),
    ]
    for x, y, texto, color in capacidades:
        patch = FancyBboxPatch((x, y), 2.6, 1.0, boxstyle="round,pad=0.03,rounding_size=0.10",
                               linewidth=1.4, edgecolor="#123C69", facecolor=color)
        ax.add_patch(patch)
        ax.text(x + 1.3, y + 0.5, texto, ha="center", va="center", fontsize=10, color="#102A43")

    for y in [6.3, 4.4, 2.5, 0.6]:
        ax.annotate("", xy=(6.0, 3.95), xytext=(3.6, y), arrowprops=dict(arrowstyle="->", lw=1.7, color="#123C69"))

    centro = FancyBboxPatch((6.0, 3.2), 2.4, 1.5, boxstyle="round,pad=0.03,rounding_size=0.12",
                            linewidth=1.6, edgecolor="#123C69", facecolor="#E8F1FA")
    ax.add_patch(centro)
    ax.text(7.2, 3.95, "Integracion\nparcial en\nel mercado", ha="center", va="center", fontsize=11, color="#102A43")

    museiq = FancyBboxPatch((9.1, 2.8), 2.2, 2.3, boxstyle="round,pad=0.03,rounding_size=0.12",
                            linewidth=1.8, edgecolor="#123C69", facecolor="#D8F3DC")
    ax.add_patch(museiq)
    ax.text(10.2, 3.95, "MuseIQ\nintegra las\ncapacidades", ha="center", va="center", fontsize=12, color="#102A43", weight="bold")
    ax.annotate("", xy=(9.1, 3.95), xytext=(8.4, 3.95), arrowprops=dict(arrowstyle="->", lw=1.8, color="#123C69"))

    ax.set_title("Integracion de capacidades en el mercado frente a la propuesta MuseIQ", fontsize=14, color="#102A43", pad=14)
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

import sys

from generar_grafico import (
    grafico_arquitectura_conceptual_museiq,
    grafico_barras,
    grafico_barras_horizontales,
    grafico_brecha_demanda_mediacion,
    grafico_categorias_oferta_mundial,
    grafico_criterios_mercado_prioritario,
    grafico_diagrama_museiq_componentes,
    grafico_diagrama_principios_museiq,
    grafico_ecosistema_museos_inteligentes,
    grafico_ecosistema_nacional_adopcion,
    grafico_heatmap,
    grafico_integracion_capacidades,
    grafico_lineas,
    grafico_lineas_multiples,
    grafico_mapa_problema_central,
    grafico_mapa_segmentacion,
    grafico_pastel,
    grafico_posicionamiento_museiq,
    grafico_relacion_problema_solucion_aporte,
    grafico_ruta_validacion,
)


def _totales_escenario(nuevos_por_anio, precio_impl, precio_sub, retencion, proporcion_adicional, precio_adicional, factor=0.5):
    activos_previos = 0
    totales = []

    for nuevos in nuevos_por_anio:
        ingreso_impl = nuevos * precio_impl
        base_recurrente = retencion * activos_previos + factor * nuevos
        ingreso_recurrente = base_recurrente * precio_sub
        ingreso_adicional = base_recurrente * proporcion_adicional * precio_adicional
        ingreso_total = ingreso_impl + ingreso_recurrente + ingreso_adicional
        totales.append(round(ingreso_total, 2))
        activos_previos = retencion * activos_previos + nuevos

    return totales


# Capitulo 1
def generar_smartphones_peru():
    grafico_lineas(
        x=[2019, 2021, 2022, 2023, 2024],
        y=[78.0, 88.4, 91.9, 92.8, 94.8],
        titulo="Evolucion de hogares peruanos con smartphone",
        eje_x="Anio",
        eje_y="Porcentaje de hogares (%)",
        nombre_salida="smartphones_peru_2019_2024.png",
        serie="Hogares con smartphone",
    )


def generar_visitas_museos():
    grafico_lineas(
        x=[2019, 2020, 2022, 2023, 2024],
        y=[1956034, 353153, 1067571, 1543872, 1790502],
        titulo="Evolucion de visitas a museos administrados por el Estado",
        eje_x="Anio",
        eje_y="Numero de visitantes",
        nombre_salida="visitas_museos_peru_2019_2024.png",
        serie="Visitantes",
    )


def generar_mapa_problema():
    grafico_mapa_problema_central("mapa_problema_central_museiq.png")


def generar_arquitectura_conceptual():
    grafico_arquitectura_conceptual_museiq("arquitectura_conceptual_museiq.png")


def generar_relacion_problema_solucion():
    grafico_relacion_problema_solucion_aporte("relacion_problema_solucion_aporte.png")


# Capitulo 2
def generar_panorama_global_submercados():
    grafico_barras(
        categorias=["Mercado total", "Tours virtuales", "Hardware", "Software", "Servicios"],
        valores=[10.9, 1.96, 7.261, 2.492, 1.309],
        etiquetas=["USD 10.9B", "USD 1.96B", "USD 7.261B", "USD 2.492B", "USD 1.309B"],
        titulo="Panorama global de submercados museales digitales en 2024",
        eje_x="Segmento",
        eje_y="Mercado estimado (miles de millones USD)",
        nombre_salida="panorama_global_submercados_2024.png",
    )


def generar_brecha_demanda_mediacion():
    grafico_brecha_demanda_mediacion("brecha_demanda_mediacion_digital.png")


def generar_ecosistema_museos_inteligentes():
    grafico_ecosistema_museos_inteligentes("ecosistema_museos_inteligentes.png")


def generar_ruta_validacion():
    grafico_ruta_validacion("ruta_metodologica_validacion_museiq.png")


# Capitulo 3
def generar_segmentos_prioridad():
    grafico_barras_horizontales(
        categorias=[
            "Museos publicos y de sitio",
            "Museos privados y universitarios",
            "Centros culturales",
            "Mercado potencial ampliado",
        ],
        valores=[3, 2, 2, 1],
        etiquetas=["Alta", "Media", "Media", "Media-baja"],
        titulo="Prioridad relativa de los segmentos del mercado objetivo",
        eje_x="Nivel de prioridad relativo",
        eje_y="Segmento",
        nombre_salida="segmentos_mercado_objetivo_prioridad.png",
    )


def generar_mapa_segmentacion():
    grafico_mapa_segmentacion("mapa_segmentacion_mercado_objetivo.png")


def generar_criterios_mercado():
    grafico_criterios_mercado_prioritario("criterios_mercado_objetivo_prioritario.png")


def generar_ecosistema_nacional():
    grafico_ecosistema_nacional_adopcion("ecosistema_nacional_adopcion_museiq.png")


# Capitulo 4
def generar_comparacion_oferta():
    grafico_heatmap(
        matriz=[
            [0, 0, 0.2, 1.0, 0.6],
            [0, 0, 0.8, 1.0, 0.8],
            [0, 0.3, 0.8, 0.8, 0.7],
            [0, 0.5, 0.1, 1.0, 1.0],
            [1.0, 0, 0.1, 0.6, 0.6],
            [1.0, 0, 0.1, 0.4, 0.3],
            [1.0, 0, 0, 0.2, 0.5],
            [0, 1.0, 0.4, 0.4, 0.4],
        ],
        etiquetas_filas=[
            "Bloomberg Connects",
            "Smartify",
            "SmartGuide",
            "izi.TRAVEL / Nubart / Hearonymus",
            "Locatify",
            "Navigine",
            "Verde et al. (2023)",
            "Wang (2024)",
        ],
        etiquetas_columnas=["BLE/indoor", "Voz", "IA", "Acceso ligero", "Afinidad con MuseIQ"],
        titulo="Comparacion visual de capacidades en la oferta tecnologica mundial",
        nombre_salida="comparacion_capacidades_oferta_mundial.png",
    )


def generar_categorias_oferta():
    grafico_categorias_oferta_mundial("categorias_oferta_tecnologica_mundial.png")


def generar_posicionamiento_museiq():
    grafico_posicionamiento_museiq("posicionamiento_museiq_oferta_mundial.png")


def generar_integracion_capacidades():
    grafico_integracion_capacidades("integracion_capacidades_mercado_vs_museiq.png")


# Capitulo 5
def generar_estructura_ingresos():
    grafico_barras_horizontales(
        categorias=["Implementacion", "Suscripcion anual", "Servicios adicionales"],
        valores=[5000, 2500, 1000],
        etiquetas=["USD 5,000", "USD 2,500", "USD 1,000"],
        titulo="Estructura referencial de ingresos por rubro",
        eje_x="Monto referencial (USD)",
        eje_y="Rubro",
        nombre_salida="estructura_ingresos_rubro.png",
    )


def generar_flujo_ingresos():
    grafico_lineas(
        x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        y=[6400, 13780, 22855, 34152, 42812, 52235, 62484, 73626, 77917, 86044],
        titulo="Flujo de ingresos proyectados de MuseIQ a 10 anios",
        eje_x="Anio",
        eje_y="Ingreso total anual (USD)",
        nombre_salida="flujo_ingresos_10_anios.png",
        serie="Escenario base",
    )


def generar_instituciones_activas():
    grafico_lineas(
        x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        y=[1.00, 2.90, 5.61, 9.05, 12.14, 14.93, 17.44, 19.70, 20.73, 21.65],
        titulo="Crecimiento de instituciones activas en el escenario base",
        eje_x="Anio",
        eje_y="Instituciones activas",
        nombre_salida="instituciones_activas_10_anios.png",
        serie="Base activa",
    )


def generar_escenarios_ingresos():
    grafico_lineas_multiples(
        x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        series=[
            {
                "nombre": "Conservador",
                "y": _totales_escenario(
                    nuevos_por_anio=[1] * 10,
                    precio_impl=4000,
                    precio_sub=2000,
                    retencion=0.85,
                    proporcion_adicional=0.20,
                    precio_adicional=800,
                ),
            },
            {
                "nombre": "Base",
                "y": [6400, 13780, 22855, 34152, 42812, 52235, 62484, 73626, 77917, 86044],
            },
            {
                "nombre": "Optimista",
                "y": _totales_escenario(
                    nuevos_por_anio=[1, 2, 3, 4, 4, 4, 4, 4, 3, 3],
                    precio_impl=6000,
                    precio_sub=3000,
                    retencion=0.95,
                    proporcion_adicional=0.40,
                    precio_adicional=1200,
                ),
            },
        ],
        titulo="Comparacion de escenarios de ingresos proyectados",
        eje_x="Anio",
        eje_y="Ingreso total anual (USD)",
        nombre_salida="escenarios_ingresos_comparados.png",
    )


# Capitulo 6
def generar_fundamentos_componentes():
    grafico_diagrama_museiq_componentes("fundamentos_museiq_componentes.png")


def generar_principios_museiq():
    grafico_diagrama_principios_museiq("principios_diseno_museiq.png")


# Capitulo 10
def generar_composicion_inversion():
    grafico_pastel(
        categorias=["Base de prototipo", "Adecuacion preoperativa"],
        valores=[1055, 1500],
        titulo="Composicion de la inversion inicial de MuseIQ",
        nombre_salida="composicion_inversion_inicial.png",
    )


def generar_flujo_economico():
    grafico_lineas_multiples(
        x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        series=[
            {
                "nombre": "Ingresos",
                "y": [6400, 13780, 22855, 34152, 42812, 52235, 62484, 73626, 77917, 86044],
            },
            {
                "nombre": "Costos totales",
                "y": [3900, 6057, 8743, 11906, 13992, 15887, 17602, 19157, 19065, 19754],
            },
            {
                "nombre": "Flujo neto",
                "y": [2500, 7723, 14112, 22247, 28820, 36348, 44882, 54469, 58852, 66290],
            },
        ],
        titulo="Comparacion entre ingresos, costos y flujo neto",
        eje_x="Anio",
        eje_y="Monto anual (USD)",
        nombre_salida="flujo_economico_anual.png",
    )


def generar_sensibilidad_van():
    grafico_barras_horizontales(
        categorias=[
            "Tasa de descuento de 15%",
            "Incremento de 20% en gasto fijo anual",
            "Incremento de 20% en costo recurrente",
            "Reduccion de 20% en ingresos",
            "Escenario base",
        ],
        valores=[125295, 146628, 142153, 105807, 149653],
        etiquetas=["USD 125,295", "USD 146,628", "USD 142,153", "USD 105,807", "USD 149,653"],
        titulo="Sensibilidad del VAN de MuseIQ",
        eje_x="Valor actual neto (USD)",
        eje_y="Escenario",
        nombre_salida="sensibilidad_van.png",
    )


# Registro de graficos individuales
GRAFICOS = {
    "smartphones_peru": generar_smartphones_peru,
    "visitas_museos": generar_visitas_museos,
    "mapa_problema": generar_mapa_problema,
    "arquitectura_conceptual": generar_arquitectura_conceptual,
    "relacion_problema_solucion": generar_relacion_problema_solucion,
    "panorama_global_submercados": generar_panorama_global_submercados,
    "brecha_demanda_mediacion": generar_brecha_demanda_mediacion,
    "ecosistema_museos_inteligentes": generar_ecosistema_museos_inteligentes,
    "ruta_validacion": generar_ruta_validacion,
    "segmentos_prioridad": generar_segmentos_prioridad,
    "mapa_segmentacion_mercado_objetivo": generar_mapa_segmentacion,
    "criterios_mercado_objetivo": generar_criterios_mercado,
    "ecosistema_nacional_adopcion": generar_ecosistema_nacional,
    "comparacion_oferta_mundial": generar_comparacion_oferta,
    "categorias_oferta_tecnologica_mundial": generar_categorias_oferta,
    "posicionamiento_museiq": generar_posicionamiento_museiq,
    "integracion_capacidades": generar_integracion_capacidades,
    "estructura_ingresos": generar_estructura_ingresos,
    "flujo_ingresos": generar_flujo_ingresos,
    "instituciones_activas": generar_instituciones_activas,
    "escenarios_ingresos": generar_escenarios_ingresos,
    "fundamentos_componentes": generar_fundamentos_componentes,
    "principios_museiq": generar_principios_museiq,
    "composicion_inversion": generar_composicion_inversion,
    "flujo_economico": generar_flujo_economico,
    "sensibilidad_van": generar_sensibilidad_van,
}


# Agrupacion por capitulo
CAPITULOS = {
    "cap1": [
        "smartphones_peru",
        "visitas_museos",
        "mapa_problema",
        "arquitectura_conceptual",
        "relacion_problema_solucion",
    ],
    "cap2": [
        "panorama_global_submercados",
        "brecha_demanda_mediacion",
        "ecosistema_museos_inteligentes",
        "ruta_validacion",
    ],
    "cap3": [
        "segmentos_prioridad",
        "mapa_segmentacion_mercado_objetivo",
        "criterios_mercado_objetivo",
        "ecosistema_nacional_adopcion",
    ],
    "cap4": [
        "comparacion_oferta_mundial",
        "categorias_oferta_tecnologica_mundial",
        "posicionamiento_museiq",
        "integracion_capacidades",
    ],
    "cap5": [
        "estructura_ingresos",
        "flujo_ingresos",
        "instituciones_activas",
        "escenarios_ingresos",
    ],
    "cap6": [
        "fundamentos_componentes",
        "principios_museiq",
    ],
    "cap10": [
        "composicion_inversion",
        "flujo_economico",
        "sensibilidad_van",
    ],
}


def imprimir_ayuda():
    print("Uso:")
    print("  python ejemplos_uso.py all")
    print("  python ejemplos_uso.py cap1")
    print("  python ejemplos_uso.py <nombre_grafico>")
    print("")
    print("Capitulos disponibles:")
    for capitulo, nombres in CAPITULOS.items():
        print(f"  - {capitulo}: {', '.join(nombres)}")
    print("")
    print("Graficos disponibles:")
    for nombre in sorted(GRAFICOS):
        print(f"  - {nombre}")


def main():
    if len(sys.argv) == 1:
        imprimir_ayuda()
        return

    objetivo = sys.argv[1].strip()

    if objetivo in {"all", "todo"}:
        for generador in GRAFICOS.values():
            generador()
        return

    if objetivo in CAPITULOS:
        for nombre in CAPITULOS[objetivo]:
            GRAFICOS[nombre]()
        return

    if objetivo in {"help", "--help", "-h"}:
        imprimir_ayuda()
        return

    generador = GRAFICOS.get(objetivo)
    if generador is None:
        print(f"No existe el grafico '{objetivo}'.")
        print("")
        imprimir_ayuda()
        raise SystemExit(1)

    generador()


if __name__ == "__main__":
    main()

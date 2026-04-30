import sys

from generar_grafico import (
    grafico_arquitectura_conceptual_museiq,
    grafico_barras,
    grafico_barras_horizontales,
    grafico_brecha_demanda_mediacion,
    grafico_categorias_oferta_mundial,
    grafico_capas_tecnologicas_museiq,
    grafico_clasificacion_datos_entrada_museiq,
    grafico_criterios_mercado_prioritario,
    grafico_diagrama_museiq_componentes,
    grafico_diagrama_principios_museiq,
    grafico_ecosistema_museos_inteligentes,
    grafico_ecosistema_nacional_adopcion,
    grafico_flujo_contextual_museiq,
    grafico_heatmap,
    grafico_integracion_capacidades,
    grafico_lineas,
    grafico_lineas_multiples,
    grafico_mapa_problema_central,
    grafico_mapa_segmentacion,
    grafico_mapeo_beacon_sala_museiq,
    grafico_modelo_logico_datos_museiq,
    grafico_pastel,
    grafico_posicionamiento_museiq,
    grafico_relacion_problema_solucion_aporte,
    grafico_ruta_validacion,
)


def _valores_sensibilidad_van_cobro_variable():
    # Se modela un contrato con piso fijo que cubre el uso base
    # y un sobrecargo por sobreconsumo cuando la voz supera
    # el umbral del escenario central.
    costos_ia = {
        "Conservador 10%": 2128,
        "Base 20%": 8530,
        "Alto 35%": 22349,
    }
    van_base = 3383
    costo_base = 8530
    precio_base = 10200
    factor_sobrecargo = 1.10
    margen_base = 10200 - 8530
    factor_activos_descuento = 6.63

    categorias = []
    valores = []
    etiquetas = []

    for categoria, costo in costos_ia.items():
        if costo <= costo_base:
            precio = precio_base
        else:
            precio = precio_base + factor_sobrecargo * (costo - costo_base)
        margen = precio - costo
        van = round(van_base + (margen - margen_base) * factor_activos_descuento)
        categorias.append(categoria)
        valores.append(van)
        etiquetas.append(f"S/ {van:,.0f}")

    return categorias, valores, etiquetas


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
        nombre_salida="cap1/smartphones_peru_2019_2024.png",
        serie="Hogares con smartphone",
    )


def generar_visitas_museos():
    grafico_lineas(
        x=[2019, 2020, 2022, 2023, 2024],
        y=[1956034, 353153, 1067571, 1543872, 1790502],
        titulo="Evolucion de visitas a museos administrados por el Estado",
        eje_x="Anio",
        eje_y="Numero de visitantes",
        nombre_salida="cap1/visitas_museos_peru_2019_2024.png",
        serie="Visitantes",
    )


def generar_mapa_problema():
    grafico_mapa_problema_central("cap1/mapa_problema_central_museiq.png")


def generar_arquitectura_conceptual():
    grafico_arquitectura_conceptual_museiq("cap1/arquitectura_conceptual_museiq.png")


def generar_relacion_problema_solucion():
    grafico_relacion_problema_solucion_aporte("cap1/relacion_problema_solucion_aporte.png")


# Capitulo 2
def generar_panorama_global_submercados():
    grafico_barras(
        categorias=["Mercado total", "Tours virtuales", "Hardware", "Software", "Servicios"],
        valores=[10.9, 1.96, 7.261, 2.492, 1.309],
        etiquetas=["USD 10.9B", "USD 1.96B", "USD 7.261B", "USD 2.492B", "USD 1.309B"],
        titulo="Panorama global de submercados museales digitales en 2024",
        eje_x="Segmento",
        eje_y="Mercado estimado (miles de millones USD)",
        nombre_salida="cap2/panorama_global_submercados_2024.png",
    )


def generar_brecha_demanda_mediacion():
    grafico_brecha_demanda_mediacion("cap2/brecha_demanda_mediacion_digital.png")


def generar_ecosistema_museos_inteligentes():
    grafico_ecosistema_museos_inteligentes("cap2/ecosistema_museos_inteligentes.png")


def generar_ruta_validacion():
    grafico_ruta_validacion("cap2/ruta_metodologica_validacion_museiq.png")


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
        nombre_salida="cap3/segmentos_mercado_objetivo_prioridad.png",
    )


def generar_mapa_segmentacion():
    grafico_mapa_segmentacion("cap3/mapa_segmentacion_mercado_objetivo.png")


def generar_criterios_mercado():
    grafico_criterios_mercado_prioritario("cap3/criterios_mercado_objetivo_prioritario.png")


def generar_ecosistema_nacional():
    grafico_ecosistema_nacional_adopcion("cap3/ecosistema_nacional_adopcion_museiq.png")


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
        nombre_salida="cap4/comparacion_capacidades_oferta_mundial.png",
    )


def generar_categorias_oferta():
    grafico_categorias_oferta_mundial("cap4/categorias_oferta_tecnologica_mundial.png")


def generar_posicionamiento_museiq():
    grafico_posicionamiento_museiq("cap4/posicionamiento_museiq_oferta_mundial.png")


def generar_integracion_capacidades():
    grafico_integracion_capacidades("cap4/integracion_capacidades_mercado_vs_museiq.png")


# Capitulo 5
def generar_estructura_ingresos():
    grafico_barras_horizontales(
        categorias=[
            "Implementacion inicial",
            "Mantenimiento tecnico anual",
            "IA y analitica anual",
            "Servicios adicionales referenciales",
        ],
        valores=[5100, 900, 10200, 1000],
        etiquetas=["S/ 5,100", "S/ 900", "S/ 10,200", "S/ 500-1,500"],
        titulo="Precios base del modelo de ingresos de MuseIQ",
        eje_x="Monto referencial (S/)",
        eje_y="Rubro",
        nombre_salida="cap5/estructura_ingresos_rubro.png",
    )


def generar_flujo_ingresos():
    grafico_lineas(
        x=[2026, 2027, 2028],
        y=[5100, 11600, 11100],
        titulo="Flujo de ingresos del piloto base en Sipan",
        eje_x="Anio",
        eje_y="Ingreso total anual (S/)",
        nombre_salida="cap5/flujo_ingresos_10_anios.png",
        serie="Piloto base",
    )


def generar_instituciones_activas():
    grafico_lineas_multiples(
        x=[2026, 2027, 2028],
        series=[
            {"nombre": "Piloto base", "y": [1, 1, 1]},
            {"nombre": "2 museos nuevos/anio", "y": [1, 3, 5]},
            {"nombre": "3 museos nuevos/anio", "y": [1, 4, 7]},
            {"nombre": "4 museos nuevos/anio", "y": [1, 5, 9]},
        ],
        titulo="Museos activos acumulados segun escenario de expansion",
        eje_x="Anio",
        eje_y="Museos activos",
        nombre_salida="cap5/instituciones_activas_10_anios.png",
    )


def generar_escenarios_ingresos():
    grafico_lineas_multiples(
        x=[2026, 2027, 2028],
        series=[
            {
                "nombre": "Piloto base",
                "y": [5100, 11100, 11100],
            },
            {
                "nombre": "2 museos nuevos/anio",
                "y": [5100, 21300, 43500],
            },
            {
                "nombre": "3 museos nuevos/anio",
                "y": [5100, 26400, 59700],
            },
            {
                "nombre": "4 museos nuevos/anio",
                "y": [5100, 31500, 75900],
            },
        ],
        titulo="Escenarios de ingresos segun ritmo de expansion comercial",
        eje_x="Anio",
        eje_y="Ingreso total anual (S/)",
        nombre_salida="cap5/escenarios_ingresos_comparados.png",
    )


# Capitulo 6
def generar_fundamentos_componentes():
    grafico_diagrama_museiq_componentes("cap6/fundamentos_museiq_componentes.png")


def generar_principios_museiq():
    grafico_diagrama_principios_museiq("cap6/principios_diseno_museiq.png")


# Capitulo 10
def generar_composicion_inversion():
    grafico_pastel(
        categorias=["Base de prototipo", "Adecuacion preoperativa"],
        valores=[1055, 1500],
        titulo="Composicion de la inversion inicial de MuseIQ",
        nombre_salida="cap10/composicion_inversion_inicial.png",
    )


def generar_flujo_economico():
    grafico_lineas_multiples(
        x=[1, 2, 3, 4, 5],
        series=[
            {
                "nombre": "Ingresos",
                "y": [5100, 16200, 27300, 38400, 49500],
            },
            {
                "nombre": "Costos totales",
                "y": [6300, 15802, 25306, 34813, 44321],
            },
            {
                "nombre": "Flujo neto",
                "y": [-1200, 398, 1994, 3587, 5179],
            },
        ],
        titulo="Flujo economico anual de MuseIQ en el escenario base",
        eje_x="Anio",
        eje_y="Monto anual (S/)",
        nombre_salida="cap10/flujo_economico_anual.png",
    )


def generar_sensibilidad_van():
    categorias, valores, etiquetas = _valores_sensibilidad_van_cobro_variable()
    grafico_barras_horizontales(
        categorias=categorias,
        valores=valores,
        etiquetas=etiquetas,
        titulo="Sensibilidad del VAN con piso fijo y cobro por sobreuso de voz",
        eje_x="Valor actual neto (S/)",
        eje_y="Escenario",
        nombre_salida="cap10/sensibilidad_van.png",
    )


def generar_flujo_expansion_escenarios():
    grafico_lineas_multiples(
        x=[1, 2, 3, 4, 5],
        series=[
            {"nombre": "1 museo/anio", "y": [-1200, 398, 1994, 3587, 5179]},
            {"nombre": "2 museos/anio", "y": [-1200, 1598, 4864, 8127, 11389]},
            {"nombre": "3 museos/anio", "y": [-1200, 2798, 7734, 12667, 17599]},
            {"nombre": "4 museos/anio", "y": [-1200, 3998, 10604, 17207, 23809]},
        ],
        titulo="Flujo neto anual segun ritmo de expansion comercial",
        eje_x="Anio",
        eje_y="Flujo neto anual (S/)",
        nombre_salida="cap10/flujo_neto_escenarios_expansion.png",
    )


def generar_van_expansion():
    grafico_barras_horizontales(
        categorias=[
            "1 museo nuevo/anio",
            "2 museos nuevos/anio",
            "3 museos nuevos/anio",
            "4 museos nuevos/anio",
        ],
        valores=[3383, 12792, 22200, 31609],
        etiquetas=["S/ 3,383", "S/ 12,792", "S/ 22,200", "S/ 31,609"],
        titulo="VAN de MuseIQ segun escenarios de expansion",
        eje_x="Valor actual neto (S/)",
        eje_y="Escenario",
        nombre_salida="cap10/van_escenarios_expansion.png",
    )


# Capitulo 7
def generar_capas_tecnologicas():
    grafico_capas_tecnologicas_museiq("cap7/capas_tecnologicas_museiq.png")


def generar_flujo_contextual():
    grafico_flujo_contextual_museiq("cap7/flujo_contextual_museiq.png")


# Capitulo 8
def generar_clasificacion_datos_entrada():
    grafico_clasificacion_datos_entrada_museiq("cap8/clasificacion_datos_entrada_museiq.png")


def generar_mapeo_beacon_sala():
    grafico_mapeo_beacon_sala_museiq("cap8/mapeo_beacon_sala_museiq.png")


def generar_modelo_logico_datos():
    grafico_modelo_logico_datos_museiq("cap8/modelo_logico_datos_museiq.png")


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
    "capas_tecnologicas_museiq": generar_capas_tecnologicas,
    "flujo_contextual_museiq": generar_flujo_contextual,
    "clasificacion_datos_entrada_museiq": generar_clasificacion_datos_entrada,
    "mapeo_beacon_sala_museiq": generar_mapeo_beacon_sala,
    "modelo_logico_datos_museiq": generar_modelo_logico_datos,
    "composicion_inversion": generar_composicion_inversion,
    "flujo_economico": generar_flujo_economico,
    "sensibilidad_van": generar_sensibilidad_van,
    "flujo_expansion_escenarios": generar_flujo_expansion_escenarios,
    "van_expansion": generar_van_expansion,
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
    "cap7": [
        "capas_tecnologicas_museiq",
        "flujo_contextual_museiq",
    ],
    "cap8": [
        "clasificacion_datos_entrada_museiq",
        "mapeo_beacon_sala_museiq",
        "modelo_logico_datos_museiq",
    ],
    "cap10": [
        "composicion_inversion",
        "flujo_economico",
        "sensibilidad_van",
        "flujo_expansion_escenarios",
        "van_expansion",
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

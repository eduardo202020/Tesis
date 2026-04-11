from generar_grafico import (
    grafico_barras,
    grafico_barras_horizontales,
    grafico_heatmap,
    grafico_lineas,
    grafico_lineas_multiples,
    grafico_pastel,
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
grafico_lineas(
    x=[2019, 2021, 2022, 2023, 2024],
    y=[78.0, 88.4, 91.9, 92.8, 94.8],
    titulo="Evolucion de hogares peruanos con smartphone",
    eje_x="Anio",
    eje_y="Porcentaje de hogares (%)",
    nombre_salida="smartphones_peru_2019_2024.png",
    serie="Hogares con smartphone",
)

grafico_lineas(
    x=[2019, 2020, 2022, 2023, 2024],
    y=[1956034, 353153, 1067571, 1543872, 1790502],
    titulo="Evolucion de visitas a museos administrados por el Estado",
    eje_x="Anio",
    eje_y="Numero de visitantes",
    nombre_salida="visitas_museos_peru_2019_2024.png",
    serie="Visitantes",
)


# Capitulo 2
grafico_barras(
    categorias=["Mercado total", "Tours virtuales", "Hardware", "Software", "Servicios"],
    valores=[10.9, 1.96, 7.261, 2.492, 1.309],
    etiquetas=["USD 10.9B", "USD 1.96B", "USD 7.261B", "USD 2.492B", "USD 1.309B"],
    titulo="Panorama global de submercados museales digitales en 2024",
    eje_x="Segmento",
    eje_y="Mercado estimado (miles de millones USD)",
    nombre_salida="panorama_global_submercados_2024.png",
)


# Capitulo 3
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


# Capitulo 4
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


# Capitulo 5
grafico_barras_horizontales(
    categorias=["Implementacion", "Suscripcion anual", "Servicios adicionales"],
    valores=[5000, 2500, 1000],
    etiquetas=["USD 5,000", "USD 2,500", "USD 1,000"],
    titulo="Estructura referencial de ingresos por rubro",
    eje_x="Monto referencial (USD)",
    eje_y="Rubro",
    nombre_salida="estructura_ingresos_rubro.png",
)

grafico_lineas(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y=[6400, 13780, 22855, 34152, 42812, 52235, 62484, 73626, 77917, 86044],
    titulo="Flujo de ingresos proyectados de MuseIQ a 10 anios",
    eje_x="Anio",
    eje_y="Ingreso total anual (USD)",
    nombre_salida="flujo_ingresos_10_anios.png",
    serie="Escenario base",
)

grafico_lineas(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y=[1.00, 2.90, 5.61, 9.05, 12.14, 14.93, 17.44, 19.70, 20.73, 21.65],
    titulo="Crecimiento de instituciones activas en el escenario base",
    eje_x="Anio",
    eje_y="Instituciones activas",
    nombre_salida="instituciones_activas_10_anios.png",
    serie="Base activa",
)

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


# Capitulo 10
grafico_pastel(
    categorias=["Base de prototipo", "Adecuacion preoperativa"],
    valores=[1055, 1500],
    titulo="Composicion de la inversion inicial de MuseIQ",
    nombre_salida="composicion_inversion_inicial.png",
)

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

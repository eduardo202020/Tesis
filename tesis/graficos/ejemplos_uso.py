from generar_grafico import (
    grafico_barras,
    grafico_barras_horizontales,
    grafico_dispersion,
    grafico_lineas,
    grafico_pastel,
)


# Este archivo sirve para crear graficos concretos sin tocar la logica base.
# Puedes borrar, duplicar o editar bloques segun necesites.

grafico_barras(
    categorias=["NO", "OFF", "NOE", "OFG"],
    valores=[23000, 4500, 2700, 400],
    etiquetas=["75.4%", "14.5%", "8.7%", "1.4%"],
    titulo="Distribucion de etiquetado",
    eje_x="Etiqueta",
    eje_y="Cantidad",
    nombre_salida="distribucion_etiquetado.png",
)

grafico_lineas(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y=[6400, 13780, 22855, 34152, 42812, 52235, 62484, 73626, 77917, 86044],
    titulo="Flujo de ingresos proyectados a 10 anios",
    eje_x="Anio",
    eje_y="Ingreso total anual (USD)",
    nombre_salida="flujo_ingresos_10_anios.png",
    serie="Escenario base",
)

grafico_pastel(
    categorias=["Costos directos", "Costos indirectos"],
    valores=[205, 850],
    titulo="Composicion del presupuesto preliminar",
    nombre_salida="composicion_presupuesto_museiq.png",
)

grafico_barras_horizontales(
    categorias=["Implementacion", "Suscripcion", "Servicios adicionales"],
    valores=[5000, 2500, 1000],
    etiquetas=["USD 5,000", "USD 2,500", "USD 1,000"],
    titulo="Estructura referencial de ingresos por rubro",
    eje_x="Monto referencial (USD)",
    eje_y="Rubro",
    nombre_salida="estructura_ingresos_rubro.png",
)

grafico_dispersion(
    x=[1, 2, 3, 4, 5, 6],
    y=[3900, 6057, 8743, 11906, 13992, 15887],
    titulo="Crecimiento del costo total anual en el escenario base",
    eje_x="Anio",
    eje_y="Costo total anual (USD)",
    nombre_salida="dispersion_costos_anuales.png",
)

# Verificación de concordancia del flujo de caja MuseIQ

## Archivos comparados

- `FLUJO DE CAJA DE PROYECTO DE TITULO FIEE UNI.xls`: modelo económico-financiero proporcionado por el profesor.
- `FLUJO_DE_CAJA_MUSEIQ.xlsx` y `FLUJO_DE_CAJA_MUSEIQ.xls`: adaptación dinámica para MuseIQ.
- `tesis-plantilla/tesis-plantilla.pdf`: referencia de secuencia y redacción del capítulo económico.

## Resultado general

El libro MuseIQ conserva las 26 hojas funcionales del modelo del profesor y agrega la hoja `SUPUESTOS` para concentrar entradas editables, fórmulas financieras y fuentes verificables. La adaptación no replica la cantidad de filas del proyecto médico porque MuseIQ no requiere inventarios clínicos, terrenos, edificios ni maquinaria hospitalaria; sí conserva la cadena metodológica completa.

La conversión final del archivo `.xls` conserva 3,290 fórmulas. El balance proyectado presenta un residuo máximo de S/0.0124 por la precisión decimal del formato binario antiguo, equivalente a S/0.00 con el formato monetario mostrado.

| Bloque metodológico | Hojas del profesor | Adaptación MuseIQ | Estado |
|---|---|---|---|
| Volumen e ingresos | `INGRESOS` | Museos nuevos, activos, implementación y recurrencia | Conforme |
| Costos de producción | `COSTOS`, `COSTO DE PRODUCCION UNITARIO`, `PLANILLA` | Hardware, instalación, IA, soporte y personal | Conforme |
| Gastos de operación | `GASTOS_ADM_VTAS_FINANZAS` | Administración, ventas, intereses y amortización | Conforme |
| Inversión | `DEPRECIACIONES AMORTIZACION`, `PLAN DE INVERSION`, `BALANCE DE APERTURA` | Activos tecnológicos, intangibles y capital de trabajo | Conforme |
| Estados financieros | `COSTO DE VENTA`, `ESTADO DE RESULTADOS`, `PRESUPUESTO CAJA`, `BALANCE GENERAL PROYECTADO` | Estados enlazados mediante fórmulas | Conforme |
| Evaluación | `RAZONES FINANCIERAS`, `PUNTO DE EQUILIBRIO`, `FLUJO DE EFECTIVO`, `COSTO CAPITAL VAN TIR IR` | Indicadores, VAN, TIR, IR y recuperación | Conforme |
| Riesgos | Hojas 18 a 26 | Ingresos, gastos, interés, cobranza, administración, escenario optimista y precio | Conforme |

## Correcciones realizadas durante la verificación

1. Se corrigió la fórmula del flujo neto para evitar sumar simultáneamente ingresos, egresos y su diferencia. La TIR correcta es 19.96%, no 289.64%.
2. Se corrigió la clasificación de la deuda corriente: el balance utiliza la amortización exigible del año siguiente. El balance proyectado cuadra en los diez años.
3. Las hojas de sensibilidad muestran su propia tasa de corte, VAN, TIR, índice de rentabilidad y criterio de decisión.
4. La cartera comercial se alineó con el Capítulo 5: 35 museos, distribuidos en 5 contratos Básicos, 20 Estándar y 10 Avanzados.
5. Se eliminó el recargo adicional de 20% y la inflación acumulada sobre flujos expresados en soles constantes.

## Indicadores verificados del escenario base

- Inversión inicial: S/300,000.
- Tasa real de corte: 12.35%.
- VAN: S/180,940.08.
- TIR: 19.96%.
- Índice de rentabilidad: 1.60.
- Recuperación descontada: 8.23 años.
- Saldo mínimo de caja: S/36,029.24.

## Criterio de concordancia

La concordancia se evalúa por función financiera y trazabilidad, no por igualdad literal de filas. Las partidas médicas del archivo original se sustituyen por unidades propias de MuseIQ, mientras se conservan las relaciones entre presupuestos, estados financieros, flujo de efectivo e indicadores.

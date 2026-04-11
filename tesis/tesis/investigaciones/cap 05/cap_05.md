# Capítulo 5: Flujo de ingresos proyectados para MuseIQ

## Sentido del flujo de ingresos en una tesis de ingeniería aplicada

**A. Explicación conceptual del modelo de ingresos**

Proyectar un flujo de ingresos en una tesis tecnológica de ingeniería aplicada significa **traducir una propuesta técnica (arquitectura, alcance, desempeño esperado y modo de despliegue institucional) a una estructura económica verificable**: qué se cobra, a quién, con qué periodicidad, bajo qué supuestos de adopción y con qué relación de consistencia frente a los costos. En evaluación económico-financiera, este paso es imprescindible porque la comparación posterior entre costos y beneficios (o ingresos) requiere **series temporales consistentes**, no solo descripciones cualitativas. Esta lógica es coherente con guías de evaluación de proyectos que recomiendan construir proyecciones explícitas de demanda y de flujos monetarios, como parte de la sostenibilidad financiera del proyecto. citeturn1search0turn1search1

En el caso de MuseIQ, la necesidad de este capítulo se refuerza por tres hechos observables del contexto ya documentado en la tesis: (i) **alta disponibilidad de smartphones** en hogares peruanos (condición habilitante del enfoque BYOD), (ii) **masa crítica de visitas en museos administrados por el Estado** y (iii) existencia de **oferta tecnológica global** (audioguías, BYOD, QR/PWA, BLE, indoor navigation, IA) que impone condiciones de competencia y comparación. citeturn0search1turn5search1turn0search2

Desde una perspectiva metodológica para tesis, este capítulo cumple una función puente entre:  
**(a)** el análisis de mercado objetivo y la oferta tecnológica (Capítulos 3 y 4), y **(b)** la evaluación económico-financiera (Capítulo 10), porque define la **arquitectura de ingresos** (rubros, precios, recurrencias, escenarios) que luego se contrastará con la estructura de costos, inversiones, OPEX y criterios de rentabilidad o sostenibilidad (p. ej., VAN/TIR o métricas equivalentes según el enfoque). citeturn1search0turn1search33

**Datos observables que condicionan el flujo de ingresos (y que deben reflejarse en el modelo):**  
- Al cierre de 2024, **94,8% de hogares peruanos cuenta con smartphone** (más de 10 millones de familias), lo que hace defendible una solución BYOD como interfaz principal. citeturn0search1  
- En 2024 se registraron **1 790 502 visitas a los 56 museos administrados por el Ministerio de Cultura** (en el marco de indicadores de política). citeturn5search1  
- Existen plataformas globales de guías digitales que operan como **programas gratuitos para instituciones** (caso Bloomberg Connects) y/o como **SaaS de contenido** (Smartify, STQRY, izi.TRAVEL), lo cual presiona precios y obliga a justificar diferenciación (MuseIQ no compite solo por “tener una app”). citeturn0search2turn6search2turn6search3turn6search0  

## Naturaleza económica de MuseIQ como solución híbrida para instituciones

**Naturaleza económica de MuseIQ (corresponde al punto obligatorio 2)**

MuseIQ debe entenderse económicamente como una **solución híbrida producto–servicio (Product–Service System, PSS)** orientada a organizaciones, con dos rasgos dominantes:

1) **Componente “producto/activo” (tangible y configurable):** infraestructura BLE (beacons basados en ESP32), configuración de sala/zona y despliegue local en el museo. Este componente implica costos de implementación física, pruebas en sitio, calibración y reposición/soporte de hardware (aunque de bajo costo unitario respecto a alternativas de mayor precisión). citeturn8search20turn8search22  

2) **Componente “servicio/plataforma” (intangible y recurrente):** software móvil, backend de contenidos (RAG), operación de servicios de voz (TTS/STT) y capa conversacional/IA contextual, además de monitoreo, mantenimiento, soporte y actualización evolutiva. Esto se comporta como **plataforma institucional** más cercana a un “SaaS con servicios profesionales asociados” que a una app de consumo masivo. La literatura sobre PSS distingue modelos donde el valor se entrega como combinación de artefacto + servicio, y donde la monetización suele combinar pagos iniciales y pagos por uso/tiempo, favoreciendo continuidad y fidelización contractual. citeturn1search2turn2search28turn2search33  

Esta clasificación se justifica además por el **tipo de cliente**: MuseIQ se orienta a **museos públicos peruanos de alta o media afluencia** y, posteriormente, a museos privados/universitarios y centros culturales. En estos segmentos, la decisión de adopción suele ser institucional, con restricciones presupuestales y de contratación, y con necesidad de despliegue gradual (pilotos, ampliaciones por fases). En ese marco, modelos típicos de monetización B2B combinan (i) **proyecto de implementación** (servicio/obra tecnológica) y (ii) **contratos recurrentes** (mantenimiento, soporte, licencias/suscripciones, hosting y operación). citeturn5search1turn3search2turn1search2  

**Conexión explícita con los costos preliminares del documento complementario:** el documento `MuseIQ.pdf` plantea costos directos (hardware ESP32 y pruebas de TTS/STT/RAG) e indirectos (horas de desarrollo, consultoría, infraestructura). Esa mezcla ya sugiere que el costo no es solo “desarrollo de app”, sino un conjunto híbrido de actividades y consumos, lo que refuerza el encuadre PSS/plataforma institucional. fileciteturn0file1  

## Coherencia estratégica entre Capítulo 4, mercado objetivo y diseño de ingresos

**Relación entre el Capítulo 4, la base de costos y el Capítulo 5 (corresponde al punto obligatorio 3)**

El Capítulo 4 de la tesis concluye que existe oferta global madura en audioguías, BYOD, QR/PWA, BLE/indoor y asistentes con IA, pero **no es común** una arquitectura integrada que combine BLE + apoyo de orientación + voz + IA contextual (RAG) con enfoque de bajo costo y despliegue ligero para museos con restricciones, como los peruanos. Esa conclusión tiene consecuencias económicas directas: el modelo de ingresos de MuseIQ no puede copiar sin más ni (a) el esquema clásico de audioguía por alquiler de dispositivo, ni (b) el esquema puro SaaS global que asume escala internacional, onboarding estandarizado y costos de soporte distribuidos en grandes volúmenes. fileciteturn0file0  

En paralelo, el mercado objetivo priorizado (museos públicos de alta/media afluencia) implica que la captación y sostenimiento dependen de:  
- **viabilidad presupuestal** (capacidad de contratar implementación y pagar mantenimiento),  
- **viabilidad operativa** (capacidad del museo para mantener contenidos y operar la solución), y  
- **viabilidad institucional** (procesos de aprobación, contratación pública y continuidad anual).  
La evidencia comparada sobre transformación digital en museos describe barreras persistentes en recursos humanos y financieros, riesgo de obsolescencia, y necesidad de enfoques sostenibles (no solo “proyectos de vitrina”). citeturn9search9turn9search6turn9search0  

**Implicancias económicas específicas derivadas del Capítulo 4 (inferencia analítica sustentada):**  
- Si MuseIQ compite en un ecosistema donde existen guías digitales globales (incluyendo alternativas gratuitas para instituciones), el ingreso principal defendible debe provenir de **lo que estas alternativas no cubren** en el mismo paquete: despliegue BLE en sitio, calibración por sala, integración curatorial para RAG, accesibilidad por voz en sala, y analítica operacional orientada al museo. citeturn0search2turn6search2turn8search20  
- El ingreso debe organizarse de modo que **la barrera de entrada sea gestionable** para museos públicos: contrato inicial acotado (piloto) y recurrencia anual moderada (soporte/operación), evitando exigir una inversión inicial tipo “gran plataforma” o “hardware propietario por visitante”. citeturn5search1turn1search2turn9search6  

**Por qué MuseIQ no debe pensarse igual que una audioguía tradicional:** una audioguía clásica se monetiza muchas veces mediante alquiler por visitante y logística de dispositivos (CAPEX en equipos dedicados, mantenimiento físico). MuseIQ, al ser BYOD, desplaza ese CAPEX hacia el visitante (smartphone ya existente) y traslada el énfasis económico hacia: implementación de infraestructura de sala (beacons) + software + operación de servicios digitales. Esto se alinea con la tendencia de plataformas museales que promueven “no más hardware” y con modelos institucionales basados en suscripción/licencia. citeturn0search1turn6search15turn1search2  

**Por qué MuseIQ tampoco es equivalente a un SaaS global “solo software”:** porque requiere (i) un componente técnico local (BLE, calibración) y (ii) un componente de conocimiento institucional (contenidos curatoriales estructurados para RAG) cuyo esfuerzo inicial es específico por museo. Estos rasgos justifican una mezcla de ingresos por **proyecto (setup)** y por **servicio recurrente (operación, soporte, actualizaciones)**, coherente con la lógica PSS. citeturn1search2turn2search33turn1search0  

## Lectura crítica de la base de costos existente y trazabilidad para ingresos

**B. Lectura crítica de la base de costos de `tesis/MuseIQ.pdf` (corresponde al punto obligatorio 4)**

El documento complementario `MuseIQ.pdf` presenta un presupuesto estimado de **USD 1 055**, desagregado en **costos directos (USD 205)** y **costos indirectos (USD 850)**. fileciteturn0file1

### Componentes principales identificados en la base de costos

**Costos directos (USD 205, según el documento):**  
- Hardware inicial: **ESP32 (3 unidades) por USD 90**, más cables/accesorios (USD 20) y fuente de alimentación (USD 15).  
- Herramientas de desarrollo/diseño: licencia asociada al entorno de desarrollo (USD 50), herramientas de diseño (USD 30) y herramienta de escaneo BLE sin costo (nRF Connect: USD 0).  
- Pruebas de servicios de voz e IA: pruebas TTS (USD 20), STT (USD 20) y RAG/LLM (USD 50). fileciteturn0file1  

**Costos indirectos (USD 850, según el documento):**  
- Horas de desarrollo personal (USD 500).  
- Infraestructura de trabajo (PC, internet, electricidad: USD 100).  
- Consultoría externa eventual para integración de IA (USD 200).  
- Costos administrativos (documentación/licencias: USD 50). fileciteturn0file1  

### Interpretación económica: qué representa realmente este presupuesto

Esta base de costos es consistente con un **escenario de prototipo/piloto académico**, no con un despliegue institucional completo. La presencia de: (i) 3 ESP32, (ii) “pruebas” de TTS/STT/RAG y (iii) valorización reducida de horas de desarrollo, sugiere que el objetivo fue estimar **el costo de construir y validar un MVP**, no el costo total de operar MuseIQ como servicio para múltiples museos. fileciteturn0file1  

### Vacíos o simplificaciones relevantes (que deben declararse antes de proyectar ingresos)

Sin invalidar la utilidad del documento como punto de partida, para sostener un Capítulo 5 defendible conviene explicitar al menos seis simplificaciones:

1) **Escala de hardware insuficiente para museo real mediano/grande.** Tres beacons difícilmente cubren múltiples salas; en despliegues reales se requiere dimensionamiento por área/salas y calibración. citeturn8search20turn8search22  

2) **No se explicita costo recurrente de operación digital.** En producción, TTS/STT/LLM suelen cobrarse por consumo (minutos, caracteres, tokens) y, además, hay costos de hosting/monitoreo. Las propias páginas de precios muestran esquemas de cobro por volumen. citeturn4search0turn4search1turn4search2turn4search3  

3) **No se incluye una línea específica de “producción/curaduría de contenidos para RAG”.** En museos, convertir fichas, guiones curatoriales, metadatos y señalética en un repositorio consultable y trazable suele ser un esfuerzo relevante, y la literatura de transformación digital destaca restricciones de capacidades y recursos humanos. citeturn9search9turn9search6  

4) **No se incluye soporte en campo ni mantenimiento de beacons.** Aunque BLE es costo-efectivo, igual requiere revisiones, reposiciones, cambios de batería y control de funcionamiento. citeturn8search22turn8search15  

5) **Capex vs Opex están mezclados de forma preliminar.** Para el modelo de ingresos, es necesario mapear qué costos se recuperan en un cobro “setup/implementación” y cuáles requieren **ingreso recurrente**. citeturn1search0turn1search33  

6) **No se considera la presión competitiva de soluciones gratuitas o de bajo costo.** Bloomberg Connects declara gratuidad para instituciones y ofrece entrenamiento/soporte a socios, lo que obliga a justificar ingresos por valor diferencial (BLE + voz + RAG + analítica). citeturn0search2  

**Resultado de la lectura crítica (síntesis):** el presupuesto del documento complementario es una base trazable para el piloto (y útil para construir coherencia), pero el Capítulo 5 debe **reclasificar** estos costos en: (a) inversión inicial por cliente (hardware + instalación + configuración + preparación de contenidos) y (b) costos recurrentes (operación IA/voz, hosting, soporte, mejoras), porque el flujo de ingresos debe cubrir ambos para ser sostenible. fileciteturn0file1  

## Fuentes potenciales de ingreso y evaluación de viabilidad

**C. Identificación y evaluación de fuentes de ingreso (corresponde al punto obligatorio 5)**

A continuación se listan fuentes de ingreso compatibles con MuseIQ, indicando **quién paga, periodicidad, viabilidad y vínculo con la estructura de costos**. Se presentan como un portafolio; no se asume un modelo único sin justificación.

### Implementación por proyecto

**Descripción:** servicio de despliegue inicial (levantamiento en sitio, diseño de ubicación de beacons, instalación/configuración, calibración por sala/zona, configuración de la app y del backend, carga inicial de contenidos, pruebas de aceptación).  
**Quién paga:** la institución (museo) o un nivel articulador (p. ej., unidad ejecutora o dirección sectorial), según el esquema institucional.  
**Periodicidad:** pago único por proyecto (por museo o por sede).  
**Viabilidad:** alta, porque calza con prácticas de contratación pública/servicios profesionales y porque MuseIQ no es “solo software”; requiere intervención en sitio. citeturn3search2turn3search0  
**Rol:** ingreso principal en etapas tempranas (años iniciales) para financiar despliegues y aprendizaje operativo.

**Relación con costos:** cubre hardware (beacons/ESP32 y accesorios), horas de configuración, consultoría, pruebas en campo y parte de costos indirectos de ingeniería. fileciteturn0file1  

### Licenciamiento anual o suscripción institucional

**Descripción:** derecho de uso + operación del sistema (hosting, actualizaciones, soporte, monitoreo básico, mantenimiento correctivo del software, y eventualmente una bolsa de consumo de IA/voz).  
**Quién paga:** institución usuaria (museo) o ente financiador recurrente.  
**Periodicidad:** anual (a veces con pagos mensuales, pero anual es más coherente en sector público).  
**Viabilidad:** alta, porque el mercado comparable de guías digitales opera ampliamente con suscripciones/licencias anuales. Por ejemplo, Smartify publica planes anuales para instituciones; y el programa enterprise de izi.TRAVEL publica rangos mensuales según volumen de accesos. citeturn6search2turn6search3  
**Rol:** ingreso principal de mediano y largo plazo (sostenibilidad), especialmente cuando la base instalada crece.

**Relación con costos:** cubre OPEX recurrente: operación y soporte, evolución de software, hosting, y consumos variables (TTS/STT/LLM) que en proveedores cloud se tarifan por uso. citeturn4search0turn4search1turn4search3  

### Mantenimiento y soporte técnico extendido

**Descripción:** niveles de servicio (SLA) diferenciados: soporte en horario extendido, tiempos de respuesta, soporte en sitio, mantenimiento preventivo de beacons, reportes operativos.  
**Quién paga:** institución que requiere mayor criticidad o confiabilidad.  
**Periodicidad:** anual, como add-on.  
**Viabilidad:** media–alta, porque instituciones con alta afluencia pueden exigir continuidad. Contratos públicos de “mantenimiento y soporte” anual son frecuentes en software e infraestructura. citeturn3search2turn3search9  
**Rol:** ingreso complementario, útil para escalamiento y profesionalización del servicio.

**Relación con costos:** cubre OPEX de soporte (horas técnicas), logística de reposición de hardware y gestión de incidentes. citeturn8search22turn3search0  

### Personalización y producción de contenidos

**Descripción:** servicios de estructuración curatorial (curación digital, guiones, segmentación por sala, etiquetado, generación de corpus para RAG con trazabilidad), traducción, voces, accesibilidad (p. ej., audio-descripción), y actualización editorial por exposiciones temporales.  
**Quién paga:** museo (curaduría/educación/comunicaciones) o proyectos financiados externamente.  
**Periodicidad:** proyecto (por exposición o por lote de salas), con posible retainer anual.  
**Viabilidad:** alta como servicio, porque muchas instituciones no tienen capacidad interna suficiente para sostener producción digital continua; esta limitación aparece repetidamente en literatura de transformación digital museal. citeturn9search9turn9search30turn9search6  
**Rol:** ingreso complementario significativo, especialmente en museos con exposiciones temporales.

**Relación con costos:** cubre horas especializadas (equipo de contenido/datos) y reduce el riesgo de que el sistema fracase por falta de insumos curatoriales. citeturn9search9turn1search0  

### Instalación/venta de infraestructura BLE y reposición tecnológica

**Descripción:** provisión de beacons (como venta o como “paquete”), reposición por ciclo de vida, mejoras de firmware, y eventualmente mejoras de cobertura (más salas).  
**Quién paga:** museo.  
**Periodicidad:** inicial + eventos de reposición (cada cierto número de años o ante fallas).  
**Viabilidad:** media en museos públicos si se plantea como compra de bienes; alta si se empaqueta dentro del proyecto de implementación.  
**Rol:** complemento; funciona mejor como parte del setup.

**Relación con costos:** corresponde a costos directos de hardware ya presentes en la base preliminar. fileciteturn0file1  

### Módulos premium de analítica y gestión

**Descripción:** dashboards de flujo de visita, interacción con contenidos, métricas por sala, y exportaciones para planificación museográfica/educativa.  
**Quién paga:** museos con equipos de gestión interesados en evidencia de uso.  
**Periodicidad:** anual (add-on).  
**Viabilidad:** media, porque depende de madurez de gestión y de políticas de datos; pero puede ser un diferencial frente a soluciones “solo contenido”. La literatura destaca que medir y gestionar la transformación digital requiere marcos e indicadores, y en museos esto suele ser un desafío. citeturn9search27turn1search0  
**Rol:** complementario; puede aumentar ARPA (ingreso por cliente) sin elevar proporcionalmente costos de hardware.

### Integraciones institucionales

**Descripción:** integración con catálogos, CMS, ticketing, sistemas de inventario o portales institucionales.  
**Quién paga:** instituciones de mayor complejidad.  
**Periodicidad:** proyecto.  
**Viabilidad:** media; depende de interoperabilidad y disponibilidad de APIs/formatos.  
**Rol:** complementario; relevante en museos grandes.

**Inferencia clave:** dado el mercado objetivo y la necesidad de despliegue ligero/costo contenido, **los ingresos principales más defendibles** tienden a ser (i) implementación por proyecto + (ii) suscripción/licencia anual; el resto funciona como “capas” opcionales según capacidad y madurez del museo. Esta estructura es coherente con modelos híbridos en software, donde los servicios complementan el producto y fortalecen la relación con el cliente. citeturn2search33turn2search28turn1search2  

## Modelo de monetización más defendible para MuseIQ

**Modelo de monetización más defendible (corresponde al punto obligatorio 6)**

Para MuseIQ, el modelo más defendible para tesis (en el contexto de museos públicos peruanos, y coherente con el posicionamiento del Capítulo 4) es un **modelo mixto en dos niveles**, con modularidad controlada:

### Núcleo del modelo (dos niveles)

1) **Contrato de implementación (pago único por sede/museo)**  
Incluye: diagnóstico, diseño de despliegue BLE, configuración por salas, instalación y calibración, carga inicial de contenidos y pruebas en sitio.  
**Justificación:** MuseIQ incorpora componentes locales (BLE + calibración) y trabajo inicial específico por museo (contenidos para RAG), lo que no se cubre bien con una simple suscripción estándar “self-service”. citeturn1search2turn8search20  

2) **Suscripción/licencia anual institucional (pago recurrente)**  
Incluye: hosting/operación, soporte, actualizaciones, monitoreo, seguridad básica y—si se decide—una bolsa de consumo para servicios de voz e IA (o una política de “fair use”).  
**Justificación:** la sostenibilidad requiere cubrir OPEX y evolución; además, plataformas comparables en el sector cultural ofrecen planes anuales y escalamiento por capacidad/volumen (objetos, tours, accesos). citeturn6search2turn6search3turn1search0  

### Complementos (add-ons) con criterio de prudencia presupuestal

- **Contenido & RAG pack:** producción/estructuración curatorial por salas o por exposición.  
- **Soporte extendido y mantenimiento preventivo BLE:** para museos de alta afluencia.  
- **Analítica premium:** para gestión y planificación.

Este enfoque evita dos riesgos frecuentes:  
- **Riesgo 1: subestimar costos recurrentes** (p. ej., IA/voz, soporte) y depender solo de ingresos únicos, lo que suele ser inestable en proyectos tecnológicos. citeturn1search0turn4search3  
- **Riesgo 2: copiar un SaaS global “plug-and-play”** que presupone onboarding sin fricción, cuando en museos existen límites de capacidades y recursos y hay presión por soluciones gratuitas. citeturn9search9turn0search2  

**Coherencia con restricciones de museos públicos:** en contratación pública es frecuente separar “implementación” (servicio/proyecto) de “mantenimiento/suscripción anual” (servicio recurrente). Existen múltiples ejemplos de contratación estatal de renovaciones anuales de suscripción y mantenimiento de software. citeturn3search2turn3search0  

## Variables y supuestos para proyectar ingresos con trazabilidad

**D. Variables del modelo (corresponde al punto obligatorio 7)**  
**E. Supuestos del modelo (corresponde al punto obligatorio 8)**

### Variables clave propuestas

Para construir el flujo de ingresos anual a 10 años, las variables mínimas recomendadas son:

**Variables de mercado y adopción institucional**
- **N₀ (base instalada inicial):** instituciones con MuseIQ al inicio del horizonte (típicamente 0 o 1 si el año 1 es piloto).  
- **Nᵧ (clientes nuevos por año):** número de nuevas instituciones que contratan implementación en el año y.  
- **Aᵧ (clientes activos acumulados):** instituciones con contrato vigente al cierre del año y.  
- **r (tasa de retención anual):** proporción de instituciones que renuevan la suscripción/licencia anual (proxy de continuidad institucional y satisfacción).  
- **L (límite de mercado abordable):** tamaño del mercado en el que el modelo opera (p. ej., 56 museos administrados por el Ministerio de Cultura como mercado primario; potencial ampliado con otros museos del catastro). citeturn5search1turn5search5  

**Variables de precios (por rubro de ingreso)**
- **P_impl (precio de implementación):** ingreso por nuevo cliente (setup + despliegue).  
- **P_sub (precio anual de suscripción/licencia):** ingreso recurrente por cliente activo.  
- **P_add (precio de servicios adicionales):** ingreso por paquete de contenido/analítica/soporte extendido, cuando aplica.  
- **α (tasa de adopción de add-ons):** proporción de clientes activos que adquieren add-ons.

**Variables de reconocimiento temporal**
- **f_onboard (factor de activación anual):** proporción del año en que un cliente nuevo paga y usa el servicio (si el onboarding promedio ocurre a mitad de año, f_onboard ≈ 0,5). Este factor evita sobreestimar ingresos recurrentes del primer año por cliente nuevo. citeturn1search0  

### Observables que fijan rangos y límites (no supuestos)

- **Mercado primario:** 56 museos administrados por el Ministerio de Cultura y 1 790 502 visitas en 2024 (base de demanda presencial donde MuseIQ agrega valor durante la visita). citeturn5search1  
- **Mercado ampliado potencial:** catastro reporta cientos de museos (p. ej., 372 museos en el catastro de la DGM, y 800 instituciones museales mapeadas en el catastro, según reportes difundidos por Ibermuseos). citeturn5search5turn5search29  
- **Rangos públicos de precios del “SaaS de guía digital” (comparables, útiles como ancla):** Smartify publica planes institucionales anuales desde £1,800 a £9,500; y el programa enterprise de izi.TRAVEL declara planes desde €100/mes a €1,000/mes según volumen; STQRY reporta planes alrededor de $199/mes (≈$2,295/año). citeturn6search2turn6search3turn6search0  

### Supuestos explícitos por escenario

A continuación se proponen **tres conjuntos de supuestos** (conservador, base, optimista) para 10 años. Se presentan como hipótesis de modelado, no como “hechos”.

**Supuestos conservadores (prudencia para adopción pública)**
- Nᵧ: 1 museo nuevo por año (adopción lenta por restricciones presupuestales/procesos).  
- r: 0,85 (riesgo de no renovación por cambios de gestión o presupuesto).  
- P_sub: en la parte baja del rango comparable de SaaS cultural (≈USD 2 000/año como valor **referencial** alineado a planes económicos de plataformas).  
- P_impl: moderado (≈USD 4 000 por museo **referencial**), justificable como múltiplo razonable del costo de hardware + servicio y dentro de un orden de magnitud “miles” (no “decenas de miles”), coherente con enfoque de bajo costo y con costos de plataforma observados. citeturn6search0turn6search2turn8search22  
- α: 0,20 (solo una minoría contrata add-ons).

**Supuestos base (escenario defendible para tesis)**
- Nᵧ: crecimiento gradual (1,2,3,4,4,4,4,4,3,3) con expansión del segmento primario al secundario hacia mitad del horizonte.  
- r: 0,90 (continuidad razonable si el sistema aporta valor y se institucionaliza).  
- P_sub: ≈USD 2 500/año (**referencial**) en línea con rangos publicados de plataformas de guía digital. citeturn6search0turn6search2  
- P_impl: ≈USD 5 000 (**referencial**) para cubrir despliegue BLE + configuración + carga inicial, manteniendo posicionamiento “bajo costo” frente a soluciones propietarias más pesadas (y reconociendo que Bloomberg Connects existe como alternativa gratuita). citeturn0search2turn8search20turn6search2  
- α: 0,30 (una parte de museos compra módulos de contenido/analítica).  

**Supuestos optimistas (aceleración por evidencia de valor y escalamiento)**
- Nᵧ: (2,3,4,6,6,6,6,6,5,5), habilitado por replicabilidad y estandarización del despliegue.  
- r: 0,95 (retención alta por dependencia operativa del servicio).  
- P_sub: ≈USD 3 000/año (**referencial**) aún dentro del orden de magnitud de SaaS cultural publicado, especialmente para instituciones con necesidades avanzadas. citeturn6search2turn6search3  
- P_impl: ≈USD 6 000 (**referencial**) por mayor alcance (más salas/servicios e integraciones).  
- α: 0,40 (adopción mayor de add-ons).

**Nota metodológica clave:** en todos los escenarios, si se decide incluir consumo de IA/voz como parte del servicio, el costo marginal existe y debe ser cubierto por P_sub o por sobrecargos por uso. Los precios oficiales de STT/TTS y de tokens en LLM muestran que estos consumos son cuantificables y modelables, incluso con sensibilidad. citeturn4search0turn4search1turn4search3  

## Metodología para proyectar ingresos y tabla a diez años

**F. Tabla de ingresos proyectados a 10 años (corresponde a los puntos obligatorios 9 y 10)**  
**G. Escenarios conservador, base y optimista (corresponde al punto obligatorio 11)**

### Metodología paso a paso (replicable en hoja de cálculo)

La construcción del flujo anual puede seguir esta secuencia (alineada con guías de evaluación financiera que recomiendan hipótesis explícitas y trazabilidad entre demanda, precios y flujos): citeturn1search0turn1search33  

1) **Definir el mercado abordable (L)**  
   - Mercado primario: 56 museos administrados por el Ministerio de Cultura (límite natural del primer segmento). citeturn5search1  
   - Mercado secundario/potencial: otros museos del catastro (centenas) para escalamiento. citeturn5search5  

2) **Definir la trayectoria de adopción anual (Nᵧ)**  
   - Asignar Nᵧ por año en cada escenario, cuidando no exceder L primario si no se incluye el secundario.

3) **Modelar la base activa**  
   - Aᵧ = Aᵧ₋₁·r + Nᵧ  
   Interpretación: base activa esperada al cierre del año.

4) **Definir precios por rubro**  
   - P_impl, P_sub, α y P_add.  
   - Justificar P_sub con rangos observables de plataformas comparables y P_impl con la presencia de trabajo en sitio (BLE + calibración + contenidos). citeturn6search2turn6search3turn8search20  

5) **Reconocimiento de ingresos recurrentes del primer año (f_onboard)**  
   - Para no sobreestimar, aplicar f_onboard a nuevos clientes en el año de implementación (p. ej., 0,5 si el contrato promedio entra a mitad de año). citeturn1search0  

6) **Calcular ingresos por rubro**  
   - Ingreso implementaciónᵧ = Nᵧ·P_impl  
   - Ingreso recurrenteᵧ = (Aᵧ₋₁·r)·P_sub + (Nᵧ·f_onboard)·P_sub  
   - Ingreso add-onsᵧ = [(Aᵧ₋₁·r)·α + (Nᵧ·f_onboard)·α]·P_add  

7) **Consolidar ingreso total anual**  
   - Totalᵧ = Implementaciónᵧ + Recurrenteᵧ + Add-onsᵧ  

8) **Validación de coherencia con costos preliminares**  
   - Verificar que la recurrencia anual cubra al menos hosting/soporte y consumos variables previsibles (TTS/STT/LLM) cuando corresponda. citeturn4search0turn4search1turn4search3turn0file1  

### Tabla modelo de flujo de ingresos a diez años (escenario base)

Los valores siguientes son **referenciales/ilustrativos**, construidos dentro del orden de magnitud observable en plataformas comparables (suscripciones de guías digitales) y añadiendo un componente de implementación por tratarse de una solución con despliegue BLE + configuración local (característica diferencial frente a SaaS “solo contenido”). citeturn6search2turn6search3turn8search22turn0search2  

**Parámetros del escenario base (ilustrativos):**  
- r = 0,90; f_onboard = 0,5  
- P_impl = USD 5 000 por museo  
- P_sub = USD 2 500 por museo/año  
- Add-on promedio: P_add = USD 1 000; α = 0,30  

| Año | Clientes institucionales nuevos (Nᵧ) | Instituciones activas esperadas (Aᵧ) | Ingresos por implementación (USD) | Ingresos recurrentes (USD) | Ingresos por servicios adicionales (USD) | Ingreso total anual (USD) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1,00 | 5 000 | 1 250 | 150 | 6 400 |
| 2 | 2 | 2,90 | 10 000 | 3 375 | 405 | 13 780 |
| 3 | 3 | 5,61 | 15 000 | 7 013 | 842 | 22 855 |
| 4 | 4 | 9,05 | 20 000 | 12 636 | 1 516 | 34 152 |
| 5 | 4 | 12,14 | 20 000 | 20 368 | 2 444 | 42 812 |
| 6 | 4 | 14,93 | 20 000 | 28 781 | 3 454 | 52 235 |
| 7 | 4 | 17,44 | 20 000 | 37 932 | 4 552 | 62 484 |
| 8 | 4 | 19,70 | 20 000 | 47 880 | 5 746 | 73 626 |
| 9 | 3 | 20,73 | 15 000 | 56 176 | 6 741 | 77 917 |
| 10 | 3 | 21,65 | 15 000 | 63 432 | 7 612 | 86 044 |

**Lectura de la tabla:**  
- El peso de ingresos se desplaza gradualmente desde implementación hacia recurrencia, lo cual es deseable para estabilidad.  
- Aᵧ son “instituciones activas esperadas” (valor esperado) por el uso de r como proporción; en una hoja de cálculo puede redondearse o trabajarse en enteros por escenario. citeturn1search0  

### Escenarios comparados (resumen)

A continuación se resume cómo cambian los resultados al variar adopción, retención y precios (manteniendo la misma estructura de rubros).

**Escenario conservador (referencial):** Nᵧ=1 constante; r=0,85; P_impl=4 000; P_sub=2 000; α=0,20; P_add=800.  
- La base activa crece lentamente y el ingreso total anual al año 10 queda dominado por implementación + recurrencia moderada.  
- Este escenario refleja fricciones institucionales y baja expansión. citeturn9search9turn3search0  

**Escenario base (tabla anterior):** crecimiento gradual, r=0,90; precios en zona media de comparables. citeturn6search2turn6search3  

**Escenario optimista (referencial):** adopción acelerada; r=0,95; P_impl=6 000; P_sub=3 000; α=0,40; P_add=1 200.  
- Se acelera el punto en que los ingresos recurrentes dominan el total.  
- Requiere estandarización de despliegue y evidencia sólida de valor para superar la presión de alternativas gratuitas/competencia. citeturn0search2turn2search33turn9search6  

## Análisis crítico del flujo de ingresos, redacción para tesis, conclusión, referencias y datos por precisar

**Análisis crítico del flujo de ingresos (corresponde al punto obligatorio 12)**

### Sensibilidad y variables críticas

En MuseIQ, las variables más críticas para el ingreso total a 10 años son:

1) **Adopción anual (Nᵧ):** en modelos institucionales, pequeños cambios en Nᵧ generan grandes diferencias acumuladas, porque cada cliente nuevo arrastra ingresos recurrentes. Esta lógica se alinea con la economía de modelos de suscripción y con hallazgos sobre cómo los servicios se vuelven relevantes en el desempeño de empresas de software, al crear continuidad de relación cliente–proveedor. citeturn2search33turn2search28  

2) **Retención (r):** un r menor erosiona el “stock” de clientes activos y reduce ingresos recurrentes. En museos, la retención está influida por capacidades internas, entrenamiento y sostenibilidad operativa; la literatura registra riesgos de falta de recursos y de obsolescencia/abandono de tecnologías si no se integran en procesos. citeturn9search9turn9search30  

3) **Precio de suscripción (P_sub) vs presión competitiva:** Bloomberg Connects declara ser “free for institutions”, lo que obliga a que P_sub se sostenga por valor diferencial (BLE + voz + RAG + analítica) y no por “ser una guía digital más”. citeturn0search2  

4) **Costo variable de IA/voz (no modelado aún como costo en este capítulo, pero determinante):** los servicios de STT/TTS/LLM son cobrados por volumen; si la adopción por visitantes y el uso de voz aumentan, el costo variable puede crecer y debe estar cubierto por el ingreso recurrente o por tarifas por uso. Esto conecta directamente con la coherencia costos–ingresos pedida para el paso hacia Capítulo 10. citeturn4search0turn4search1turn4search3  

### Riesgos de adopción y barreras institucionales

- **Fricción por “una app por museo”:** existe evidencia (aunque no académica revisada por pares) de baja tasa de descarga/uso de apps nativas oficiales en museos (≈2,47%), lo que sugiere que el valor de MuseIQ debe justificarse aun si el porcentaje de visitantes que usa la app no es alto. En un modelo B2B institucional, esto se aborda enfatizando beneficios institucionales (accesibilidad, autoguiado, reducción de carga humana, analítica) más que “descargas”. citeturn0search3turn0search7  
- **Capacidades internas:** transformación digital demanda habilidades y tiempo del personal; sin capacitación, el sistema puede degradarse por falta de actualización de contenidos o por operación irregular. citeturn9search30turn9search9  
- **Restricción presupuestal y vulnerabilidad a shocks externos:** reportes sectoriales muestran pérdidas e inestabilidad financiera en museos (especialmente en crisis), lo cual se traduce en riesgo de no renovación. citeturn9search0turn9search22  

### Coherencia (y tensiones) con la base de costos preliminar

- **Coherencia:** la estructura de ingresos propuesta (implementación + recurrencia) es coherente con la estructura de costos del documento `MuseIQ.pdf`, que mezcla hardware inicial y “pruebas” de servicios (costos directos) con horas de desarrollo/consultoría (indirectos). Esa mezcla es típica de soluciones híbridas. fileciteturn0file1  
- **Tensión:** el presupuesto de USD 1 055 no representa el costo real de operar y mantener la solución por 10 años; si se usara como costo total, induciría precios irreales. Por ello, la tesis debe declarar explícitamente que esa base es de prototipo y que el Capítulo 10 deberá reestimar costos de operación y despliegue por museo. fileciteturn0file1  

**H. Redacción académica utilizable directamente en la tesis (corresponde al punto obligatorio 13)**

Texto propuesto (adaptable y editable):

> **Capítulo 5 – Flujo de Ingresos Proyectados**  
>  
> La proyección del flujo de ingresos constituye una etapa necesaria para vincular la propuesta tecnológica MuseIQ con su viabilidad económica dentro del horizonte de evaluación. En proyectos de ingeniería aplicada, esta sección traduce el diseño técnico y el posicionamiento de la solución en un conjunto explícito de fuentes de ingreso, supuestos de adopción institucional y series anuales que permitan, en el capítulo de evaluación económico-financiera, contrastar ingresos con costos, inversiones y operación. Esta lógica es consistente con metodologías de evaluación de proyectos que recomiendan proyectar ingresos a partir del análisis de demanda y de la estrategia de precios, asegurando trazabilidad entre mercado, capacidad de despliegue y flujos monetarios. citeturn1search0turn1search33  
>  
> MuseIQ se entiende económicamente como una solución híbrida producto–servicio orientada a instituciones culturales. Su arquitectura integra infraestructura BLE de bajo costo (beacons basados en ESP32 y calibración por sala o zona), interacción por voz (TTS/STT) y una capa de inteligencia conversacional anclada mediante recuperación aumentada (RAG). En consecuencia, la generación de valor no se limita a una aplicación móvil, sino a un sistema implementable por proyecto en un recinto físico y operable como plataforma tecnológica institucional. La literatura sobre sistemas producto–servicio sustenta la pertinencia de modelos donde el ingreso combina componentes iniciales (implementación) y recurrentes (servicio en el tiempo), particularmente cuando la solución requiere despliegue local y soporte continuo. citeturn1search2turn2search28  
>  
> El mercado objetivo priorizado corresponde a museos públicos peruanos de alta o media afluencia, con posibilidad de escalamiento posterior hacia museos privados, universitarios y centros culturales. Este enfoque se apoya en condiciones habilitantes del entorno: alta penetración de smartphones en hogares peruanos (aproximadamente 94,8% al cierre de 2024) y una demanda presencial significativa (1 790 502 visitas en 2024 en los 56 museos administrados por el Ministerio de Cultura). Estas condiciones favorecen estrategias BYOD y justifican el despliegue de soporte digital en sala. citeturn0search1turn5search1  
>  
> La relación con el análisis de oferta tecnológica mundial (Capítulo 4) es directa: aunque existen audioguías, plataformas BYOD, soluciones QR/PWA, sistemas con BLE e iniciativas con IA, no es frecuente encontrar una arquitectura integrada que combine reconocimiento por sala, apoyo de orientación, voz e IA contextual con enfoque de bajo costo para museos con restricciones presupuestales. Por ello, MuseIQ no se monetiza como una audioguía tradicional basada en alquiler de dispositivos, ni como un SaaS global puramente estandarizado, sino como una solución institucional con implementación en sitio y operación recurrente. fileciteturn0file0  
>  
> En coherencia con la base preliminar de costos del documento complementario, que identifica hardware BLE, herramientas de desarrollo y consumos de prueba de TTS/STT/RAG, además de horas de desarrollo e infraestructura, se plantean dos fuentes principales de ingresos: (i) un pago único por implementación (despliegue BLE, configuración y puesta en marcha por museo) y (ii) una suscripción/licencia anual institucional que cubra operación, hosting, soporte y actualizaciones. Complementariamente, se consideran servicios de producción y actualización de contenidos (incluyendo estructuración para RAG), capacitación y módulos opcionales de analítica. Esta estructura permite diferenciar costos iniciales de costos recurrentes y construir una proyección anual a 10 años con supuestos explícitos de adopción, permanencia y precios referenciales anclados a rangos observables de plataformas comparables en el sector cultural. citeturn6search2turn6search3turn0file1  
>  
> Finalmente, se establecen escenarios conservador, base y optimista, variando las trayectorias de adopción y la tasa de renovación anual, con el objetivo de evaluar la sensibilidad del ingreso total a factores institucionales y operativos. Este enfoque prepara el paso al capítulo de evaluación económico-financiera, donde los flujos de ingresos aquí planteados deberán contrastarse con el redimensionamiento de costos de despliegue y operación, así como con métricas de sostenibilidad y riesgo.

**Conclusión del capítulo (corresponde al punto obligatorio 14)**

En síntesis, el flujo de ingresos de MuseIQ debe construirse como un modelo B2B institucional coherente con su naturaleza híbrida: **implementación por proyecto** (por requerir despliegue BLE, calibración y preparación inicial por museo) y **servicio recurrente anual** (para sostener operación, soporte, actualización y consumos digitales asociados a voz e IA). La evidencia del entorno peruano (penetración de smartphones y volumen de visitas en museos estatales) respalda la viabilidad de una interfaz BYOD, mientras que la oferta global (incluyendo alternativas gratuitas para instituciones y SaaS de guías digitales con precios publicados) condiciona el nivel y la estructura de precios, exigiendo diferenciación por valor técnico y operacional. citeturn0search1turn5search1turn0search2turn6search2  
Con las variables y supuestos definidos, el capítulo deja preparado el insumo central para el Capítulo 10: una **serie anual de ingresos** por rubros y escenarios, lista para integrarse con el redimensionamiento de costos (CAPEX/OPEX) y con la evaluación económico-financiera (sostenibilidad, sensibilidad y riesgo). citeturn1search0turn0file1  

**I. Referencias utilizadas o sugeridas (selección)**

- entity["organization","Comisión Europea","eu regional policy cba guide"]. *Guide to Cost-Benefit Analysis of Investment Projects* (2014). citeturn1search0  
- entity["organization","UNIDO","industrial feasibility studies manual"]. *Manual for the Preparation of Industrial Feasibility Studies* y *Guidelines…* (ediciones disponibles). citeturn1search1turn1search33  
- Tukker, A. (2004). *Eight types of product–service system…* citeturn1search2  
- Kowalkowski, C. et al. (2024). *Subscription offers in business-to-business markets* (taxonomía de ofertas de suscripción B2B). citeturn2search28  
- Cusumano, M. A., Suarez, F. F., & Kahl, S. J. (2013). *Services and the Business Models of Product Firms…* citeturn2search9turn2search33  
- entity["organization","OSIPTEL","telecom regulator peru"]. ERESTEL: 94,8% de hogares con smartphone al cierre de 2024. citeturn0search1  
- entity["organization","Ministerio de Cultura del Perú","cultural ministry lima peru"]. Reporte de cumplimiento 2024: 1 790 502 visitas a 56 museos administrados. citeturn5search1  
- entity["organization","Bloomberg Connects","cultural guide app"]. Información institucional: app gratuita y “free for institutions”. citeturn0search2  
- Nikolaou, P. (2024). *Museums and the Post-Digital…* (desafíos y déficits de recursos en transformación digital). citeturn9search9  
- entity["organization","Banco Interamericano de Desarrollo","idb museums latin america report"]. *Museums Trends and Digital Strategies…* (ALC). citeturn9search6  
- NEMO. *Survey on the impact of the COVID-19 situation on museums in Europe* (impacto económico, vulnerabilidades). citeturn9search0  
- Google Cloud: precios de Text-to-Speech y Speech-to-Text (referencia para modelar OPEX variable). citeturn4search0turn4search1  
- AWS: precios de Amazon Polly (TTS). citeturn4search2  
- entity["company","OpenAI","api pricing"]: precios API (tokens y modelos multimodales). citeturn4search3turn4search7  
- Smartify (pricing para instituciones). citeturn6search2  
- izi.TRAVEL (Enterprise Partner Program, pricing por volumen). citeturn6search3  
- STQRY (ancla de orden de magnitud de suscripción en plataformas de tours). citeturn6search0  
- Verde et al. (2023). BLE en museo y evidencia de precisión por sala (sustento técnico para BLE). citeturn8search20  

**J. Datos que aún convendría precisar**

Para convertir este Capítulo 5 en un insumo “cerrado” para la evaluación económico-financiera (Capítulo 10), convendría precisar al menos:

1) **Dimensionamiento de despliegue BLE por tipología de museo** (número de salas, m², número estimado de beacons, estrategia de alimentación/batería y plan de mantenimiento). Esto transformará P_impl de “referencial” a costo calculado. citeturn8search20turn8search22  

2) **Arquitectura de operación (hosting, seguridad, disponibilidad) y su costo anual**: si el backend es cloud gestionado, on-premise o híbrido; y qué parte del costo se distribuye por museo. citeturn4search3turn1search0  

3) **Modelo de consumo de voz e IA por visitante**: promedio de consultas STT por visita, longitud de respuesta TTS, tokens promedio por interacción, y política de “bolsa incluida” vs cobro por sobreuso. Los precios oficiales permiten modelarlo, pero falta el volumen esperado. citeturn4search0turn4search1turn4search3  

4) **Estrategia de contenidos para RAG**: volumen de objetos por museo, disponibilidad de fichas curatoriales, esfuerzo de digitalización/limpieza/etiquetado y responsable institucional. La sostenibilidad del sistema depende de este insumo. citeturn9search9turn9search6  

5) **Lista de museos “alta o media afluencia” dentro de los 56** (criterio de corte y ranking por visitas, idealmente con datos oficiales por museo). El portal estadístico del Ministerio sugiere que existe registro detallado; incorporarlo fortalecería Nᵧ y L en el modelo. citeturn5search2turn5search24  

6) **Estrategia de contratación y financiamiento**: si el comprador será cada museo, una unidad ejecutora central o programas específicos de digitalización; esto afecta tanto el ritmo de adopción como el diseño contractual (implementación + mantenimiento). citeturn3search2turn9search6  

7) **Evidencia local de disposición a pagar (WTP) institucional**: entrevistas, cartas de intención, benchmarking de contratos nacionales similares (SEACE) para servicios de soporte/renovación anual y para proyectos de digitalización en cultura; esto fortalecería la defensa de P_sub y P_impl con datos del entorno peruano. citeturn3search2turn3search9turn3search15
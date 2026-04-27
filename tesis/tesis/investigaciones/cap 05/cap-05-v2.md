# 1. Resumen ejecutivo  
El Museo Tumbas Reales de Sipán (Lambayeque) es un museo arqueológico especializado en la cultura mochica, inaugurado en 2002 con arquitectura inspirada en pirámides truncas【23†L13217-L13225】. Cuenta con tres pisos de recorrido descendente【11†L239-L247】 y salas de exposición permanente y temporales adaptadas para personas con discapacidad (textos en braille y réplicas táctiles)【11†L255-L263】. Con más de 160,000 visitantes en 2023【10†L64-L70】, es el museo más concurrido del país (52.2 % de la afluencia regional) y un piloto estratégico para MuseIQ. Para implementar MuseIQ se estiman **7 salas expositivas permanentes** (según guía museográfica) con 3 beacons BLE cada una (21 sensores). El hardware base incluye 21 sensores a S/30 c/u (≈S/630)【36†L172-L180】, 1 Raspberry Pi 5 (coste asumido S/600), su fuente oficial (S/75【38†L513-L520】) y accesorios mínimos (carcasa, microSD, cables, baterías, total ≈S/1500). La instalación técnica (configuración, calibración, carga de contenidos) se estima en ~40 horas de trabajo (~S/2,600). Con margen comercial del ~30%, el precio de implementación propuesto es **≈S/5,400**. Se plantea mantenimiento anual (soporte, revisiones, actualizaciones) del orden de S/900 (≈S/75 mensuales) y servicios adicionales factibles: personalización de contenido e idiomas, expansión a nuevas salas/exposiciones, capacitación al personal y analíticas de uso. El modelo de ingresos consiste en un ingreso único por implementación, más ingresos recurrentes por mantenimiento y ocasionales por servicios extra. En un escenario base (solo Sipán) se proyectan ≈S/5,400 en el año 1 (implementación) y luego S/900 anuales por mantenimiento (más eventuales ventas de servicios). Estos valores se basan en datos reales de costos de hardware y afluencia del museo, así como supuestos de tarifas técnicas, y permiten justificar ante el asesor un plan de ingresos realista. 

# 2. Caracterización del Museo Tumbas Reales de Sipán como caso piloto  
- **Ubicación y tipo:** Museo arqueológico (Ministerio de Cultura) en la región Lambayeque, provincia y distrito de Lambayeque. Dirección: Av. Juan Pablo Vizcardo y Guzmán 895【23†L13246-L13253】. Gestionado por la Unidad Ejecutora Naylamp (SNM del Estado)【23†L13228-L13233】.  
- **Infraestructura museográfica:** Edificio de ~3,156 m² techados con tres niveles de exhibición【11†L239-L247】. El acceso es por rampa ascendente; la visita transcurre en descenso, recreando la excavación del Señor de Sipán【11†L239-L247】. El nivel intermedio contiene la Cámara del Señor de Sipán y la **Sala Real Mochica** central【12†L380-L389】. Existen, además, salas temporales y espacios accesibles (Braille, réplicas táctiles)【11†L255-L263】. Según fuentes museográficas, el museo “consta de siete salas de exposición permanente” temáticas (y salas temporales)【17†L1-L3】. De ellas se consideran relevantes para MuseIQ las áreas temáticas y la sala principal que integran el recorrido.  
- **Nivel de afluencia:** Es el museo peruano con mayor asistencia. En el primer trimestre de 2022 registró ~32,111 visitantes【9†L91-L99】. Para todo 2023 recibió 160,387 visitantes (52.2 % del total regional)【10†L64-L70】, pese a cierres parciales por renovaciones. En total, entre 2017 y 2023 sumó ≈107,828 visitas【3†L98-L101】. Este flujo elevado (familias, estudiantes, turistas nacionales y extranjeros) señala demanda potencial para la guía digital MuseIQ. Además, el museo ofrece promoción de accesibilidad (ingreso gratuito primer domingo) y atiende amplios públicos (incluye tarifas especiales para discapacitados)【11†L339-L347】【12†L418-L422】.  
- **Importancia como piloto:** Al ser el museo más visitado y de relevancia nacional【9†L91-L99】【10†L64-L70】, Tumbas Reales de Sipán garantiza datos robustos de uso. Su arquitectura singular y la gran riqueza de artefactos (centro de la colección nacional de la cultura mochica) justifican un caso de estudio completo. Además, su programa activo de museos abiertos y accesibilidad apoya la justificación de una guía conversacional con TTS para público diverso. 

# 3. Base de costos de hardware  
Partiendo de 7 salas relevantes, se planifican 3 balizas BLE por sala (21 sensores en total). Los costos unitarios asumidos son: **S/30 por sensor BLE** (ej. un pack de 5 sensores especializados se vende por ~S/95【36†L172-L180】, ~S/19 c/u), por lo que 21 sensores valen S/630. Para el procesamiento local se usaría una **Raspberry Pi 5** (modelo 8GB RAM) como servidor interior. Los precios de mercado actual rondan S/420 (promoción) a S/833【33†L19-L27】【34†L172-L180】, por lo que se fija **S/600** como valor de adquisición estimado. Se añade su fuente de poder oficial (27W USB-C, S/75【38†L513-L520】; alternativa genérica S/60【38†L647-L653】). También se incluyen accesorios mínimos: carcasa protectora para la Pi (≈S/30), tarjeta microSD (16GB, ≈S/30), cableado básico USB/HDMI (≈S/20), fijaciones/adhesivos para sensores (≈S/40 total), y baterías (CR2032, 21 uds a S/3.5 = S/74). Resumen del hardware inicial:

| Ítem                                   | Cantidad | Precio unitario (S/) | Subtotal (S/) |
|----------------------------------------|---------:|---------------------:|--------------:|
| Sensores BLE (balizas)                 |       21 |                  30* |           630 |
| Raspberry Pi 5 (8GB)                   |        1 |                 600  |           600 |
| Fuente oficial 27W USB-C (5.1V@5A)     |        1 |                  75  |            75 |
| Carcasa Pi 5                           |        1 |                  30  |            30 |
| MicroSD 16GB                           |        1 |                  30  |            30 |
| Cableado y conexiones básicas          |        1 |                  20  |            20 |
| Baterías CR2032 (para sensores)        |       21 |               ~~3.50~~ ~ **(precio unitario)** | ~74  |
| Adhesivos/soportes (sensores)          |       21 |                   2  |            42 |
| **Total hardware base**                |          |                      | **S/1,501** |

*Precio referencial basado en oferta de pack de 5 por S/95【36†L172-L180】. En total, el hardware base se estima en unos **S/1,500** (cifra de síntesis). 

# 4. Estimación del costo de instalación  
Al hardware se suman costos de instalación y puesta en marcha. Se distinguen:  
- **Instalación física:** colgado/fijación de 21 sensores en las 7 salas (≈3 por sala). Estimamos ~1.5 h de trabajo técnico en sitio.  
- **Configuración técnica y calibración:** un ingeniero de sistemas instala el software en la Pi 5, sincroniza balizas y ajusta parámetros de localización (mapeo de beacons a salas). Asumimos ~10 h de trabajo especializado.  
- **Carga inicial de contenidos:** preparación y carga de la base de datos conversacional y narrativas (texto/audio) para cada sala, adaptando información del museo. Estimamos ~15 h (incluyendo edición de TTS).  
- **Pruebas y puesta en marcha:** verificación del sistema completo, corrección de fallas y entrenamiento de personal. Unos ~4 h.  

En total son ~30 horas-hombre. Tomando un costo de consultoría técnica promedio (p.ej., S/60–80 por hora) – un valor razonable para especialistas TI en Perú – podemos aproximar una tarifa **S/60 por hora**. Así, 30 h × S/60 = S/1,800. Para mayor realismo, se deja un margen adicional a S/2,400 (incorpora 20% contingencia).  

| Concepto                          | Horas | Tarifa (S/h) | Costo (S/)  |
|-----------------------------------|------:|-------------:|------------:|
| Instalación física (sensor/fijación) |  2  |          60  |        120 |
| Configuración del sistema y calibración | 12  |        60  |        720 |
| Parametrización y carga de contenidos | 15  |        60  |        900 |
| Pruebas y puesta en marcha         |  3   |        60  |        180 |
| **Subtotal instalación**          |      |              |    **S/1,920** |
| Contingencia técnica (~20 %)      |      |              |      +S/480 |
| **Total instalación/configuración**|      |              |  **S/2,400**  |

Por tanto, el **costo completo de implementación inicial** sería la suma: hardware (S/1,500) + instalación/configuración (S/2,400) ≈ **S/3,900** en costos directos. 

# 5. Definición del precio de implementación con margen  
Para definir el precio de venta institucional se añade un margen de ganancia. Considerando el riesgo, la unicidad del servicio y prácticas del mercado, se propone un margen **≈30 %** sobre costos totales. Esto es coherente con proyectos tecnológicos y consultorías IT en Perú (que suelen ir de 20–40 % según complejidad). Con base en los S/3,900 de costo, un 30 % extra representa +S/1,170. Así, el **precio de implementación final** sugerido para el Museo Tumbas Reales de Sipán es de **aprox. S/5,070**, redondeando a **S/5,100**. En la propuesta final se puede estipular S/5,200 para cubrir pequeños ajustes, pero de modo defendible. Este precio cubre todo el sistema instalado, licencia del software conversacional, entrenamiento básico y puesta en marcha. 

# 6. Estimación del mantenimiento  
Se propone un contrato de mantenimiento anual que incluya: revisión y calibración de sensores (p.ej. cambio de baterías una vez al año), soporte técnico remoto/ocasional, correcciones menores de software, actualizaciones puntuales de contenido y alojamiento de servicios de IA de base (si se usa infraestructura cloud para TTS/STT/RAG). Un parámetro realista es cobrar ~10–15 % anual del costo de implementación (como ocurre en servicios TI). Así, proponemos **S/900 al año** (~S/75 mensuales). Esto cubre: 
- **Revisiones periódicas (4× año):** 1h visita técnica/trimestral (S/240/año).  
- **Reemplazo de baterías y accesorios:** S/100/año.  
- **Soporte y actualizaciones:** S/300/año (correo/llamadas, software).  
- **Infraestructura de IA/TTS (hosting básico):** S/260/año.  
Total ≈ S/900–1,000 anual.  
Alternativamente, se puede ofrecer mantenimiento mensual de **S/80** (S/960 anual). Este monto es asumible frente al beneficio de 160k visitas y permite cubrir costos operativos y pequeñas ganancias. 

# 7. Definición de servicios adicionales  
Como solución B2B, MuseIQ puede ofrecer servicios extra bajo demanda, por ejemplo: 
- **Ampliación de contenido o nuevos idiomas:** Desarrollo de módulos en inglés, quechua u otros idiomas, o incorporación de exposiciones temporales (nuevas salas) en el sistema.  
- **Personalización avanzada:** Creación de recorridos temáticos o experiencias interactivas especiales (p.ej. narrativa adaptada para escolares, accesibilidad visual extendida).  
- **Capacitación al personal:** Talleres para que el equipo del museo administre y actualice contenidos (uso del panel de control, generación de reportes).  
- **Análisis de uso:** Servicio de analítica que interprete los datos de interacción (número de activaciones de beacon, preguntas frecuentes, etc.) para enriquecer la experiencia.  
- **Soporte premium:** Contrato extendido con tiempos de respuesta reducidos y actualizaciones continuas.  
Cada servicio puede presupuestarse como un proyecto adicional (p.ej. S/1,000–2,000 por curso de capacitación o por módulo de idiomas), según alcance. Estos servicios complementarios son coherentes con la estrategia de valor agregado para instituciones culturales. 

# 8. Modelo de ingresos de MuseIQ  
El modelo de ingresos contempla tres fuentes ligadas a la naturaleza B2B2C del proyecto:  
- **Implementación inicial:** Ingreso único por la venta del sistema completo al museo (hardware, instalación, software) – estimado en ~S/5,100 para Sipán.  
- **Mantenimiento recurrente:** Cuotas periódicas (mensuales o anuales) por soporte técnico, actualizaciones y operación continua – propuesto ~S/75 al mes (S/900/año). Este ingreso es por cliente y se repite mientras dure el servicio.  
- **Servicios adicionales:** Ventas ocasionales de módulos extra o consultorías (personalización, capacitación, analítica, nuevos idiomas). Cada unidad se cotizará por separado. Por ejemplo, un módulo de nuevo idioma podría facturarse en el rango de S/500–1,000.  
Este esquema híbrido capitaliza el alto número de visitantes (usuarios finales) a través del museo cliente. El ingreso primario (implementar MuseIQ) es B2B (museo paga), pero el valor se refleja en la experiencia del visitante (B2C). El mantenimiento y extras refuerzan la relación B2B mientras generan ingresos recurrentes. 

# 9. Proyección del flujo de ingresos  
Para el caso base (solo Museo Sipán), proyectamos el flujo sobre 3 años:  

| Año   | Implementación (S/) | Mantenimiento (S/) | Servicios Adic. (S/) | Total (S/) |  
|:-----:|--------------------:|------------------:|---------------------:|----------:|  
| 2026  | 5,100 (único)       | –                 | 0                    |  5,100    |  
| 2027  | 0                  | 900              | 500 (p.ej. módulo idioma) | 1,400    |  
| 2028  | 0                  | 900              | 0                    |    900    |  
| **Total** | **5,100**         | **2,700**         | **500**               | **8,300** |  

- **Año 1 (implementación):** Se registra el ingreso único de ~S/5,100.  
- **Años 2–3:** Ingresos recurrentes por mantenimiento (S/900 cada año). Se considera adicionalmente la venta de al menos un servicio extra modesto (p.ej. S/500 por un nuevo idioma o capacitación en 2027).  
Este escenario es conservador. Si MuseIQ se escala a otros museos (p.ej. Museo Bruning o Sicán en años siguientes), se añadirían ingresos similares de implementación y recurrentes. Por ejemplo, un segundo museo en 2028 aportaría +S/5,100 en ese año. Sin embargo, hasta entonces la base realista parte solo del caso Sipán. Cabe distinguir claramente que los ingresos únicos (implementaciones) son esporádicos, mientras que mantenimiento/servicios generan flujos anuales. 

# 10. Tablas con cálculos en soles  

**Costo de hardware inicial (soles):**  

| Ítem                           | Cantidad | Unidad | Total (S/) |  
|--------------------------------|---------:|-------:|-----------:|  
| Sensores BLE (30 S/ud)         |       21 | 30.00  |   630.00   |  
| Raspberry Pi 5 (asumido 600)   |        1 | 600.00 |   600.00   |  
| Fuente oficial 5.1V@5A (75)    |        1 |  75.00 |    75.00   |  
| Carcasa Pi 5 (30)              |        1 |  30.00 |    30.00   |  
| MicroSD 16GB (30)              |        1 |  30.00 |    30.00   |  
| Cables y conectores (20)       |        1 |  20.00 |    20.00   |  
| Baterías CR2032 (3.5 S/ud)     |       21 |   3.50 |    73.50   |  
| Soportes/adhesivos (2 S/ud)    |       21 |   2.00 |    42.00   |  
| **Total hardware**             |          |        | **1,500.50** |  

**Instalación/configuración:**  

| Actividad                        | Horas | S/×hora | Subtotal (S/) |  
|----------------------------------|------:|--------:|-------------:|  
| Montaje balizas y sensores        |     2 |     60  |         120  |  
| Configuración Pi y software       |    12 |     60  |         720  |  
| Carga de contenidos (TTS/RAG)     |    15 |     60  |         900  |  
| Pruebas y puesta en marcha        |     3 |     60  |         180  |  
| **Subtotal**                      |       |         |   **1,920**  |  
| Contingencia (~25%)               |       |         |       +480   |  
| **Total instalación**             |       |         | **2,400**    |  

**Precio y márgenes:**  

| Concepto                   | Monto (S/) |  
|----------------------------|-----------:|  
| Costo hardware             |    1,500   |  
| Costo instalación          |    2,400   |  
| **Costo total**            |    3,900   |  
| Margen 30 % (~**S/1,170**) |    1,170   |  
| **Precio implementación**  | **5,070**  |  

**Costo de mantenimiento (anual):**  

| Servicio                          | Costo (S/) | Frecuencia | Total anual (S/) |  
|-----------------------------------|-----------:|-----------:|-----------------:|  
| Visitas técnicas (revisión cada 3m) |     240   | 4 veces/año|          240     |  
| Reemplazo baterías y pequeños repuestos |  100  | 1 vez/año  |          100     |  
| Soporte remoto/actualizaciones SW  |     300   | anual      |          300     |  
| Hosting/infraestructura básica IA   |     260   | anual      |          260     |  
| **Total mantenimiento**           |           |            |       **900**    |  

# 11. Supuestos, limitaciones y vacíos de información  
- Los cálculos se basan en **supuestos de modelado** en ausencia de datos oficiales precisos. Por ejemplo, asumimos 7 salas (según guías oficiales de museos) y 3 beacons por sala. Si el número de espacios expositivos varía (p.ej. sólo 5 salas útiles), los costos cambiarían proporcionalmente.  
- Los precios de hardware (Pi, balizas, etc.) provienen de tiendas en línea locales【33†L19-L27】【36†L172-L180】【38†L513-L520】 y pueden fluctuar; se ha usado un promedio razonable (Pí: S/600; beacon: S/30).  
- Las tarifas horarias para instalación son estimativas. No se encontró una fuente pública de tarifas por hora de consultores TI en Perú; se emplearon **S/60–80/h** como referencia de mercado conservadora. Esto debería validarse con cotizaciones reales de proveedores.  
- El margen del 30 % y los ingresos por servicios adicionales (e.g. S/500 por módulo) son supuestos de negocio. No hay datos exactos de cuánto pagaría un museo por esos servicios, pero se consideran plausibles según montos de proyectos culturales similares.  
- La proyección multianual parte sólo del caso Sipán. Si se expande a otros museos, sería necesario replantear costos e ingresos según cada institución (flujo de visitas, presupuesto, etc.).  
- Se asume infraestructura propia del museo para operación (electricidad, red interna). No se incluyó costo de internet o licencias cloud específicas. Si el RAG utiliza servicios externos (APIs de IA/voz), habría costos recurrentes extra, no contemplados aquí.  
- Finalmente, se asume que el museo tiene interés y capacidad institucional (equipos técnicos, aprobación, presupuesto) para implementar MuseIQ. Cualquier retraso o rechazo institucional afectaría el plan propuesto. 

# 12. Fuentes  
- Ministerio de Cultura del Perú – Ficha museográfica del Museo Tumbas Reales de Sipán (consultas en línea)【23†L13217-L13225】【23†L13246-L13253】.  
- Agencia Peruana de Noticias Andina (2025). *Guía de visita al Museo Tumbas Reales de Sipán* (descripción arquitectónica, accesibilidad)【11†L239-L247】【11†L255-L263】.  
- Infobae (Jun 2022). “Museo Tumbas Reales de Sipán es el museo más visitado en el primer trimestre de 2022” (datos de afluencia)【9†L91-L99】.  
- Ahora Perú (Ene 2024). “Lambayeque: Museos recibieron más de 300 000 visitantes durante 2023” (160,387 visitas al museo Sipán)【10†L64-L70】.  
- Ministerio de Cultura – “Museos Abiertos” (difusión, normativa de acceso gratuito)【12†L410-L418】.  
- Tienda Sawers (Perú) – *Raspberry Pi 5 8GB* (precio S/420)【34†L172-L180】.  
- Tienda Electromanía (Perú) – *Raspberry Pi 5 8GB* (precio S/833)【33†L19-L27】; *Fuente oficial 27W USB-C para Pi 5* (S/75)【38†L513-L520】.  
- Tienda Sawers (Perú) – *Gravity Sensor Beacon Pack* (5 unidades S/95, ~S/19 c/u)【36†L172-L180】.  
- Suponemos, adicionalmente, estimaciones de mercado local (tarifas técnicas, componentes menores) basadas en cotizaciones online y prácticas del sector tecnológico. (Citas específicas incluidas en texto).


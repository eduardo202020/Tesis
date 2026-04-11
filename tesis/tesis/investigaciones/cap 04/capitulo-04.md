# Capítulo 4: Oferta Tecnológica Mundial

## Introducción del capítulo

En el contexto de esta tesis, la **oferta tecnológica mundial** se entiende como el conjunto de **productos comerciales, plataformas institucionales, estándares técnicos y prototipos académicos** que hoy permiten —en museos y espacios culturales— algún grado de **mediación digital in situ**: entrega de contenidos interpretativos durante la visita, orientación/wayfinding, accesibilidad multimodal, analítica de recorridos y, más recientemente, asistentes conversacionales basados en IA. Esta oferta es heterogénea porque combina modelos históricos (audioguías dedicadas) con enfoques actuales BYOD (Bring Your Own Device), localización indoor y herramientas de IA generativa, en distintos niveles de madurez y adopción. citeturn2search7turn2search33

Este análisis es importante para justificar el posicionamiento de MuseIQ por tres razones. Primero, porque permite **evitar “falsos vacíos” de innovación**: muchas funciones (audioguía, mapas, CMS de contenidos) existen desde hace años; la pregunta académica relevante es **qué combinaciones están efectivamente disponibles y desplegadas**, y con qué trade-offs técnicos y de adopción. citeturn2search7turn5view2 Segundo, porque ayuda a caracterizar la **brecha entre prototipos y mercado**: la literatura reporta soluciones avanzadas, pero su transferencia a operaciones museales reales suele enfrentar costos de infraestructura, mantenimiento, gobernanza de contenidos y sostenibilidad institucional. citeturn2search33turn2search3 Tercero, porque el mercado objetivo priorizado en tu tesis (museos públicos peruanos de alta o media afluencia) se desenvuelve en condiciones de adopción donde la **fricción de acceso**, la **conectividad** y la **capacidad operativa** de los museos importan tanto como la sofisticación técnica; por ello, entender la oferta mundial permite identificar qué enfoques son “transportables” al contexto peruano y cuáles no. citeturn4search0turn4search1turn3search8

Documento base proporcionado (contexto de tu tesis): [tesis(3).pdf](sandbox:/mnt/data/tesis(3).pdf)

## Criterios de comparación

Para comparar soluciones comparables a MuseIQ con rigor (sin sesgo promocional), se emplean criterios orientados a **arquitectura**, **experiencia de visita** y **adopción institucional**. Los criterios están diseñados para distinguir entre “tener contenido digital” y “resolver mediación contextual en visita presencial”, que es el núcleo de MuseIQ.

**Criterios funcionales y de interacción**
- **Tipo de mediación**: audioguía lineal (selección por número/lista) vs. mediación contextual (por sala/obra) vs. diálogo (Q&A).
- **Modo de interacción**: pantalla/tap, audio, voz (TTS/STT), multimodal; presencia de interacción hands-free para accesibilidad.
- **Accesibilidad**: soporte explícito a audiodescripción, lenguaje sencillo, lengua de señas, compatibilidad con lectores de pantalla y principios WCAG (cuando aplica). citeturn8search2turn14search0turn7search3

**Criterios técnicos**
- **Localización indoor / disparo contextual**: presencia/ausencia; granularidad (sala, punto de interés, sub-metro) y tecnología (BLE/iBeacon/Eddystone, QR/NFC, Wi‑Fi RTT, UWB, visión, sensor-fusión). citeturn10search0turn16search3turn9view1
- **Infraestructura requerida**: sin infraestructura (QR), infraestructura ligera (BLE beacons), infraestructura media/alta (UWB anchors, calibración intensiva, mapas indoor detallados y mantenimiento), o dependencia de hardware propietario. citeturn10search0turn16search0
- **Arquitectura de IA**: inexistente; personalización basada en reglas/analítica; LLM; y (cuando existe evidencia) **RAG o variantes** para anclar respuestas en fuentes verificables y reducir alucinaciones. citeturn7search0turn7search26turn7search18
- **Gestión de contenidos (CMS) y ciclo editorial**: quién produce/actualiza contenidos, con qué herramientas y qué tan viable es mantenerlo con equipos pequeños. citeturn1search9turn1search31

**Criterios de despliegue y adopción**
- **Modelo de despliegue**: BYOD (app nativa o PWA/web) vs. préstamo de dispositivos; online/offline.
- **Costos y modelo económico**: precios publicados (si existen) o clasificación por complejidad (baja/media/alta) cuando el mercado oculta tarifas. citeturn1search0turn5view3turn15search1
- **Grado de adopción real**: plataforma multisede (alto despliegue), producto comercial (despliegue variable), piloto académico (limitado), o prototipo experimental. citeturn0search11turn0search6turn9view2
- **Riesgos operativos**: batería y mantenimiento de beacons, estabilidad de RSSI, privacidad (tracking), requisitos de señalética (QR) y dependencia de conectividad local. citeturn16search13turn10search0turn1search32

## Clasificación de la oferta tecnológica mundial

La oferta comparable puede organizarse en categorías que reflejan **cómo se “engancha” el contenido a la experiencia presencial** y qué tan automatizada/contextual es la mediación.

### Audioguías dedicadas y sistemas “clásicos” de interpretación

**Qué resuelven.** Proveen narración interpretativa para recorridos (generalmente por selección de número/estación), con alta confiabilidad operativa y control museográfico.

**Cómo funcionan.** Históricamente se basan en **dispositivos del museo** (handheld con teclado, o reproductores multimedia), que descargan/contienen contenido, a veces con sincronización con pantallas o rutas definidas. Estos sistemas siguen vigentes en museos con gran volumen de visitantes o donde se prefiere controlar hardware/software por razones de soporte, ingresos por alquiler y experiencia uniforme. citeturn13search5turn1search7turn13search28

**Ventajas.** Alta estabilidad, contenido offline garantizado, soporte multi-idioma, control de la experiencia.

**Limitaciones.** Costos de adquisición, logística (carga, higiene, pérdidas), escalabilidad por inventario, y menor flexibilidad para personalización fina o diálogo contextual. citeturn5view2turn13search5turn13search28

### Apps móviles de mediación cultural y guías digitales BYOD

**Qué resuelven.** Trasladan el guía al smartphone: mapas, listas de obras, audio, multimedia, a veces analítica y notificaciones.

**Cómo funcionan.** Se despliegan como **apps nativas** (App Store/Google Play) o como **web apps/PWA**. En la práctica, muchas instituciones enfrentan el problema de “fricción de descarga”: el visitante llega, escanea información, pero evita instalar apps específicas para un único museo, lo que ha motivado enfoques PWA o acceso web inmediato. citeturn5view2turn1search31turn3search8

**Ventajas.** BYOD reduce costos de hardware; actualización de contenidos más ágil; potencial de continuidad post-visita.

**Limitaciones.** Adopción real puede ser baja si requiere descarga; dependencia de señal (si no hay offline); mantenimiento editorial y de UX. citeturn3search8turn1search32

### Soluciones “sin app” basadas en QR/PWA y disparo manual

**Qué resuelven.** Reducen al mínimo la fricción: el visitante escanea un QR y accede a contenido web (audioguía/multimedia), con o sin monetización.

**Cómo funcionan.** QR por sala/obra o QR general que abre un recorrido; la “localización” es en gran parte **manual** (el usuario elige) o basada en señalética.

**Ventajas.** Infraestructura mínima; costos relativamente bajos; despliegue rápido; útil para museos con limitaciones presupuestales.

**Limitaciones.** Menor automatización contextual; experiencia depende de señalización; navegación indoor es limitada si no se combina con mapas o sensores. citeturn13search2turn1search17turn1search32

### Sistemas con BLE beacons y mediación por proximidad (room‑level / POI)

**Qué resuelven.** Automatizan parte de la mediación: identificar cercanía a una sala/obra para disparar contenido sin que el usuario busque.

**Cómo funcionan.** Se instalan beacons BLE (frecuentemente iBeacon/Eddystone) que transmiten identificadores; el móvil escanea, estima proximidad por RSSI y dispara contenido según reglas. En iBeacon, la identificación se estructura con UUID y valores major/minor programables. citeturn12search0turn9view1turn0search20

**Ventajas.** Infraestructura ligera comparada con RTLS de alta precisión; adecuada para “reconocimiento de sala” (el enfoque de MuseIQ). La literatura muestra que BLE puede ser efectiva para experiencias de museo “context‑aware”, aunque la precisión absoluta puede variar por multipath y condiciones físicas. citeturn0search20turn9view1turn10search0

**Limitaciones.** Variabilidad del RSSI; calibración/ajustes; mantenimiento de baterías si los beacons no son alimentados; y consideraciones de privacidad si se registra analítica individual. citeturn10search0turn16search13

### Plataformas de indoor navigation/wayfinding y RTLS

**Qué resuelven.** No solo “qué contenido mostrar”, sino **cómo guiar físicamente** al visitante: rutas, accesibilidad espacial, reducción de congestión y analítica de flujos.

**Cómo funcionan.** Integran mapas indoor, motor de rutas y posicionamiento mediante BLE, Wi‑Fi, UWB o fusión con IMU (sensores inerciales). Las revisiones recientes señalan que Wi‑Fi, BLE, UWB e IMU se combinan en distintos esquemas para balancear precisión, costo y robustez. citeturn10search0turn16search3turn16search0

**Ventajas.** Mayor valor operacional (gestión de flujos, accesibilidad, seguridad); habilita experiencias avanzadas (misiones, rutas personalizadas).

**Limitaciones.** Mayor costo/implementación; necesidad de mapas precisos y mantenimiento; UWB tiende a asociarse a alta precisión y más infraestructura (anchors/tags), aunque con beneficios en exactitud. citeturn16search0turn16search3turn10search0

### Asistentes conversacionales y personalización con IA en contextos culturales

**Qué resuelven.** Permiten Q&A “tipo guía humano”, personalización de recorridos y acceso natural a conocimiento patrimonial.

**Cómo funcionan.** Incluyen desde chatbots con bases estructuradas (RDF/temas) hasta asistentes con IA generativa. En el estado del arte, se observa un giro hacia IA generativa para interacción; sin embargo, la discusión académica advierte riesgos de **autenticidad, exactitud y alucinaciones**, por lo que enfoques de anclaje (p. ej., RAG) son relevantes cuando el dominio exige trazabilidad. citeturn6search0turn2search1turn7search0turn7search26

**Ventajas.** Interacción natural; potencial de accesibilidad (voz) y de exploración profunda (lo que el visitante pregunta, no solo lo que se lista).

**Limitaciones.** Gobernanza del conocimiento (qué fuentes, qué versión), evaluación de seguridad/errores, costos de operación (cómputo), y necesidad de políticas institucionales para uso responsable de IA en cultura. citeturn2search31turn7search18turn2search1

## Identificación de soluciones o referentes concretos

A continuación se presenta un conjunto de referentes relevantes, distinguiendo **oferta comercial real**, **plataformas ampliamente desplegadas**, y **prototipos/pilotos académicos** comparables en algún componente clave de MuseIQ (localización BLE, voz, IA contextual).

### Plataformas institucionales de gran despliegue

**entity["organization","Bloomberg Connects","arts guide app"] (global).**  
Finalidad: guías digitales gratuitas para museos y espacios culturales, con mapas y contenidos multimedia. Evidencia pública: el catálogo oficial declara “guías interactivas” para **más de 1000** instituciones dentro de una sola app. citeturn0search11turn0search27  
Tecnologías: app móvil centralizada; el posicionamiento indoor con BLE no es presentado como núcleo del producto en la evidencia pública revisada (predominan mapas/lookup numbers y contenido curado). citeturn0search27turn0search11  
Fortalezas: enorme escala de adopción institucional; estandarización de experiencia; bajo costo directo para el visitante (app gratuita). Limitaciones: no es una arquitectura explícitamente centrada en “reconocimiento por sala con BLE + voz + RAG”; la personalización contextual depende del diseño de contenido y navegación interna, no de sensórica in situ en su forma base. citeturn0search11turn0search27  
Relación con MuseIQ: referente de **adopción masiva y UX de guía**, útil para comparar estrategia de acceso, onboarding y patrón de contenidos.

### Oferta comercial real: guías digitales, CMS y modelos BYOD

**entity["company","Smartify","arts and culture app uk"] (Reino Unido, plataforma global).**  
Finalidad: plataforma para que instituciones publiquen tours/objetos y ofrezcan guías web/móviles. Evidencia pública: página de productos describe soporte de BYOD y dispositivos, incluyendo **PWAs “sin descarga”**; y su página de precios publica planes anuales con capacidades como “AI translations” y “AI personalised tours” en niveles superiores. citeturn1search31turn1search0  
Tecnologías: CMS + web/PWA + apps; IA aplicada a traducción y personalización (según planes). Fortalezas: transparencia relativa de precios, enfoque operativo (CMS), estrategia PWA alineada con fricción baja. Limitaciones: la documentación pública no describe como núcleo un esquema BLE con beacons propios del museo tipo ESP32; la IA es una capa de plataforma, no necesariamente un asistente RAG con fuentes curatoriales locales. citeturn1search0turn1search31  
Relación con MuseIQ: buen comparable en **modelo BYOD (incl. PWA)** y “funciones IA” como componente de plataforma.

**entity["company","SmartGuide","digital guide platform"] (plataforma para museos/atracciones).**  
Finalidad: audioguía digital con módulos de analítica y funciones de IA. Evidencia pública: su página para museos publica precios mensuales por tamaño, y lista funciones como “AI tour planner” y “AI Guide chat linked to vetted content” en planes avanzados. citeturn5view3  
Tecnologías: app + CMS + analítica; IA para planificación y chat (según su descripción). Fortalezas: explícita incorporación de “AI Guide chat” (cercano al objetivo conversacional). Limitaciones: la evidencia pública revisada no confirma BLE/ESP32 como base; su orientación es de producto SaaS, no de arquitectura abierta basada en hardware propio del museo. citeturn5view3  
Relación con MuseIQ: comparable por **chat/IA** y por su enfoque en “contenido curado”, aunque sin el énfasis técnico de RAG y sensórica descrito en MuseIQ.

**entity["company","izi.TRAVEL","audio tour platform"] (plataforma global).**  
Finalidad: creación y distribución de audioguías y tours; en museos, el acceso puede hacerse por QR (“scan QR code of the object”). La empresa también ofrece documentación de producción de audioguías indoor usando CMS. citeturn1search17turn1search9turn1search5  
Tecnologías: app móvil, CMS, disparo por GPS (outdoor) y QR en museo (según su descripción). Fortalezas: barrera baja para producción; modelo extendido global; buen referente para “estructura de museo/objetos” y flujos editoriales. Limitaciones: no es un sistema centrado en BLE; su disparo contextual en museo depende más de QR/selección manual. citeturn1search17turn1search9  
Relación con MuseIQ: comparable como **audioguía BYOD low‑cost**; menos comparable en localización BLE y voz interactiva.

**entity["company","Nubart","audio guide pwa spain"] (España; enfoque PWA/QR).**  
Finalidad: audioguías accesibles vía **PWA** mediante QR, con promesa de “nada que descargar”. Evidencia pública: su página describe explícitamente acceso por QR a una PWA. citeturn13search2  
Referencia económica/operativa: publica un análisis propio de adopción de apps nativas de audioguía (2.47% promedio en su muestra) y lo discute en un foro profesional (AAM Community), útil como **insumo de mercado** pero con origen empresariales (debe tratarse como evidencia industrial, no como hallazgo académico indexado). citeturn13search14turn3search8  
Relación con MuseIQ: comparable por su tesis de “acceso ligero” y por explorar la barrera de adopción; no aborda el mismo stack (BLE+sensores+voz+RAG) como arquitectura integrada.

**entity["company","Hearonymus","audio guide platform vienna"] (Austria).**  
Finalidad: plataforma de audioguías para smartphones; la evidencia pública indica que se pueden activar capítulos mediante **QR, NFC o GPS** y que ofrece opciones de accesibilidad (p. ej. descripciones para discapacidad visual, lengua de señas, lenguaje fácil). citeturn14search0turn14search3  
Referencia económica puntual: un caso público (institución patrimonial) muestra una audioguía a €3.99 como ejemplo de monetización por guía, aunque no equivale a estructura de costos B2B completa. citeturn14search17turn14search0  
Relación con MuseIQ: comparable en **audio y accesibilidad**, menos comparable en indoor‑BLE y conversación RAG.

**entity["company","Locatify","location-based app platform iceland"] (Islandia).**  
Finalidad: plataforma de apps/location‑based content; ofrece proyectos indoor con **BLE beacons** y también menciona UWB en su oferta; publica planes de precios (p. ej., “Audio Guides” desde €79/mes en su página de pricing). citeturn15search1turn15search5turn15search0  
Tecnologías: CMS + app; BLE beacons y/o UWB (según su material público). Fortalezas: combina gamificación, mapas y disparo por localización; tiene documentación técnica e incluso materiales tipo whitepaper sobre “automatic museum guide” con beacons. citeturn15search22turn15search6  
Limitaciones: su enfoque comercial no está centrado en voz interactiva; la IA conversacional contextual no es el eje principal en la evidencia revisada. citeturn15search5turn15search1  
Relación con MuseIQ: comparable por **BLE/proximidad + UX de guía + CMS**, y porque muestra el “estado de mercado” de beacons en museos.

**entity["company","Navigine","indoor navigation platform"] (plataforma global de indoor navigation).**  
Finalidad: SDK y plataforma de posicionamiento indoor/wayfinding; tiene una vertical explícita para museos y propone integración en apps existentes, con capacidades de navegación indoor. citeturn14search5turn14search2  
Tecnologías: enfoque multi‑tecnología (BLE/Wi‑Fi/UWB en su narrativa corporativa) y despliegue con beacons en casos museales. citeturn14search10turn14search22  
Fortalezas: orientado a wayfinding (más allá de audioguía); útil para comparar contra MuseIQ en “orientación indoor”. Limitaciones: mayor complejidad (mapas indoor + calibración + plataforma), potencialmente más costosa que un esquema “room‑level BLE” con beacons simples; no es un producto centrado en voz+RAG como core. citeturn14search4turn10search0  
Relación con MuseIQ: comparable en la dimensión “orientación indoor”; prueba que el mercado ofrece soluciones avanzadas, con costo operativo asociado.

**entity["company","Orpheo","visitor solutions company france"] / entity["company","Acoustiguide","audio guide company"] (ecosistema hardware+software).**  
Finalidad: soluciones integrales (dispositivos, apps, producción multimedia). Evidencia pública: muestra la continuidad de la línea “device‑based” y su coexistencia con apps, además de cifras corporativas en brochures (p. ej. dispositivos y sitios equipados) que sirven como señal de escala comercial (sin reemplazar evaluación independiente). citeturn13search28turn13search5turn1search7  
Relación con MuseIQ: comparable por “audioguía profesional” y por el modelo de provisión integral (que MuseIQ no replica si busca bajo costo y hardware propio).

**entity["company","GuidiGO","tour creation platform"] (plataforma de tours y experiencias).**  
Finalidad: creación de tours y juegos “sin código”; ofrece también experiencias AR (la evidencia pública indica “50+ AR experiences”). citeturn13search3turn13search11  
Relación con MuseIQ: comparable más por “mediación móvil y engagement” que por localización BLE y asistente conversacional.

### Prototipos/pilotos académicos comparables por tecnología

A diferencia del mercado, la literatura académica suele explorar combinaciones avanzadas (BLE+analítica+personalización, voz, AR), con evaluaciones controladas o en casos reales.

**entity["people","David Verde","researcher sensors 2023"] et al. — “Indoor Content Delivery Solution for a Museum Based on BLE Beacons” (Sensors, 2023).**  
Finalidad: solución de entrega de contenido indoor basada en beacons BLE. La publicación reporta diseño y validación en un entorno museístico real y es especialmente relevante por evidenciar que BLE puede servir para entrega contextual en museo (enfocado en disparo de contenidos más que en RTLS de alta precisión). DOI: 10.3390/s23177403. citeturn0search20  
Relación con MuseIQ: altamente comparable por **BLE/proximidad** como mecanismo de reconocimiento contextual.

**“BLE Beacons for Indoor Positioning at an Interactive IoT‑based Smart Museum” (arXiv, 2020).**  
Finalidad: arquitectura de “smart museum” con beacons BLE, estimación por RSSI y un filtro (Kalman) en el smartphone; además, captura analítica y propone recomendaciones. DOI (arXiv): 10.48550/arXiv.2001.07686. citeturn9view1  
Relación con MuseIQ: comparable por pipeline **beacons BLE + estimación local + analítica**, y por el argumento de que la localización relativa/proximidad puede ser más práctica que la localización absoluta en museos donde cambian exhibiciones. citeturn9view1

**entity["people","Xi Wang","researcher voice guide 2024"] — “Co‑Design of a Voice‑Driven Interactive Smart Guide for Museum Accessibility and Management” (Journal of Audiovisual Translation, 2024).**  
Finalidad: guía con interacción por voz orientada a accesibilidad (visitantes ciegos o con baja visión) en un caso real (atracción museo). DOI: 10.47476/jat.v7i1.2024.267. citeturn0search17turn0search9  
Relación con MuseIQ: comparable por el énfasis en **voz (STT/TTS)** como interfaz; diferencia: no se observa aquí la combinación explícita con BLE+RAG como stack unificado. citeturn0search9

**“Gamified Mobile Guide Using iBeacon: Enhancing Informal Learning in a Taiwanese Science Museum” (IJIET, 2025).**  
Finalidad: evaluación a escala de un guía gamificado con iBeacon en un museo de ciencia; reporta despliegue con numerosos beacons y medición de impacto en comportamiento/engagement. DOI: 10.18178/ijiet.2025.15.10.2404. citeturn9view2  
Relación con MuseIQ: comparable porque muestra beneficios y costos prácticos de un despliegue iBeacon real; útil para discutir escalabilidad y mantenimiento.

### Asistentes conversacionales (académicos) en cultura y museos

**entity["people","Vasilis Bouras","researcher cultural chatbots 2023"] et al. — “Chatbots for Cultural Venues: A Topic‑Based Approach” (Algorithms, 2023).**  
Finalidad: metodología para construir chatbots que ofrecen acceso a información de museos/venues y sugiere un enfoque estructurado (temas, triples RDF). DOI: 10.3390/a16070339. citeturn6search0  
Relación con MuseIQ: comparable en el componente de **conversación**, pero con tecnología distinta (chatbot con organización semántica) y sin localización BLE como eje.

**entity["people","Octavian-Mihai Machidon","researcher cultural ai 2020"] et al. — “CulturalERICA: A conversational agent improving the exploration of European cultural heritage” (Journal of Cultural Heritage, 2020).**  
Finalidad: asistente conversacional vinculado a conocimiento patrimonial (Europa). DOI: 10.1016/j.culher.2019.07.010. citeturn6search2  
Relación con MuseIQ: comparable como precedente de “guía conversacional” en patrimonio; no aporta, por sí mismo, un stack BLE+sensores+voz.

**entity["people","Mihai Duguleană","researcher virtual assistant 2020"] et al. — “A Virtual Assistant for Natural Interactions in Museums” (Sustainability, 2020).**  
Finalidad: asistente virtual para interacción natural en museos; útil como marco de diseño e interacción. DOI: 10.3390/su12176958. citeturn8search3  
Relación con MuseIQ: comparable en el objetivo de interacción natural; diferencia: MuseIQ plantea explícitamente RAG y sensórica BLE/smartphone como anclaje contextual.

**“Experiencing Art Museum with a Generative Artificial Intelligence Chatbot” (ACM IMX, 2025).**  
Finalidad: chatbot generativo en smartphone para interacción en museo de arte; reporta evaluación de engagement y preferencia por formatos textual y auditivo. DOI: 10.1145/3706370.3731650. citeturn6search5  
Relación con MuseIQ: comparable por uso de IA generativa en visita; diferencia: no se evidencia como núcleo el reconocimiento por sala mediante beacons BLE ni RAG explícito; el foco es el chatbot como interfaz de mediación. citeturn6search5

## Tabla comparativa de soluciones

La tabla sintetiza la comparabilidad de cada referente respecto a los componentes de MuseIQ: **BLE (proximidad/sala), orientación indoor, voz, IA contextual, accesibilidad** y **complejidad**. Cuando no existe información pública verificable, se marca como “No público”.

| Solución / referencia | Tipo | Contexto de aplicación | BLE / indoor positioning | Voz | IA / personalización | Accesibilidad | Infraestructura requerida | Costo / complejidad relativa | Principal fortaleza | Principal limitación | Relevancia para MuseIQ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bloomberg Connects | Plataforma institucional global | Museos multisede, guía digital | No enfatizado públicamente | Audio/multimedia (sí) | No central (público) | Variable por guía | Baja (app + contenido) | Media (alianza/plataforma) | Escala masiva “1000+” instituciones | No centrado en localización BLE + RAG | Benchmark de adopción/UX citeturn0search11turn0search27 |
| Smartify | Plataforma comercial | Museos/organizaciones culturales | No central (público) | Audio (sí) | AI translations / AI personalised tours (planes) | Depende de implementación | Baja–media (PWA/app + CMS) | Media (precios publicados) | PWA sin descarga + CMS + IA | No evidencia de BLE como núcleo | Comparable por estrategia BYOD/IA citeturn1search31turn1search0 |
| SmartGuide | Plataforma comercial | Museos/atracciones | No público (en evidencia revisada) | Audio (sí) | “AI tour planner” + “AI Guide chat” | No público (detalle limitado) | Baja–media (app + CMS) | Media (precios publicados) | Incorpora chat IA “linked to vetted content” | No confirma BLE/IPS como base | Referente de chat IA en guía citeturn5view3 |
| izi.TRAVEL | Plataforma comercial | Museos/turismo | QR (museos) + GPS (outdoor) | Audio (sí) | No central | No público | Baja (QR + app) | Baja–media | Fácil creación/distribución global | Localización indoor limitada (QR) | Referente “low‑infra” y CMS citeturn1search17turn1search9 |
| Nubart GUIDE | Producto comercial (PWA) | Museos (QR/PWA) | No (QR; no IPS) | Audio (sí) | No central (público) | Enfoque accesible (público) | Baja (QR) | Baja–media | Acceso sin descarga; reduce fricción | Mediación contextual depende de QR | Referente “acceso ligero” citeturn13search2turn13search14 |
| Hearonymus | Plataforma comercial | Museos/atracciones | QR/NFC/GPS (no BLE en evidencia principal) | Audio (sí) | No central | Opciones: SL/LS/AD (público) | Baja | Baja–media | Opciones accesibilidad y disparo simple | No es guía contextual BLE | Útil en accesibilidad y monetización citeturn14search0turn14search17 |
| Locatify | Plataforma comercial | Museos (indoor) + turismo | BLE beacons y también UWB (oferta) | Audio (sí) | No central (público) | No público (detalle variable) | Media (beacons/UWB + mapas) | Media–alta | Combina localización + contenido + gamificación | IA conversacional no es eje | Muy comparable en BLE/indoor citeturn15search5turn15search22turn15search1 |
| Navigine | Plataforma comercial (SDK) | Indoor navigation (incl. museos) | BLE/Wi‑Fi/UWB (plataforma) | No central | No central | No público | Alta (mapas + beacons + SDK) | Alta | Wayfinding/RTLS y analítica | Coste/operación mayores; foco distinto | Comparable en “orientación indoor” citeturn14search5turn14search22turn14search10 |
| Orpheo / Acoustiguide | Proveedor comercial integral | Museos grandes, hardware + apps | Posible, pero no eje en evidencia pública revisada | Audio/multimedia (sí) | No público | No público | Media–alta (hardware + operación) | Alta | Solución end-to-end escalada | Dependencia de proveedor/hardware | Benchmark de “audioguía industrial” citeturn13search28turn13search5 |
| GuidiGO | Plataforma comercial | Tours + juegos + AR | No público | Audio (sí) | No central | No público | Baja–media | Media | Herramientas “sin código”; AR | No centrado en BLE/voz/IA contextual | Referente de engagement y authoring citeturn13search3turn13search11 |
| Indoor Content Delivery BLE Beacons (Sensors 2023) | Académico (validación) | Museo real + BLE | Sí (BLE) | No central | Personalización/entrega contextual (según estudio) | No público | Media (beacons + app) | Media | Evidencia académica de BLE en museo | No integra voz+RAG como núcleo | Referente técnico directo (BLE) citeturn0search20 |
| IoT Smart Museum BLE + Kalman (arXiv 2020) | Académico (prototipo) | Museo “smart” | Sí (BLE RSSI) | No | Recomendación/analítica | No público | Media | Media | Arquitectura BLE + analítica + filtro local | No es producto; transferencia incierta | Inspira fusión sensorial / robustez citeturn9view1 |
| Co‑Design Voice‑Driven Smart Guide (2024) | Académico (caso real) | Accesibilidad en atracción/museo | No | Sí (voz interactiva) | Q&A por voz (guía inteligente) | Fuerte foco BLV | Baja–media | Media | Aporta evidencia sobre voz para accesibilidad | No combina BLE+RAG | Referente directo para módulo voz citeturn0search17turn0search9 |
| Gamified iBeacon iGuide (IJIET 2025) | Académico (despliegue a escala) | Museo ciencia (Taiwán) | Sí (iBeacon) | No | Personalización por tipologías/analítica | No público | Alta (muchos beacons + mapas) | Alta | Evidencia de impacto y escalamiento | Coste/operación altos; no voz/IA | Útil para discutir escalabilidad BLE citeturn9view2 |
| Chatbots for Cultural Venues (Algorithms 2023) | Académico | Venues culturales | No | No (texto) | Chatbot (temas/RDF) | No público | Baja | Media | Metodología para chatbot cultural | No localización/voz; no RAG explícito | Base conceptual para conversación cultural citeturn6search0 |
| CulturalERICA (JCH 2020) | Académico | Patrimonio europeo | No | No (no central) | Agente conversacional | No público | Media | Media | Enlace a conocimiento patrimonial | No integra localización in situ | Referente de agente patrimonial citeturn6search2 |
| Virtual Assistant in Museums (Sustainability 2020) | Académico | Interacción natural | No | Potencial (según diseño) | Asistente virtual | No público | Media | Media | Marco de asistente para museo | No evidencia de BLE+RAG | Referente conceptual de interacción citeturn8search3 |
| Generative AI Chatbot in Art Museum (ACM 2025) | Académico | Museo de arte (app) | No público | Sí (auditory output reportado) | IA generativa | No público | Media | Media | Evidencia de engagement con chatbot | Riesgo de exactitud; no BLE/RAG explícito | Referente de IA generativa en visita citeturn6search5 |

## Análisis crítico de la oferta mundial

La evidencia revisada sugiere que la oferta mundial se organiza alrededor de tres estrategias dominantes:

La primera es la **estrategia de guía digital “contenido‑primero”**: plataformas como Bloomberg Connects, Smartify o izi.TRAVEL priorizan **publicación, curaduría y UX** (mapas, audio, multimedia) en un modelo BYOD “a gran escala”. Son soluciones efectivas para mediación digital general, pero no necesariamente resuelven la necesidad de MuseIQ de **contexto automático por sala** ni la interacción por voz como mecanismo principal. citeturn0search11turn1search31turn1search17

La segunda estrategia es la **mediación por disparo contextual “infraestructura ligera”** (QR/PWA y/o BLE). Aquí se observa una tensión práctica: reducir fricción (PWA/QR) suele sacrificar automatización contextual; y aumentar automatización mediante BLE beacons introduce tareas de despliegue/mantenimiento y problemas conocidos de RSSI. La literatura de smart museums y los estudios en BLE indoor positioning subrayan la necesidad de considerar multipath, dinámica del entorno y técnicas de filtrado/fusión para estabilizar estimaciones. citeturn3search8turn10search0turn9view1turn0search20

La tercera estrategia es la **orientación indoor/wayfinding como servicio** (SDKs RTLS). Soluciones tipo Navigine representan un segmento con mayor complejidad: necesitan mapas indoor y un ciclo de calibración y mantenimiento más cercano al de proyectos de localización empresarial (malls, aeropuertos), aunque su valor es alto para accesibilidad espacial y analítica de flujos. En el continuo de tecnologías, las revisiones de indoor localization muestran que BLE, Wi‑Fi, UWB e IMU se combinan para balancear costo y desempeño; UWB aporta alta precisión a costa de infraestructura, mientras BLE suele considerarse más conveniente cuando se busca granularidad “suficiente” y menor costo. citeturn14search5turn10search0turn16search3turn16search0

En **voz y accesibilidad**, el principal hallazgo es que la oferta comercial mainstream se queda en **audio pregrabado**. La voz interactiva aparece con más claridad en trabajos académicos centrados en accesibilidad (p. ej., guías por voz para BLV) y en prototipos de agentes conversacionales; esto sugiere que, aunque el componente de voz es técnicamente viable, su normalización en productos comerciales de museo no está plenamente consolidada o no se comunica como rasgo central. citeturn0search17turn14search0turn6search0

Respecto a **IA**, el mercado comienza a introducir funciones “IA” (traducciones, planificación, chat) en plataformas de guías, mientras la academia reporta chatbots generativos en museos con resultados prometedores en engagement. No obstante, el debate académico y normativo enfatiza riesgos de exactitud, autenticidad y la necesidad de gobernanza institucional, especialmente en dominios patrimoniales donde un error puede afectar confianza y valor educativo. citeturn5view3turn6search5turn2search1turn2search31

Finalmente, sobre la pregunta clave de esta tesis —**qué tan común es integrar BLE + orientación móvil + voz + IA contextual (RAG) en una sola arquitectura**— la evidencia sugiere que es **poco común** en productos comerciales generalistas. Se ven integraciones parciales: (i) BLE+guía+gamificación (despliegues iBeacon), (ii) voz+guía inteligente para accesibilidad, (iii) chatbots (estructurados o generativos) para mediación cultural, y (iv) plataformas con funciones IA. La combinación completa que propone MuseIQ se asemeja más a una **arquitectura “composite”** donde se integran módulos que, en el mercado, suelen venderse por separado o aparecer en prototipos académicos. Esta conclusión es una **interpretación** basada en la comparación de descripciones técnicas públicas y literatura revisada. citeturn9view2turn0search17turn6search5turn0search20turn7search0

## Posicionamiento de MuseIQ frente a la oferta mundial

A partir del análisis comparativo, MuseIQ se ubica en un espacio intermedio entre “guía digital BYOD” y “smart museum context‑aware”, con un énfasis específico: **mejorar la experiencia presencial** mediante la conjunción de **reconocimiento de proximidad/sala con BLE**, **apoyo de orientación con sensores del smartphone**, **interacción por voz (TTS/STT)** y **QA contextual con RAG** sobre contenidos museísticos.

**Similitudes con la oferta existente (convergencias).**  
MuseIQ converge con plataformas globales en la ambición de ser una guía BYOD y en la necesidad de CMS/curaduría, aunque plataformas como Bloomberg Connects o Smartify resuelven esto a escala de red de instituciones. citeturn0search11turn1search31 Converge con soluciones BLE académicas y comerciales (Locatify; estudios en Sensors y arXiv) en usar beacons para disparo contextual y, potencialmente, analítica. citeturn15search5turn0search20turn9view1 Y converge con investigaciones de voz (Wang, 2024) en concebir la voz como interfaz útil para accesibilidad. citeturn0search17

**Diferencias (propuesta diferencial probable, sin exagerar).**  
La diferenciación de MuseIQ no sería “inventar” audioguías, ni “ser el primero” en usar BLE o chatbots, porque ambos existen. La diferenciación más defendible —como interpretación derivada de la revisión— es la **integración deliberada, en una arquitectura única y orientada al contexto peruano**, de cuatro piezas que hoy aparecen dispersas:
- BLE “room‑level” como mecanismo de contextualización in situ (en vez de depender solo de QR o navegación manual). citeturn0search20turn12search0  
- Orientación y soporte a wayfinding usando sensores del smartphone (IMU/rotación), reduciendo la dependencia de una plataforma RTLS completa tipo enterprise. Evidencia técnica de base: Android documenta sensores y clases para orientación/rotación; y revisiones de indoor localization muestran el rol de IMU y fusión para mejorar robustez. citeturn11search0turn11search1turn10search0  
- Interacción por voz como canal principal de mediación (no solo audio pregrabado), alineada con hallazgos académicos sobre accesibilidad y experiencias guiadas por voz. citeturn0search17  
- IA contextual con RAG para anclar respuestas en fuentes curatoriales, alineada con literatura que motivó RAG como combinación de memoria paramétrica y recuperación, y con estudios de mitigación de alucinaciones mediante recuperación. citeturn7search0turn7search26turn7search18

**Valor para museos peruanos (argumento contextual).**  
La pertinencia para museos públicos peruanos se apoya en condiciones estructurales documentadas: alta presencia de smartphone en hogares y un ecosistema de museos administrados por el Ministerio de Cultura con volumen significativo de visitas, lo que habilita pilotos con impacto y replicabilidad. citeturn4search0turn4search1 En escenarios de recursos limitados, MuseIQ apunta a una infraestructura **ligera** (BLE con emisores de bajo costo y uso de sensores del visitante) frente a soluciones de wayfinding de infraestructura alta. Esta ventaja es plausible (interpretación), pero exige validación económica en el capítulo de ingresos/costos. citeturn10search0turn16search0

**Advertencia metodológica.**  
La viabilidad diferencial de MuseIQ dependerá de dos factores que la oferta comercial ha aprendido a priorizar: (i) **fricción de acceso** (idealmente PWA o onboarding extremadamente simple) y (ii) **sostenibilidad editorial** (CMS y flujos de actualización). En el mercado, la evidencia industrial reporta que la fricción de descargar apps puede ser una barrera relevante; por ello, la estrategia de acceso de MuseIQ es un punto crítico de diseño y adopción institucional. citeturn3search8turn1search31

## Conclusión del capítulo

La oferta tecnológica mundial comparable a MuseIQ muestra un mercado maduro en **audioguías y guías digitales BYOD**, con plataformas robustas para publicación y experiencia de visita; y, en paralelo, un campo activo de investigación en **smart museums**, **localización indoor** y **asistentes conversacionales**. La brecha central no es la ausencia de tecnología aislada, sino la dificultad de integrar de forma sostenible —y con costos compatibles con museos con restricciones— una mediación **contextual, accesible y verificable** durante la visita presencial. citeturn2search7turn10search0turn2search31

Desde esta lectura, el espacio de MuseIQ se justifica como una arquitectura integradora que, si se valida en el contexto peruano, podría ubicarse como alternativa “ligera” frente a RTLS de alta infraestructura y como alternativa “más contextual” frente a guías QR/PWA puramente manuales. Este cierre prepara el tránsito al capítulo de flujo de ingresos/evaluación económica: allí deberá demostrarse si la combinación BLE+voz+IA contextual reduce costos totales (TCO) y aumenta valor percibido en museos públicos, frente a contratar plataformas comerciales o implementar pilotos aislados. citeturn14search5turn15search1turn4search1

### Bibliografía final

A continuación se separan fuentes **académicas indexadas**, **documentos institucionales/oficiales** y **referentes de mercado**. Para cada fuente se indica DOI cuando está disponible; el enlace verificable corresponde a la referencia citada.

#### Fuentes académicas indexadas

- entity["people","David Verde","researcher sensors 2023"] et al. *Indoor Content Delivery Solution for a Museum Based on BLE Beacons.* **Sensors** (2023). DOI: 10.3390/s23177403. citeturn0search20  
- Lin, C.-L., & Lin, Y.-N. *Gamified Mobile Guide Using iBeacon: Enhancing Informal Learning in a Taiwanese Science Museum.* **International Journal of Information and Education Technology** (2025). DOI: 10.18178/ijiet.2025.15.10.2404. citeturn9view2  
- entity["people","Xi Wang","researcher voice guide 2024"]. *Co-Design of a Voice-Driven Interactive Smart Guide for Museum Accessibility and Management.* **Journal of Audiovisual Translation** (2024). DOI: 10.47476/jat.v7i1.2024.267. citeturn0search17turn0search9  
- entity["people","Rosen Ivanov","researcher smart museums 2025"] & entity["people","Victoria Velkova","researcher smart museums 2025"]. *Analyzing Visitor Behavior to Enhance Personalized Experiences in Smart Museums: A Systematic Literature Review.* **Computers** (2025). DOI: 10.3390/computers14050191. citeturn0search6  
- Leitch, S. G., et al. *On Indoor Localization Using WiFi, BLE, UWB, and IMU Technologies.* **Sensors** (2023). DOI: 10.3390/s23208598. citeturn10search0  
- Qiao, J., et al. *Advancements in Indoor Precision Positioning: A Comprehensive Survey of UWB and Wi‑Fi RTT Positioning Technologies.* **Network** (2024). DOI: 10.3390/network4040027. citeturn16search3  
- entity["people","Vasilis Bouras","researcher cultural chatbots 2023"] et al. *Chatbots for Cultural Venues: A Topic-Based Approach.* **Algorithms** (2023). DOI: 10.3390/a16070339. citeturn6search0  
- entity["people","Octavian-Mihai Machidon","researcher cultural ai 2020"] et al. *CulturalERICA: A conversational agent improving the exploration of European cultural heritage.* **Journal of Cultural Heritage** (2020). DOI: 10.1016/j.culher.2019.07.010. citeturn6search2  
- entity["people","Mihai Duguleană","researcher virtual assistant 2020"] et al. *A Virtual Assistant for Natural Interactions in Museums.* **Sustainability** (2020). DOI: 10.3390/su12176958. citeturn8search3  
- Wang, H., & Matviienko, A. *Experiencing Art Museum with a Generative Artificial Intelligence Chatbot.* **ACM IMX** (2025). DOI: 10.1145/3706370.3731650. citeturn6search5  
- entity["people","Patrick Lewis","nlp researcher rag 2020"] et al. *Retrieval‑Augmented Generation for Knowledge‑Intensive NLP Tasks.* (2020). DOI (arXiv): 10.48550/arXiv.2005.11401. citeturn7search0  
- Gupta, S., Ranjan, R., & Singh, S. N. *A Comprehensive Survey of Retrieval‑Augmented Generation (RAG).* (2024). DOI (arXiv): 10.48550/arXiv.2410.12837. citeturn7search1  
- Béchard, P., & Ayala, O. M. *Reducing hallucination in structured outputs via Retrieval‑Augmented Generation.* (NAACL Industry Track, 2024). DOI: 10.18653/v1/2024.naacl-industry.19. citeturn7search26turn7search2  

#### Documentos institucionales u oficiales

- entity["organization","OSIPTEL","telecom regulator peru"]. Nota institucional ERESTEL: **94.8% de hogares peruanos con smartphone** (cierre 2024; publicado 2025). citeturn4search0  
- entity["organization","Ministerio de Cultura del Perú","culture ministry peru"]. *Reporte de cumplimiento 2024 de la Política Nacional de Cultura al 2030* (publicado 2025). Evidencia: visitas registradas y magnitudes de público museal. citeturn4search1  
- entity["organization","UNESCO","un cultural agency"]. *UNESCO Global Report on Cultural Policies | Culture: the Missing SDG; executive summary 2025.* DOI: 10.58337/IWCF6031. citeturn4search26turn4search11  
- entity["organization","UNESCO","un cultural agency"]. *Artificial Intelligence and Culture* (Independent Expert Group report, 2025). citeturn2search31  
- entity["organization","ICOM CIDOC","museum documentation committee"]. Digital Strategy Development Working Group (materiales y guías para estrategia digital en museos). citeturn2search3  
- entity["company","Apple","technology company"]. Documentación de iBeacon: programación con UUID/major/minor y proximidad. citeturn12search0turn12search18  
- entity["company","Google","technology company"]. Eddystone specification (GitHub) y definición de frames UID/URL/TLM. citeturn12search1turn12search5  
- Android Developers. Sensores de posición/orientación: acelerómetro, magnetómetro y rotation vector. citeturn11search0turn11search1  
- Espressif (ESP‑IDF). Ejemplo oficial de iBeacon advertising / device discovery BLE. citeturn12search3turn12search14  

#### Referentes de mercado

- entity["organization","Bloomberg Connects","arts guide app"]. Catálogo de guías y declaración “over 1000” instituciones. citeturn0search11  
- entity["company","Smartify","arts and culture app uk"]. Pricing y capacidades (incl. AI translations / AI personalised tours) y productos (incl. PWA sin descarga). citeturn1search0turn1search31  
- entity["company","SmartGuide","digital guide platform"]. Página de pricing y lista de funciones (AI tour planner; AI Guide chat). citeturn5view3  
- entity["company","izi.TRAVEL","audio tour platform"]. Descripción de uso en museos por QR y documentación CMS indoor. citeturn1search17turn1search5  
- entity["company","Nubart","audio guide pwa spain"]. Producto PWA/QR y estudio industrial de adopción (2.47%) + discusión profesional AAM. citeturn13search2turn13search14turn3search8  
- entity["company","Hearonymus","audio guide platform vienna"]. Triggering por QR/NFC/GPS y opciones de accesibilidad; ejemplo de precio por guía en un sitio patrimonial. citeturn14search0turn14search17  
- entity["company","Locatify","location-based app platform iceland"]. About (fundación), pricing, y oferta con BLE/UWB para museos. citeturn15search0turn15search1turn15search5  
- entity["company","Navigine","indoor navigation platform"]. Vertical para museos y descripción de despliegue (SDK + beacons). citeturn14search5turn14search22  
- entity["company","GuidiGO","tour creation platform"]. Plataforma de tours/juegos sin código y oferta AR. citeturn13search3turn13search11  
- entity["company","Orpheo","visitor solutions company france"]. Brochure corporativo (escala de sitios/dispositivos) y línea de productos. citeturn13search28turn13search9  

### Vacíos de información que convendría precisar

1) **Estrategia de acceso** de MuseIQ (app nativa vs PWA vs híbrida) y su racional explícito frente a la evidencia de fricción de descarga observada en mercado (esto impacta directamente adopción y costos de soporte). citeturn3search8turn1search31  

2) **Modelo de gestión de contenidos**: quién curará y actualizará el corpus para RAG (curadores del museo, equipo centralizado, convenio con MINCUL), y con qué herramientas (CMS propio vs integración). Este punto define costo recurrente y sostenibilidad. citeturn2search3turn7search18  

3) **Política de trazabilidad/verificación** en IA: cómo se mostrarán fuentes y cómo se manejarán respuestas “no sé” para mitigar alucinaciones en contenidos patrimoniales (criterios y métricas de calidad). citeturn7search0turn7search26turn2search31  

4) **Supuesto técnico de granularidad**: precisión requerida (sala vs obra) y su validación con BLE en condiciones reales del museo objetivo en Perú (densidad de visitantes, materiales, interferencias). Esto conecta con selección de hardware y número de beacons. citeturn10search0turn0search20turn9view2  

5) **Recolección de datos/privacidad**: si MuseIQ registrará recorridos/tiempos por usuario y cómo se gestionará consentimiento, anonimización y retención (especialmente en instituciones públicas). citeturn16search13turn2search31
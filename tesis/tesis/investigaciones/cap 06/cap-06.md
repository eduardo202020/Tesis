# Capítulo 6 de tesis: fundamentos de MuseIQ para mediación cultural inteligente en visita presencial

## A. Título sugerido del capítulo

**CAPÍTULO 6: FUNDAMENTOS CONCEPTUALES, FUNCIONALES Y TÉCNICOS DE MUSEIQ**

## B. Justificación breve del papel del capítulo dentro de la tesis

Este capítulo cumple la función de **fundamentar con rigor** las decisiones de ingeniería que sostienen a MuseIQ **antes** de entrar a capítulos de diseño técnico detallado. Su aporte central es articular (i) el marco conceptual de la experiencia museal y la mediación cultural, (ii) la lógica funcional de contextualización “situada” (por sala/zona y momento de visita), y (iii) los fundamentos técnicos generales que hacen viable una guía inteligente basada en **reconocimiento de sala**, sensores del smartphone, interacción por voz y **RAG**. En coherencia con una tesis de ingeniería aplicada, el capítulo delimita criterios y supuestos que justifican la propuesta como sistema, sin convertirse en estado del arte repetido ni en arquitectura implementativa.

## C. Propuesta de estructura del capítulo con numeración tipo tesis

- **6.1 Base conceptual o técnica**  
  - **6.1.1 Mediación cultural digital en visitas presenciales**  
  - **6.1.2 Contextualización del contenido museístico como sistema “context-aware”**  
  - **6.1.3 Proximidad, sala y orientación como variables interpretativas de contexto**  
  - **6.1.4 Fundamento de localización funcional en interiores**  
  - **6.1.5 Justificación de reconocimiento de sala/zona frente a precisión centimétrica**  
  - **6.1.6 Interacción multimodal y accesibilidad mediante voz**  
  - **6.1.7 Smartphone como interfaz principal en guías BYOD**  
  - **6.1.8 Recuperación contextual del conocimiento y RAG en dominios museísticos**  
  - **6.1.9 Trazabilidad, control de respuesta y responsabilidad en patrimonio cultural**  
  - **6.1.10 Modulación, escalabilidad y bajo costo como principios de ingeniería**  
  - **6.1.11 Relación de los fundamentos con el contexto peruano del proyecto**  

- **6.2 Características principales**  
  - **6.2.1 Mediación situada por reconocimiento de sala y zona probable de observación**  
  - **6.2.2 Orientación y apoyo a la navegación interpretativa con sensores del smartphone**  
  - **6.2.3 Interacción por voz TTS/STT como capa de accesibilidad y continuidad de flujo**  
  - **6.2.4 Asistente conversacional con RAG y respuestas controladas por evidencia**  
  - **6.2.5 Curaduría digital, gobernanza del conocimiento y mantenimiento evolutivo**  
  - **6.2.6 Arquitecturabilidad: modularidad, escalabilidad y operación de bajo costo**  
  - **6.2.7 Confiabilidad operativa: tolerancia a variabilidad indoor, conectividad y contexto real**  

## D. Desarrollo extenso del contenido en redacción académica, listo para adaptar a LaTeX

**Capítulo 6**  
**Fundamentos conceptuales, funcionales y técnicos de MuseIQ**

La propuesta MuseIQ se plantea como una guía virtual inteligente orientada a museos y espacios culturales que busca mejorar la experiencia de visita presencial mediante contextualización situada, interacción multimodal y acceso a conocimiento curatorial. En términos de ingeniería aplicada, el valor diferencial del sistema no reside únicamente en incorporar tecnologías aisladas (beacons BLE, sensores del smartphone, TTS/STT o modelos de IA), sino en **integrarlas** bajo fundamentos que alineen: (i) la lógica de mediación cultural, (ii) la pertinencia contextual del contenido, (iii) la robustez operativa en interiores, y (iv) la responsabilidad sobre información patrimonial. La presente sección define dichos fundamentos como marco previo al diseño técnico detallado.

### 6.1 Base conceptual o técnica

#### 6.1.1 Mediación cultural digital en visitas presenciales

La mediación cultural en museos puede entenderse como el conjunto de estrategias que facilitan la relación entre visitantes, objetos patrimoniales y relatos interpretativos, con el propósito de favorecer comprensión, apropiación cultural y experiencia significativa. Desde la perspectiva de interpretación del patrimonio, existe un consenso histórico en que la información museal no se limita al dato descriptivo, sino que requiere **conexión con sentido**, orientación narrativa y adaptación al interés del visitante; esta tradición se formaliza, por ejemplo, en los principios de interpretación de entity["people","Freeman Tilden","heritage interpretation author"], que sostienen que la interpretación debe relacionar el contenido con la experiencia del público y provocar interés más que solo instruir. citeturn8search1turn8search5

En el contexto contemporáneo, la mediación digital complementa la mediación física al habilitar capas de información, accesibilidad y personalización que pueden operar en tiempo real, con bajo freno operativo cuando se apalanca en dispositivos del visitante. La literatura reciente sobre transformación digital en museos enfatiza que tecnologías digitales (sensores, sistemas móviles, analítica e IA) han ampliado las posibilidades de diseño de exposiciones y engagement, pero su beneficio depende de cómo se integran a los objetivos curatoriales y a la experiencia de visita, evitando la sobreestimulación o la disociación del objeto real. citeturn8search18turn4search8turn8search6

Bajo esta lógica, MuseIQ se justifica como mediación digital **in situ** (durante la visita presencial) por tres razones conceptuales: (a) el museo es una experiencia situada y multimodal, donde el espacio físico y la trayectoria del visitante aportan significado; (b) el visitante requiere pertinencia contextual —no solo abundancia informativa— para sostener atención; y (c) la accesibilidad se incrementa cuando el sistema reduce dependencia de lectura prolongada o interacción visual continua, especialmente mediante audio y voz. Estos principios son coherentes con enfoques centrados en el visitante como unidad de diseño museográfico, en los que el valor se mide por la calidad de la experiencia y el aprendizaje libre-elección (free-choice learning), más que por la simple entrega de contenidos. citeturn8search8turn8search0

#### 6.1.2 Contextualización del contenido museístico como sistema “context-aware”

En ingeniería de sistemas interactivos, la contextualización se apoya en el concepto de *context-aware computing*, donde el sistema adapta información y servicios según la situación del usuario. Un aporte canónico establece que “contexto” es cualquier información que caracterice la situación de una entidad relevante para la interacción y que un sistema es context-aware si usa ese contexto para ofrecer información/servicios cuya relevancia depende de la tarea del usuario. citeturn0search1turn0search9turn0search5

La traducción al dominio museístico implica que la “situación” del visitante no se reduce a coordenadas; incluye su ubicación semántica (sala/zona), proximidad a piezas, orientación aproximada (hacia qué vitrina/panel se posiciona), tiempo de permanencia, ritmo de recorrido e incluso necesidades de accesibilidad. La evidencia en aplicaciones de patrimonio cultural muestra que el valor de la context-awareness reside en optimizar la experiencia cultural entregando contenido adaptado al entorno y al visitante (perfil, comportamiento y parámetros del ambiente), constituyendo un enfoque transversal a distintas estrategias (recomendación, narrativas adaptativas, guías móviles, IoT cultural). citeturn4search18turn8search11

En consecuencia, MuseIQ se fundamenta en una hipótesis operacional: **un museo puede interpretarse como un conjunto de contextos discretos (salas, zonas o puntos de interés) donde el visitante adopta intenciones interpretativas detectables por señales de interacción y proximidad**. Esta hipótesis habilita dos implicancias funcionales de ingeniería:

Primero, prioriza la reducción de carga cognitiva: el sistema entrega contenido cuando existe alta probabilidad de relevancia, evitando menús extensos o navegación manual constante. Segundo, permite personalizar el “momento” interpretativo: el sistema no compite con la mirada del visitante, sino que se acopla a su recorrido. Esto es consistente con resultados empíricos donde guías context-aware basadas en beacons han mostrado mejoras en interacción y aprendizaje informal al comparar recorridos con y sin disparadores contextuales. citeturn4search4turn4search7

#### 6.1.3 Proximidad, sala y orientación como variables interpretativas de contexto

En visitas presenciales, la **posición relativa** del visitante frente a objetos y su desplazamiento por el espacio operan como indicadores de atención, interés y oportunidad de interpretación. En términos funcionales, “estar en una sala” no es un dato logístico únicamente: delimita un **conjunto semántico** de obras y una narrativa probable. La proximidad, por su parte, actúa como señal de “enfoque” hacia un sector o pieza (por ejemplo, acercamiento a una vitrina), mientras que la orientación aproximada del dispositivo puede contribuir a inferir cuál elemento dentro de una zona es el foco de observación, con mayor control contextual que usar proximidad sola en espacios densos.

Este fundamento es relevante porque MuseIQ se plantea como mediación “no invasiva”: la interacción debe integrarse al ritmo natural de la visita. Por ello, la proximidad y la sala se consideran variables interpretativas **suficientes** para activar contenidos sin exigir al usuario que busque manualmente o que el sistema calcule coordenadas exactas. La literatura sobre proximidad indoor con BLE reconoce que estos sistemas son valiosos cuando el objetivo es habilitar servicios acotados espacialmente (*space-bounded services*) y no necesariamente estimar la posición absoluta con alta exactitud, debido a las condiciones de propagación en interiores. citeturn4search6turn1search0

Adicionalmente, en museos el “contexto físico” se integra a la experiencia. El marco del *Contextual Model of Learning* (aprendizaje en museos) subraya que la experiencia del visitante emerge de la interacción entre contextos personales, socioculturales y físicos; por tanto, diseñar mediación digital efectiva requiere reconocer el espacio como parte del proceso de interpretación y aprendizaje. citeturn8search8turn8search0

**Análisis (inferencia de ingeniería):** bajo este marco, la combinación “sala + proximidad + orientación” puede considerarse un *mínimo viable de contexto* para guías inteligentes presenciales: no busca inferir intención con precisión perfecta, sino aumentar significativamente la probabilidad de pertinencia del contenido frente a un visitante heterogéneo, en escenarios de infraestructura limitada.

#### 6.1.4 Fundamento de localización funcional en interiores

La localización en interiores (*indoor localization / indoor positioning*) es un campo consolidado que reconoce múltiples técnicas (RSSI, AoA, ToF, fingerprinting, UWB, Wi‑Fi, BLE, RFID, etc.) y muestra trade-offs inevitables entre exactitud, costo, consumo energético, infraestructura, escalabilidad y robustez. Revisiones de amplio alcance describen que la variabilidad del canal radioeléctrico indoor (multitrayectoria, oclusión por personas/objetos, interferencia) complica la estimación precisa de distancias y posiciones cuando se depende de potencia recibida, especialmente en despliegues de bajo costo. citeturn1search0turn1search14turn1search6

En este escenario, resulta crítico distinguir entre dos nociones de localización:

- **Localización física**: asociada a coordenadas (modelo geométrico).  
- **Localización simbólica o semántica**: asociada a lugares con significado (por ejemplo “Sala Paracas”, “Galería 2”, “Zona de cerámica”), donde la utilidad proviene de su interpretabilidad humana y su vínculo directo con servicios. citeturn1search1turn1search5

La evidencia en sistemas location-aware sugiere que añadir semántica a la localización (ubicación simbólica) facilita habilitar servicios más relevantes para usuarios, porque alinea el “lugar” con la tarea. citeturn1search1turn0search1

Por tanto, MuseIQ adopta una noción de **localización funcional**: la localización es un medio para la mediación cultural, no un fin de exactitud métrica. Esta elección es coherente con el principio de ingeniería aplicada señalado en revisiones de servicios basados en localización: el desempeño debe juzgarse por el valor del servicio entregado (en este caso, mediación interpretativa contextual), no por una métrica aislada de error en metros si no aporta proporcionalmente a la experiencia. citeturn1search1turn1search0

#### 6.1.5 Justificación de reconocimiento de sala/zona frente a precisión centimétrica

MuseIQ prioriza el reconocimiento de sala o zona por cinco fundamentos técnicos-funcionales principales:

Primero, **alineación con la estructura museográfica**. Los museos organizan narrativas por salas, ejes temáticos y secuencias espaciales; por tanto, el nivel “sala/zona” coincide con unidades curatoriales prácticas para activar contenidos, sin requerir el costo de instrumentar cada vitrina con precisión centimétrica.

Segundo, **robustez ante el entorno indoor**. En BLE basado en RSSI, la potencia recibida es altamente variable por multitrayectoria, sombras y absorción por el cuerpo humano. La literatura reciente continúa documentando el impacto de la colocación del beacon, la posición del dispositivo en el cuerpo y la configuración del receptor sobre desempeño de recepción y localización. citeturn1search6turn1search14turn1search0

Tercero, **evidencia empírica en museos**. Un estudio aplicado a entrega de contenido indoor en un museo reportó una exactitud alta en identificación de sala mediante BLE, señalando que el enfoque de detección de señal puede ser suficiente para el caso de uso museístico. citeturn0search2turn4search0

Cuarto, **adecuación al estado actual de la tecnología de beacons**. En el ámbito de tecnologías museales, se ha señalado explícitamente que los beacons son especialmente aptos para aplicaciones que requieren sensación de proximidad más que ubicación exacta; es decir, su mejor ajuste es “detectar cerca/lejos” o “en qué área” antes que resolver coordenadas finas. citeturn4search11turn4search6

Quinto, **principio de costo-beneficio y escalabilidad**. En contextos donde la inversión en infraestructura es una restricción fuerte, insistir en precisión centimétrica suele exigir más densidad de infraestructura, calibración compleja y mantenimiento costoso. En cambio, un enfoque por sala/zona logra un punto de equilibrio entre utilidad y costo, con mayor probabilidad de adopción institucional.

**Análisis (inferencia de ingeniería):** en MuseIQ, la exactitud deseable no es “error en metros”, sino “tasa de activación correcta de contenidos” y “reducción de fricción en la visita”. Esta reconceptualización transforma la localización en un componente instrumental al servicio de la mediación.

#### 6.1.6 Interacción multimodal y accesibilidad mediante voz

La interacción humano-computadora en entornos culturales tiene una exigencia particular: debe sostener el foco en el objeto patrimonial y la experiencia física, no desplazarla hacia la pantalla. En este sentido, la interacción multimodal —uso coordinado de más de un modo natural de comunicación, como voz, tacto, gesto, orientación, audio— ofrece ventajas cuando se requiere reducir carga visual, aumentar flexibilidad y atender diversidad de usuarios. Definiciones ampliamente citadas caracterizan sistemas multimodales como aquellos que procesan modos combinados de entrada natural (voz, gesto, escritura, etc.) en coordinación. citeturn6search7turn6search11

Dentro de las modalidades, la voz se justifica como mecanismo de accesibilidad y continuidad de flujo porque habilita interacción **hands-free / eyes-free**, reduciendo dependencia de lectura y navegación visual. Revisiones sobre asistentes de voz y VUI sostienen beneficios de interacción manos libres y ojos libres, particularmente en contextos donde la atención se divide con una tarea primaria (p. ej., desplazarse). citeturn3search5turn3search17

En el dominio museístico, se ha documentado el co-diseño de guías inteligentes por voz orientadas a accesibilidad para visitantes ciegos o con baja visión, subrayando la viabilidad de que instituciones desarrollen o gestionen guías descriptivas interactivas para mejorar experiencia y accesibilidad. citeturn3search0turn3search8

Para MuseIQ, este eje implica dos fundamentos:

- **Fundamento funcional**: la voz permite consulta espontánea (“¿qué significa este símbolo?”, “¿quién fue este personaje?”) sin forzar al visitante a interrumpir la contemplación.  
- **Fundamento técnico general**: la integración de TTS/STT convierte el contenido curatorial en una capa audible y navegable, incrementando accesibilidad potencial y ampliando el espectro de usuarios.

Adicionalmente, la accesibilidad digital requiere criterios verificables. Aunque MuseIQ no se restringe a contenidos web tradicionales, estándares de accesibilidad como las Pautas WCAG 2.2 proporcionan una referencia formal para diseñar interfaces y contenidos más accesibles (perceptibles, operables, comprensibles y robustos), útil como marco de criterio en sistemas móviles y web asociados a servicios culturales. citeturn1search3turn1search7turn1search11

#### 6.1.7 Smartphone como interfaz principal en guías BYOD

MuseIQ se fundamenta en la adopción del smartphone como interfaz principal bajo un modelo “bring your own device” (BYOD). La lógica de ingeniería es que el smartphone integra sensores (acelerómetro, magnetómetro, proximidad), conectividad (Bluetooth), capacidades multimedia (audio, micrófono) y familiaridad de uso; y además desplaza inversión desde la institución hacia el dispositivo ya disponible en el visitante, reduciendo costos y logística (distribución, desinfección, pérdidas de dispositivos dedicados).

Evidencia reciente sobre guías móviles en museos (en un análisis de aplicaciones BYOD en museos de alta visitación) muestra que la guía móvil constituye una estrategia vigente y que su continuidad se ha visto influida por condiciones recientes que incrementaron interés en recorridos auto-guiados. citeturn3search3

En el plano técnico, el smartphone es también una plataforma robusta para inferir orientación y movimiento. La documentación oficial de Android describe, por ejemplo, la determinación de orientación del dispositivo combinando sensores como acelerómetro y geomagnético, así como el uso de sensores de proximidad. Esto sustenta la viabilidad de usar sensores del smartphone como apoyo a la orientación y al contexto espacial, complementando la proximidad BLE sin demandar infraestructura adicional. citeturn3search2turn3search6

En el contexto peruano, la viabilidad BYOD no solo depende de la disponibilidad técnica, sino del acceso real: reportes oficiales señalan una alta penetración de smartphones en hogares y un incremento sostenido, lo cual refuerza la pertinencia de diseñar un servicio que se apoye en dispositivos del visitante como estrategia principal. citeturn7search0turn7search4

#### 6.1.8 Recuperación contextual del conocimiento y RAG en dominios museísticos

El componente conversacional de MuseIQ se justifica por la naturaleza del consumo informativo en museos: los visitantes plantean preguntas abiertas, comparativas o explicativas (“¿por qué esta pieza es importante?”, “¿qué técnica se usó?”, “¿cómo se relaciona con otra cultura?”), las cuales son difíciles de resolver con menús rígidos sin elevar fricción.

Sin embargo, implementar IA generativa en patrimonio cultural exige un fundamento técnico orientado al control. El enfoque de *Retrieval-Augmented Generation* (RAG) combina recuperación de fuentes relevantes desde una memoria externa (corpus documental y/o base vectorial) con generación lingüística, con el objetivo de mejorar desempeño en tareas intensivas en conocimiento y reducir dependencia exclusiva de “conocimiento paramétrico” del modelo. El trabajo seminal que formaliza RAG enfatiza que estos modelos pueden generar lenguaje más factual cuando se condicionan en pasajes recuperados, e identifica la provisión de procedencia/provenance como un problema relevante. citeturn2search0turn2search4

En dominios museísticos, el fundamento de RAG es particularmente fuerte por tres motivos:

Primero, el conocimiento relevante es **curatorial y localizado** (por museo, colección y sala), por lo que el desempeño depende de corpus propio (catálogos, fichas técnicas, textos curatoriales, glosarios, guiones de mediación) más que de información general. Segundo, el contenido puede tener sensibilidad histórica, identitaria o política; por tanto, el sistema debe reducir riesgo de “alucinación” (respuestas plausibles pero incorrectas). Tercero, la institución requiere gobernanza del contenido (qué se dice y con qué sustento), demandando trazabilidad.

La literatura reciente sobre alucinación en modelos de lenguaje constata que este fenómeno representa un riesgo estructural para confiabilidad y que se requieren estrategias de mitigación (incluyendo grounding, evaluación, atribución y controles) cuando se despliegan sistemas en entornos donde la exactitud es crítica. citeturn2search1turn2search13

En consecuencia, MuseIQ se sostiene en el principio técnico general de que la IA conversacional debe operar como **capa de interacción** sobre una base de conocimiento curada, no como fuente autónoma de verdad.

#### 6.1.9 Trazabilidad, control de respuesta y responsabilidad en patrimonio cultural

En museos, la información tiene un componente de **confianza pública**: es conocimiento institucional que representa patrimonio natural, cultural y científico. Códigos de ética museal establecen deberes de custodia (*stewardship*) que incluyen documentación, accesibilidad y responsabilidad, reforzando que la institución debe mantener integridad y trazabilidad en su relación con el público. citeturn5search0turn5search12

En sistemas con IA generativa, la trazabilidad se vuelve un requerimiento funcional clave: no basta con “responder”, sino que se debe poder justificar **de dónde proviene** la respuesta y bajo qué fuentes se construyó. Marcos institucionales de referencia en ética y gestión de riesgos de IA sostienen que propiedades como transparencia, explicabilidad, responsabilidad, y auditabilidad/traceability son críticas para sistemas confiables y para protección de derechos. La Recomendación sobre Ética de la IA de entity["organization","UNESCO","un agency"] menciona explícitamente mecanismos de auditoría y trazabilidad; y el marco de gestión de riesgos de entity["organization","NIST","standards agency us"] caracteriza atributos de IA confiable incluyendo responsabilidad y transparencia. citeturn2search2turn2search14turn2search3turn2search7

En el nivel técnico, investigaciones recientes discuten la atribución de fuentes en RAG como mecanismo para aumentar verificabilidad, pero también advierten que “citar” no garantiza fidelidad: pueden existir citaciones post-racionalizadas o divergencias entre contenido citado y contenido generado, lo que implica que la trazabilidad debe diseñarse como propiedad evaluable, no como un adorno de interfaz. citeturn5search14turn5search18turn5search2

Para MuseIQ, este fundamento se concreta en requisitos conceptuales y funcionales:

- **Conceptual**: el patrimonio requiere responsabilidad informativa; por tanto, la IA debe subordinarse a la evidencia curatorial.  
- **Funcional**: el sistema debe permitir al museo controlar corpus, versionamiento y visibilidad de fuentes; y registrar interacciones para auditoría.  
- **Técnico general**: el pipeline conversacional debe habilitar grounding (RAG), mecanismos de atribución y estrategias de mitigación de alucinación.

Como soporte complementario, estándares de representación semántica en patrimonio cultural como CIDOC CRM (modelo conceptual de referencia para integración de información patrimonial) se proponen como fundamento de interoperabilidad y claridad documental, especialmente útil cuando el proyecto busca escalar a múltiples instituciones con estructuras de datos heterogéneas. citeturn5search1turn5search5

#### 6.1.10 Modulación, escalabilidad y bajo costo como principios de ingeniería

MuseIQ se formula para un entorno institucional donde la adopción tecnológica suele estar condicionada por restricciones presupuestales, heterogeneidad de infraestructura y necesidad de mantenimiento sostenible. Por ello, se adoptan tres principios orientadores:

**Modularidad**: capacidad de descomponer el sistema en componentes relativamente independientes (p. ej., módulo de proximidad, módulo de contenidos, módulo conversacional, módulo de voz), lo que reduce acoplamiento, facilita reemplazo tecnológico y acelera evolución.

**Escalabilidad**: capacidad de crecer en (a) número de salas y beacons, (b) cantidad de contenidos, (c) cantidad de usuarios concurrentes, y (d) incorporación de museos adicionales, sin reescritura completa del sistema.

**Bajo costo**: elección de tecnologías y estrategias que minimicen CAPEX/OPEX y costos de operación local, privilegiando infraestructura ligera, uso de dispositivo del visitante y componentes IoT ampliamente disponibles.

Estos principios se relacionan con atributos de calidad de software ampliamente aceptados (mantenibilidad, portabilidad, fiabilidad, eficiencia de desempeño, seguridad, usabilidad) descritos en modelos de calidad como ISO/IEC 25010, que permiten traducir principios generales a criterios evaluables en capítulos de diseño y validación. citeturn5search7turn5search3

En el plano técnico general, la viabilidad de una infraestructura de beacons BLE de bajo costo se sustenta en: (i) la ubicuidad de BLE en smartphones y su perfil de bajo consumo en modo beacon, y (ii) la disponibilidad de microcontroladores integrados con Bluetooth y Wi‑Fi como la familia ESP32, diseñada explícitamente como solución IoT de conectividad integrada. Documentación técnica describe al ESP32 como un chip combinado Wi‑Fi/Bluetooth, orientado a aplicaciones de bajo consumo, versátil y robusto para escenarios diversos. citeturn6search0turn6search8turn6search9

#### 6.1.11 Relación de los fundamentos con el contexto peruano del proyecto

La pertinencia de MuseIQ dentro del contexto peruano puede justificarse desde un enfoque de adecuación tecnológica y social:

Primero, la alta disponibilidad de smartphones —evidenciada por reportes oficiales de penetración en hogares— habilita una estrategia BYOD como base realista de acceso a mediación digital, sin presuponer disponibilidad de dispositivos dedicados por parte de museos. citeturn7search0turn7search4

Segundo, la diversidad institucional del sector museal (museos nacionales, regionales, de sitio y espacios culturales) sugiere que la adopción tecnológica debe tolerar heterogeneidad de conectividad, infraestructura y capacidades de operación. En este marco, el enfoque por reconocimiento de sala/zona y modularidad favorece escalamiento gradual: el museo no requiere instrumentación completa desde el inicio, sino que puede desplegar por etapas (salas prioritarias) sin perder coherencia funcional.

Tercero, el componente de accesibilidad es particularmente relevante: documentos de evaluación institucional del sector cultural reportan metas e indicadores asociados a servicios inclusivos en museos, mostrando que la inclusión es una dimensión de política pública sectorial, aunque aún exista espacio de mejora en cobertura y profundidad. citeturn7search9

Cuarto, el uso de voz y contenidos auditivos se alinea con necesidades de accesibilidad (personas con baja visión, dificultades lectoras, o visitantes que prefieren audio), y se sostiene en evidencia de diseño participativo de guías por voz para mejorar accesibilidad. citeturn3search0turn3search8

Quinto, el tratamiento de datos en una solución que potencialmente registra interacciones (consultas, tiempos de permanencia aproximados o analítica de uso) requiere incorporar desde el diseño principios de protección de datos y cumplimiento normativo local. En entity["country","Perú","country"], la Ley N.° 29733 establece el objeto de garantizar el derecho a la protección de datos personales mediante un tratamiento adecuado; por ello, MuseIQ debe fundarse en minimización de datos, consentimiento informado y seguridad de datos, aspectos que se desarrollarán con mayor formalidad en capítulos de normas y diseño. citeturn7search3turn7search7

### 6.2 Características principales

Las características principales de MuseIQ se derivan directamente de los fundamentos presentados y deben entenderse como propiedades funcionales y técnico-generales del sistema (no como especificación arquitectónica detallada). En conjunto, describen cómo MuseIQ materializa la mediación digital situada mediante una combinación coherente de contexto espacial, interacción multimodal e IA controlada.

#### 6.2.1 Mediación situada por reconocimiento de sala y zona probable de observación

MuseIQ se caracteriza por activar mediación interpretativa según **reconocimiento de sala/zona** usando proximidad BLE y reglas de contextualización. La evidencia en museos con BLE muestra que la identificación de sala puede alcanzar niveles de exactitud altos para habilitar entrega de contenido por ambientes, lo cual valida la elección de diseñar por “zonas interpretativas” más que por coordenadas exactas. citeturn0search2turn4search0turn4search11

Esta característica se traduce en una experiencia donde el visitante recibe (o solicita) contenido pertinente al entorno inmediato, reduciendo búsqueda manual y reforzando el carácter no intrusivo de la guía.

#### 6.2.2 Orientación y apoyo a la navegación interpretativa con sensores del smartphone

MuseIQ incorpora el smartphone como sensor contextual que complementa la proximidad. En particular, el uso de orientación/movimiento permite apoyar dos objetivos: (a) mejorar inferencias de foco cuando hay múltiples piezas cercanas, y (b) habilitar micro-asistencias de recorrido (por ejemplo, reorientar al visitante hacia un punto de interés o confirmar que se desplaza hacia otra sala).

La factibilidad de inferir orientación a partir de sensores del smartphone está sustentada por documentación oficial sobre sensores de posición y movimiento, lo que habilita conceptualizar el smartphone como parte del sistema de localización funcional sin infraestructura adicional. citeturn3search2turn3search6

**Análisis (inferencia de ingeniería):** el valor de la orientación no depende de grados perfectos, sino del incremento marginal en pertinencia contextual: incluso una orientación aproximada puede ayudar a resolver ambigüedades típicas en salas con alta densidad de objetos.

#### 6.2.3 Interacción por voz TTS/STT como capa de accesibilidad y continuidad de flujo

MuseIQ integra TTS/STT como característica central de accesibilidad y de alineación con la dinámica de visita presencial. En términos de HCI, la voz permite interacción eyes-free/hands-free y puede reducir fricción en personas que no quieren o no pueden leer cartelas extensas o navegar menús durante la observación. citeturn3search5turn3search17

En el dominio museal, el diseño y co-diseño de guías por voz dirigidas a visitantes ciegos o con baja visión constituye evidencia directa de pertinencia, mostrando que la voz puede ser un vector de accesibilidad y mejora de experiencia. citeturn3search0turn3search8

Asimismo, aunque MuseIQ no sea una “web” tradicional, adoptar criterios inspirados en estándares de accesibilidad (como WCAG 2.2) aporta una base verificable para diseñar textos, controles, feedback y alternativas de presentación de contenido accesibles. citeturn1search3turn1search11

#### 6.2.4 Asistente conversacional con RAG y respuestas controladas por evidencia

MuseIQ integra una IA conversacional con RAG cuya característica esencial es **responder desde evidencia curada**. RAG se sustenta en la idea de recuperar pasajes relevantes desde un corpus externo y condicionar la generación, mejorando factualidad y facilitando la provisión de procedencia. citeturn2search0turn2search4

La necesidad de RAG en museos se intensifica por el riesgo de alucinación en modelos generativos; por ello, MuseIQ se caracteriza por incorporar grounding y control de fuentes como propiedades funcionales, no como optimización opcional. Revisiones recientes sobre alucinación en LLMs enfatizan la importancia de mitigación en dominios de alta exigencia factual. citeturn2search1turn2search13

#### 6.2.5 Curaduría digital, gobernanza del conocimiento y mantenimiento evolutivo

MuseIQ se fundamenta en la idea de que el conocimiento museístico es **curatorial**: no se debe depender de respuestas genéricas sin control institucional. Por ello, una característica principal debe ser la gobernanza del conocimiento: capacidad de cargar, versionar y mantener el corpus; auditar cambios; y asegurar coherencia interpretativa.

Este enfoque se alinea con principios de confianza pública y documentación presentes en códigos éticos museales, los cuales enfatizan la responsabilidad del museo en documentación y accesibilidad. citeturn5search0turn5search12

Adicionalmente, si se busca escalamiento a más de una institución, es deseable sostener el conocimiento con estructuras interoperables. En esa línea, CIDOC CRM se reconoce como herramienta para integración de información patrimonial, útil como fundamento para futuras extensiones semánticas, sin imponer en este capítulo una implementación específica. citeturn5search1turn5search5

#### 6.2.6 Arquitecturabilidad: modularidad, escalabilidad y operación de bajo costo

MuseIQ se caracteriza por diseñarse como sistema **arquitecturable** (capaz de evolucionar sin rediseños disruptivos), gracias a modularidad y escalabilidad. Desde el punto de vista de calidad, esto se traduce en atributos como mantenibilidad, portabilidad y fiabilidad, los cuales pueden formalizarse bajo modelos como ISO/IEC 25010 en capítulos de diseño y evaluación. citeturn5search7turn5search3

En términos operativos, el bajo costo se apoya en BLE y microcontroladores IoT disponibles, así como en el uso del smartphone del visitante. Documentación técnica respalda que ESP32 integra conectividad Bluetooth y Wi‑Fi para aplicaciones IoT, y documentación de industria sobre beacons BLE subraya su adecuación por consumo reducido y ecosistema existente en smartphones. citeturn6search0turn6search8turn6search9

#### 6.2.7 Confiabilidad operativa: tolerancia a variabilidad indoor, conectividad y contexto real

Una característica transversal de MuseIQ es la confiabilidad bajo condiciones reales de interiores: variabilidad de señal, densidad de visitantes, obstáculos y cambios en la instalación. La literatura sobre BLE indoor reconoce explícitamente que RSSI es sensible a multipath, shadowing e interferencias, por lo que el sistema debe diseñarse para tolerar incertidumbre y operar por clasificación robusta (sala/zona) más que por estimación métrica frágil. citeturn1search0turn1search14turn1search6

Además, MuseIQ debe asumir condiciones de conectividad variables. Aunque este capítulo no especifica mecanismos (cache, offline-first, balanceo, etc.), el fundamento es que el sistema debe degradar con gracia: si falla una capa (por ejemplo, conectividad del backend), la guía debería mantener funciones mínimas (p. ej., entrega de contenido local básico por sala) para no colapsar la experiencia.

Finalmente, la confiabilidad incluye responsabilidad de IA: los marcos de ética y riesgo enfatizan transparencia, accountability y trazabilidad como condiciones para confianza, especialmente en servicios públicos. citeturn2search3turn2search14turn2search2

## E. Referencias sugeridas o utilizadas

A continuación se listan referencias clave (científicas, revisiones, institucionales y documentación oficial) que sustentan el capítulo. Se sugieren también **claves tipo BibTeX** para facilitar integración posterior.

- Dey, A. K. (2001). *Understanding and Using Context*. Personal and Ubiquitous Computing. (Sugerencia de clave: `Dey2001Context`). citeturn0search1turn0search5turn0search9  
- Falk, J. H., & Dierking, L. D. (2016). *The Museum Experience Revisited*. Routledge. (Clave: `FalkDierking2016MuseumExperience`). citeturn8search8turn0search4  
- Falk, J., & Storksdieck, M. (2005). Using the Contextual Model of Learning to understand visitor learning… *Science Education*. (Clave: `FalkStorksdieck2005CML`). citeturn8search0  
- Tilden, F. (1957). *Interpreting Our Heritage*. University of North Carolina Press. (Clave: `Tilden1957Interpretation`). citeturn8search5turn8search1  
- Li, J., et al. (2024). Systematic review of digital transformation technologies in museum exhibitions. *Computers in Human Behavior*. (Clave: `Li2024DTTMuseums`). citeturn8search18turn4search8  
- Michalakis, K., & Caridakis, G. (2022). Context awareness in cultural heritage applications: a survey. *ACM Journal on Computing and Cultural Heritage*. (Clave: `MichalakisCaridakis2022ContextCH`). citeturn8search3turn8search11turn4search18  
- Verde, D., et al. (2023). Indoor Content Delivery Solution for a Museum Based on BLE Beacons. *Sensors (MDPI)*. (Clave: `Verde2023BLEMuseum`). citeturn4search0turn0search2  
- Barsocchi, P., et al. (2021). Detecting Proximity with Bluetooth Low Energy Beacons… (proximity detection). (Clave: `Barsocchi2021BLEProximity`). citeturn4search6  
- Spachos, P., & Plataniotis, K. N. (2020). BLE Beacons for Indoor Positioning at an Interactive IoT-Based Smart Museum. (Clave: `SpachosPlataniotis2020SmartMuseum`). citeturn4search9turn0search10  
- Zafari, F., Gkelias, A., & Leung, K. K. (2017/2019). *A Survey of Indoor Localization Systems and Technologies*. (Clave: `Zafari2017IndoorSurvey`). citeturn1search0  
- Schmidtke, H. R., et al. (2020). Location-aware systems or location-based services: a survey… (incluye ubicación simbólica vs física). (Clave: `Schmidtke2020LocationSurvey`). citeturn1search1  
- Wang, X. (2024). Co-design of a Voice-Driven Interactive Smart Guide for Museum Accessibility and Management. (Clave: `Wang2024VoiceGuideMuseum`). citeturn3search0turn3search8  
- Deshmukh, A. M., et al. (2024). User Experience and Usability of Voice User Interfaces: A Systematic Literature Review. (Clave: `Deshmukh2024VUI_SLR`). citeturn3search17turn3search1  
- W3C (2023–2024). *Web Content Accessibility Guidelines (WCAG) 2.2*. (Clave: `W3CWCAG22`). citeturn1search3turn1search7turn1search11  
- ISO (2019). ISO 9241-210: Human-centred design for interactive systems. (Clave: `ISO9241_210_2019`). citeturn6search2turn6search18  
- Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (NeurIPS). (Clave: `Lewis2020RAG`). citeturn2search4turn2search0  
- Huang, L., et al. (2025). A Survey on Hallucination in Large Language Models. (Clave: `Huang2025HallucinationSurvey`). citeturn2search1  
- UNESCO (2021). Recommendation on the Ethics of Artificial Intelligence. (Clave: `UNESCO2021EthicsAI`). citeturn2search2turn2search14turn2search10  
- NIST (2023). AI Risk Management Framework (AI RMF 1.0). (Clave: `NIST2023AIRMF`). citeturn2search3turn2search7  
- ICOM (2013). ICOM Code of Ethics for Museums. (Clave: `ICOM2013CodeEthics`). citeturn5search0turn5search12  
- CIDOC CRM (sitio oficial). Conceptual Reference Model para patrimonio cultural. (Clave: `CIDOC_CRM`). citeturn5search1  
- Bekiari, C., et al. (SmallMuseums). CIDOC CRM y documentación en museos pequeños (documento de apoyo). (Clave: `CIDOCSmallMuseums`). citeturn5search5  
- Wallat, J., et al. (2025). Correctness is not Faithfulness in Retrieval Augmented Generation (sobre fidelidad de citaciones). (Clave: `Wallat2025CitationFaithfulness`). citeturn5search14  
- Nematov, I., et al. (2025). Source Attribution in Retrieval-Augmented Generation (atribución en RAG). (Clave: `Nematov2025RAGAttribution`). citeturn5search2  
- Girolami, M., et al. (2024). Bluetooth dataset for proximity detection in an indoor museum (dataset y contexto). (Clave: `Girolami2024MuseumBLEData`). citeturn4search17  
- Espressif Systems. ESP32 Series Datasheet. (Clave: `EspressifESP32Datasheet`). citeturn6search0turn6search8  
- Android Developers. Sensors and location (position/motion sensors). (Clave: `AndroidSensorsDocs`). citeturn3search2turn3search6  
- OSIPTEL (2024 data; publicación 2025). ERESTEL: hogares con smartphone. (Clave: `OSIPTELERESTEL2024`). citeturn7search0turn7search4  
- Ministerio de Cultura (Perú). Estadística de visitantes / información sectorial. (Clave: `MINCULVisitantes`). citeturn7search1turn7search2  
- Congreso de la República (Perú). Ley N.° 29733 (Protección de Datos Personales). (Clave: `PeruLey29733`). citeturn7search3turn7search7  

## F. aspectos que convendría desarrollar después en capítulos técnicos

A partir de los fundamentos establecidos, los capítulos técnicos posteriores deberían desarrollar con mayor detalle (sin duplicar este capítulo) los siguientes puntos, como continuidad lógica de una tesis de ingeniería aplicada:

1. **Modelo de datos y corpus museístico para RAG**: estructura de fichas curatoriales, taxonomías, metadatos mínimos, criterios de chunking, versionamiento, y estrategia de actualización; evaluación de interoperabilidad (p. ej., mapeos parciales a CIDOC CRM cuando sea pertinente). citeturn5search1turn2search4  

2. **Diseño del pipeline de RAG con control**: recuperación (vectorial/híbrida), reranking, *guardrails* de contenido, políticas de respuesta (cuándo abstenerse, cuándo pedir aclaración), formato de respuesta con evidencia, y evaluación de “fidelidad de citas” además de exactitud. citeturn5search14turn5search2turn2search1  

3. **Estrategia de trazabilidad y auditoría**: registro de consultas, fuentes citadas, versión del corpus, versión del modelo, decisiones de filtrado; criterios de auditoría alineados con marcos de transparencia y accountability. citeturn2search14turn2search3turn5search0  

4. **Diseño de localización por sala/zona**: metodología de despliegue de beacons, densidad por sala, calibración inicial, umbrales RSSI por zona, tratamiento de ambigüedad cuando hay detección múltiple, y métricas de desempeño centradas en “activación correcta de contenido” más que error en metros. citeturn4search0turn1search0turn4search6  

5. **Integración de sensores del smartphone**: fusión lógica (no necesariamente matemática compleja) entre proximidad BLE y orientación/movimiento para resolver ambigüedades; consumo energético y experiencia de usuario; pruebas en condiciones reales con diversidad de dispositivos. citeturn3search2turn3search6turn1search6  

6. **Diseño de interacción multimodal**: flujos específicos de voz (STT/TTS), manejo de errores (reconocimiento imperfecto), accesibilidad (tamaño tipográfico, contrastes, alternativas), y evaluación con métodos/heurísticas de VUI. citeturn3search17turn1search3turn3search0  

7. **Arquitectura de software y despliegue**: diagrama de bloques, módulos, integración backend, consideraciones de escalabilidad (múltiples museos), operación en conectividad variable, y estrategia de mantenimiento. Vincular decisiones a atributos de calidad (ISO/IEC 25010) y a diseño centrado en humanos (ISO 9241-210). citeturn5search7turn6search2turn2search3  

8. **Privacidad y cumplimiento normativo**: definición explícita de datos personales tratados, consentimiento, minimización, seguridad, periodos de retención, y medidas acordes a la Ley 29733, especialmente si se incluyen analíticas o perfiles. citeturn7search3turn2search3
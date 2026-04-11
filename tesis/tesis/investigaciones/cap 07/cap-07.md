# Tecnologías base para MuseIQ

## A. Título sugerido del capítulo

**CAPÍTULO 7: TECNOLOGÍAS BASE DEL PROYECTO (MuseIQ)**. fileciteturn0file0

## B. Justificación breve del papel del capítulo dentro de la tesis

Este capítulo cumple una función de **bisagra** entre (i) los **fundamentos conceptuales y técnicos** ya establecidos en el avance hasta el Capítulo 6 —donde MuseIQ se sustenta como una propuesta de *mediación situada*, con *localización funcional* (sala/zona) y con *interacción multimodal* y *trazabilidad del conocimiento*— y (ii) los capítulos posteriores orientados al **diseño de datos**, **diseño/arquitectura** e **implementación y despliegue**. fileciteturn0file0

Desde el punto de vista metodológico, el contenido se alinea con la exigencia académica de **identificar y describir las tecnologías o teorías novedosas a aplicar**, justificando su elección y explicitando su impacto en la solución, sin convertir el capítulo en manual ni adelantarse al nivel de especificación propio de los capítulos de diseño, integración e implementación. fileciteturn0file1

## C. Propuesta de estructura del capítulo con numeración tipo tesis

La siguiente estructura preserva la lógica solicitada (primero *percepción/contexto*, luego *interacción*, luego *inteligencia y conocimiento*, y finalmente *integración*), enfatizando además criterios de costo, escalabilidad y viabilidad técnica:

**7.1 Tecnologías de localización y contexto**  
7.1.1 Bluetooth Low Energy (BLE) como base de proximidad  
7.1.2 Beacons y su implementación con ESP32  
7.1.3 RSSI y reconocimiento funcional por sala o zona  
7.1.4 Sensores del smartphone para orientación y contexto  
7.1.5 Restricciones operativas en entornos reales (interferencia, heterogeneidad, energía)

**7.2 Tecnologías de interacción con el visitante**  
7.2.1 Smartphone como plataforma base (BYOD)  
7.2.2 Tecnologías de voz: TTS y STT  
7.2.3 Interacción multimodal en visita museística (texto–audio–voz–contexto)

**7.3 Tecnologías de inteligencia y conocimiento**  
7.3.1 Modelos de lenguaje y capacidad conversacional  
7.3.2 Recuperación aumentada de información (RAG)  
7.3.3 Corpus curatorial, representación del conocimiento y control de respuestas  
7.3.4 Riesgos: alucinación, privacidad, seguridad y gobernanza del contenido

**7.4 Integración tecnológica en MuseIQ**  
7.4.1 Relación entre capas tecnológicas (contexto–interacción–inteligencia)  
7.4.2 Pertinencia de la combinación tecnológica elegida  
7.4.3 Implicancias para capítulos posteriores de datos, diseño e implementación

## D. Desarrollo extenso del contenido en redacción académica, listo para adaptar a LaTeX

El Capítulo 6 estableció que MuseIQ no persigue una localización geométrica de alta precisión, sino una **localización funcional**: identificar con confiabilidad suficiente la **sala o zona probable de observación** para activar mediación cultural contextual, sosteniendo costos y mantenimiento compatibles con instituciones con recursos limitados. fileciteturn0file0 Sobre esa base, el presente capítulo responde a la pregunta **“¿qué tecnologías sostienen MuseIQ y por qué son adecuadas?”** especificando las tecnologías habilitadoras, describiendo su funcionamiento general, su pertinencia para el proyecto, y sus ventajas y limitaciones bajo criterios de viabilidad técnica, costo, escalabilidad y mantenimiento. fileciteturn0file1turn0file0

**7.1 Tecnologías de localización y contexto**

**7.1.1 Bluetooth Low Energy (BLE) como base de proximidad**  
Bluetooth Low Energy (BLE) es una variante de Bluetooth diseñada para comunicaciones inalámbricas de corto alcance con **bajo consumo energético**, especialmente adecuada cuando se requiere transmisión intermitente o de baja tasa de datos. La arquitectura de BLE adopta una lógica asimétrica de responsabilidades: dispositivos con mayor disponibilidad energética (por ejemplo, smartphones) pueden asumir tareas más intensivas, mientras que dispositivos de alimentación limitada (por ejemplo, balizas con batería) operan con patrones de transmisión ligeros, contribuyendo al carácter “low power” del ecosistema BLE. citeturn12view1turn9view0

En términos funcionales, BLE ofrece modos **con conexión** y **sin conexión**. Para servicios de proximidad típicos —como los requeridos por MuseIQ— resulta especialmente relevante la comunicación **connectionless** (sin conexión), que permite **broadcasting** (uno-a-muchos) mediante publicidad (“advertising”) y escaneo (“scanning”). En BLE, “advertising” se define explícitamente como un modo de comunicación sin conexión que puede usarse para transferir datos o para indicar disponibilidad de conexión, siendo el fundamento técnico de las balizas (beacons) que transmiten identificadores o datos de contexto. citeturn12view3turn6view1turn7view0

A nivel físico, BLE opera en la banda ISM de 2.4 GHz y divide el espectro en **40 canales**; clásicamente, **tres canales** (37, 38, 39) se reservan para paquetes de advertising, mientras el resto se usa para intercambio de datos en conexiones. Esta estructura es altamente pertinente para museos: (i) facilita despliegues de proximidad por broadcast, (ii) reduce complejidad de infraestructura, y (iii) habilita un patrón de operación robusto para activar contenidos por sala o zona sin requerir sincronización fina ni hardware dedicado de alto costo. citeturn9view0turn7view0turn12view0

La adecuación de BLE para MuseIQ, por tanto, se fundamenta en una relación costo–beneficio consistente con la localización funcional: BLE permite inferir **cercanía relativa** y reconocer **contextos espaciales discretos** (sala/zona) mediante intensidades de señal y patrones de recepción, con despliegue incremental de balizas y mantenimiento razonable. La evidencia empírica en entornos museísticos reales refuerza esta pertinencia, al mostrar que BLE con RSSI puede sostener entrega de contenidos contextuales a escala de sala en escenarios operativos. citeturn6view8

Como limitación, el comportamiento radioeléctrico en interiores introduce incertidumbre: reflexiones y multi-trayectoria (multipath), presencia de personas, obstáculos y variabilidad entre receptores afectan la estabilidad de mediciones y, por ende, la precisión de inferencias basadas en señal. Estas limitaciones no invalidan BLE para MuseIQ, pero sí exigen un enfoque metodológico coherente: (i) privilegiar reconocimiento de sala/zona antes que coordenadas métricas, y (ii) incorporar filtrado temporal y criterios robustos de decisión, aspectos que quedarán formalizados en los capítulos de diseño y validación. citeturn7view0turn7view2turn6view8

**7.1.2 Beacons y su implementación con ESP32**  
Un beacon puede definirse operativamente como un dispositivo que **emite periódicamente paquetes BLE de advertising** con una carga útil (payload) de tamaño reducido —por ejemplo, identificadores o metadatos— de modo que otros dispositivos (típicamente smartphones) puedan detectarlo mediante escaneo. En localización indoor basada en fingerprinting o proximidad, la recepción de advertising y su intensidad (RSS/RSSI) se emplea para construir firmas o señales útiles para inferencia de ubicación. citeturn7view0turn12view0turn6view1

La elección de **ESP32** como plataforma de beacon se justifica por criterios de integración, disponibilidad y escalabilidad. El ESP32 se describe como un SoC (system-on-chip) con conectividad Wi‑Fi y Bluetooth; específicamente, integra controladores Bluetooth (BR/EDR) y Bluetooth LE, soporte de múltiples conexiones y capacidades como **advertising y scanning simultáneos**, lo cual simplifica prototipado y despliegue de balizas y pruebas de campo. citeturn14view0turn14view2 Asimismo, incorpora mecanismos de gestión energética y modos de baja potencia (p. ej., deep-sleep con memoria RTC y coprocesador ULP), relevantes para diseñar balizas con consumo controlado y mantenimiento predecible (batería/energía). citeturn14view3turn6view3

Desde la perspectiva de ingeniería de firmware, la documentación oficial de ESP-IDF incluye guías específicas sobre BLE que explican el proceso de descubrimiento por advertising/scanning y proveen ejemplos como **NimBLE_Beacon**, lo que reduce barreras de implementación y refuerza la viabilidad técnica del stack seleccionado. citeturn7view3turn0search9 Además, el repositorio oficial de ESP-IDF incorpora ejemplos que demuestran advertising compatible con perfiles de proximidad ampliamente usados, como iBeacon, evidenciando que ESP32 puede configurarse para emitir tramas beacon interoperables con aplicaciones móviles típicas. citeturn7view4turn0search13

La pertinencia de beacons con ESP32 en MuseIQ es doble. En primer lugar, permite instalar una infraestructura mínima por sala o zona (balizas por ambiente o puntos clave) para habilitar mediación situada, consistente con el objetivo de reconocer sala/zona y activar contenidos curatoriales pertinentes. En segundo lugar, la elección facilita el escalamiento por fases: añadir balizas y ajustar parámetros de advertising (intervalo, potencia) conforme se amplía cobertura, sin rediseñar el sistema completo. Este enfoque es congruente con criterios de modularidad y despliegue progresivo discutidos en el avance de la tesis. fileciteturn0file0

Como limitaciones principales, el uso de microcontroladores como beacons introduce desafíos de mantenimiento (energía/batería, reemplazo físico), configuración inicial (potencia/intervalos) y control de consistencia (evitar colisiones y saturación radioeléctrica). Aun así, estos riesgos son gestionables en un esquema de localización funcional: la meta no es el tracking continuo de alta resolución, sino la activación contextual confiable dentro de márgenes operativos razonables. citeturn7view0turn9view0

**7.1.3 RSSI y reconocimiento funcional por sala o zona**  
El Received Signal Strength Indicator (RSSI) se usa como indicador de potencia de señal recibida y, en BLE de proximidad, suele emplearse para inferir cercanía relativa o establecer reglas de decisión (por ejemplo, “beacon dominante” o “zona probable”). Sin embargo, RSSI no constituye una medición absoluta estándar y puede variar en su escala e interpretación entre chipsets y plataformas. En términos prácticos, esto significa que el valor absoluto de RSSI puede ser menos útil que su **tendencia**, su comparación relativa entre emisores, o su integración en esquemas de muestreo/filtrado. citeturn13view0turn7view0

En localización en interiores, el RSSI presenta variaciones por factores de propagación compleja: desvanecimiento rápido (fast fading), multi-trayectoria, orientación del receptor y cambios dinámicos del entorno (como flujo de visitantes). Estudios de fingerprinting BLE describen explícitamente la complejidad de la propagación indoor y la susceptibilidad de BLE a fenómenos de fading; también sostienen que las tramas de advertising son la base natural para posicionamiento oportunista por su carácter de broadcast y por el uso de fuerza de señal como firma por ubicación. citeturn7view0 Revisiones recientes sobre localización indoor con Bluetooth enfatizan asimismo que el ancho de banda efectivo de BLE limita la separación de trayectorias y que el multipath impacta negativamente la precisión, problema inevitable cuando se intenta incrementar exactitud. citeturn7view2

En MuseIQ, el valor del RSSI no se explota para estimar distancia métrica precisa, sino para **reconocimiento funcional**: determinar sala o zona como variable de contexto para mediación. Esta traducción metodológica alinea tecnología con propósito: dado que la narrativa museográfica se organiza por salas, módulos o ejes, el reconocimiento por sala resulta una granularidad operativa suficiente, más económica y mantenible que infraestructuras orientadas a precisión centimétrica. fileciteturn0file0 En ese marco, la evidencia en museos reales muestra que sistemas BLE basados en RSSI pueden habilitar entrega de contenidos contextuales y validarse en condiciones de campo, como ilustra el estudio aplicado en un museo real (Foz Côa Museum) donde se propone una solución BLE+RSSI para localización y entrega de contenido. citeturn6view8turn1search2

La decisión tecnológica, por tanto, se justifica por cuatro razones: (i) disponibilidad de RSSI a través de APIs móviles estándar y sin hardware adicional, (ii) costo reducido al usar beacons y smartphones, (iii) escalabilidad incremental por ambientes, y (iv) compatibilidad con estrategias de filtrado y clasificación robustas. A nivel de ingeniería, el sistema puede operar mediante ventanas de observación de RSSI, filtros temporales y reglas de decisión orientadas a estabilidad (por ejemplo, considerar persistencia del beacon dominante), evitando depender de valores instantáneos. Estas decisiones técnicas se desarrollarán formalmente en los capítulos de datos y diseño. citeturn13view0turn11view0

Las limitaciones clave del RSSI para MuseIQ se sintetizan en: heterogeneidad de teléfonos (distintos receptores generan RSSI no comparables en términos absolutos), sensibilidad al cuerpo humano y a la orientación del dispositivo, interferencias en 2.4 GHz, y necesidad de muestreo suficiente para reducir “falsos cambios” de sala. Estas limitaciones no contradicen el enfoque MuseIQ; al contrario, refuerzan la decisión de localización funcional y la necesidad de fusionar RSSI con otros indicadores de contexto (sensores del smartphone y estructura curatorial). citeturn13view0turn7view0turn7view5

**7.1.4 Sensores del smartphone para orientación y contexto**  
El smartphone, además de ser interfaz de interacción, actúa como **plataforma sensorial**. En MuseIQ, los sensores no se incorporan para construir un sistema de navegación milimétrica, sino para enriquecer el contexto con variables útiles de mediación: orientación aproximada del dispositivo, cambios de postura/movimiento y señales de interacción implícita (por ejemplo, si el visitante se detiene o gira). Esta lógica es consistente con el avance de tesis: los sensores complementan la señal BLE para reforzar activación contextual de contenidos. fileciteturn0file0

En Android (referencia pertinente por la disponibilidad masiva de dispositivos), la documentación oficial describe cómo computar orientación combinando lecturas del acelerómetro y del sensor geomagnético (magnetómetro), construyendo una matriz de rotación y derivando ángulos de orientación (azimuth, pitch, roll). Esta capacidad técnica habilita que MuseIQ estime dirección relativa del dispositivo para mejorar la pertinencia del contenido, por ejemplo, privilegiando piezas cercanas al frente o confirmando que el usuario se orienta hacia una zona de exhibición. citeturn7view5turn0search2

Desde el punto de vista funcional, el aporte de sensores se entiende como **reducción de ambigüedad contextual**. BLE puede sugerir “sala probable”, pero no necesariamente “foco de observación” dentro de la sala; la orientación del dispositivo, aunque imperfecta, puede apoyar decisiones como: (i) activar una explicación de un objeto cercano, (ii) seleccionar subtemas curatoriales relacionados con el módulo hacia el cual se dirige el visitante, o (iii) ajustar el modo de interacción (texto vs. voz) según dinámica del recorrido. citeturn7view5turn11view0

Las limitaciones de sensores móviles incluyen ruido, drift y susceptibilidad a condiciones físicas (campos magnéticos perturbados en interiores, variabilidad de calibración, interferencias). En consecuencia, su papel en MuseIQ debe ser auxiliar y probabilístico: aportar señales que complementen RSSI, no reemplazar el reconocimiento por sala. Dicho de otro modo, los sensores fortalecen un enfoque de fusión de contexto “suficiente” para mediación, pero no garantizan exactitud geométrica. Esta delimitación preserva viabilidad técnica y reduce riesgo de sobreprometer precisión. citeturn7view5turn7view0

**7.1.5 Restricciones operativas en entornos reales**  
Todo sistema indoor basado en radio enfrenta condiciones de campo: variabilidad temporal (densidad de personas), cambios en disposición museográfica, coexistencia con Wi‑Fi en 2.4 GHz, y heterogeneidad de receptores. La literatura de fingerprinting BLE subraya que el muestreo y filtrado son necesarios para mitigar efectos como fast fading y “smearing” cuando el usuario está en movimiento, lo cual afecta la estabilidad de firmas por ubicación si la tasa de observación es insuficiente o si se toman decisiones con ventanas demasiado pequeñas. citeturn7view0

A ello se suman restricciones de plataforma móvil relevantes para viabilidad: en Android, el escaneo BLE es una actividad intensiva en batería, por lo que se recomienda detener escaneo cuando se logra el objetivo, evitar bucles de escaneo y establecer límites temporales; adicionalmente, desde Android 12 se requieren permisos explícitos (p. ej., BLUETOOTH_SCAN) con prácticas de compatibilidad para versiones previas. citeturn11view0turn6view4 Este conjunto de restricciones no invalida el enfoque, pero condiciona decisiones de ingeniería que MuseIQ debe adoptar: escaneo intermitente, uso con el app en primer plano durante la visita, y diseño de flujo de usuario que facilite permisos sin fricción excesiva. citeturn6view5turn6view4

---

**7.2 Tecnologías de interacción con el visitante**

**7.2.1 Smartphone como plataforma base (BYOD)**  
MuseIQ adopta una estrategia **Bring Your Own Device (BYOD)**: el visitante utiliza su propio teléfono como interfaz, lo cual reduce costos de hardware dedicado (audioguías físicas) y habilita escalabilidad sin logística de préstamo, limpieza, mantenimiento y reposición por institución. Esta decisión ya fue sustentada en el avance de tesis como un fundamento técnico-económico: el smartphone integra conectividad Bluetooth, sensores, micrófono y audio, y permite ejecutar la capa de interacción de forma suficiente para una guía contextual; además, fortalece viabilidad institucional en contextos de restricción presupuestal. fileciteturn0file0

Desde la base tecnológica, BYOD implica seleccionar un enfoque de desarrollo compatible con BLE, sensores y voz. Aunque existen alternativas web (por ejemplo, Web Bluetooth), la documentación técnica advierte que el Web Bluetooth API tiene **disponibilidad limitada** y se recomienda revisar compatibilidad antes de uso en producción; además, el estándar se mantiene en el ámbito de un grupo comunitario y no en una especificación W3C en “standards track”. citeturn5search14turn5search29turn5search10 En consecuencia, cuando BLE es un pilar del sistema (como en MuseIQ), un enfoque de aplicación móvil (nativa o híbrida con acceso a APIs nativas) se vuelve más coherente como base tecnológica, especialmente si se busca cobertura transversal de dispositivos y control del ciclo de permisos, sensores y audio. citeturn6view4turn11view0

Una implicancia adicional de BYOD es la heterogeneidad: distintos modelos y versiones de sistema operativo pueden variar en sensibilidad BLE, desempeño de sensores y calidad de micrófono. Esta limitación se gestiona por diseño: MuseIQ privilegia decisiones robustas (sala/zona) y flujos de interacción que toleren incertidumbre (por ejemplo, confirmación contextual mediante UI/voz). Esa aproximación es consistente con la localización funcional y con la tolerancia a condiciones reales mencionada en el avance de tesis. fileciteturn0file0

**7.2.2 Tecnologías de voz: TTS y STT**  
La interacción por voz en MuseIQ combina dos tecnologías complementarias. **Text-to-Speech (TTS)** sintetiza voz a partir de texto, permitiendo que el sistema “hable” explicaciones curatoriales o respuestas del asistente. En Android, la clase TextToSpeech se define explícitamente como un componente que **sintetiza habla desde texto** para reproducción inmediata o creación de archivos; su disponibilidad en el sistema operativo permite implementar salida audible sin requerir hardware adicional. citeturn10view0turn6view6

Por su parte, **Speech-to-Text (STT)** permite capturar preguntas del visitante y transformarlas a texto para su procesamiento por la capa conversacional. En Android, SpeechRecognizer provee acceso al servicio de reconocimiento de voz; el propio API advierte que su implementación probablemente transmita audio a servidores remotos y que no está pensado para reconocimiento continuo por consumo de batería y ancho de banda, además de requerir permisos de grabación de audio (RECORD_AUDIO). citeturn10view2turn10view4turn6view7 Estas características definen un marco de uso apropiado para MuseIQ: interacción tipo “push-to-talk” o activación por intención del usuario, minimizando escucha constante y reduciendo costos y riesgos de privacidad. citeturn10view2turn6view5

La pertinencia de voz en museos no es únicamente tecnológica, sino funcional: la evidencia en guías inteligentes con voz sugiere mejoras de accesibilidad y autonomía, particularmente para visitantes ciegos o con baja visión. Un caso documentado describe el co-diseño de una guía descriptiva interactiva por voz para una institución museística/turística, con foco explícito en accesibilidad y experiencia de visita. citeturn6view10turn2search3 En MuseIQ, esta tecnología es además coherente con la premisa de reducir fricción de uso durante el recorrido presencial (mirar el entorno físico más que la pantalla) y con la lógica multimodal ya justificada en el Capítulo 6. fileciteturn0file0

Las limitaciones son claras: la voz es sensible a ruido ambiental, acentos, y condiciones de conectividad si se usa STT remoto. Además, la captura de audio involucra consideraciones éticas y normativas (consentimiento, tratamiento de datos). Por ello, el diseño debe contemplar degradación controlada (modo texto), indicadores de grabación y políticas de privacidad; estos aspectos se articulan naturalmente con capítulos posteriores de normas y de implementación. citeturn10view2turn0file1

**7.2.3 Interacción multimodal en visita museística**  
MuseIQ se sitúa en un paradigma de **interacción multimodal** (BLE + sensores + UI + voz), no como acumulación de canales, sino como estrategia para sostener continuidad interpretativa bajo condiciones heterogéneas de usuarios y contextos. La multimodalidad permite que el visitante elija o combine modos (leer, escuchar, preguntar) y que el sistema adapte la entrega según contexto: por ejemplo, activar contenido por sala cuando se detecta proximidad, y permitir consulta libre por voz para profundizar. Esta lógica coincide con el enfoque de mediación situada y accesibilidad expuesto en el avance. fileciteturn0file0

En términos tecnológicos, la multimodalidad también funciona como mecanismo de robustez: cuando BLE tiene ambigüedad (por fluctuación RSSI), la UI puede solicitar confirmación de sala/objeto; cuando el ambiente es ruidoso, la salida puede preferir texto; cuando el visitante no desea leer, TTS puede sostener flujo informativo. En museos, donde no existe una interacción “tipo escritorio”, este acoplamiento entre contexto físico e interacción es precisamente el valor diferencial de una guía inteligente orientada a visita presencial. citeturn6view8turn6view10

---

**7.3 Tecnologías de inteligencia y conocimiento**

**7.3.1 Modelos de lenguaje y capacidad conversacional**  
La capa conversacional de MuseIQ se apoya en modelos de lenguaje modernos capaces de interpretar preguntas abiertas y producir respuestas naturales. La base técnica dominante de estos modelos es la arquitectura **Transformer**, propuesta como un modelo de atención que prescinde de recurrencia y convolución y que demostró ventajas de paralelización y desempeño en tareas de secuencias. citeturn6view11turn3search0 Este fundamento explica por qué los modelos de lenguaje contemporáneos pueden sostener diálogo, generar explicaciones y reformular contenidos, capacidades relevantes para una guía museística interactiva.

Sin embargo, la pertinencia de un modelo conversacional en MuseIQ no se reduce a “usar IA”, sino a **instrumentar una interfaz natural de consulta** sobre contenido curatorial. En un museo, el visitante formula preguntas situadas (“¿qué significa…?”, “¿por qué esta pieza…?”, “¿cuál es la relación con…?”) que no siempre están cubiertas por textos de sala lineales. Un modelo conversacional aporta flexibilidad para responder, siempre que se controle su salida mediante anclaje a fuentes institucionales y restricciones curatoriales. fileciteturn0file0

La principal limitación técnica de modelos generativos es su tendencia a producir texto plausible pero incorrecto (alucinación) o respuestas excesivamente generales cuando la evidencia es insuficiente. La literatura especializada ha sistematizado el problema de alucinaciones en LLMs, proponiendo taxonomías, causas y líneas de mitigación. Esto refuerza que, en dominios patrimoniales, la IA debe operar con mecanismos de grounding y trazabilidad. citeturn6view15turn3search25

**7.3.2 Recuperación aumentada de información (RAG)**  
Retrieval-Augmented Generation (RAG) es un paradigma que integra un modelo generativo con un mecanismo de recuperación sobre una memoria externa (no paramétrica) para mejorar respuestas en tareas intensivas en conocimiento. En su formulación clásica, RAG combina un modelo seq2seq con un índice vectorial denso de documentos (por ejemplo, Wikipedia) y un recuperador neuronal; su objetivo es condicionar la generación a pasajes recuperados, aumentando especificidad y soporte factual. citeturn6view12turn0search3

El valor de RAG para MuseIQ es directo: el museo no necesita “opiniones creativas”, sino mediación basada en **contenido institucional** (fichas, guiones, textos curatoriales, catálogos). RAG permite que, antes de responder, el sistema recupere fragmentos relevantes del **corpus curatorial**, y que el modelo genere una respuesta guiada por ese contexto. Este enfoque es coherente con el fundamento de trazabilidad enfatizado en el avance: la respuesta debe estar anclada a conocimiento recuperado, reduciendo riesgo de errores y facilitando control semántico. fileciteturn0file0turn6view12

Técnicamente, implementar RAG requiere: (i) una estrategia de indexación del corpus (segmentación y representación), (ii) un mecanismo de recuperación (sparse o dense), y (iii) mecanismos de selección/filtrado del contexto que entra al prompt. En recuperación densa, trabajos como Dense Passage Retrieval (DPR) muestran cómo se aprende un recuperador basado en embeddings (dual-encoder) para superar baselines BM25 en tareas de QA abiertas, consolidando el rol de embeddings como base práctica de recuperación semántica. citeturn6view13turn4search0 En la práctica, librerías de búsqueda vectorial como Faiss son relevantes por su foco en eficiencia de búsqueda y clustering de vectores, proponiendo diseños que equilibran restricciones (compresión de vectores, búsqueda no exhaustiva) para escalar indexación y consulta. citeturn6view14turn4search29

Las limitaciones del enfoque RAG en MuseIQ incluyen: dependencia de calidad del corpus (si el corpus no está bien curado, la recuperación no mejora), sensibilidad a la segmentación (fragmentos demasiado grandes o pequeños afectan relevancia), y riesgos de seguridad/privacidad propios de incorporar conocimiento externo al contexto del modelo. Además, el rendimiento percibido por el visitante depende de latencia y disponibilidad de red si el RAG corre en backend. Estas decisiones se profundizarán en capítulos posteriores de datos e implementación, pero su mención aquí es necesaria para justificar por qué RAG se presenta como tecnología base y bajo qué supuestos opera. citeturn6view12turn6view14turn0file1

**7.3.3 Corpus curatorial, representación del conocimiento y control de respuestas**  
El **corpus curatorial** es la fuente de verdad institucional que MuseIQ consulta para responder. Su rol es equivalente al de una “base documental gobernada”: textos de sala, fichas de objeto, guiones educativos, metadatos de colección, y documentos interpretativos. Para que RAG funcione como control de respuestas, el corpus debe estar (i) digitalizado, (ii) versionado, (iii) estructurado con metadatos mínimos (autoridad, sala, periodo, tipo de pieza), y (iv) mantenido bajo prácticas curatoriales.

En el campo del patrimonio cultural, existen modelos y estándares orientados a la integración de información heterogénea. El CIDOC Conceptual Reference Model (CIDOC CRM) se define como una ontología/formalismo para facilitar integración, mediación e intercambio de información de patrimonio cultural; su especificación formal ha sido reconocida como estándar ISO en sucesivas versiones (por ejemplo, ISO 21127). citeturn6view18turn3search10turn3search6 Asimismo, modelos como Europeana Data Model (EDM) proveen especificaciones formales de clases y propiedades para representar y compartir metadatos de objetos culturales en ecosistemas agregadores, reforzando el principio de que el dato cultural requiere estructura y contexto para interoperabilidad. citeturn6view19turn3search3

Para MuseIQ, la relevancia de estos marcos no implica implementar completamente una ontología patrimonial en esta etapa, sino adoptar sus principios: **identificación de entidades**, **relaciones**, **proveniencia**, y **separación entre objeto y representación digital**. Esto habilita control de respuestas en dos niveles: (i) control de recuperación (filtrar por sala/zona, periodo, colección), y (ii) control de generación (citar o referenciar fragmentos recuperados, restringir afirmaciones a lo documentado). Estos mecanismos conectan directamente con el fundamento de trazabilidad y responsabilidad descrito en el avance. fileciteturn0file0

**7.3.4 Riesgos: alucinación, privacidad, seguridad y gobernanza del contenido**  
La incorporación de modelos generativos en mediación patrimonial requiere explicitar riesgos. En primer lugar, la alucinación es un problema ampliamente estudiado; revisiones académicas proponen taxonomías y discuten causas y mitigaciones, lo que sustenta la necesidad de grounding (por ejemplo, RAG) y de políticas de respuesta (rechazo cuando no hay evidencia, o respuestas con incertidumbre). citeturn6view15turn3search25

En segundo lugar, RAG introduce superficies de ataque adicionales: el pipeline de acceso a conocimiento externo abre fronteras de confianza (ingesta del corpus, manipulación de recuperación, explotación del contexto recuperado y exfiltración). Trabajos recientes de seguridad en RAG proponen taxonomías de ataques/defensas y enfatizan que los riesgos pueden ser RAG-introducidos o RAG-amplificados, precisamente porque el contenido recuperado se vuelve parte del *model-visible context* y puede influir la generación. citeturn15view1turn15view2 En línea con ello, se han estudiado riesgos de fuga de privacidad en sistemas RAG, mostrando que la combinación de dataset de recuperación, embeddings, y LLM puede habilitar vectores de filtración o inferencia no deseada si no se aplican controles. citeturn6view16turn4search19

En tercer lugar, desde una perspectiva aplicada, marcos de riesgos de seguridad para LLMs advierten sobre prompt injection y debilidades asociadas a vectores/embeddings, particularmente relevantes cuando se opera con bases vectoriales y recuperación semántica. citeturn6view17turn4search7

Para MuseIQ, estos riesgos se traducen en exigencias de gobernanza tecnológica: políticas de ingestión del corpus, control de fuentes, mecanismos de filtrado y citación, logging/auditoría de respuestas, y diseño de experiencia de usuario que comunique límites del sistema. La tesis ya anticipa la importancia de trazabilidad; aquí se refuerza que dicha trazabilidad no es un “extra”, sino un requisito tecnológico cuando se despliega IA en patrimonio cultural. fileciteturn0file0

---

**7.4 Integración tecnológica en MuseIQ**

**7.4.1 Relación entre capas tecnológicas (contexto–interacción–inteligencia)**  
La propuesta MuseIQ se sostiene por una integración de capas que se refuerzan mutuamente:

La **capa de contexto** (BLE + beacons + RSSI + sensores) estima el estado situacional del visitante: sala probable, proximidad relativa y orientación aproximada. Esta información no se interpreta como coordenadas exactas, sino como variables interpretativas para activar mediación. citeturn6view8turn7view5turn13view0

La **capa de interacción** (BYOD + UI + voz) convierte ese contexto en experiencia usable: notifica contenidos por proximidad, permite consulta libre vía STT, y entrega respuestas por texto y/o TTS según necesidad y accesibilidad. Tecnológicamente, se apoya en APIs móviles que formalizan síntesis (TextToSpeech) y reconocimiento (SpeechRecognizer), con restricciones explícitas sobre permisos y consumo que obligan a un diseño de uso intencional y no invasivo. citeturn10view0turn10view2turn6view4

La **capa de inteligencia** (LLM + RAG + vector search) produce respuestas contextualizadas a partir del corpus curatorial, recuperando evidencia relevante y condicionando generación para reducir alucinación y aumentar trazabilidad. citeturn6view12turn6view14turn6view15

En conjunto, la arquitectura tecnológica se explica por composición funcional: el contexto espacial guía qué parte del corpus es más probable y pertinente; la voz/UI articula la consulta y la respuesta; y el RAG reduce incertidumbre semántica al anclar la generación a documentos curatoriales. citeturn6view8turn6view12

**7.4.2 Pertinencia de la combinación tecnológica elegida**  
La combinación elegida es pertinente por cuatro criterios centrales:

**Costo y despliegue.** BLE broadcasting con beacons es una infraestructura ligera; ESP32 es un SoC integrado con Bluetooth LE, con modos de baja potencia y disponibilidad amplia, facilitando prototipado y escalamiento. citeturn14view2turn14view3turn7view3

**Escalabilidad y mantenimiento.** El sistema escala por incorporación incremental de salas (balizas por ambiente y contenidos por corpus); el mantenimiento se concentra en activos controlados (beacons y backend/corpus) y no en reparto de hardware por visitante, gracias a BYOD. fileciteturn0file0

**Viabilidad técnica basada en estándares.** BLE, APIs Android de sensores y voz, y paradigmas RAG documentados en literatura científica conforman una base tecnológica defendible y replicable. citeturn9view0turn7view5turn10view2turn6view12

**Control y responsabilidad.** El uso de RAG, junto con un corpus curatorial gobernado y potencialmente alineable a estándares patrimoniales (CIDOC CRM/EDM), aborda explícitamente los riesgos de alucinación y de inconsistencias en patrimonio cultural, reforzando trazabilidad. citeturn6view18turn6view19turn6view15turn15view2

**7.4.3 Implicancias para capítulos posteriores de datos, diseño e implementación**  
La selección tecnológica define con claridad qué deben resolver los capítulos siguientes:

En **Diseño de los Datos de Entrada**, será necesario formalizar el esquema de datos del corpus curatorial (segmentación, metadatos, versionado), el mapeo de beacon→sala/zona, y la representación de contexto (variables sensoriales y eventos). citeturn6view12turn7view5turn7view3

En **Diseño y Despliegue**, se deberá especificar arquitectura (móvil–backend–RAG), estrategia de operación de escaneo BLE (ventanas y tiempos), gestión de permisos, y mecanismos de observabilidad (logging, métricas, auditoría). citeturn11view0turn6view4turn15view2

En **Evaluación**, el desempeño se medirá en términos funcionales (exactitud de sala/zona, latencia percibida, satisfacción, accesibilidad), manteniendo coherencia con el objetivo de mediación situada. citeturn6view8turn6view10

Finalmente, en **Normas técnicas**, el proyecto deberá traducir riesgos (voz, datos, IA) en controles: privacidad, seguridad del corpus, mitigación contra prompt injection y políticas de uso de modelos. citeturn6view17turn15view1turn6view16

## E. Referencias sugeridas o utilizadas

Las siguientes referencias son coherentes con el tipo de fuentes requeridas (documentación oficial y literatura científica) y cubren las tecnologías base discutidas:

Bluetooth SIG. *The Bluetooth® Low Energy Primer*. citeturn6view0turn12view1turn12view3  
Bluetooth SIG. *Bluetooth Core Specification — Low Energy Controller / Link Layer Specification (advertising/scanning states)*. citeturn6view1  
Tosi, J., Taffoni, F., Santacatterina, M., Sannino, R., & Formica, D. (2017). *Performance Evaluation of Bluetooth Low Energy: A Systematic Review*. *Sensors*, 17(12), 2898. citeturn9view0  
Faragher, R., & Harle, R. (2015). *Location Fingerprinting With Bluetooth Low Energy Beacons*. *IEEE Journal on Selected Areas in Communications*, 33(11). citeturn7view0  
Verde, D., et al. (2023). *Indoor Content Delivery Solution for a Museum Based on BLE Beacons*. *Sensors*, 23(17), 7403. citeturn6view8turn1search2  
Shi, T., et al. (2024). *A Survey of Bluetooth Indoor Localization*. arXiv. citeturn7view2turn1search5  

Espressif Systems. *ESP32 Series Datasheet* (conectividad y modos de potencia). citeturn6view3turn14view2turn14view3turn14view0  
Espressif Systems. *ESP-IDF BLE Getting Started / Device Discovery (Advertising & Scanning)*. citeturn7view3turn0search1  
Espressif Systems (GitHub oficial). *ESP-IDF iBeacon example (advertising compatible)*. citeturn7view4turn0search13  

Android Developers. *Position sensors: compute device orientation (SensorManager.getRotationMatrix / getOrientation)*. citeturn7view5turn0search2  
Android Developers. *Bluetooth permissions (Android 12+)*. citeturn6view4turn1search3  
Android Developers. *Find BLE devices (scan guidelines; battery-intensive scanning)*. citeturn11view0turn8search29  
Android Developers. *Communicate in the background (BLE)*. citeturn6view5turn1search27  
Android Developers. *TextToSpeech API Reference*. citeturn10view0turn6view6  
Android Developers. *SpeechRecognizer API Reference (permiso RECORD_AUDIO; posible streaming remoto; no continuo)*. citeturn10view2turn10view4turn6view7  

Wang, X. (2024). *Co-design of a Voice-Driven Interactive Smart Guide for Museum Accessibility and Management*. *Journal of Audiovisual Translation*. citeturn6view10turn2search3  

Vaswani, A., et al. (2017). *Attention Is All You Need* (Transformer). NeurIPS / arXiv. citeturn6view11turn3search0  
Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS. citeturn6view12turn0search3  
Karpukhin, V., et al. (2020). *Dense Passage Retrieval for Open-Domain Question Answering*. EMNLP / arXiv. citeturn6view13turn4search0  
Douze, M., et al. (2024). *The Faiss library*. arXiv. citeturn6view14turn4search29  
Huang, L., et al. (2023). *A Survey on Hallucination in Large Language Models*. arXiv. citeturn6view15turn3search25  
Zeng, S., et al. (2024). *Exploring Privacy Issues in Retrieval-Augmented Generation*. Findings of ACL. citeturn6view16turn4search19  
Xu, Y., et al. (2026). *Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions*. arXiv. citeturn15view1turn15view2  
OWASP. *LLM01: Prompt Injection; riesgos asociados y debilidades en sistemas RAG*. citeturn6view17turn4search7  

Doerr, M., et al. *Definition of the CIDOC Conceptual Reference Model (CIDOC CRM)*. citeturn6view18turn3search22  
Europeana. *EDM Documentation / EDM Definition*. citeturn6view19turn3search3  

## F. Aspectos que convendría desarrollar después en capítulos técnicos

Con base en las tecnologías seleccionadas, y sin adelantarse al contenido de diseño/implementación, conviene planificar que los siguientes capítulos técnicos desarrollen con precisión:

En **Capítulo 8 (Diseño de datos de entrada)**: esquema de metadatos del corpus curatorial (mínimos obligatorios para RAG), criterios de segmentación (“chunking”), versionado y trazabilidad; además del modelo de datos beacon→sala→contenido y su sincronización con backend. citeturn6view12turn6view19

En **Capítulo 9 (Diseño y despliegue)**: definición de arquitectura móvil–backend–RAG (componentes y responsabilidades), políticas de escaneo BLE (tiempos, filtros, consumo), estrategia de permisos (Bluetooth y audio), y diseño de degradación (modo sin voz / modo con conectividad limitada). citeturn11view0turn6view4turn10view2

En **Capítulo de implementación/prototipo**: parametrización experimental de beacons (intervalo y potencia), lineamientos de instalación por sala, procedimientos de calibración ligera y evaluación en condiciones reales (densidad de visitantes, cambios museográficos). citeturn7view0turn6view8turn14view3

En **Capítulo de validación**: métricas funcionales (exactitud de sala/zona, estabilidad temporal, latencia de activación, tasa de errores STT en ambiente real), junto con evaluación de accesibilidad y experiencia de usuario en visita. citeturn6view10turn11view0turn10view2

En **Capítulo de normas y seguridad**: política de gobernanza del corpus y controles de seguridad para RAG (protección ante envenenamiento del corpus, inyección indirecta en contexto recuperado, mitigación de fuga de datos), alineadas con riesgos documentados en literatura y marcos de seguridad de LLM. citeturn15view2turn6view16turn6view17
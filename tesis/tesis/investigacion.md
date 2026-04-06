Sí. Tomé como referencia la estructura de **tesis-plantilla.pdf** para replicar la lógica de los capítulos 2 y 3, y la adapté a tu propuesta **MuseIQ**, que actualmente se describe como una app móvil con **BLE + beacons ESP32 + TTS + STT + IA/RAG** orientada a museos y espacios culturales. En la plantilla, el Capítulo 2 se organiza como análisis del panorama actual y el Capítulo 3 como mercado objetivo; además, el archivo base repite por error el rótulo de 3.1/3.2, así que aquí lo normalizo como **3.1 Identificación**, **3.2 Caracterización**, **3.3 Elección** y **3.4 Panorama nacional**.  

A continuación te dejo una **versión redactada, investigada y lista para insertar** en tu tesis.

---

# Capítulo 2

## Análisis del panorama actual de los sistemas de guía virtual inteligente en museos y espacios culturales

### 2.1. Estadísticas actuales

En el contexto peruano, el desarrollo de soluciones digitales para museos resulta pertinente debido a la existencia de una red institucional amplia y con demanda comprobada. El Ministerio de Cultura del Perú administra **56 museos a nivel nacional**, distribuidos en diversas regiones del país, lo que configura un escenario real para la adopción progresiva de herramientas de guía digital, localización y acceso contextual a contenidos culturales. ([Museos][1])

La demanda de visita presencial también es significativa. De acuerdo con el Ministerio de Cultura, en **2024** se registraron **1 790 502 visitas** a los 56 museos administrados por la entidad, mientras que solo cinco de los museos más visitados superaron en conjunto el millón de visitas. Entre ellos destacan el Museo Tumbas Reales de Sipán, el Museo de Sitio Pucllana y el Museo Nacional de Arqueología, Antropología e Historia del Perú. Estas cifras muestran que el mercado museístico peruano no es marginal, sino un entorno con flujo real de usuarios y con necesidad de mejorar su experiencia de atención e interpretación cultural. 

A ello se suma una condición tecnológica favorable para soluciones móviles. En el cuarto trimestre de **2025**, el **60,1 %** de los hogares del país contó con acceso a Internet, y el **89,2 %** de la población usuaria de Internet de 6 y más años accedió a este servicio mediante teléfono celular. En Lima Metropolitana, el uso de Internet alcanzó el **90,3 %**, y el acceso a Internet en hogares llegó al **78,2 %**. Estos datos respaldan la viabilidad de una solución basada en smartphone, como MuseIQ, especialmente para una primera implementación en entornos urbanos y de alta afluencia. ([Gobierno del Perú][2])

Además, la política cultural internacional reconoce el papel estratégico de la transformación digital. UNESCO identifica como uno de los ejes de su informe global sobre políticas culturales el uso de tecnologías digitales para **reducir desigualdades, estimular innovación y ampliar el acceso a la cultura**, lo que refuerza la pertinencia de investigar sistemas inteligentes de mediación cultural dentro de museos y espacios patrimoniales. ([UNESCO][3])

### 2.2. Impacto de la necesidad actual

Los museos y espacios culturales enfrentan hoy una doble exigencia: preservar y difundir el patrimonio, y al mismo tiempo ofrecer experiencias más accesibles, personalizadas e interactivas. La literatura reciente sobre museos inteligentes muestra que los sistemas de posicionamiento en interiores permiten activar **audio guías personalizadas** y contenidos contextuales según la proximidad del visitante a una obra o zona específica, apoyando así el aprendizaje y la participación. Asimismo, las revisiones sistemáticas sobre personalización en museos concluyen que estas estrategias se asocian con mejores resultados de involucramiento, satisfacción y adecuación de la experiencia al perfil del usuario. ([MDPI][4])

La necesidad no es solo funcional, sino también de accesibilidad. Un estudio sobre una guía inteligente controlada por voz para Titanic Belfast señala que este tipo de solución fue concebida específicamente para **mejorar la accesibilidad y la experiencia del visitante**, especialmente en personas ciegas o con baja visión. El mismo trabajo reporta que una guía de este tipo puede ofrecer a los museos una alternativa más asequible y sostenible que las audioguías tradicionales centradas en dispositivos rígidos y poco interactivos. ([JAT Journal][5])

En ese marco, la propuesta MuseIQ responde a una necesidad concreta: pasar de una mediación museográfica estática —basada en cartelas, lectura manual, códigos QR o recorridos no adaptativos— hacia una guía capaz de **detectar ubicación**, **narrar contenido en tiempo real** y **responder preguntas del visitante** de manera conversacional. Tu documento de proyecto ya plantea exactamente esa dirección, al integrar localización por BLE, narración TTS, interacción STT y consulta contextual mediante IA/RAG. 

### 2.3. Casos y referentes relevantes

El panorama actual muestra que la digitalización museística ya está en marcha tanto en Perú como en el exterior, aunque todavía con niveles distintos de profundidad. En el Perú, el Ministerio de Cultura cuenta con la plataforma **Visita Virtual**, así como con páginas de museos que integran recorridos virtuales, recursos 3D y experiencias en línea. También existe la sección de **museos virtuales**, donde se promueven iniciativas como el Museo Caral y otros espacios digitales. Esto evidencia que ya existe una base institucional favorable para continuar evolucionando desde la digitalización informativa hacia la asistencia inteligente durante la visita presencial. ([Visita Virtual - Ministerio de Cultura][6])

En el ámbito académico y aplicado, un caso relevante es el del **Foz Côa Museum** en Portugal, donde se implementó y probó en entorno real una solución de localización en interiores y entrega de contenido basada en **BLE beacons** y RSSI. El estudio demuestra que la combinación de posicionamiento indoor y activación contextual de contenidos ya no es solo conceptual, sino una línea técnicamente validada para museos. ([PMC][7])

En paralelo, el mercado internacional evidencia una transición hacia experiencias móviles, multilingües y personalizadas. **Bloomberg Connects** ofrece guías para más de **1250 museos, galerías y espacios culturales** en una sola app; **Guide-ID** comercializa sistemas de audioguía con gestor de contenidos y analítica de comportamiento de visitantes; y **SmartGuide** promueve soluciones móviles para museos con guías digitales en **30 idiomas**, sin necesidad de hardware dedicado para cada visitante. En el plano investigativo, propuestas recientes ya incorporan asistentes basados en LLM para responder preguntas contextuales sobre objetos museísticos. ([Bloomberg Connects][8])

Estos casos muestran una tendencia clara: el sector se está desplazando desde audioguías unidireccionales hacia sistemas que combinan **movilidad**, **personalización**, **analítica**, **multilingüismo**, **accesibilidad** y, progresivamente, **IA conversacional**. ([Bloomberg Connects][8])

### 2.4. Mercado global

El mercado global de guías digitales para museos no debe entenderse únicamente como venta de audioguías, sino como un ecosistema de soluciones de mediación cultural. Este ecosistema incluye plataformas multiinstitución, apps móviles de recorrido, dispositivos dedicados de audio, herramientas de gestión de contenidos, analítica del comportamiento del visitante y sistemas inteligentes que usan proximidad, visión computacional o asistentes conversacionales. La oferta observada en Bloomberg Connects, Guide-ID y SmartGuide confirma que existe una demanda internacional por soluciones escalables que conecten contenido cultural con experiencias autónomas, móviles y más inmersivas. ([Bloomberg Connects][8])

Al mismo tiempo, la investigación reciente indica que el museo inteligente se está configurando como un entorno donde el análisis de comportamiento del visitante y la entrega personalizada de contenido son componentes centrales. Esto sugiere que el valor ya no reside solo en “digitalizar” una sala, sino en ofrecer una experiencia adaptativa que acompañe al visitante antes, durante y después del recorrido. ([MDPI][9])

Desde esta perspectiva, MuseIQ se ubica en una intersección atractiva dentro del mercado global: combina una infraestructura relativamente accesible —smartphone + beacons BLE— con funciones de alto valor percibido, como guía hablada, activación contextual y preguntas/respuestas basadas en IA. En términos de tesis, esto le da a la propuesta una justificación no solo técnica, sino también de pertinencia de mercado, porque se alinea con una dirección ya visible en la evolución internacional del sector.  ([PMC][7])

---

# Capítulo 3

## Mercado objetivo

### 3.1. Identificación del mercado objetivo

El mercado objetivo de la propuesta está conformado, en primer término, por **museos, museos de sitio, centros de interpretación y espacios culturales con atención presencial al público** que requieren mejorar la experiencia de visita mediante herramientas digitales. Dentro de este universo, los actores con mayor afinidad son aquellos que gestionan recorridos autónomos, reciben visitantes nacionales y extranjeros, desarrollan actividades educativas y necesitan ampliar su capacidad de mediación sin depender exclusivamente de guías humanos en todo momento. ([Museos][1])

En el caso peruano, este mercado incluye principalmente a los museos administrados por el Ministerio de Cultura, pero también puede extenderse a museos municipales, universitarios, privados, lugares de memoria, centros culturales y exposiciones temporales. La amplitud de instituciones listadas por la plataforma oficial de museos y la existencia de museos virtuales y recorridos virtuales muestran que el sector ya reconoce el valor de los canales digitales para difusión y educación. ([Museos][1])

Desde el punto de vista del usuario final, el mercado meta está formado por visitantes que utilizan su teléfono móvil como herramienta cotidiana de acceso a información, orientación y consumo cultural. En Perú, ese supuesto es razonable porque la mayor parte de usuarios de Internet accede mediante celular, lo que hace viable una experiencia de guía basada en dispositivos personales, en lugar de exigir equipamiento exclusivo del museo para cada recorrido. ([Gobierno del Perú][2])

### 3.2. Caracterización del mercado objetivo

El cliente institucional de MuseIQ no es solamente “el museo” como entidad abstracta, sino áreas concretas dentro de la organización: dirección, educación y mediación, atención al visitante, museografía, proyectos digitales o innovación. Estas áreas comparten necesidades comunes: ofrecer información contextualizada, atender mayores volúmenes de público, mantener actualizable el contenido y mejorar indicadores de experiencia sin incrementar de manera proporcional los costos operativos. La propuesta MuseIQ encaja en esa lógica porque su arquitectura busca funcionar sobre dispositivos móviles y beacons BLE, con capacidad de actualización del contenido y respuesta contextual a consultas del visitante. 

En cuanto al perfil de visitantes, la distribución de público en museos peruanos durante 2024 muestra que el segmento **adulto** representa el grupo mayoritario (**57,6 %**), seguido por **niñas y niños** (**25,7 %**) y **estudiantes** (**14,4 %**). Esto indica que el sistema debe servir simultáneamente para turismo cultural, visitas familiares y visitas educativas. En consecuencia, el mercado no demanda una sola interfaz, sino una solución flexible: contenidos narrados, lenguaje comprensible, activación automática por cercanía y potencial adaptación por tipo de usuario o recorrido. 

A nivel funcional, el mercado objetivo valora características que ya son visibles en la oferta internacional: uso en el propio teléfono del visitante, soporte multilingüe, facilidad de actualización de contenidos, posibilidad de conocer rutas o preferencias de visita, y reducción de fricciones operativas asociadas al préstamo y mantenimiento de hardware dedicado. Estas señales de mercado son consistentes con la orientación que muestran plataformas como SmartGuide, Bloomberg Connects y Guide-ID. ([Bloomberg Connects][8])

### 3.3. Elección del mercado objetivo

Para una primera etapa de implementación, el mercado objetivo más adecuado es el de los **museos públicos peruanos de alta o media afluencia, con prioridad inicial en Lima Metropolitana**. Esta elección se justifica por tres razones. Primero, Lima presenta mejores condiciones de conectividad y uso de Internet móvil que facilitan la adopción de una solución basada en smartphone. Segundo, concentra museos con alta visibilidad nacional y flujo constante de visitantes. Tercero, ofrece mayor proximidad logística y académica para pruebas piloto, iteración tecnológica y validación con usuarios reales. ([Gobierno del Perú][2])

Dentro de esta primera priorización, resultan especialmente pertinentes los museos y espacios donde la visita autónoma ya es común o donde existe alta necesidad de reforzar mediación cultural: museos nacionales, museos de sitio, lugares de memoria y recintos con recorridos educativos. La presencia de recorridos virtuales oficiales y catálogos digitales en el ecosistema del Ministerio de Cultura sugiere que estas instituciones ya se encuentran en una fase inicial de digitalización y, por tanto, constituyen un terreno razonable para evolucionar hacia una guía virtual inteligente in situ. ([Visita Virtual - Ministerio de Cultura][6])

Como mercado secundario, y para una fase posterior, pueden considerarse museos regionales, municipales, privados y universitarios, así como exposiciones itinerantes o temporales que necesiten una solución flexible, portable y de rápida configuración. Esta escalabilidad es consistente con el propio enfoque del proyecto MuseIQ, que plantea una arquitectura modular basada en app móvil, localización indoor y contenidos consultables por IA. 

### 3.4. Panorama nacional en museos y espacios culturales

El panorama nacional peruano muestra señales claras de oportunidad. El Ministerio de Cultura no solo administra una red de **56 museos**, sino que también ha consolidado mecanismos para acercar el patrimonio a la ciudadanía, como **Museos Abiertos**, iniciativa que en **2025** alcanzó **234 109 visitantes**, con un crecimiento del **47 %** respecto del año anterior y cerca de **900 actividades culturales gratuitas**. Incluso en una sola jornada, como la edición del 1 de junio de 2025, se registraron **16 384 visitantes** en más de 50 museos. Estas cifras evidencian una base real de usuarios y una política pública activa de acceso cultural. ([Gobierno del Perú][10])

Paralelamente, el país ya cuenta con un ecosistema básico de mediación digital a través de **Visita Virtual**, recorridos 3D, museos virtuales y catálogos en línea. Sin embargo, estas herramientas se orientan principalmente a la consulta remota o a la visualización previa/posterior de contenidos, y no necesariamente resuelven la necesidad de acompañamiento inteligente durante el recorrido físico dentro del museo. Allí es donde surge el espacio de oportunidad para MuseIQ: cubrir la brecha entre digitalización informativa y asistencia contextual en tiempo real. ([Visita Virtual - Ministerio de Cultura][6])

Por tanto, el mercado nacional no parte de cero. Existe infraestructura institucional, flujo de visitantes, creciente cultura digital y una línea de política pública que favorece el acceso y la innovación cultural. Lo que aún falta, y constituye el núcleo de esta propuesta, es una solución que combine **localización indoor**, **narración automática**, **interacción por voz** y **respuestas contextualizadas** dentro del espacio museístico. En ese sentido, MuseIQ no se plantea como una idea aislada, sino como una evolución lógica del proceso de transformación digital que ya atraviesan los museos peruanos. ([Gobierno del Perú][10])

---

Si te sirve, en el siguiente paso te lo convierto en una **versión más formal de tesis**, con estilo más académico, citas numeradas y redacción lista para pegar directamente en Word o LaTeX.

[1]: https://museos.cultura.pe/museos "Museos del Ministerio de Cultura | Museos"
[2]: https://www.gob.pe/institucion/inei/noticias/1371146-el-98-4-de-los-hogares-de-lima-metropolitana-conto-con-telefonia-movil-durante-el-cuarto-trimestre-de-2025 "El 98,4% de los hogares de Lima Metropolitana contó con telefonía móvil  durante el cuarto trimestre de 2025 - Noticias - Instituto Nacional de Estadística e Informática - Plataforma del Estado Peruano"
[3]: https://www.unesco.org/en/culture/global-report "UNESCO Global Report on Cultural Policies | UNESCO"
[4]: https://www.mdpi.com/2220-9964/15/1/33 "Ultra-Wideband System for Museum Visitors Tracking: Towards the Integration of the Positioning System with the Vision Sensors"
[5]: https://jatjournal.org/index.php/jat/article/view/267 "
		Co-design of a Voice-Driven Interactive Smart Guide for Museum Accessibility and Management
							\| Journal of Audiovisual Translation
			"
[6]: https://visitavirtual.cultura.pe/?utm_source=chatgpt.com "Visita Virtual - Ministerio de Cultura"
[7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10490640/ "
            Indoor Content Delivery Solution for a Museum Based on BLE Beacons - PMC
        "
[8]: https://www.bloombergconnects.org/ "Bloomberg Connects"
[9]: https://www.mdpi.com/2073-431X/14/5/191 "Analyzing Visitor Behavior to Enhance Personalized Experiences in Smart Museums: A Systematic Literature Review | MDPI"
[10]: https://www.gob.pe/institucion/cultura/noticias/1309934-museos-abiertos-cerro-un-2025-historico-con-un-crecimiento-del-47-en-visitas-a-nivel-nacional "Museos Abiertos cerró un 2025 histórico con un crecimiento del 47% en visitas a nivel nacional - Noticias - Ministerio de Cultura - Plataforma del Estado Peruano"

Perfecto. Reorganicé la investigación con la estructura que pediste y añadí tablas con la evolución de **smartphones en hogares peruanos** y **visitas a museos administrados por el Ministerio de Cultura**. Para mantener consistencia metodológica, la serie de smartphones usa la **ERESTEL de OSIPTEL**, que reporta **hogares con smartphone** y no usuarios únicos individuales; en museos usé la serie oficial de visitantes de los **56 museos administrados por el Ministerio de Cultura** y el dato base pre-pandemia de 2019 del PESEM sectorial. ([Osiptel][1])

## Contexto

La propuesta **MuseIQ** se ubica en la intersección entre transformación digital, mediación cultural y accesibilidad en museos. En el Perú, el entorno de adopción tecnológica es favorable: la tenencia de smartphones en hogares pasó de **78.0 % en 2019** a **94.8 % en 2024**, y en 2023 ya se reportaban **9 779 068 hogares** con este dispositivo; para 2024, OSIPTEL indicó que eran **más de 10 millones de familias**. Esta expansión convierte al teléfono móvil en una plataforma realista para desplegar guías inteligentes basadas en contexto, proximidad y contenido personalizado. ([Osiptel][1])

### Tabla 1. Evolución de hogares peruanos con smartphone

| Año  |      Indicador oficial | Dato reportado |
| ---- | ---------------------: | -------------: |
| 2019 | Hogares con smartphone |         78.0 % |
| 2021 | Hogares con smartphone |         88.4 % |
| 2022 | Hogares con smartphone |         91.9 % |
| 2023 | Hogares con smartphone |         92.8 % |
| 2024 | Hogares con smartphone |         94.8 % |

**Fuente:** OSIPTEL–ERESTEL 2021, 2022, 2023 y 2024; el valor de 2019 aparece como línea base retrospectiva en la nota oficial de 2023. ([Osiptel][1])

En paralelo, el sector museístico peruano muestra una recuperación clara de la demanda presencial. El PESEM del Sector Cultura reportó **1 956 034 visitas a museos en 2019**; en 2020, la pandemia redujo la cifra a **353 153**. Luego, la recuperación avanzó a **1 067 571** en 2022, **1 543 872** en 2023 y **1 790 502** en 2024. Aunque el nivel de 2024 todavía quedó alrededor de **8.5 % por debajo de 2019**, la tendencia es claramente ascendente y confirma que existe una base de público suficiente para justificar innovación en experiencia de visita. 

### Tabla 2. Evolución de visitas a los museos administrados por el Ministerio de Cultura

| Año  | Visitantes | Observación                                                |
| ---- | ---------: | ---------------------------------------------------------- |
| 2019 |  1 956 034 | Línea base pre-pandemia                                    |
| 2020 |    353 153 | Caída por COVID-19                                         |
| 2022 |  1 067 571 | Recuperación parcial                                       |
| 2023 |  1 543 872 | Recuperación sostenida                                     |
| 2024 |  1 790 502 | Nivel más alto desde la reapertura, aún por debajo de 2019 |

**Fuente:** PESEM 2022–2030 del Sector Cultura; Memoria Anual de Gestión 2020, 2022 y 2023; Reporte de cumplimiento 2024 de la Política Nacional de Cultura al 2030. 

En el plano internacional, UNESCO viene subrayando que las tecnologías digitales están transformando la forma en que las personas **acceden, experimentan y preservan la cultura**, y su Global Report 2025 dedica un capítulo específico al uso de tecnologías digitales para **reducir desigualdades y estimular innovación** en el sector cultural. Esta perspectiva respalda la pertinencia de una solución como MuseIQ, no solo como producto tecnológico, sino como respuesta a una tendencia estructural en la gestión cultural contemporánea. ([UNESCO][2])

## Descripción del Problema

Pese al crecimiento del público y a la alta penetración móvil, muchos museos todavía dependen de mecanismos de mediación estáticos o de baja personalización: cartelas, recorridos lineales, audioguías rígidas o información poco contextualizada. Esto genera varias limitaciones: el visitante no siempre recibe contenido en el momento exacto en que lo necesita, la experiencia no se adapta a su idioma o ritmo de recorrido, y la accesibilidad para personas con discapacidad visual o con necesidades de apoyo auditivo y textual sigue siendo desigual. ([MDPI][3])

En términos operativos, el problema puede formularse así: **los museos requieren una solución de mediación digital capaz de identificar de forma suficientemente confiable la ubicación y la orientación del visitante dentro de una sala, para activar contenido contextual, accesible y actualizable, usando infraestructura de bajo costo y dispositivos ya presentes en la vida cotidiana del público**. Esa formulación responde directamente a las brechas observadas entre la demanda cultural creciente, la digitalización parcial del sector y la necesidad de experiencias más autónomas y personalizadas. ([PMC][4])

## Solución Tecnológica

La solución propuesta por **MuseIQ** consiste en una guía inteligente para museos que combina cuatro componentes: **beacons BLE basados en ESP32**, **sensores del smartphone**, **procesamiento de voz con TTS/STT** y **generación aumentada con recuperación (RAG)**. El objetivo no es alcanzar posicionamiento centimétrico, sino identificar con suficiente robustez la **sala**, la **zona** y la **dirección probable de observación** del visitante para activar contenido útil en tiempo real. ([PMC][4])

Desde el punto de vista técnico, la propuesta se apoya en BLE por su bajo costo y escalabilidad. Un caso real implementado en el **Foz Côa Museum** mostró que una solución museográfica basada en beacons BLE y RSSI logró **96 % de precisión en identificación de sala**, lo que es especialmente relevante para MuseIQ porque valida que la lógica de “reconocimiento por ambiente” es viable aun sin infraestructura costosa. El mismo estudio indica, además, que dos o más beacons por sala pueden ser una configuración práctica según el entorno. ([PMC][4])

La precisión percibida puede mejorarse con la orientación del celular. Android documenta que la orientación del dispositivo puede inferirse usando lecturas del **acelerómetro** y del **sensor de campo geomagnético**, lo que permite estimar hacia dónde apunta el teléfono en el marco de referencia del mundo físico. En MuseIQ, esta información puede combinarse con la proximidad BLE para inferir qué obra o zona está mirando el visitante, haciendo más natural la activación de narraciones, textos o respuestas contextuales. ([Android Developers][5])

La capa de inteligencia se apoya en **RAG**, que AWS define como una técnica para optimizar la salida de un modelo de lenguaje haciendo que consulte una base de conocimiento autorizada antes de responder. En un museo, eso significa que la app no tendría que “inventar” información: podría recuperar datos de fichas curatoriales, catálogos, guiones museográficos y bases institucionales para responder preguntas del visitante con mayor pertinencia y trazabilidad. Complementariamente, el uso de **TTS** y **STT** permite convertir el sistema en una guía hablada e interactiva, útil tanto para accesibilidad como para enriquecer la experiencia del recorrido. ([Amazon Web Services, Inc.][6])

## Referencias a tomar en cuenta

### Tabla 3. Trabajos y referentes clave para MuseIQ

| Referente                                                                                                  | Tipo                        | Aporte principal                                                                             | Relevancia para MuseIQ                                                    |
| ---------------------------------------------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Verde et al. (2023), *Indoor Content Delivery Solution for a Museum Based on BLE Beacons*                  | Artículo científico         | Implementa BLE + RSSI en museo real; reporta 96 % de precisión en identificación de sala     | Valida el uso de BLE para reconocimiento por sala y activación contextual |
| Wang (2024), *Co-design of a Voice-Driven Interactive Smart Guide for Museum Accessibility and Management* | Artículo científico         | Diseña una guía por voz centrada en accesibilidad y experiencia del visitante                | Sustenta TTS/STT y enfoque inclusivo                                      |
| Ivanov y Velkova (2025), *Analyzing Visitor Behavior to Enhance Personalized Experiences in Smart Museums* | Revisión sistemática        | Resume 33 estudios; destaca personalización en tiempo real, IA y location tracking           | Sustenta la lógica de personalización contextual                          |
| Bloomberg Connects                                                                                         | Referente comercial/oficial | Plataforma con más de 1200 instituciones culturales; accesibilidad, tours, guías y analítica | Muestra madurez del mercado y demanda internacional por guías móviles     |

**Fuente:** literatura científica y sitios oficiales consultados. ([PMC][4])

Estos referentes muestran que el problema no está en demostrar si la digitalización museística es relevante, sino en **cómo integrarla** de forma viable, contextual y accesible. La literatura académica aporta validación técnica y funcional; los referentes comerciales prueban que existe un mercado consolidado para experiencias móviles, multilingües y personalizadas. ([PMC][4])

## Estado del Arte

El estado del arte actual en museos inteligentes se mueve en tres direcciones convergentes: **localización indoor**, **personalización basada en comportamiento** y **experiencias accesibles y multimodales**. La revisión sistemática de Ivanov y Velkova encontró que los sistemas de personalización en museos dependen con frecuencia de tecnologías móviles, analítica de comportamiento y seguimiento de posición, mientras que los retos más repetidos son privacidad, escalabilidad y costos de implementación. ([MDPI][3])

En localización indoor, BLE destaca como una opción pragmática frente a alternativas más costosas. El caso del Foz Côa Museum no solo demuestra viabilidad técnica, sino que también confirma algo crucial para el MVP de MuseIQ: **identificar correctamente la sala puede ser más importante que calcular coordenadas exactas**. Esto encaja con la lógica de usar pocos beacons por sala y reforzar el sistema con sensores del smartphone en lugar de perseguir precisión milimétrica desde el inicio. ([PMC][4])

En accesibilidad e interacción, Wang muestra que una guía inteligente controlada por voz puede mejorar la experiencia de visitantes ciegos o con baja visión, y Bloomberg Connects prueba a escala global que las instituciones culturales ya están adoptando guías móviles con audio, texto, captions, transcripciones y herramientas de visita. La diferencia es que MuseIQ agrega una capa más fuerte de **contextualización espacial en sitio** mediante BLE y orientación del dispositivo, junto con una capa conversacional basada en RAG. ([JAT Journal][7])

En ese sentido, el aporte diferencial de MuseIQ puede formularse así: **proponer una arquitectura de guía museográfica inteligente, de bajo costo y orientada al contexto peruano, que combine reconocimiento por sala mediante BLE, inferencia de orientación con sensores móviles y generación de contenido contextual mediante RAG, priorizando accesibilidad, escalabilidad y viabilidad de MVP**. Esa combinación aparece parcialmente en trabajos previos, pero no suele integrarse de forma explícita en una propuesta enfocada a museos peruanos con restricciones reales de infraestructura. ([PMC][4])

## Referencias usadas en formato BibTeX (@misc)

Las siguientes entradas corresponden a las fuentes efectivamente utilizadas en este borrador, adaptadas al formato `@misc` que pediste. ([Osiptel][8])

```bibtex
@misc{osiptel2021smartphone,
  author = {{OSIPTEL}},
  title  = {OSIPTEL: El 88,4 % de los hogares peruanos cuenta con un teléfono inteligente},
  year   = {2022},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://www.osiptel.gob.pe/portal-del-usuario/noticias/osiptel-el-88-4-de-los-hogares-peruanos-cuenta-con-un-telefono-inteligente/}
}

@misc{osiptel2022smartphone,
  author = {{OSIPTEL}},
  title  = {Erestel: el 91.9 % de hogares peruanos cuenta con teléfonos inteligentes o smartphones},
  year   = {2023},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://www.osiptel.gob.pe/portal-del-usuario/noticias/erestel-el-91-9-de-hogares-peruanos-cuenta-con-telefonos-inteligentes-o-smartphones/}
}

@misc{osiptel2023smartphone,
  author = {{OSIPTEL}},
  title  = {ERESTEL: el 92.8 % de las familias peruanas contó con un smartphone en 2023},
  year   = {2024},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://www.osiptel.gob.pe/portal-del-usuario/noticias/erestel-el-92-8-de-las-familias-peruanas-conto-con-un-smartphone-en-2023/}
}

@misc{osiptel2024smartphone,
  author = {{OSIPTEL}},
  title  = {Erestel: El 94.8 % de hogares peruanos cuenta con un smartphone},
  year   = {2025},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://www.osiptel.gob.pe/portal-del-usuario/noticias/erestel-el-94-8-de-hogares-peruanos-cuenta-con-un-smartphone/}
}

@misc{cultura2020memoria,
  author = {{Ministerio de Cultura del Perú}},
  title  = {Memoria Anual de Gestión 2020},
  year   = {2022},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://transparencia.cultura.gob.pe/sites/default/files/transparencia/2022/04/informacion-adicional/memoriaanual2020finalf.pdf}
}

@misc{cultura2022memoria,
  author = {{Ministerio de Cultura del Perú}},
  title  = {Memoria Anual de Gestión 2022},
  year   = {2023},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://transparencia.cultura.gob.pe/sites/default/files/transparencia/2023/06/informacion-adicional/memoriaanual2022vf-040823004f.pdf}
}

@misc{cultura2023memoria,
  author = {{Ministerio de Cultura del Perú}},
  title  = {Memoria Anual 2023},
  year   = {2024},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://transparencia.cultura.gob.pe/sites/default/files/transparencia/2024/06/informes-oficiales/memoriaanual2023culturafinal230524.pdf}
}

@misc{cultura2024reporte,
  author = {{Ministerio de Cultura del Perú}},
  title  = {Reporte de cumplimiento 2024 de la Política Nacional de Cultura al 2030},
  year   = {2025},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://transparencia.cultura.gob.pe/sites/default/files/transparencia/2025/06/informes-de-monitoreo-y-evaluacion-de-los-planes-y-politicas/informe-de-analisis-estrategico/reportedecumplimientopnc2024f.pdf}
}

@misc{culturapesem2021,
  author = {{Ministerio de Cultura del Perú}},
  title  = {Plan Estratégico Sectorial Multianual 2022--2030 - Sector Cultura},
  year   = {2021},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://transparencia.cultura.gob.pe/sites/default/files/transparencia/2021/07/resoluciones-ministeriales/resolucionministerial-000196-2021-dm-anexo.pdf}
}

@misc{verde2023blemuseum,
  author = {Verde, David and Romero, Lu{\'i}s and Faria, Pedro Miguel and Paiva, Sara},
  title  = {Indoor Content Delivery Solution for a Museum Based on BLE Beacons},
  year   = {2023},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://pmc.ncbi.nlm.nih.gov/articles/PMC10490640/}
}

@misc{wang2024voiceguide,
  author = {Wang, Xi},
  title  = {Co-design of a Voice-Driven Interactive Smart Guide for Museum Accessibility and Management},
  year   = {2024},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://jatjournal.org/index.php/jat/article/view/267}
}

@misc{android2026positionsensors,
  author = {{Android Developers}},
  title  = {Sensores de posición},
  year   = {2026},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://developer.android.com/guide/topics/sensors/sensors_position?hl=es-419}
}

@misc{aws2026rag,
  author = {{Amazon Web Services}},
  title  = {What is RAG (Retrieval-Augmented Generation)?},
  year   = {2026},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://aws.amazon.com/what-is/retrieval-augmented-generation/}
}

@misc{ivanov2025smartmuseums,
  author = {Ivanov, Rosen and Velkova, Victoria},
  title  = {Analyzing Visitor Behavior to Enhance Personalized Experiences in Smart Museums: A Systematic Literature Review},
  year   = {2025},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://www.mdpi.com/2073-431X/14/5/191}
}

@misc{bloomberg2025connects,
  author = {{Bloomberg Connects}},
  title  = {Bloomberg Connects},
  year   = {2025},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://www.bloombergconnects.org/}
}

@misc{unesco2025globalreport,
  author = {{UNESCO}},
  title  = {UNESCO Global Report on Cultural Policies | Culture: the Missing SDG},
  year   = {2025},
  note   = {Accedido el 6 de abril de 2026},
  url    = {https://www.unesco.org/en/culture/global-report}
}
```

En tu siguiente mensaje te lo convierto a **LaTeX listo para tu tesis**, con `\section{}` y `\subsection{}` exactamente en ese orden.

[1]: https://www.osiptel.gob.pe/portal-del-usuario/noticias/erestel-el-92-8-de-las-familias-peruanas-conto-con-un-smartphone-en-2023/ "ERESTEL: el 92.8 % de las familias peruanas contó con un smartphone en 2023"
[2]: https://www.unesco.org/en/culture-and-digital-technologies?hub=365&utm_source=chatgpt.com "Culture and Digital Technologies | UNESCO"
[3]: https://www.mdpi.com/2073-431X/14/5/191?utm_source=chatgpt.com "Analyzing Visitor Behavior to Enhance Personalized Experiences in Smart Museums: A Systematic Literature Review | MDPI"
[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10490640/?utm_source=chatgpt.com "Indoor Content Delivery Solution for a Museum Based on BLE Beacons - PMC"
[5]: https://developer.android.com/guide/topics/sensors/sensors_position?hl=es-419&utm_source=chatgpt.com "Sensores de posición  |  Sensors and location  |  Android Developers"
[6]: https://aws.amazon.com/what-is/retrieval-augmented-generation/?utm_source=chatgpt.com "What is RAG? - Retrieval-Augmented Generation AI Explained - AWS"
[7]: https://jatjournal.org/index.php/jat/article/view/267?utm_source=chatgpt.com "Co-design of a Voice-Driven Interactive Smart Guide for Museum Accessibility and Management | Journal of Audiovisual Translation"
[8]: https://www.osiptel.gob.pe/portal-del-usuario/noticias/osiptel-el-88-4-de-los-hogares-peruanos-cuenta-con-un-telefono-inteligente/ "OSIPTEL: El 88,4 % de los hogares peruanos cuenta  con un teléfono inteligente"

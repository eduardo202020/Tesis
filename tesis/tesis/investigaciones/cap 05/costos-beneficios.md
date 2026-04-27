Sí. Para ajustar el **Capítulo 5**, conviene agregar una sección nueva sobre **costos variables de servicios de IA**, porque actualmente el capítulo calcula hardware, instalación, mantenimiento y servicios adicionales, pero reconoce que todavía no incorpora costos variables de voz, IA o conectividad externa. Ese vacío aparece explícitamente en el análisis crítico del capítulo. 

Además, tu capítulo ya está construido sobre un piloto en el **Museo Tumbas Reales de Sipán**, con una arquitectura basada en **21 sensores BLE**, **Raspberry Pi 5** como nodo local y un costo de implementación de **S/ 5 100**.  

## Datos base para el cálculo

Para no usar supuestos débiles, se puede tomar como dato real que el Museo Tumbas Reales de Sipán recibió **191 682 visitantes en 2025** y **181 274 visitantes en 2024**, según el Ministerio de Cultura. ([Gobierno del Perú][1])

Con eso:

| Indicador               |             Valor |
| ----------------------- | ----------------: |
| Visitantes anuales 2025 |           191 682 |
| Promedio mensual        | 15 974 visitantes |
| Promedio diario         |    525 visitantes |

Como no todos los visitantes preguntarán por voz, se recomienda usar escenarios. Para el escenario base, puede asumirse que **20 % de visitantes usa la función de preguntas por voz** y que cada usuario activo genera **4 minutos de audio transcrito** durante su visita.

---

# Texto sugerido para agregar al Capítulo 5

Puedes insertar esto después de **5.5.3 Servicios adicionales** como una nueva subsección:

## 5.5.4. Costos variables por servicios de inteligencia artificial

La operación de MuseIQ no solo depende de costos fijos de hardware, instalación y mantenimiento, sino también de costos variables asociados al uso de servicios de inteligencia artificial. Estos costos se activan principalmente cuando el visitante realiza consultas por voz a través de la aplicación móvil. En ese flujo, la pregunta hablada se convierte primero en texto mediante un servicio STT, luego se vectoriza la consulta para recuperar información relevante del corpus curatorial y, finalmente, el sistema genera o selecciona una respuesta contextual que puede ser reproducida por voz.

En el caso del piloto del Museo Tumbas Reales de Sipán, se considera pertinente separar estos costos del precio inicial de implementación, debido a que dependen del volumen efectivo de uso por parte de los visitantes. La implementación inicial cubre infraestructura, configuración, parametrización y puesta en marcha; en cambio, los servicios de IA corresponden a un componente operativo recurrente u OPEX, cuyo valor aumenta o disminuye según la cantidad de consultas realizadas.

Para la transcripción de voz a texto, se toma como referencia Google Cloud Speech-to-Text, cuyo modelo estándar de la API V2 tiene un costo de **USD 0.016 por minuto de audio procesado** para los primeros 500 000 minutos mensuales. ([Google Cloud][2]) Para la vectorización de preguntas se toma como referencia el modelo **text-embedding-3-small** de OpenAI, cuyo costo es de **USD 0.02 por cada millón de tokens**. ([OpenAI Desarrolladores][3]) Como tipo de cambio referencial se adopta **S/ 3.47 por dólar**, valor cercano a la cotización oficial publicada por SUNAT/SBS para abril de 2026. ([E-Consulta SUNAT][4])

Bajo estos supuestos, el costo más relevante corresponde al STT, mientras que la vectorización de preguntas representa un costo marginal muy bajo. Esto ocurre porque cada pregunta del visitante suele contener pocos tokens, mientras que el STT se factura por tiempo de audio procesado. Por tanto, para efectos del modelo económico, el costo operativo de IA debe estimarse principalmente en función de los minutos mensuales de audio transcrito.

---

## Tabla sugerida: escenarios de costo de IA

| Escenario   | Visitantes que usan voz | Usuarios activos/año | Minutos STT por usuario | Minutos STT/año | Costo STT/año | Costo aprox. por usuario activo |
| ----------- | ----------------------: | -------------------: | ----------------------: | --------------: | ------------: | ------------------------------: |
| Conservador |                    10 % |               19 168 |                   2 min |      38 336 min |      S/ 2 128 |                         S/ 0.11 |
| Base        |                    20 % |               38 336 |                   4 min |     153 346 min |      S/ 8 514 |                         S/ 0.22 |
| Alto        |                    35 % |               67 089 |                   6 min |     402 532 min |     S/ 22 349 |                         S/ 0.33 |

En el escenario base, el costo mensual aproximado del STT sería:

[
\frac{153,346 \text{ min/año}}{12} \times 0.016 \text{ USD/min} \times 3.47
]

[
= S/ 709.48 \text{ mensuales}
]

Por tanto, el costo operativo anual de STT sería aproximadamente **S/ 8 514**.

---

## Costo de vectorización de preguntas con OpenAI

La vectorización de las preguntas mediante OpenAI tiene un costo mucho menor. Si se asume que cada usuario activo realiza **3 preguntas**, y cada pregunta contiene aproximadamente **60 tokens**, en el escenario base se tendría:

[
38,336 \text{ usuarios activos} \times 3 \text{ preguntas} \times 60 \text{ tokens}
]

[
= 6,900,480 \text{ tokens/año}
]

Con un costo de **USD 0.02 por millón de tokens**, el costo anual sería:

[
6.9 \text{ millones de tokens} \times 0.02 = USD 0.138
]

En soles:

[
USD 0.138 \times 3.47 = S/ 0.48
]

Por tanto, el costo anual de vectorizar preguntas sería prácticamente marginal. Incluso si se agrega una bolsa de seguridad para revectorización de contenidos, pruebas, errores o crecimiento del corpus curatorial, el costo de embeddings puede redondearse operativamente a **S/ 10 o S/ 20 anuales**, sin afectar significativamente el flujo económico del proyecto.

---

# Tabla sugerida para agregar al Capítulo 5

| Servicio de IA                        | Proveedor referencial         |      Unidad de cobro |              Supuesto base | Costo estimado anual |
| ------------------------------------- | ----------------------------- | -------------------: | -------------------------: | -------------------: |
| STT: voz a texto                      | Google Cloud Speech-to-Text   |     USD 0.016/minuto |            153 346 min/año |             S/ 8 514 |
| Vectorización de preguntas            | OpenAI text-embedding-3-small | USD 0.02 / 1M tokens |            6.9M tokens/año |              S/ 0.48 |
| Bolsa técnica de embeddings y pruebas | OpenAI                        |     Margen operativo |       Redondeo conservador |             S/ 10–20 |
| Total IA escenario base               | Mixto                         |                    — | 20 % de visitantes activos |  Aprox. S/ 8 530/año |

---

# Ajuste recomendado al flujo de ingresos

El flujo actual del capítulo proyecta **S/ 5 100** por implementación, **S/ 900** de mantenimiento anual y un servicio adicional de **S/ 500**, acumulando **S/ 7 400** en tres años. 

Pero si se incorpora IA, el mantenimiento anual de **S/ 900** ya no debería interpretarse como mantenimiento total del sistema, sino solo como **mantenimiento técnico básico**. El consumo de IA debe ir como una línea separada.

Una forma defendible sería crear una fuente de ingreso nueva:

## Servicio recurrente de IA y analítica

| Concepto                                       | Monto sugerido |
| ---------------------------------------------- | -------------: |
| Costo estimado de IA escenario base            |   S/ 8 530/año |
| Margen operativo y administración, 20 % aprox. |   S/ 1 700/año |
| Precio anual sugerido al museo                 |  S/ 10 200/año |
| Precio mensual sugerido                        |     S/ 850/mes |

Esto permite que MuseIQ no absorba el costo variable de IA y que el museo pague una tarifa mensual proporcional al valor recibido.

---

# Comparación con guía humano

Si un guía cuesta **S/ 50 por hora**, el costo por visitante depende del tamaño del grupo:

| Modalidad               |                       Supuesto | Costo por visitante |
| ----------------------- | -----------------------------: | ------------------: |
| Guía humano             |           Grupo de 10 personas |             S/ 5.00 |
| Guía humano             |           Grupo de 20 personas |             S/ 2.50 |
| Guía humano             |           Grupo de 30 personas |             S/ 1.67 |
| MuseIQ STT + embeddings | Usuario activo, escenario base |      Aprox. S/ 0.22 |

Esto no significa que MuseIQ reemplace completamente al guía humano. La interpretación cultural humana sigue teniendo valor pedagógico y emocional. Sin embargo, MuseIQ permite atender consultas frecuentes, orientar al visitante, entregar información contextual y ampliar la cobertura sin que el costo crezca linealmente por cada grupo atendido.

---

# Beneficios posibles para justificar el costo de IA

Puedes agregar este texto en el análisis crítico o conclusión del capítulo:

La incorporación de servicios de IA genera beneficios operativos y estratégicos para el museo. En primer lugar, permite ampliar la cobertura de orientación sin depender exclusivamente de la disponibilidad de guías humanos. En segundo lugar, mejora la accesibilidad, ya que visitantes adultos mayores, personas con discapacidad visual, usuarios con dificultad de lectura o visitantes que prefieren interacción oral pueden formular preguntas mediante voz. En tercer lugar, fortalece la personalización del recorrido, porque las respuestas pueden ajustarse a la sala detectada, al contenido curatorial disponible y al momento específico de la visita.

Asimismo, el uso de RAG y vectorización permite que las respuestas no dependan únicamente de un modelo generativo abierto, sino de una base curatorial institucional previamente organizada. Esto reduce el riesgo de respuestas imprecisas y mejora la trazabilidad de la información entregada. Además, las consultas realizadas por los visitantes pueden convertirse en insumos analíticos para el museo, permitiendo identificar qué obras generan mayor interés, qué temas producen más dudas y qué contenidos deberían reforzarse en futuras actualizaciones museográficas.

Desde la perspectiva económica, el costo variable de IA resulta bajo cuando se analiza por usuario activo. En el escenario base, el costo aproximado de STT y vectorización es de **S/ 0.22 por visitante que utiliza la función de voz**, valor considerablemente menor al costo proporcional de una visita guiada tradicional. Por ello, la IA no debe interpretarse solo como un gasto adicional, sino como un componente que incrementa la escalabilidad, accesibilidad y valor diferencial de MuseIQ frente a audioguías lineales o mecanismos tradicionales de mediación.

---

# Conclusión para tu ajuste

El Capítulo 5 debería actualizarse así:

1. Mantener el costo de implementación de **S/ 5 100**.
2. Mantener el mantenimiento técnico básico de **S/ 900/año**.
3. Agregar una nueva línea llamada **Servicio recurrente de IA y analítica**.
4. Estimar ese servicio en el escenario base en aproximadamente **S/ 850 mensuales** o **S/ 10 200 anuales**.
5. Justificar que el costo por usuario activo es bajo: aproximadamente **S/ 0.22 por visitante que pregunta por voz**.
6. Explicar que la Raspberry Pi reduce costos de infraestructura porque centraliza el RAG local, pero no elimina el costo variable del STT en la nube ni el uso de embeddings por API.

[1]: https://www.gob.pe/institucion/cultura/noticias/1333395-museo-tumbas-reales-de-sipan-alcanza-record-historico-con-mas-de-191-mil-visitantes-en-2025 "Museo Tumbas Reales de Sipán alcanza récord histórico con más de 191 mil visitantes en 2025 - Noticias - Ministerio de Cultura - Plataforma del Estado Peruano"
[2]: https://cloud.google.com/speech-to-text/pricing "Speech-to-Text API Pricing | Google Cloud"
[3]: https://developers.openai.com/api/docs/models/text-embedding-3-small "text-embedding-3-small Model | OpenAI API"
[4]: https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias "SUNAT - Tipo de Cambio Oficial"


Aquí te dejo una lista de las fuentes utilizadas, con los detalles adecuados para su inclusión en tu informe bajo el formato de citas de estilo APA 7:

### Fuentes citadas

1. **Google Cloud Speech-to-Text Pricing**
   Google Cloud. (n.d.). *Speech-to-Text pricing*. Retrieved from [https://cloud.google.com/speech-to-text/pricing](https://cloud.google.com/speech-to-text/pricing)

2. **OpenAI Pricing for Embeddings**
   OpenAI. (n.d.). *Pricing for Embeddings*. Retrieved from [https://developers.openai.com/api/docs/models/text-embedding-3-small](https://developers.openai.com/api/docs/models/text-embedding-3-small)

3. **Ministerio de Cultura - Museo Tumbas Reales de Sipán**
   Ministerio de Cultura. (2025, February 10). *Museo Tumbas Reales de Sipán alcanza récord histórico con más de 191 mil visitantes en 2025*. Retrieved from [https://www.gob.pe/institucion/cultura/noticias/1333395-museo-tumbas-reales-de-sipan-alcanza-record-historico-con-mas-de-191-mil-visitantes-en-2025](https://www.gob.pe/institucion/cultura/noticias/1333395-museo-tumbas-reales-de-sipan-alcanza-record-historico-con-mas-de-191-mil-visitantes-en-2025)

4. **Tasa de cambio de SUNAT/SBS**
   Superintendencia Nacional de Aduanas y de Administración Tributaria (SUNAT). (2026). *Tipo de cambio referencial diario*. Retrieved from [https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias](https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias)

5. **eSpeak - TTS Engine**
   eSpeak. (n.d.). *eSpeak: Open Source Speech Synthesizer*. Retrieved from [http://espeak.sourceforge.net](http://espeak.sourceforge.net)

6. **Festival TTS Engine**
   The Festival Speech Synthesis System. (n.d.). *Festival: Open Source Speech Synthesis*. Retrieved from [http://www.cstr.ed.ac.uk/projects/festival/](http://www.cstr.ed.ac.uk/projects/festival/)

7. **OpenAI Documentation**
   OpenAI. (n.d.). *API Documentation*. Retrieved from [https://developers.openai.com/docs](https://developers.openai.com/docs)

8. **Sunat Tipo de Cambio Diario**
   Superintendencia Nacional de Aduanas y de Administración Tributaria. (2026). *Tipo de cambio referencial*. Retrieved from [https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias](https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias)

Estas fuentes proveen la base para los cálculos de costos, la estimación de precios y los servicios de IA utilizados en tu proyecto, lo que las hace relevantes para tu informe y justificación de costos en el **Capítulo 5**.

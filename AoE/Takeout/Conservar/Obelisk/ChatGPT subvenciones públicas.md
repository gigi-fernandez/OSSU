Hacer una simple página web con web scrapping y llamadas a un modelo cuatom de chatGPT que busque en la página de hacienda qué ayudas podrías tener derecho a cobrar.

www.pap.hacienda.gob.es/bdnstrans/GE/es/inicio

Funcionamiento:
1. Le preguntas si tú o tu empresa cumplís con las condiciones de alguna ayuda. Obligatorio rellenar la localización de la entidad y ciertas características (forms que se revela en función del input previo (es familia/persona/empresa -> es numerosa/pyme/mujer...). Se filtra todo para lo que se califique. Se toma siempre la fecha actual. Se eliminan resultados de más de X tiempo por defecto, y todas aquellas que hayan caducado siempre.
2. GPT realiza un análisis semántico y produce un output en JSON.
3. Se realiza una búsqueda en función de ese JSON. Otra instancia de GPT4 intenta ver si cada uno de los seleccionados es relevante para el caso. Se filtran y se presentan (una vez respondidas algunas preguntas más para filtrar)


Mientras tanto, la app realiza un web scrapping periódico diario de la PAP, y almacena en su propia base de datos todas las ayudas de los últimos dos años. La app buscará en la DB propia en lugar de en la de Hacienda. Cada vez que se añada una, una instancia de gpt la etiquetará exhaustivamente. Si alguna etiqueta está en la lista de alguna cuenta, se le enviará un correo avisándole. 

Ejecución aplicación a una ayuda:
1. Idealmente, la IA se encargaría del proceso completo de aplicaciones a ayudas. Te pide los datos y documentos primarios y genera todos los derivados, los envía a los correos necesarios o (idealmente) aplica en la página web correspondiente.

Monetización:
1. El servicio es gratuito y entero para particulares (quizá, como mucho, con anuncios), pero de pago para empresas, pymes y autónomos.

QOL:
1. Detección de idioma (catalán, gallego, euskera, valenciano) y ajuste automático del contenido, pero búsqueda en español.
2. Speech to text, gpt corrige el texto generado y se lo pasa a la siguiente instancia de gpt.
3. Generación de alertas. Si no hay, o incluso si hay y se lo pides, subvenciones para lo que quieres, gpt te sugerirá si quieres que te avise por correo cuando exista alguna similar. 
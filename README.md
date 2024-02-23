# Desafío Python - FROZENBOT :rocket:

## Descripción
# Sistema de Toma de Pedidos - Frozen SRL :scroll:

El programa principal ejecuta la toma de pedidos para la Heladería Frozen SRL. Utiliza un bot interactivo llamado FROZENBOT para gestionar las interacciones
con los usuarios y responder a sus consultas. El propósito principal es facilitar la experiencia de pedidos para los clientes y gestionar el inventario de manera eficiente.

## :loudspeaker: Características Principales

- **Bienvenida con Información Climática:** Verifica la temperatura en Pehuajó y muestra un mensaje de bienvenida que incluye información climática actualizada para proporcionar una experiencia personalizada.

- **Interacción Continua:** Entra en un bucle interactivo, esperando la entrada del usuario. El bot FROZENBOT procesa cada entrada y responde de manera inteligente.

- **Verificación de Stock:** Cuando se detecta un pedido, el programa verifica si los productos solicitados están en stock. Esta verificación es crucial para confirmar o
  rechazar los pedidos de manera informada.

## :loudspeaker: Flujo de Ejecución

1. **Mensaje de Bienvenida:** El programa inicia mostrando un mensaje de bienvenida que incluye información climática.

2. **Bucle Interactivo:** Entra en un bucle interactivo donde FROZENBOT espera la entrada del usuario.

3. **Procesamiento de Entrada:** Cada vez que el usuario proporciona información, FROZENBOT procesa la entrada y responde de manera adecuada, ya sea tomando un pedido o respondiendo consultas.

4. **Verificación de Stock:** Cuando se realiza un pedido, el programa verifica el stock de los productos solicitados para determinar si puede confirmarse.

5. **Finalización del Programa:** Si el usuario ingresa "finish", el programa muestra todos los pedidos confirmados hasta ese momento y termina la ejecución.

### :bulb: Entorno de Desarrollo
- Python 3.7+
- TensorFlow 2.0+
  
## Requisitos :package:
- TensorFlow: Framework para aprendizaje automático.
- Keras: Interfaz de alto nivel para redes neuronales.
- Requests: Biblioteca para realizar solicitudes HTTP.
- Pandas: Estructuras de datos y herramientas de análisis de datos.
- Spacy: Biblioteca para procesamiento de lenguaje natural.
- scikit-learn: Herramientas simples y eficientes para análisis de datos.

- Modelo NLP: Se entrena con el conjunto de datos (tag, patterns, resposes) usando TensorFlow y Keras.
- Archivos adicionales: lematizacion-es.pickle, frozenbot.h5, responses.pkl, vocab.pkl, etc.
- 
## Uso :clipboard:
Para ejecutar tu programa en Visual Studio Code utilizando el modo de depuración (Run/Start Debugging o F5)

### :gear: Configuración del Entorno Virtual 
- Crear un Entorno Virtual: `python -m venv venv`
- Activar el Entorno Virtual: `source venv/bin/activate` (Linux/Mac) o `.\venv\Scripts\activate` (Windows)

- # Instalar dependencias :wrench:
- [TensorFlow](https://www.tensorflow.org/): `pip install tensorflow`
- [Keras](https://keras.io/): `pip install keras`
- [Requests](https://docs.python-requests.org/en/master/): `pip install requests`
- [Pandas](https://pandas.pydata.org/): `pip install pandas`
- [Spacy](https://spacy.io/): `pip install spacy` (y descargar modelos adicionales si es necesario)
- [scikit-learn](https://scikit-learn.org/stable/): `pip install scikit-learn` (opcional)

## Nota
Este programa está diseñado para mejorar la eficiencia en la toma de pedidos y proporcionar una experiencia de 
usuario agradable para los clientes de la Heladería Frozen SRL.

Problemas Conocidos
Descripción del Problema
Al ejecutar el código, se han detectado las siguientes advertencias relacionadas con el uso de funciones obsoletas en TensorFlow:

Advertencia 1:
WARNING:tensorflow: From .../keras/src/losses.py:2976:
The name tf.losses.sparse_softmax_cross_entropy is deprecated. 
Please use tf.compat.v1.losses.sparse_softmax_cross_entropy instead.

Advertencia 2:
WARNING:tensorflow: From .../keras/src/backend.py:1398:
The name tf.executing_eagerly_outside_functions is deprecated. 
Please use tf.compat.v1.executing_eagerly_outside_functions instead.

Acciones Propuestas
Sustituir tf.losses.sparse_softmax_cross_entropy por tf.compat.v1.losses.sparse_softmax_cross_entropy.
Actualizar el Código:

Sustituir tf.executing_eagerly_outside_functions por tf.compat.v1.executing_eagerly_outside_functions.
Contexto y Justificación
Estas advertencias indican que el código actual está utilizando funciones que han sido marcadas
como obsoletas en las versiones más recientes de TensorFlow. Para garantizar la compatibilidad
futura y seguir las mejores prácticas, se recomienda actualizar el código a las versiones compatibles con TensorFlow v1.

Contacto:
Johana Rangel
johanarangeldo@gmail.com

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from geo_api import GeoAPI
from product_bot import ProductBot


if __name__ == '__main__':
    """
    Función principal de ejecución del programa para la toma de pedidos de 
    una Heladeria llamada Frozen SRL, el cual hace uso de un bot llamado
    FROZENBOT para interactuar con el usuario y ayudar a responder sus consultas, 
    cuando el programa detecte algún pedido, el mismo verificará si está o no en stock 
    para saber si puede confirmarlo o no.

    - Verifica la temperatura en Pehuajó y muestra un mensaje de bienvenida con información climática.
    - Entra en un bucle interactivo, esperando la entrada del usuario.
    - Procesa la entrada del usuario y muestra los resultados.
    - Si el resultado del procesamiento del usuario es "finish", muestra todos los pedidos confirmados
      utilizando el método y termina el programa.
    """

    product_bot = ProductBot()

    if GeoAPI.is_hot_in_pehuajo():
        print(f"Bot: Bienvenido soy FrozenBOT. Te comento que hoy hace calor, la temperatura en Pehuajó es de {GeoAPI.temperature}ºC. ¿Prefieres algo refrescante?")
    else:
        print(f"Bot: Bienvenido soy FrozenBOT. Te comento que el clima no es tan cálido, la temperatura en Pehuajó es de {GeoAPI.temperature}ºC. ¿En qué más puedo ayudarte?")

    while True:
        texto_usuario = input("").lower()

        result = product_bot.process_user_input(texto_usuario)

        if result == "finish":
            # Mostrar todos los pedidos confirmados al final
            product_bot.display_confirmed_orders()
            print('Gracias por hacer uso de nuestros Servicios. Nos vemos pronto. Saludos, FROZENBOT.')
            break
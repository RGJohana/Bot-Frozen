import pandas as pd
import random

import os
# Deshabilita las opciones específicas de oneDNN en TensorFlow
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from nlp_processor import NLPProcessor


class ProductBot:
    """
    Clase que representa a FrozenBOT, un bot de pedidos de productos con 
    procesamiento de lenguaje natural (NLP).

    Attributes:
    - MAX_INTENTS (int): Número máximo de intentos para realizar un pedido.
    - _PRODUCT_DF (DataFrame): DataFrame que contiene información sobre los productos y su stock.
    - _confirmed_orders (list): Lista que almacena los pedidos confirmados.
    - nlp_processor (NLPProcessor): Instancia de NLPProcessor para el procesamiento de lenguaje natural.
    """

    def __init__(self):
        self.MAX_INTENTS = 3
        self._PRODUCT_DF = pd.DataFrame({
            "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
            "quantity": [3, 10, 0, 5]
        })
        self._confirmed_orders = []
        self.nlp_processor = NLPProcessor()


    def process_user_input(self, texto_usuario):
        """
        Parameters: 
        - texto_usuario (str): El texto ingresado por el usuario.

        Returns:
        - None: No hay un valor de retorno específico.

        Este método utiliza un modelo de procesamiento de lenguaje natural (NLP) para entender 
        la entrada del usuario y generar una respuesta. Si la confianza en la respuesta supera un umbral,
        se selecciona una respuesta y se imprime. Además, si la respuesta está relacionada con el pedido,
        se llama al método request_order.

        Ejemplo:   self.nlp_processor.generate_bow_from_text("Hola, ¿puedo hacer un pedido?")
        """

        bow = self.nlp_processor.generate_bow_from_text(texto_usuario)
        
        probs = self.nlp_processor.model.predict([bow])
        score = probs.max()
        
        if score > 0.4:  # threshold 0.4        
            index = probs.argmax(axis=1)[0]
            result = random.choice(self.nlp_processor.responses[index])
            print(result)
            
            if index in [7,8,9,10,15]:  # Indice según tu estructura de respuestas.
                return self.request_order()  # Llama a request_order si es una respuesta relacionada con el pedido
        else:
            print("Perdón, no pude entenderte. Vuelve a consultar")
            

    def is_product_available(self, product_name, quantity):
        """
        Verifica la disponibilidad de un producto en el inventario.

        Parameters:
        - product_name (str): El nombre del producto que se desea verificar.
        - quantity (int): La cantidad deseada del producto.

        Returns:
        - bool: True si el producto está disponible en la cantidad deseada, False en caso contrario.       

        """

        product_info = self._PRODUCT_DF[self._PRODUCT_DF['product_name'] == product_name]
        if not product_info.empty and product_info['quantity'].values[0] >= quantity:
            return True
        else:
            return False


    def get_product_info(self, product_name):
        """
        Obtiene la información de un producto específico.

        Parameters:
        - product_name (str): El nombre del producto del cual se desea obtener la información.

        Returns:
        - tuple or None: Una tupla que contiene el nombre y la cantidad del producto si está disponible,
          o (None, None) si el producto no está en el inventario.

        Este método busca la información de un producto en el inventario por su nombre. Si el producto
        está disponible, retorna una tupla con el nombre y la cantidad, de lo contrario, retorna (None, None).

        """

        product_info = self._PRODUCT_DF[self._PRODUCT_DF['product_name'] == product_name]
        if not product_info.empty:
            return product_info['product_name'].values[0], product_info['quantity'].values[0]
        else:
            return None, None
        

    def update_stock(self, product_name, quantity):
        """
        Actualiza el inventario al restar la cantidad pedida de un producto.

        Parameters:
        - product_name (str): El nombre del producto cuyo stock se actualizará.
        - quantity (int): La cantidad que se restará al stock.
        """
       
        product_index = self._PRODUCT_DF.index[self._PRODUCT_DF['product_name'] == product_name].tolist()[0]
        self._PRODUCT_DF.at[product_index, 'quantity'] -= quantity


    def display_products_and_quantities(self):
        """
        Muestra en la consola la lista de productos disponibles y sus cantidades en stock.

        Este método itera sobre el DataFrame de productos y muestra aquellos que tienen una cantidad disponible
        mayor que cero. La información se presenta en el formato "Producto: {nombre}, Cantidad: {cantidad}".
        """

        print("Los productos en stock son:")
        for index, row in self._PRODUCT_DF.iterrows():
            if row['quantity'] > 0:
                print(f"Producto: {row['product_name']}, Cantidad: {row['quantity']}")
        

    def is_valid_discount_code(self, discount_code):
        """
        Verifica la validez de un código de descuento.

        Parameters:
        - discount_code (str): El código de descuento a verificar.

        Returns:
            bool: True si el código de descuento es válido, False de lo contrario.
        """
        
        valid_discounts = ["FROZENYUMMY", "FROZENBASIC", "FROZENPREMIUM"]  

        if discount_code.upper() in valid_discounts:
            return True
        else:
            return False
        

    def display_confirmed_orders(self):
        """
        Muestra en la consola la información de los pedidos confirmados.
        """
        
        if self._confirmed_orders is None:
            print("No hay pedidos confirmados.")
            
        print("Pedidos Confirmados:")
        for order in self._confirmed_orders:
            
            print(f"Producto: {order['Producto']}, Cantidad: {order['Cantidad']}, Descuento: {order['Descuento']}")


    def request_order(self):
        """
        Maneja el proceso de solicitud de pedidos.

        Mientras haya intentos disponibles, solicita al usuario el sabor del producto y la cantidad deseada.
        Verifica la disponibilidad del producto, confirma el pedido, actualiza el stock y ofrece códigos de descuento.
        Registra los pedidos confirmados en la lista _confirmed_orders.

        Returns:
        - "finish" si se completó la solicitud de pedidos.
        """
         
        while self.MAX_INTENTS > 0:
            product_name = input("Me indicas el sabor para armar pedido, gracias: ").strip().title()
            
            if product_name == "Dulce De Leche":
                product_name = "Dulce de Leche"
            
            if not product_name or product_name.isdigit():
                print("El nombre del producto no debe estar vacío, con números o con caracteres especiales.")
                continue

            try:
                while True:
                    try:
                        quantity = int(input("Ingrese la cantidad deseada: "))
                        if quantity <= 0:
                            print("La cantidad no puede ser cero o negativa. Por favor, ingrese un valor mayor a cero.")
                            continue
                        else:
                            break  # Salir del bucle si la cantidad es válida
                    except ValueError:
                        print("Por favor, ingrese un valor numérico válido para la cantidad.")
            
            except ValueError:
                print("La cantidad no puede estar vacía.")
                continue 

            if self.is_product_available(product_name, quantity):
                producto, cantidad = self.get_product_info(product_name)
                
                if producto and cantidad >= quantity:
                    print(f"¡¡¡Genial!!! Producto disponible: {producto} - Cantidad solicitada: {quantity}")
                    # Ej: "FROZENYUMMY", "FROZENBASIC", "FROZENPREMIUM"
                    print("Códigos de descuentos: FROZEN-----, FROZEN-----, FROZEN-------")
                    discount_code = input("Ingrese su código de descuento (si no tiene, presione Enter): ")
                    
                    if self.is_valid_discount_code(discount_code):
                        print("Código de descuento válido. ¡Pedido confirmado!")
                        self.update_stock(product_name, quantity)
                        self.MAX_INTENTS -= 1  # Reducir el número de intentos disponibles

                        # Agregar el pedido confirmado a la lista
                        self._confirmed_orders.append({"Producto": producto, "Cantidad": quantity, "Descuento": discount_code})

                        # Verificar si quiere hacer otro pedido habilitarlo otra vez los tres intentos
                        another_order = input("¿Desea realizar otro pedido con otro sabor? (s/n): ").strip().lower()
                        if another_order == "s":
                            self.MAX_INTENTS = 3
                            continue  # Continuar con el siguiente pedido
                        else:
                            print("Gracias por su pedido. ¡Hasta luego!")
                            return "finish"
                        
                    else:
                        print("Código de descuento inválido. Por favor, vuelva a intentarlo.")
                        
            else:
                producto, cantidad = self.get_product_info(product_name)
                if producto and cantidad < quantity:
                    print(f"Lo siento, el producto '{producto}' está disponible, pero no hay suficiente stock para su orden.")
                    
                if not producto:
                    print(f"Lo siento, el producto '{product_name}' no está disponible.")
                    
                self.display_products_and_quantities()

            self.MAX_INTENTS -= 1

        print(f"Se han agotado los intentos. Por favor, vuelva a intentarlo más tarde.")
        
        # Mostrar todos los pedidos confirmados al final
        self.display_confirmed_orders()
        
        return "finish"
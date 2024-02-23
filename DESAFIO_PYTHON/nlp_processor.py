import re
import string
import pickle
import spacy
import os

# Deshabilita las opciones específicas de oneDNN en TensorFlow
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from keras.models import load_model


class NLPProcessor:
    """
    Clase que procesa el texto del usuario utilizando técnicas de procesamiento de lenguaje natural (NLP).

    Attributes:
    - model (tensorflow.keras.Model): Modelo entrenado para procesar el texto del usuario.
    - lemmatizer (dict): Diccionario para lematizar palabras.
    - responses (list): Lista de respuestas predefinidas.
    - vocab (list): Vocabulario utilizado en el modelo.

    Methods:
    - preprocess_clean_text(text: str) -> str: Realiza la limpieza y preprocesamiento básico de un texto.
    - generate_bow_from_text(texto_usuario: str) -> list: Genera un "Bag of Words" (BoW) a partir del texto del usuario.
    """

    def __init__(self):
        # Cargar el modelo entrenado (frozenbot.h5)
        model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model/frozenbot.h5")
        self.model = load_model(model_path)

        # Cargar otros archivos necesarios
        self.lemmatizer = pickle.load(open("model/lematizacion-es.pickle", "rb"))
        self.responses = pickle.load(open("model/responses.pkl", "rb"))
        self.vocab = pickle.load(open("model/vocab.pkl", "rb"))


    @staticmethod
    def preprocess_clean_text(text):
        """
        Realiza la limpieza y preprocesamiento básico de un texto.

        Args:
        - text (str): El texto a procesar.

        Returns:
        - str: Texto procesado con las siguientes transformaciones:
            1. Convertido a minúsculas.
            2. Eliminación de números.
            3. Eliminación de caracteres de puntuación.
            4. Eliminación de caracteres con acento (reemplazados por letras sin acento).
        """

        # pasar a minúsculas
        text = text.lower()
        # quitar números
        pattern = r'[0-9\n]'
        text = re.sub(pattern, '', text)
        # quitar caracteres de puntiación
        text = ''.join([c for c in text if c not in (string.punctuation + "¡" + "¿")])
        # quitar caracteres con acento
        text = re.sub(r'[àáâä]', "a", text)
        text = re.sub(r'[éèêë]', "e", text)
        text = re.sub(r'[íìîï]', "i", text)
        text = re.sub(r'[òóôö]', "o", text)
        text = re.sub(r'[úùûü]', "u", text)
        return text
    

    def generate_bow_from_text(self, texto_usuario):
        """
        Genera un "Bag of Words" (BoW: conjunto de documentos en términos de las 
        palabras que contiene.) a partir del texto del usuario.

        Parameters:
        - texto_usuario (str): El texto del usuario para el cual se generará el BoW.

        Returns:
        - list: BoW representado como una lista de 1 y 0, donde 1 indica la presencia de la palabra en el vocabulario y 0 su ausencia.
        """
        
        # preprocesamiento + lematizacion
        # ------------------------------------------
        # Transformar la pregunta (input) en tokens y lematizar
        
        lemma_words = []
        tokens = NLPProcessor.preprocess_clean_text(texto_usuario).split(" ")
        
        for token in tokens:
            lemma = self.lemmatizer.get(token)
            if lemma is not None:
                lemma_words.append(lemma)

        # Transformar los tokens en "Bag of words" (arrays de 1 y 0)
        bow = [1 if word in lemma_words else 0 for word in self.vocab]

        return bow
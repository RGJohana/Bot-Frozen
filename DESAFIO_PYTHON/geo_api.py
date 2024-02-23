import requests


class GeoAPI:
    """
    Clase que proporciona funciones relacionadas con la obtención de datos 
    climáticos utilizando la API de OpenWeatherMap.

    Attributes:
    - API_KEY (str): Clave de API para acceder a OpenWeatherMap.
    - LAT (str): Latitud de la ubicación para la cual se obtendrán los datos climáticos.
    - LON (str): Longitud de la ubicación para la cual se obtendrán los datos climáticos.
    - temperature (float): Temperatura actual en la ubicación especificada.

    Methods:
    - is_hot_in_pehuajo(cls): Comprueba la temperatura actual en Pehuajó. 
    
    """

    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    temperature = None

    @classmethod
    def is_hot_in_pehuajo(cls):
        """
        Comprueba si la temperatura actual en Pehuajó se considera caliente basándose en la temperatura.

        Retorna:
        bool: True si la temperatura es mayor a 28 grados Celsius, False en caso contrario.
        """
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()
                        
            if 'main' in data and 'temp' in data['main']:
                GeoAPI.temperature = data['main']['temp']
                return GeoAPI.temperature > 28
            else:
                return False
        except requests.RequestException:
            return False
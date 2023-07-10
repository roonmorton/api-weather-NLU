

from app.config.settings import Config
import requests

class WeatherApiService:

    def __init__(self) -> None:
        self.url_api = 'https://api.weatherapi.com/v1'
    
    def obtener_clima_actual_by_ciudad(self,query_ciudad:str, aqi: str):
        url = f"{self.url_api}/current.json"
        params = {
            'key': Config.WEATHERAPI_KEY,
            'q': query_ciudad,
            'aqi': aqi,
            'lang': 'es'
        }
        #print(params)
        #print(url)
        response = requests.get(url, params=params)
        if response.status_code == 200 :
            return response.json()
        else:
            print("Error consultando clu azure", response.status_code)
            return None 


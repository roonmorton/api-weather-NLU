from fastapi import APIRouter

from app.services.weatherapi_service import WeatherApiService
from app.services.clu_azure_service import CLUAzureService

router = APIRouter()

weather_service = WeatherApiService()
clu_azure_service = CLUAzureService()



# Ruta y función de manejo de la solicitud
@router.get("/hello")
def hello_world():
    return {
        "message": "Hello world"
    }


@router.get("/question")
def question(query: str):
    
    
    res_clu_az = clu_azure_service.query(query=query)
    if res_clu_az is None: 
        return {
            "result": 1,
            "response": "No se pudo consultar el servicio..."
        } 
      
    top_intent = res_clu_az["result"]["prediction"]["topIntent"]

    if top_intent == "ConsultarTemperaturaClima" or top_intent == "ConsultarCalidadAireClima":
        # Realizar acciones relacionadas con la intención de consultar temperatura/clima
        entities = res_clu_az.get("result", {}).get("prediction", {}).get("entities", [])
        city = None
        for entity in entities:
            if entity.get("category") == 'city':
                city = entity.get("text")
        if city is None :
            return {
                'code': 2,
                "message": 'Favor ingresar la ciudad que desea saber el clima'
            }
        res_clima = weather_service.obtener_clima_actual_by_ciudad(query_ciudad=city, aqi = 'no' if top_intent == "ConsultarTemperaturaClima" else 'yes')
        if res_clima is None :
            return {
                'code': 4,
                'message': f'No se pudo consultar, intentar mas tarde'
            }
        city = res_clima['location']['name']
        country = res_clima['location']['country']
        temp_c = res_clima['current']['temp_c']
        condition = res_clima['current']['condition']['text']
        wind = res_clima['current']['wind_kph']

        if top_intent == "ConsultarCalidadAireClima":
            epa_index = res_clima['current']['air_quality']['us-epa-index']
            epa_index = 'Bueno' if epa_index == 1 else 'Moderado' if epa_index == 2 else 'No saludable' if epa_index == 3 else 'Insalubre' if epa_index == 4 else 'Muy poco saludable' if epa_index == 5 else 'Peligroso'
            return {
                'code': 0,
                'message': f'Te reportamos que para {city} en {country} nos encontramos a {temp_c} °C con viento de {wind} Km/h y se reporta {condition} con indice del aire {epa_index}' 
            }
        else:
            return {
                'code': 0,
                'message': f'Te reportamos que para {city} en {country} nos encontramos a {temp_c} °C con viento de {wind} Km/h y se reporta {condition}'
            }
    else:
        # Realizar acciones por defecto o manejar intenciones no reconocidas
        return {
        "code": 3,
        "message": "No encontramos coincidencia para su consulta..."
        }

    #res_clima = weather_service.obtener_clima_actual_by_ciudad(query)



    #if res_clima.status_code == 200: 
    #    json_res = res_clima.json()
    #    print(json_res)
    #    return json_res
    #else:
    #    return {
    #        "result": 1,
    #        "response": "Ocurrio un error"
    #    }
    
    
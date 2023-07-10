from app.config.settings import Config
import requests



class CLUAzureService:

    
    def __init__(self) -> None:
        self.url_api = 'https://umg-clu-5628.cognitiveservices.azure.com/language/:analyze-conversations?api-version=2022-10-01-preview'

    def query(self, query: str):
        headers = {
            'Ocp-Apim-Subscription-Key': Config.CLU_SUBSCRIPTION_KEY,
            'Apim-Request-Id': Config.CLU_REQUEST_ID
        }
        body = {
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                "id": "1",
                "text": query,
                "participantId": "1"
                }
            },
            "parameters": {
                "projectName": "umg-test",
                "verbose": True,
                "deploymentName": "mlu-api-5628",
                "stringIndexType": "TextElement_V8"
            }
        }
        response = requests.post(
                        url=self.url_api,  
                        headers=headers,
                        json = body
                    )
        if response.status_code == 200 :
            return response.json()
        else:
            print("Error consultando clu azure", response.status_code)
            return None 

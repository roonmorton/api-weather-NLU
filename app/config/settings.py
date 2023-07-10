from dotenv import load_dotenv
import os

class Config:
    load_dotenv()
    DEBUG = os.getenv('DEBUG')
    PRODUCTION = os.getenv('PRODUCTION')
    WEATHERAPI_KEY = os.getenv('WEATHERAPI_KEY')
    LUIS_API_KEY = os.getenv('LUIS_API_KEY')
    CLU_SUBSCRIPTION_KEY = os.getenv('CLU_SUBSCRIPTION_KEY')
    CLU_REQUEST_ID = os.getenv('CLU_REQUEST_ID')
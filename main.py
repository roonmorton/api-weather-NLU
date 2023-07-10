import uvicorn
from fastapi import FastAPI
from app.controllers.weather_controller import router

# Crear instancia de FastAPI
app = FastAPI()

# Agregar controladores a la instancia de FastAPI
app.include_router(router)

if __name__ == "__main__":
    # Ejecutar la aplicación con Uvicorn en el puerto deseado
    uvicorn.run(app, port=8002)
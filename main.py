from fastapi import FastAPI
import pandas as pd
from my_module import get_max_duration

app = FastAPI()

@app.get("/saludar")
def saludar():
    return {"mensaje": "Hola mundo"}

@app.get("/get_max_duration")
def get_max_duration(year: int, platform: str, duration_type: str):
    # Llama a la función get_max_duration con los parámetros recibidos
    result = get_max_duration(year, platform, duration_type)
    return result
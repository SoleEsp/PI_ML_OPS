from fastapi import FastAPI

app = FastAPI()

@app.get("/saludar")
def saludar():
    return {"mensaje": "Hola mundo"}
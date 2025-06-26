from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#--------------------------------------------------------------

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI!"}

#--------------------------------------------------------------

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}

#--------------------------------------------------------------

@app.post("/enviar/{dato}")
def recibir_dato(dato: str):
    return {"respuesta": f"Me has enviado: {dato}"}

#--------------------------------------------------------------

class Persona(BaseModel):
    nombre: str
    cedula: str

@app.post("/registrar")
def registrar_persona(persona: Persona):
    return {
        "nombre_recibido": persona.nombre,
        "cedula_recibida": persona.cedula
    }

class Numeros(BaseModel):
    numero1 : str
    numero2 : str
    numero3 : str
    numero4 : str
    numero5 : str
    numero6 : str

@app.post("/numeros")
def numeros_ordenados(numero: Numeros):
    return {
        "numero1": numero.numero1,
        "numero2": numero.numero2,
        "numero3": numero.numero3,
        "numero4": numero.numero4,
        "numero5": numero.numero5,
        "numero6": numero.numero6

    }
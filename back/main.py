# Parte do back-end do projeto de Carros
#Projeto de API para gerenciamento de carros usando FastAPI e Pydantic 

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class car(BaseModel):
    id: int
    model: str
    year: int
    power: str
    image: str | None = None

#Banco de dados simulado
porsches = [
    car(id=1, model="Porsche 911 Carrera", year=2020, power="450hp"),
    car(id=2, model="Porsche Cayenne", year=2021, power="335hp"),
    car(id=3, model="Porsche Panamera", year=2019, power="330hp"),
    car(id=4, model="Porsche Macan", year=2022, power="248hp"),
    car(id=5, model="Porsche Taycan", year=2021, power="750hp"),
    car(id=7, model="Porsche 911 Gt3 Rs", year=2021, power="800hp")
]

@app.get("/cars")
#Listar todos os carros
def get_cars():
    return porsches

@app.post("/cars")
#Adicionar um novo carro
def add_car(car:car):
    porsches.append(car)
    return {"message": "Car added successfully"}

@app.put("/cars/{car_id}")
#Atualizar um carro existente
def update_car(car_id: int, updated_car: car):
    for index, car in enumerate(porsches):
        if car.id == car_id:
            porsches[index] = updated_car
            return {"message": "Car updated successfully"}
    raise HTTPException(status_code=404, detail="Car not found")

@app.delete("/cars/{car_id}")
#Deletar um carro
def delete_car(car_id: int):
    for index, car in enumerate(porsches):
        if car.id == car_id:
            del porsches[index]
            return {"message": "Car deleted successfully"}
    raise HTTPException(status_code=404, detail="Car not found")
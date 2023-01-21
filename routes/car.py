from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bson.objectid import ObjectId
from typing import Dict, List
from controllers.car import CarController

app = FastAPI()

class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    color: str

class CarUpdate(BaseModel):
    make: str
    model: str
    year: int
    color: str

@app.post("/cars", response_model=Dict)
async def create_car(car: CarCreate):
    return await CarController.create(car.dict())

@app.get("/cars/{car_id}", response_model=Dict)
async def read_car(car_id: str):
    return await CarController.get(car_id)

@app.get("/cars", response_model=List[Dict])
async def read_cars():
    return await CarController.get_all()

@app.put("/cars/{car_id}", response_model=Dict)
async def update_car(car_id: str, car: CarUpdate):
    return await CarController.update(car_id, car.dict())

@app.delete("/cars/{car_id}", response_model=Dict)
async def delete_car(car_id: str):
    return await CarController.delete(car_id)

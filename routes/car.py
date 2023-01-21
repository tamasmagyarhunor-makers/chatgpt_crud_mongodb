from fastapi import FastAPI

app = FastAPI()

@app.get("/cars/{car_id}")
async def read_car(car_id: str):
    return await CarController.get(car_id)

@app.post("/cars")
async def create_car(car: CarModel):
    return await CarController.create(car)

@app.put("/cars/{car_id}")
async def update_car(car_id: str, car: CarModel):
    return await CarController.update(car_id, car)

@app.delete("/cars/{car_id}")
async def delete_car(car_id: str):
    return await CarController.delete(car_id)
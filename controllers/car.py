from typing import Dict, List
import pymongo

class CarController:

    @staticmethod
    async def get(car_id: str) -> Dict:
        car = await CarModel.find_one(car_id)
        return car

    @staticmethod
    async def create(car: CarModel) -> Dict:
        await car.save()
        return car.to_dict()

    @staticmethod
    async def update(car_id: str, car: CarModel) -> Dict:
        await CarModel.update(car_id, car)
        return await CarModel.find_one(car_id)

    @staticmethod
    async def delete(car_id: str) -> Dict:
        return await CarModel.delete_one(car_id)

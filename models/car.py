import pymongo
from typing import Dict

class CarModel:
    collection = pymongo.MongoClient().db.cars

    def __init__(self, car_id: str, make: str, model: str, year: int, color: str):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def to_dict(self)-> Dict:
        return vars(self)

    @staticmethod
    async def find_one(car_id: str) -> Dict:
        car = CarModel.collection.find_one({'car_id': car_id})
        return car

    @staticmethod
    async def update(car_id: str, car: Dict) -> None:
        CarModel.collection.update_one({'car_id': car_id}, {'$set': car})

    @staticmethod
    async def delete_one(car_id: str) -> Dict:
        return CarModel.collection.delete_one({'car_id': car_id})

    async def save(self):
        CarModel.collection.insert_one(self.to_dict())

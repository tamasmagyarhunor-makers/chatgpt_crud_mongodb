from typing import Dict, List
from models.car import CarModel

class CarController:
    @staticmethod
    async def get(car_id: str) -> Dict:
        car = CarModel.get(car_id)
        return car.to_dict() if car else {}
    
    @staticmethod
    async def get_all() -> List[Dict]:
        cars = CarModel.get_all()
        return [car.to_dict() for car in cars]

    @staticmethod
    async def create(car: Dict) -> Dict:
        return CarModel.create(car)
    
    @staticmethod
    async def update(car_id: str, car: Dict) -> Dict:
        return CarModel.update(car_id, car)
    
    @staticmethod
    async def delete(car_id: str) -> Dict:
        return CarModel.delete(car_id)

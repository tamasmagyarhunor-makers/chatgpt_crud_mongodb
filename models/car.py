from pymongo import MongoClient
from bson.objectid import ObjectId

class CarModel:
    collection = None
    def __init__(self, make: str, model: str, year: int, color: str):
        self._id = ObjectId()
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def to_dict(self):
        return {
            "_id": str(self._id),
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "color": self.color
        }

    @staticmethod
    def create_mongodb_client(uri: str):
        client = MongoClient(uri)
        CarModel.collection = client["your_database_name"]["your_collection_name"]
        
    @staticmethod
    def create(car: dict):
        return CarModel.collection.insert_one(car)
    
    @staticmethod
    def get(car_id: str):
        return CarModel.collection.find_one({"_id": ObjectId(car_id)})
    
    @staticmethod
    def get_all():
        cars_data = list(CarModel.collection.find({}))
        cars = [CarModel(**car_data) for car_data in cars_data]
        return cars
    
    @staticmethod
    def update(car_id: str, car: dict):
        return CarModel.collection.update_one({"_id": ObjectId(car_id)}, {"$set": car})
    
    @staticmethod
    def delete(car_id: str):
        return CarModel.collection.delete_one({"_id": ObjectId(car_id)})

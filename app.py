from fastapi import FastAPI
import pymongo

from routing import app
from controllers import CarController
from models import CarModel

def create_mongodb_client(uri: str):
    client = pymongo.MongoClient(uri)
    CarModel.collection = client.db.cars # set the collection for the model
    return client

if __name__ == '__main__':
    client = create_mongodb_client("mongodb://localhost:27017/")
    app.run(host="0.0.0.0", port=8000)

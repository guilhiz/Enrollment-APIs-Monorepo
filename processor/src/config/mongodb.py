from typing import Dict

from decouple import config
from pymongo import MongoClient


class DBManager:
    def __init__(self):
        self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
            config("MONGO_USER"),
            config("MONGO_PASSWORD"),
            config("MONGO_HOST"),
            config("MONGO_PORT"),
        )
        self.__client = MongoClient(self.__connection_string)
        self.__db = self.__client["enrollmentDB"]

    def _get_collection(self, collection_name):
        return self.__db[collection_name]

    def list_items(self, collection_name="age_groups"):
        collection = self._get_collection(collection_name)
        return collection.find()

    def upsert_item(self, item: Dict, collection_name="enrollments"):
        collection = self._get_collection(collection_name)
        collection.update_one(
            {"cpf": item["cpf"]},
            {"$set": item},
            upsert=True,
        )

db_manager = DBManager()

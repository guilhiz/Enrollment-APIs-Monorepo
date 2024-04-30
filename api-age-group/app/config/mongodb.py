from typing import Dict

from bson import ObjectId
from pymongo import MongoClient

from app.schemas.age_group import convert_age_group, convert_age_groups


class DBManager:
    def __init__(self):
        self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
            "root",
            "password",
            "mongodb",
            "27017",
        )
        self.__client = MongoClient(self.__connection_string)
        self.__db = self.__client["enrollmentDB"]

    def _get_collection(self, collection_name):
        return self.__db[collection_name]

    def read_item(self, item_id, collection_name="age_groups"):
        collection = self._get_collection(collection_name)
        item = collection.find_one({"_id": item_id})
        return convert_age_group(item)

    def list_items(self, collection_name="age_groups"):
        collection = self._get_collection(collection_name)
        items = collection.find()
        return convert_age_groups(items)

    def add_item(self, item: Dict, collection_name="age_groups"):
        collection = self._get_collection(collection_name)
        result = collection.insert_one(item)
        return self.read_item(result.inserted_id, collection_name)

    def delete_item(self, item_id: str, collection_name="age_groups"):
        collection = self._get_collection(collection_name)
        result = collection.find_one_and_delete({"_id": ObjectId(item_id)})
        return result

    def count_items(self, collection_name="age_groups"):
        collection = self._get_collection(collection_name)
        return collection.count_documents({})

    def populate_db(self, collection_name="age_groups"):
        if self.count_items(collection_name) == 0:
            self._get_collection(collection_name).insert_many(
                [
                    {"min_age": 1, "max_age": 10},
                    {"min_age": 11, "max_age": 20},
                    {"min_age": 21, "max_age": 30},
                    {"min_age": 31, "max_age": 40},
                ]
            )


db_manager = DBManager()
db_manager.populate_db()

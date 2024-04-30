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
        self.__age_collection = self.__db["age_groups"]

    def read_item(self, item_id):
        age_group = self.__age_collection.find_one({"_id": item_id})
        return convert_age_group(age_group)

    def list_items(self):
        age_groups = self.__age_collection.find()
        return convert_age_groups(age_groups)

    def add_item(self, item: Dict):
        result = self.__age_collection.insert_one(item)
        return self.read_item(result.inserted_id)

    def delete_item(self, item_id: str):
        result = self.__age_collection.find_one_and_delete({"_id": ObjectId(item_id)})
        return result

    def count_items(self):
        return self.__age_collection.count_documents({})

    def populate_db(self):
        if self.count_items() == 0:
            self.__age_collection.insert_many(
                [
                    {"min_age": 1, "max_age": 10},
                    {"min_age": 11, "max_age": 20},
                    {"min_age": 21, "max_age": 30},
                    {"min_age": 31, "max_age": 40},
                ]
            )


db_manager = DBManager()
db_manager.populate_db()

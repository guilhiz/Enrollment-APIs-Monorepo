from typing import Dict

from pymongo import MongoClient

from app.schemas.enrollment import convert_enrollment, convert_enrollments


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

    def read_item(self, query: Dict, collection_name="enrollments"):
        collection = self._get_collection(collection_name)
        item = collection.find_one(query)
        if item is None:
            return None
        return convert_enrollment(item)

    def count_items(self, collection_name="enrollments"):
        collection = self._get_collection(collection_name)
        return collection.count_documents({})

    def populate_db(self, collection_name="enrollments"):
        if self.count_items(collection_name) == 0:
            self._get_collection(collection_name).insert_many(
                [
                    {"name": "John Doe", "cpf": "12345678901", "age": 9, "enrollment_status": "active"},
                    {"name": "Jane Doe", "cpf": "12345678902", "age": 19, "enrollment_status": "active"},
                    {"name": "Joe Doe", "cpf": "12345678903", "age": 29, "enrollment_status": "active"},
                    {"name": "Jill Doe", "cpf": "12345678904", "age": 39, "enrollment_status": "active"}
                ]
            )


db_manager = DBManager()
db_manager.populate_db()

from pymongo import MongoClient

client = MongoClient("mongodb://root:password@mongodb:27017/")
db = client["enrollmentDB"]

# Criação de collections
ageCollection = db["age_groups"]
enrollmentCollection = db["enrollments"]

if ageCollection.count_documents({}) == 0:
    min_list = [1, 11, 21, 31]
    max_list = [10, 20, 30, 40]

    for idx in range(4):
        group_age = {
            "min_age": min_list[idx],
            "max_age": max_list[idx],
        }
        ageCollection.insert_one(group_age)

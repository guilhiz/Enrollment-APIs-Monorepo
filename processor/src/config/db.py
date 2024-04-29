from pymongo import MongoClient

client = MongoClient("mongodb://root:password@mongodb:27017/")
db = client["enrollmentDB"]

# Criação de collections
ageCollection = db["age_groups"]
enrollmentCollection = db["enrollments"]

from pymongo import MongoClient

client = MongoClient("mongodb://root:password@mongodb:27017/")
db = client["enrollmentDB"]

# Criação de collections
ageCollection = db["age_groups"]
enrollmentCollection = db["enrollments"]

if enrollmentCollection.count_documents({}) == 0:
    name = ["John Doe", "Jane Doe", "Joe Doe", "Jill Doe"]
    cpf = ["12345678901", "12345678902", "12345678903", "12345678904"]
    age = [9, 19, 29, 39]
    enrollment_status = ["active", "active", "active", "active"]

    for idx in range(4):
        enrollment = {"name": name[idx], "cpf": cpf[idx], "age": age[idx], "enrollment_status": enrollment_status[idx]}
        enrollmentCollection.insert_one(enrollment)

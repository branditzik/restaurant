from pymongo import MongoClient;

client = MongoClient()
db = client.restaurant

if db :
  collection = db.garnitures
  garnitures = collection.find()
  for garniture in garnitures:
    print(garniture['name'])

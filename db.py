from pymongo import MongoClient;

client = MongoClient()
db = client.restaurant

if db :
  collection = db.sauces
  sauces = collection.find()
  for sauce in sauces:
    print(sauce['name'])
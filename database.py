from pymongo import MongoClient
import json

conn_str = "mongodb+srv://rahul:rahul@cluster0.rb9pz.mongodb.net/covid?retryWrites=true&w=majority"

client = MongoClient(conn_str)
# print(client.list_database_names())

db = client['covid']
# print(db.list_collection_names())

bedrequests = db['bedrequests']

def upload_json():
    with open('data.json','r') as f:
        data = json.load(f)

    bedrequests.insert_one(data)

# clear_data()
# upload_json()
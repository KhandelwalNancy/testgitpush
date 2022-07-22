import pymongo

client = pymongo.MongoClient("mongodb+srv://NancyKhandelwal:toni$784@cluster0.efvmb.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
import pymongo

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

print('-----------')
print(mydb)
print('-----------')
print(myclient.list_database_names())


mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(mydb.list_collection_names())
print('-----------')
x = mycol.find_one()

print(x)
print('-----------')
myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
print('-----------')
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)
print('-----------')

for x in mycol.find({},{ "address": 0 }):
  print(x)
print('-----------')

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
print('-----------')
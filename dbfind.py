import pymongo

#connection = pymongo.MongoClient("mongodb://localhost")
connection = pymongo.MongoClient("mongodb+srv://MongoBKWSU:Spring2019Databass@mongobkwsu-ljuj6.gcp.mongodb.net/test?retryWrites=true")

db = connection.test
users = db.users

doc = {'firstName': 'Briank','lastName':'Klein'}
print(doc)
print("about to insert the document")

try:
    users.insert_one(doc)
except Exception as e:
    print("insert failed", e)

print("insert succeeded: ")
print(doc)

#find all results
#results = users.find()

#find all results where firstName = "Brian"
#results = users.find({'firstName': 'Brian'})

#find all results where first name is a regular expression and starts with "B"
results = users.find({'firstName': {"$regex": "^B"}})

for entry in results:
    print(entry)
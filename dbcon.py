import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstName': 'Brian','lastName':'Klein'}
print(doc)
print("about to insert the document")

try:
    users.insert_one(doc)
except Exception as e:
    print("insert failed", e)

print("insert succeeded: ")
print(doc)
from pymongo import MongoClient
client = MongoClient()

db = client['video']                 # I already created this on my local
collection = db['movies']            # and this too, but if you don't it

documents = collection.find()        # select * from 'movies'

print("All the current documents in our collection:")
for doc in documents:
    print(doc)
    
new_item = {"title": "Planet of the Apes",
            "year": 1975,
            "imdb": "tt1234543210"}

#collection.insert_one(new_item)   #add item
#collection.delete_one(new_item)   #remove item

print("The row we just inserted:")
one_doc = collection.find_one({"year": 1975})
print(one_doc)
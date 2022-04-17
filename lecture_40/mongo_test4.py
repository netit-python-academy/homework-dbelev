import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.python_course

# write the title of all documents

for doc in db.todos.find({'priority':1}, {'title':1}):
    print(doc['title'])
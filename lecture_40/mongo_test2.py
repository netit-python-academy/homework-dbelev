from pymongo import MongoClient

# ------------------------- Connect to MongoDB Server ------------------------ #
client = MongoClient("mongodb://localhost:27017")

# ----------------------- Switch context to a database ----------------------- #
# get "python_course" database:
db = client.python_softacad

# ------------------- Show all Collections in the database: ------------------ #
# get all collections in "python_course ":
collections = db.list_collection_names()
print(collections)

## insert a new document into "todos" collection:
#res = db.todos.insert_one({"title": "Learn MongoDB", "done": False})
## get the id of the inserted document:
#print(res.inserted_id)

# insert multiple documents into "todos" collection:
res = db.todos.insert_many([
    {"title": "Learn Python", "done": True},
    {"title": "Learn Flask", "done": False},
    {"title": "Learn Flask-MongoDB", "done": False}
])
print(res.inserted_ids)

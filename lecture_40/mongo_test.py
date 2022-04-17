from pymongo import MongoClient

def connect_to_local_cluster():
  # connect using connection string:
  # 'mongodb://<username?>:<password?>@localhost:27017/<dbname?>
  connection_string = 'mongodb://localhost:27017/python_softacad'

  return MongoClient(connection_string)


def connect_to_atlas_cluster():
  # connect using connection string:
  # mongodb+srv://<username>:<password>@cluster0.xm0yw.mongodb.net/<dbname?>
  connection_string = 'mongodb+srv://donislav:XUKn!Hq6RkJYPJB@cluster0.chonl.mongodb.net/python_softacad'

  return MongoClient(connection_string)

atlas_client = connect_to_atlas_cluster()
local_client = connect_to_local_cluster()

print(atlas_client)
print(local_client)
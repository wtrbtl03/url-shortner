from pymongo import MongoClient


conn_str = "mongodb://localhost:27017"

client = MongoClient(conn_str)
db = client['urls']
collection = db['mappings']

data = {
    "map_of" : "https://twitter.com/",
    "map_to" : "twitter"
}
collection.insert_one(data)
# print(get_db_handle('urls', 'localhost', '27017', '', ''))

from django.shortcuts import redirect, HttpResponse
from pymongo import MongoClient

CONN_STR = "mongodb://localhost:27017"

CLIENT = MongoClient(CONN_STR)
DB_NAME = 'mappings'
DB = CLIENT[DB_NAME]
COLLECTION_NAME = 'maps'
COLLECTION = DB[COLLECTION_NAME]
ERROR_PAGE = 'home.views.test'
# ERROR_PAGE = 'home.views.not_found'


def resolve(request, map_str):
    try:
        document = COLLECTION.find_one({"map_to":  map_str})
        target_URL = document["map_of"]
        return redirect(target_URL)
    except:
        return redirect(ERROR_PAGE)

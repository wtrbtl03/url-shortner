from django.shortcuts import render, HttpResponse
from .input_field_form import InputField
from pymongo import MongoClient
import random
import hashlib

CHARSET_BASE62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz0123456789"

CONN_STR = "mongodb://localhost:27017"

CLIENT = MongoClient(CONN_STR)
DB_NAME = 'mappings'
DB = CLIENT[DB_NAME]
COLLECTION_NAME = 'maps'
COLLECTION = DB[COLLECTION_NAME]

def fetch_input_url(request):
    # [TODO] add validation
    map = request.POST.get('input_url')
    return map

def encode_url(url):
    salt = str(random.randint(0, 1234))
    salted_url = url + salt
    encoded_text = hashlib.sha3_256(salted_url.encode('UTF-8'))
    encoded_url = encoded_text.hexdigest()
    return encoded_url

def get_map(request):
    url = fetch_input_url(request)
    hash = encode_url(url)
    new_document = {'map_of' : url,
                    'map_to' : hash}
    COLLECTION.insert_one(new_document)
    return HttpResponse(f"Done at : localhost:8000/{hash}")
    

# def get_map(request):
#     url = fetch_input_url(request)
    
#     return HttpResponse(url)
    

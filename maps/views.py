from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
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
    map = request.GET.get('input_url')
    return map


def encode_url(url):
    # placeholder encoding
    salt = str(random.randint(0, 1234))
    salted_url = url + salt
    encoded_text = hashlib.sha3_256(salted_url.encode('UTF-8'))
    encoded_url = encoded_text.hexdigest()
    return encoded_url


def get_short(request):
    url = fetch_input_url(request)
    hash = encode_url(url)[:5]
    domain_name = "localhost:8000"
    shortned_url = domain_name+'/'+hash
    new_document = {'map_of': url,
                    'map_to': hash}
    COLLECTION.insert_one(new_document)
    response = {'shortned_url': shortned_url}
    return JsonResponse(response)

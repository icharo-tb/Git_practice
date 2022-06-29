from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(
        '<h1>Welcome to my Django and MongoDB practice <u>Django App</u> Project_1</h1>'
    )

import pymongo
from django.conf import settings

connection_string = 'mongodb+srv://Icharo-tb:abcdefg@clustericharo.cl5p9.mongodb.net/?retryWrites=true&w=majority'
my_client = pymongo.MongoClient(connection_string)

db_name = my_client
collection_name = db_name['info']
collection_info = collection_name.find({})
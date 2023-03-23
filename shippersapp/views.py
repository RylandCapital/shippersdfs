import os 
import pymongo

from dotenv import load_dotenv

from django.shortcuts import render
from django.http import HttpResponse

load_dotenv()
MONGO = os.getenv("MONGO")



# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")

# Create your views here.
client = pymongo.MongoClient(MONGO)


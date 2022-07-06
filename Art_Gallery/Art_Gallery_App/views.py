from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse
# import models from models.py
from .models import *
from django.forms.models import model_to_dict
# Create your views here.
# Art Gallery App views.py

def index(request):
    # dynamically access and fetch Portrait data from db or admin actions
    paintingObjects = Portrait.objects.all()
    # pass the other images as a dictionary
    galleryObjects = Portrait.objects.values(
        'painting_left',
        'painting_right',
        'painting_top',
        'painting_bottom',
        'painting_back'
        )[0]

    context = {
        'paintingObjects': paintingObjects,
        'galleryObjects' : galleryObjects
    }


    # display  index.html file in templates folder with data 
    return render(request, "index.html", context)

# ajax
def getPortraitData(request):
    pass

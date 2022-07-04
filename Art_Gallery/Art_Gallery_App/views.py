from django.shortcuts import render
from django.http import JsonResponse
# import Portrait class from models.py
from .models import Portrait
from django.forms.models import model_to_dict
# Create your views here.
# Art Gallery App views.py

def index(request):
    # dynamically access and fetch Portrait data from db or admin actions
    paintingObjects = Portrait.objects.all()
    # display  index.html file in templates folder with data 
    return render(request, "index.html",{'paintingObjects': paintingObjects})

# ajax
def getPortraitData(request):
    context = {}
    paintingObjects = Portrait.objects.values()
    context[paintingObjects] = Portrait.objects.all()

    if request.method == 'POST' and request.is_ajax():
        print('hello')

        ID = request.POST.get('id')
        paintingInstance = paintingObjects.get(pk=ID)  # So we send the company instance
        painting_name = Portrait.objects.get(pk=ID).marca # to have the related fields - marca
        painting_name = model_to_dict(painting_name) # better in dict
        painting_name = painting_name['painting'] # to define marca for the product

        return JsonResponse({ 'paintingInstance' : paintingInstance, 'painting' : painting_name})

    # paintingObjects = Portrait.objects.all()
    # # json response
    # return JsonResponse({"paintingObjects":list(paintingObjects.values())})

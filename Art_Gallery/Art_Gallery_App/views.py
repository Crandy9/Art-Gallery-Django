from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .models import *
from django.core import serializers

def index(request, pk=None):
    # dynamically access and fetch Portrait data from db or admin actions
    paintingObjects = Portrait.objects.all()
    # returns <QuerySet [<Portrait: NEW TEST>, <Portrait: TEST 2>]>
    context = {
        'paintingObjects': paintingObjects
    }


    # display  index.html file in templates folder with data 
    return render(request, "index.html", context)

def carousel(request, pk=None):

    if request.method == 'GET':
        # get the specific object by its pk
        # exclude empty or null values
        carouselObjects = Portrait.objects.get(pk=pk)
        # get query set of all image fields
        carouselImageObjects = Portrait.objects.filter(id=pk).values(
            'painting',
            'painting_back',
            'painting_bottom',
            'painting_left',
            'painting_right',
            'painting_top')
        # returns something like:
        '''
        <QuerySet [{
            'painting': 'paintings/painting2Main.png', 
            'painting_back': '0', 
            'painting_bottom': '0', 
            'painting_left': 'carousel_paintings/painting2.1.png', 
            'painting_right': 'carousel_paintings/painting2.2.png', 
            'painting_top': 'carousel_paintings/painting2.3.png'
        }]>

        '''
        # remove columns whose values are 0
        carouselImageObjects = [{r:c for r,c in row.items() if c != '0'} for row in carouselImageObjects]
        # returns a list of a dictionary of images like:
        '''
        [{
            'painting': 'paintings/painting2Main.png', 
            'painting_left': 'carousel_paintings/painting2.1.png', 
            'painting_right': 'carousel_paintings/painting2.2.png', 
            'painting_top': 'carousel_paintings/painting2.3.jpg'
        }]
        '''
        # convert it from list to dictionary
        carouselImageObjects = carouselImageObjects[0]
        # returns a dictionary
        '''
        {
            'painting': 'paintings/painting2Main.png', 
            'painting_left': 'carousel_paintings/painting2.1.png', 
            'painting_right': 'carousel_paintings/painting2.2.png', 
            'painting_top': 'carousel_paintings/painting2.3.jpg'
        }
        '''
        # convert dictionary values to a list
        carousel_list = list(carouselImageObjects.values())
        # returns a list
        '''
        [
            'paintings/painting2Main.png', 
            'carousel_paintings/painting2.1.png', 
            'carousel_paintings/painting2.2.png', 
            'carousel_paintings/painting2.3.jpg'
            ]
        '''

        # return both carousel object and carousel list
        context = {
            'carouselObjects': carouselObjects
        }

        # return the data with the specific object data
        return render(request, "carousel.html", context)

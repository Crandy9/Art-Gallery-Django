from django.shortcuts import render

# import Portraits class from models.py
from .models import Portraits
# Create your views here.
# Art Gallery App views.py

def index(request):
    # Portraits object
    # normally, all of this data would be fetched from a database
    # and we wouldn't populate each object manually like this
    """
    Manually entered data COMMENTED OUT TO MAKE WAY FOR DYNAMICALLY
    ADDING DATA
     dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'Welcome to Sendai, city of TREEES'
    dest1.price = 5000
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Indonesia'
    dest2.desc = 'Muk use acid, muk use acid acid'
    dest2.price = 900
    dest2.img = 'destination_2.jpg'
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'San Francisco'
    dest3.desc = 'When ya ride the train, watch out for crackheads'
    dest3.price = 1
    dest3.img = 'destination_3.jpg'
    dest3.offer = True
    
    # create an object to hold all of the objects
    # useful for iterating over and displaying each unique object on page
    # see index.html line 290
    dests = [dest1, dest2, dest3]

    # passing objects to index.html
    return render(request, "index.html", 
        # passing dictionaries as objects to index.html
        # {   'dest1': dest1,
        #     'dest2': dest2,
        #     'dest3': dest3
        #     }

        # OR pass the dests list which contains all of the objects
        {'dests': dests}
        )
    """
    # dynamically access and fetch Portrait data from db or admin actions
    paintingObjects = Portraits.objects.all()
    # display  index.html file in templates folder with data 
    return render(request, "index.html",{'paintingObjects': paintingObjects})
    
    
        

from django.db import models

#Art_Gallery_app models.py

# Create your models here for dbs.
# can create classes/objects here

# instantiate these objects in views.py
# class alone is not a model, it is only a simple class
# to convert class to model, specify model in params (models.Model)
class Portraits(models.Model):
    # uninitialized class variables 
    # primary char var
    # id: int id not needed when migrating models to db, 
    # primary key will be automatically created

    # object characteristics which will be columns in db
    # to accurately specify each type of field (string, numbers, emails etc.), follow
    # django doc reference https://docs.djangoproject.com/en/4.0/ref/models/fields/
    # remove colons : and use equals = to create columns in database table
    name = models.CharField(max_length= 100)

    # make sure to pip install pillow before attempting migration
    # creates filechooser on admin page, images can be from any dir in host machine
    # pics is the folder name where images will be placed uner media folder
    img = models.ImageField(upload_to= 'pics')
    desc = models.TextField()
    price = models.IntegerField()

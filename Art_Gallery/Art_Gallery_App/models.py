from email.policy import default
from django.db import models

#Art_Gallery_app models.py

# Create your models here for dbs.
# can create classes/objects here

# instantiate these objects in views.py
# class alone is not a model, it is only a simple class
# to convert class to model, specify model in params (models.Model)
# give it a singular object name not plural admin appends an (s) to end of model name.
class Portrait(models.Model):

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
    # pics is the folder name where images will be placed under media folder uploaded to paintings subfolder
    # painting field was originally called destinations and upload_to= 'pics'
    # when renaming, I had to delete the pics folder manually and re-upload the images from computer.
    main_painting = models.ImageField(default=0, upload_to= 'paintings', null=True,blank=True)
    long_description = models.TextField()
    short_description = models.TextField(default=0)
    # extra paintings not required
    painting_2 = models.ImageField(default=0, upload_to= 'carousel_paintings', null=True,blank=True)
    painting_3 = models.ImageField(default=0, upload_to= 'carousel_paintings', null=True,blank=True)
    painting_4 = models.ImageField(default=0, upload_to= 'carousel_paintings', null=True,blank=True)
    painting_5 = models.ImageField(default=0, upload_to= 'carousel_paintings', null=True,blank=True)
    painting_6 = models.ImageField(default=0, upload_to= 'carousel_paintings', null=True,blank=True)
    painting_7 = models.ImageField(default=0, upload_to= 'carousel_paintings', null=True,blank=True)
    painting_8 = models.ImageField(default=0, upload_to= 'carousel_paintings', null=True,blank=True)
    painting_9 = models.ImageField(default=0, upload_to= 'carousel_paintings', null=True,blank=True)
    painting_10 = models.ImageField(default=0, upload_to= 'carousel_paintings', null=True,blank=True)
    # price
    price = models.IntegerField()
    japan_shipping_price = models.IntegerField(default=0, null=True,blank=True)
    dollar_price = models.DecimalField(default =0, max_digits=10, decimal_places=2, blank=True)
    usa_shipping_price = models.IntegerField(default=0, null=True,blank=True)


    # English data
    english_name = models.CharField(default=0,max_length= 100)
    english_long_description = models.TextField(default=0, null=True,blank=True)
    english_short_description = models.TextField(default=0, null=True,blank=True)
    # size in centimeters
    cm_size = models.CharField(default=0,max_length= 100, null=True,blank=True)
    # inches
    in_size = models.CharField(default=0,max_length= 100, null=True,blank=True)
    # is sold label
    is_sold = models.BooleanField(default=False)
    # name the objects in admin page using the name attribute
    def __str__(self):
        return self.name

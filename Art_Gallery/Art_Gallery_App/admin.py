from django.contrib import admin
from .models import *
# Register your models here.
# after registering models, django will automatically create page
# in admin page

# this is really cool because in the admin page you can add data for
# each of the fields you created in your models.py class object
# readonly_fields = ['uuid']
# admin.site.register(Portrait)
@admin.register(Portrait)
class AdminClassName(admin.ModelAdmin):
    readonly_fields = ['uuid']
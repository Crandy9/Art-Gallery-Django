# Generated by Django 4.0.5 on 2022-08-23 06:41

from django.db import migrations, models
import uuid

def gen_uuid(apps, schema_editor):
    # if it doesn't work use portrait and try again
    MyModel = apps.get_model('Art_Gallery_App', 'Portrait')
    for row in MyModel.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])

class Migration(migrations.Migration):

    dependencies = [
        ('Art_Gallery_App', '0005_portrait_uuid'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]

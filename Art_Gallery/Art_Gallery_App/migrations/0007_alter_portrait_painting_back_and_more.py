# Generated by Django 4.0.5 on 2022-07-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Art_Gallery_App', '0006_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portrait',
            name='painting_back',
            field=models.ImageField(upload_to='carousel_paintings'),
        ),
        migrations.AlterField(
            model_name='portrait',
            name='painting_bottom',
            field=models.ImageField(upload_to='carousel_paintings'),
        ),
        migrations.AlterField(
            model_name='portrait',
            name='painting_left',
            field=models.ImageField(upload_to='carousel_paintings'),
        ),
        migrations.AlterField(
            model_name='portrait',
            name='painting_right',
            field=models.ImageField(upload_to='carousel_paintings'),
        ),
        migrations.AlterField(
            model_name='portrait',
            name='painting_top',
            field=models.ImageField(upload_to='carousel_paintings'),
        ),
    ]
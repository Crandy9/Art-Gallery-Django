# Generated by Django 4.0.5 on 2022-07-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Art_Gallery_App', '0002_alter_portrait_painting_alter_portrait_painting_back_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portrait',
            name='painting',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='paintings'),
        ),
        migrations.AlterField(
            model_name='portrait',
            name='painting_back',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='carousel_paintings'),
        ),
        migrations.AlterField(
            model_name='portrait',
            name='painting_bottom',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='carousel_paintings'),
        ),
        migrations.AlterField(
            model_name='portrait',
            name='painting_left',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='carousel_paintings'),
        ),
        migrations.AlterField(
            model_name='portrait',
            name='painting_right',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='carousel_paintings'),
        ),
        migrations.AlterField(
            model_name='portrait',
            name='painting_top',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='carousel_paintings'),
        ),
    ]
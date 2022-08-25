# Generated by Django 4.0.5 on 2022-08-23 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Art_Gallery_App', '0003_portrait_japan_shipping_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portrait',
            name='usa_shipping_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]
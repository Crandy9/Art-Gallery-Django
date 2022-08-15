# Generated by Django 4.0.5 on 2022-08-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_account_email_remove_account_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='country',
            field=models.CharField(choices=[('JP', 'Japan'), ('US', 'United States')], default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='postal_code',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='state_prefecture',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='street1',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='street2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 4.0.5 on 2022-08-12 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_password_account_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
    ]

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

# first time migrating, specify app like: python manage.py makemigrations account
# account model to extend the User model for adding mailing addresses
# and other contact info

class Account(models.Model):
    # when a User is deleted, this account will be deleted, the opposite is not true
    # this generates a user_id field whose value is the pk of this same user in the auth_user table
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # phone_number field
    phone_number = PhoneNumberField()
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_account(sender, instance, **kwargs):
#     instance.accounts.save()
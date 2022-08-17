from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _

COUNTRIES = (
    ('JP','日本'),
    ('US', 'United States'),
)

PREFECTURES = {
    ('Hokkaido','北海道'),
    ('Aomori','青森県'),
    ('Iwate','岩手県'),
    ('Miyagi','宮城県'),
    ('Akita','秋田県'),
    ('Yamagata','山形県'),
    ('Fukushima','福島県'),
    ('Ibaraki','茨城県'),
    ('Tochigi','栃木県'),
    ('Gunma','群馬県'),
    ('Saitama','埼玉県'),
    ('Chiba','千葉県'),
    ('Tokyo','東京都'),
    ('Kanagawa','神奈川県'),
    ('Niigata','新潟県'),
    ('Toyama','富山県'),
    ('Ishikawa','石川県'),
    ('Fukui','福井県'),
    ('Yamanashi','山梨県'),
    ('Nagano','長野県'),
    ('Gifu','岐阜県'),
    ('Shizuoka','静岡県'),
    ('Aichi','愛知県'),
    ('Mie','三重県'),
    ('Shiga','滋賀県'),
    ('Kyoto','京都府'),
    ('Osaka','大阪府'),
    ('Hyogo','兵庫県'),
    ('Nara','奈良県'),
    ('Wakayama','和歌山県'),
    ('Tottori','鳥取県'),
    ('Shimane','島根県'),
    ('Okayama','岡山県'),
    ('Hiroshima','広島県'),
    ('Yamaguchi','山口県'),
    ('Tokushima','徳島県'),
    ('Kagawa','香川県'),
    ('Ehime','愛媛県'),
    ('Kochi','高知県'),
    ('Fukuoka','福岡県'),
    ('Saga','佐賀県'),
    ('Nagasaki','長崎県'),
    ('Kumamoto','熊本県'),
    ('Oita','大分県'),
    ('Miyazaki','宮崎県'),
    ('Kagoshima','鹿児島県'),
    ('Okinawa	','沖縄県'),
}

STATES = (
    ('Armed Forces','Armed Forces - AA'),
    ('Armed Forces Europe','Armed Forces Europe - AE'),
    ('Armed Forces Pacific','Armed Forces Pacific - AP'),
    ('Alabama','Alabama'),
    ('Alaska','Alaska'),
    ('Arizona','Arizona'),
    ('Arkansas','Arkansas'),
    ('California','California'),
    ('Colorado','Colorado'),
    ('Connecticut','Connecticut'),
    ('Delaware','Delaware'),
    ('District of Columbia', 'District of Columbia'),
    ('Florida','Florida'),
    ('Georgia','Georgia'),
    ('Hawaii','Hawaii'),
    ('Idaho','Idaho'),
    ('Illinois','Illinois'),
    ('Indiana','Indiana'),
    ('Iowa','Iowa'),
    ('Kansas','Kansas'),
    ('Kentucky','Kentucky'),
    ('Louisiana','Louisiana'),
    ('Maine','Maine'),
    ('Maryland','Maryland'),
    ('Massachusetts','Massachusetts'),
    ('Michigan','Michigan'),
    ('Minnesota','Minnesota'),
    ('Mississippi','Mississippi'),
    ('Missouri','Missouri'),
    ('Montana','Montana'),
    ('Nebraska','Nebraska'),
    ('Nevada','Nevada'),
    ('New Hampshire','New Hampshire'),
    ('New Jersey','New Jersey'),
    ('New Mexico','New Mexico'),
    ('New York','New York'),
    ('North Carolina','North Carolina'),
    ('North Dakota','North Dakota'),
    ('Ohio','Ohio'),
    ('Oklahoma','Oklahoma'),
    ('Oregon','Oregon'),
    ('Pennsylvania','Pennsylvania'),
    ('Rhode Island','Rhode Island'),
    ('South Carolina','South Carolina'),
    ('South Dakota','South Dakota'),
    ('Tennessee','Tennessee'),
    ('Texas','Texas'),
    ('Utah','Utah'),
    ('Vermont','Vermont'),
    ('Virgin Islands','Virgin Islands'),
    ('Virginia','Virginia'),
    ('Washington','Washington'),
    ('West Virginia','West Virginia'),
    ('Wisconsin','Wisconsin'),
    ('Wyoming','Wyoming'),
    ('Guam','Guam'),
    ('Puerto Rico', 'Puerto Rico'),
)


# first time migrating, specify app like: python manage.py makemigrations account
# account model to extend the User model for adding mailing addresses
# and other contact info
class Account(models.Model):
    # when a User is deleted, this account will be deleted, the opposite is not true
    # this generates a user_id field whose value is the pk of this same user in the auth_user table
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    # phone_number field japanese phone number format is +81-XXX-XXXX-XXXX
    # us format is: +1-XXX-XXX-XXXX 
    phone_number = models.CharField(max_length=14,blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    # Shipping Addresses:
    # US Shipping Address 
    street1 = models.CharField(max_length=100, blank=True)
    street2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(choices=COUNTRIES, max_length=2, blank=True, null=True)
    state = models.CharField(choices =STATES, max_length=50, blank=True, null=True)
    prefecture = models.CharField(choices=PREFECTURES, max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True)
    address_entered = models.BooleanField(default=False)


    def __str__(self):
        # return str(self.user)
        return self.user.username

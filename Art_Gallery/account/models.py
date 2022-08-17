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

PREFECTURES = [
    ('Hokkaido','北海道 Hokkaido'),
    ('Aomori','青森県 Aomori'),
    ('Iwate','岩手県 Iwate'),
    ('Miyagi','宮城県 Miyagi'),
    ('Akita','秋田県 Akita'),
    ('Yamagata','山形県 Yamagata'),
    ('Fukushima','福島県 Fukushima'),
    ('Ibaraki','茨城県 Ibaraki'),
    ('Tochigi','栃木県 Tochigi'),
    ('Gunma','群馬県 Gunma'),
    ('Saitama','埼玉県 Saitama'),
    ('Chiba','千葉県 Chiba'),
    ('Tokyo','東京都 Tokyo'),
    ('Kanagawa','神奈川県 Kanagawa'),
    ('Niigata','新潟県 Niigata'),
    ('Toyama','富山県 Toyama'),
    ('Ishikawa','石川県 Ishikawa'),
    ('Fukui','福井県 Fukui'),
    ('Yamanashi','山梨県 Yamanashi'),
    ('Nagano','長野県 Nagano'),
    ('Gifu','岐阜県 Gifu'),
    ('Shizuoka','静岡県 Shizuoka'),
    ('Aichi','愛知県 Aichi'),
    ('Mie','三重県 Mie'),
    ('Shiga','滋賀県 Shiga'),
    ('Kyoto','京都府 Kyoto'),
    ('Osaka','大阪府 Osaka'),
    ('Hyogo','兵庫県 Hyogo'),
    ('Nara','奈良県 Nara'),
    ('Wakayama','和歌山県 Wakayama'),
    ('Tottori','鳥取県 Tottori'),
    ('Shimane','島根県 Shimane'),
    ('Okayama','岡山県 Okayama'),
    ('Hiroshima','広島県 Hiroshima'),
    ('Yamaguchi','山口県 Yamaguchi'),
    ('Tokushima','徳島県 Tokushima'),
    ('Kagawa','香川県 Kagawa'),
    ('Ehime','愛媛県 Ehime'),
    ('Kochi','高知県 Kochi'),
    ('Fukuoka','福岡県 Fukuoka'),
    ('Saga','佐賀県 Saga'),
    ('Nagasaki','長崎県 Nagasaki'),
    ('Kumamoto','熊本県 Kumamoto'),
    ('Oita','大分県 Oita'),
    ('Miyazaki','宮崎県 Miyazaki'),
    ('Kagoshima','鹿児島県 Kagoshima'),
    ('Okinawa','沖縄県 Okinawa'),
]

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

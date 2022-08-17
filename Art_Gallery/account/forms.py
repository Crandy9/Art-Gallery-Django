from importlib.abc import ExecutionLoader
from django import forms
from account.models import Account
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import re
from django.db import models


US_PHONE_NUM_REGEX = "^\d{3}(-)?\d{3}(-)?\d{4}$"
JPN_PHONE_NUM_REGEX = "^\d{3}(-)?\d{4}(-)?\d{4}$"
# create user form to update it along with account form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]

    def clean_first_name(self, *args, **kwargs):
        first_name = self.cleaned_data.get("first_name")
        # if len(first_name) == 0:
        if first_name is None or len(first_name) == 0:
        # if first_name is None:
            raise forms.ValidationError(_('名を入力してください'))
        else:
            return first_name
        

    def clean_last_name(self, *args, **kwargs):
        last_name = self.cleaned_data.get("last_name")
        if last_name is None or len(last_name) == 0:
            raise forms.ValidationError(_('姓を入力してください'))
        else:
            return last_name

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if email is None or len(email) == 0:
            raise forms.ValidationError(_('有効なメールアドレスを入力してください。(配達をサポートするために使用される可能性があります)'))
        else:
            return email
    
    # giving placeholder to email
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'email':
                field.widget.attrs["placeholder"] = _('メールアドレス')




# getting the rest of the user's data from the account model
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ['id','password','date_created','user']


    # need to validate US and/or Japanese phone number 
    def clean_phone_number(self, *args, **kwargs):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number is None or len(phone_number) == 0:
            raise forms.ValidationError(_('有効な電話番号を入力して下さい\n(配達をサポートするために使用される可能性があります)'))
        elif not re.search(US_PHONE_NUM_REGEX,phone_number) and not re.search(JPN_PHONE_NUM_REGEX,phone_number):
            raise forms.ValidationError(_('有効な電話番号を入力して下さい)'))
        else:
            return phone_number

    def clean_country(self, *args, **kwargs):
        country = self.cleaned_data.get("country")
        if country is None or len(country) == 0:
            raise forms.ValidationError(_('ドロップダウン メニューから国を選択してください'))
        else:
            return country

    def clean_state(self, *args, **kwargs):
        # if the country is Japan, state is not needed
        country = self.cleaned_data.get("country")
        print('country:'+str(country)+'\n')
        if country == 'JP':
            return
        state = self.cleaned_data.get("state")
        if state is None or len(state) == 0:
            raise forms.ValidationError(_('ドロップダウン メニューから州を選択してください'))
        else:
            return state

    def clean_prefecture(self, *args, **kwargs):
        # if the country is United States, state is not needed
        country = self.cleaned_data.get("country")
        if country == 'US':
            return
        prefecture = self.cleaned_data.get("prefecture")
        if prefecture is None or len(prefecture) == 0:
            raise forms.ValidationError(_('ドロップダウン メニューから府県を選択してください'))
        else:
            return prefecture

    def clean_street1(self, *args, **kwargs):
        street1 = self.cleaned_data.get("street1")
        if street1 is None or len(street1) == 0:
            raise forms.ValidationError(_('有効な住所を入力して下さい'))
        else:
            return street1

    def clean_city(self, *args, **kwargs):
        city = self.cleaned_data.get("city")
        if city is None or len(city) == 0:
            raise forms.ValidationError(_('有効な市区町村を入力して下さい'))
        else:
            return city

    def clean_postal_code(self, *args, **kwargs):
        postal_code = self.cleaned_data.get("postal_code")
        if postal_code is None or len(postal_code) == 0:
            raise forms.ValidationError(_('有効な郵便番号を入力して下さい'))
        else:
            return postal_code
    # make all textfields have form-control Bootstrap class
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)

        # setting order for prefecture dropdowns
        self.fields['prefecture'].queryset = Account.objects.order_by('prefecture')
        for field_name, field in self.fields.items():
            # giving placeholders to textfields
            if field_name == 'phone_number':
                field.widget.attrs["placeholder"] = _('例：000-0000-0000')
            if field_name == 'street1':
                field.widget.attrs["placeholder"] = _('住所')
            if field_name == 'street2':
                field.widget.attrs["placeholder"] = _('部屋番号')
            if field_name == 'city':
                field.widget.attrs["placeholder"] = _('例：〇〇市〇〇町')           
            if field_name == 'postal_code':
                field.widget.attrs["placeholder"] = _('例 ： 000-0000')

            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'


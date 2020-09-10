from django.core.validators import *
from django.forms import *


class UserForm(Form):
    username = CharField(label='Username', max_length=150)
    email = CharField(label='E-mail', max_length=150, validators=[validate_email])
    password = CharField(label='Password', max_length=150, widget=PasswordInput(), required=False)
    password_confirm = CharField(label='Confirm password', max_length=150, widget=PasswordInput(), required=False)

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['password_confirm']:
            self._errors["password"] = "Password do not match"
            del form_data['password']
        return form_data

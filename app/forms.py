from django import forms
from app.models import *

class UserModelForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widges={'password':forms.PasswordInput}
        help_texts={'username':''}


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','profile_pic']

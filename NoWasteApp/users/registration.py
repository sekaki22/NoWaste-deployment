from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from django.core import validators
import string

# Let's create a password validators

# def pw_validator (value):
#
#     digits = '1234567890'
#     symbols = string.punctuation
#     flag_digits = False
#     flag_symbols = False
#
#     for char in value:
#         if char in digits:
#             flag_digits = True
#         elif char in symbols:
#             flag_symbols = True
#
#     if flag_digits == False or flag_symbols == False or len(value) < 8:
#         raise forms.ValidationError("Your password should consist out of at least one digit, one symbol and should at least consist out of 8 characters")


# Building the registration model

class Signup (forms.ModelForm):
    password = forms.CharField ( widget=forms.PasswordInput)
    verify_pw = forms.CharField ( widget=forms.PasswordInput, label = "Double check your password")
    botcatcher = forms.CharField (required = False,
                                    widget = forms.HiddenInput)

    class Meta:
        model = User # Connect form to the database
        fields = ('username', 'first_name', 'last_name', 'email', 'password') # Include all the fields into the form

    # def clean (self):
    #         # This function graps all the data filled out in the forms
    #     all_clean_data = super().clean()
    #     pw = all_clean_data.get('pw')
    #     vpw = all_clean_data.get('verify_pw')
    #
    #     if pw != vpw:
    #         raise forms.ValidationError("Passwords are not matching! Please fill in matching passwords")

    def clean_botcatcher (self): # Keyword clean stands for a validation procedure
        botcatcher = self.cleaned_data ['botcatcher']

        if len (botcatcher) > 0:
            raise forms.ValidationError("BOT ERROR")

class IncludePic (forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        exclude = ('user',)

from django import forms
from app import models

#Authorization Form
class AuthUserForm(forms.ModelForm):
    class Meta:
        model = models.Accounts
        fields = ['usernameAcc', 'psswdAcc']
        widgets = {
            'usernameAcc': forms.TextInput(attrs={"class": "form-control form-auth__input"}),
            'psswdAcc': forms.PasswordInput(attrs={"class": "form-control form-auth__input"})
        }

#Register Form for Users
class RegistrationForm(forms.Form):
    reg_username = forms.CharField(label="Your username:",
                                   help_text="Please write username for this site",
                                   widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    reg_email = forms.EmailField(label="Your email:",
                                 help_text="Please, add the part '@example.com'",
                                 widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    reg_psswd = forms.CharField(label="Your password:",
                                help_text="Please write a password for your account",
                                widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))
    reg_chkpsswd = forms.CharField(label="Repeat your password:",
                                   help_text="Please, write password again and don't forget!",
                                   widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))
    regUserCompChoice = forms.ChoiceField(label="Who do you want to register?",
                                          choices=[(1, "User"), (2, "Company")],
                                          widget=forms.RadioSelect(attrs={"class": "form-check-input form-auth__input"}))

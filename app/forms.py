from django import forms

class AuthUserForm(forms.Form):
    email = forms.EmailField(label="Email:",
                             help_text="You need to add '@example.com' at the end",
                             widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    psswd = forms.CharField(label="Password:",
                            widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))

class RegistrationUserForm(forms.Form):
    name = forms.CharField(label="Your name:",
                           help_text="Write your name",
                           widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    reg_email = forms.EmailField(label="Your email:",
                                 help_text="Write your email, with '@example.com'",
                                 widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    reg_psswd = forms.CharField(label="Your password:",
                                help_text="Write your password, and don't forgive!",
                                widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))
    chk_psswd = forms.CharField(label="Repeat password:",
                                help_text="Rewrite your new password",
                                widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))

class RegistrationCompanyForm(forms.Form):
    company_name = forms.CharField(label="Your company:",
                                   help_text="Please, write name your company",
                                   widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    email_company = forms.EmailField(label="Company email:",
                                     help_text="Write company's email, with '@example.com'",
                                     widget=forms.TextInput(attrs={"class": "form-control form-auth__input"}))
    psswd_company = forms.CharField(label="Password:",
                                    help_text="Write company's password, and don't forgive!",
                                    widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))
    chkpsswd_company = forms.CharField(label="Repeat password:",
                                       help_text="Repeat password:",
                                       widget=forms.PasswordInput(attrs={"class": "form-control form-auth__input"}))
    about_company = forms.CharField(label="About Company:",
                                    help_text= "Write a few sentences about your company",
                                    widget=forms.Textarea(attrs={"class": "form-control form-auth__input"}))


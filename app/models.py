from django.db import models

class Roles(models.Model):
    role_name = models.CharField('Roles Name', max_length=100)

    def __str__(self):
        return "Roles"

class Accounts(models.Model):
    usernameAcc = models.CharField('Username', max_length=100)
    psswdAcc = models.CharField('Password', max_length=100)
    emailAcc = models.EmailField('Email', max_length=200)
    telephoneAcc = models.CharField('Telephone', max_length=100, null=True, blank=True)
    aboutCompAcc = models.CharField('About company', max_length=1000, null=True, blank=True)
    logoCompAcc = models.ImageField('Image', upload_to="companies_photo/", null=True, blank=True)
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return "SiteUsers"
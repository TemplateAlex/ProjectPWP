# Generated by Django 4.0.1 on 2022-02-26 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100, verbose_name='Roles Name')),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernameAcc', models.CharField(max_length=100, verbose_name='Username')),
                ('psswdAcc', models.CharField(max_length=100, verbose_name='Password')),
                ('emailAcc', models.EmailField(max_length=200, verbose_name='Email')),
                ('telephoneAcc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telephone')),
                ('aboutCompAcc', models.CharField(blank=True, max_length=1000, null=True, verbose_name='About company')),
                ('logoCompAcc', models.ImageField(blank=True, null=True, upload_to='companies_photo/', verbose_name='Image')),
                ('roles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.roles')),
            ],
        ),
    ]

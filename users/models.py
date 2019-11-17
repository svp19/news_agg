from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import datetime
# from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    date_of_birth = models.DateField(default=datetime.date.today, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.IntegerField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.user.username} Profile'


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_articles = models.IntegerField(blank=True, null=True)
    num_views = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Author'

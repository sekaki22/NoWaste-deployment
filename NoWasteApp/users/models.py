from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo (models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # This User class already has the following default field:
    # 1. username, password, email, firstname, lastname

    # Additional fields:
    #site = models.URLField(blank=True)
    profile_pic = models.ImageField (upload_to = 'users/profile_pics', blank = True)


    def __str__(self):
        return self.user

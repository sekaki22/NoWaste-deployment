from django.db import models
from users.models import User
from recipes.models import Recipes
# Create your models here.

class Matches (models.Model):
    id = models.AutoField (primary_key = True, unique = True)
    user_id = models.ForeignKey (User, on_delete = models.CASCADE)
    recipe_id = models.ForeignKey (Recipes, on_delete = models.CASCADE)
    datetime = models.DateTimeField (auto_now_add = True)

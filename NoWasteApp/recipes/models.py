from django.db import models

# Create your models here.

class Recipes (models.Model):
    id = models.AutoField (primary_key=True, unique = True)
    name = models.CharField (max_length = 128)
    course = models.CharField (max_length = 64)
    cooking_time = models.IntegerField ()
    calories = models.FloatField ()
    persons = models.IntegerField ()
    description = models.TextField (default = "")


    def __str__(self):
        return self.name

class Ingredients (models.Model):
    id = models.AutoField (primary_key=True, unique = True)
    name = models.CharField (max_length = 128)
    plural = models.CharField (max_length = 256)

    def __str__(self):
        return self.name

class Measure (models.Model):
    id = models.AutoField (primary_key = True, unique = True)
    unit_name = models.CharField (max_length = 128)

    def __str__(self):
        return self.unit_name

class Ingredient_set (models.Model):
    id = models.AutoField (primary_key=True, unique = True)
    recipe_id = models.ForeignKey (Recipes, on_delete = models.CASCADE)
    ingredient_id = models.ForeignKey (Ingredients, on_delete = models.CASCADE)
    measure_id = models.ForeignKey (Measure, on_delete = models.CASCADE)
    quantity = models.FloatField ()

class Tags (models.Model):
    id = models.AutoField (primary_key = True, unique = True)
    name = models.CharField (max_length = 256)

class Tag_set (models.Model):
    id = models.AutoField (primary_key = True, unique = True)
    recipe_id = models.ForeignKey (Recipes, on_delete = models.CASCADE)
    tag_id = models.ForeignKey (Tags, on_delete = models.CASCADE)

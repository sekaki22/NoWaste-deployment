from django.contrib import admin
from recipes.models import Recipes, Ingredient_set, Tag_set, Ingredients, Measure, Tags

# Register your models here.
admin.site.register(Recipes)
admin.site.register(Ingredient_set)
admin.site.register(Tag_set)
admin.site.register(Ingredients)
admin.site.register(Measure)
admin.site.register(Tags)

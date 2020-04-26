import os

os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'NoWasteApp.settings') # Configuring settings for the project
import django
django.setup () # Configuring settings for the project

from recipes.models import Recipes, Ingredient_set, Ingredients, Measure, Tag_set, Tags
import json


def push (recipe_path): # N = number of records to populate with

    counter = 0

    with open(recipe_path) as json_file:
        recipes = json.load(json_file)

    for entry in recipes:

        counter +=1

        description = ""

            # recipe table
        name = entry ['name']
        course = entry ['course']
        cook_time = int(entry ['cooking_time'])
        calories = float(entry ['calories'])
        n_persons = int(entry ['persons'])

        for step in entry['description']:
            description += step


        # Finally populate recipe page
        record = Recipes.objects.get_or_create (name = name, course = course, cooking_time = cook_time, calories = calories, persons = n_persons, description = description) [0]
            #record.save()


        for ingredient in entry['ingredients']:
            i_name = ingredient ['singular']
            plural = ingredient ['plural']
            if i_name not in Ingredients.objects.values('name'):
                ingr_object = Ingredients.objects.get_or_create (name = i_name, plural = plural)[0]
                #ingr_object.save()

            if ingredient ['quantity_unit'] not in Measure.objects.values('unit_name'):
                measure_object = Measure.objects.get_or_create (unit_name = ingredient ['quantity_unit'])
                #measure_object.save()

            combi = Ingredient_set(recipe_id = record, ingredient_id = Ingredients.objects.get ('name' = i_name),
            measure_id = Measure.objects.get (unit_name = ingredient ['unit_name']), quantity = ingredient ['quantity'])
                #combi.save()

        for tag in entry['tags']:
            if tag not in Tags.objects.values('name'):
                tag_obj = Tags.get_or_create(name = tag)
                    #tag_obj.save()

            tag_to_rec = Tag_set(recipe_id = record, tag_id =Tags.objects.get (name = tag))
            #tag_to_rec.save()


if __name__ == '__main__': # Only run this script within this package
    print ("Population is activated")
    push ('datafiles/allerhandeDB_test.json')
    print ("Population completed!")

import os

os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'NoWasteApp.settings') # Configuring settings for the project

import django
django.setup () # Configuring settings for the project

## Here does the population start

from users.models import User
from faker import Faker
import random as rand

Fakegen = Faker()



def populate (N = 5): # N = number of records to populate with

    for entry in range (N):

        fake_id = ""

        for x in range(10):
            fake_id += str(rand.randint (0,9))
        # Create fake data
        fake_name = Fakegen.name ().split (" ")
        fake_mail = Fakegen.email ()
        fake_date = str(Fakegen.date ())

        fake_fname = fake_name [0]
        fake_lname = fake_name [-1]
        fake_username = fake_fname [0] + fake_lname + fake_date [:3]
        fake_pw = fake_fname [:2] + fake_id [-5:] + fake_lname [-2] + fake_id [:5]


        # Finally populate webpage record with fake data
        record = User.objects.get_or_create (id = fake_id, usename = fake_username, fname = fake_fname, lname = fake_lname, email = fake_mail, pw = fake_pw) [0]



if __name__ == '__main__': # Only run this script within this package
    print ("Population is activated")
    populate (50)
    print ("Population completed!")

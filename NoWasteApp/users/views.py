from django.shortcuts import render
from .registration import Signup, IncludePic

# Additional packages for login functionality
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required # All views below a login required decorator, require someone to be loged in
def user_logout (request):
    logout(request)
    return render (request, 'homepage/homepage.html')

def form_view(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = Signup(data=request.POST)
        profile_form = IncludePic(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['verify_pw']:

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True




        elif user_form.data['password'] != user_form.data['verify_pw']:
            user_form.add_error('verify_pw', 'The passwords do not match')

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)


    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = Signup()
        profile_form = IncludePic()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'users/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login (request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user: # authentication succeeded
            if user.is_active:
                login(request, user)
                return render (request, 'homepage/homepage.html')

            else:
                return HttpResponse ("Username and/or password not correct!")

        else:
            return HttpResponse ("Username and/or password invalid")

    else:
        return render(request, 'users/Login.html',{})








# def form_view (request):
#
#     registered = False
#     if request.method == 'POST':
#         form = Signup(request.POST)
#         profile_form = IncludePic(request.POST)
#
#         if form.is_valid() and profile_form.is_valid():
#             user = form.save(commit = True)
#             user.set_password (user.password) # Hashing the password
#             user.save ()
#
#             profile = profile_form.save (commit = False)
#             profile.user = user
#
#             if 'profile_pic' in request.FILES:
#                 profile.profile_pic = request.FILES['profile_pic']
#
#             profile.save()
#
#             registered = True
#
#         else:
#             print (form.errors, profile_form.errors)
#
#     else:
#         form = Signup()
#         profile_form = IncludePic()
#
#     return render (request, 'users/registration.html', {'form': form,
#                                                         'profile_form': profile_form,
#                                                         'registered': registered})

# def ThankYou_page (request):
#     return render(request, 'users/Thank_You.html')

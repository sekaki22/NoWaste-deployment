from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'users'

urlpatterns = [
    path ('signup/', views.form_view, name = 'form'),
    path ('login/', views.user_login, name = 'user_login')
    #
#    path ('thankyou/', views.ThankYou_page, name = 'thank_you')

]

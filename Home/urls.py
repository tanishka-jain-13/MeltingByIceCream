from django.contrib import admin
from django.urls import path
from Home import views
# forward urls to urls.py hello 
urlpatterns = [
    
    path("", views.index, name= 'Home'),
    path("about", views.about, name= 'About'), 
    path("services", views.services, name= 'Services'),
    path('icecream', views.icecream, name='icecream'),
    path('softy', views.softy, name='softy'),
    path('familypack', views.familypack, name='familypack'),
    path("contact", views.contact, name= 'contact')
    
]

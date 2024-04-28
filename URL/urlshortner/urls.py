from django.contrib import admin
from django.urls import path , include
from urlshortner import views


urlpatterns = [
    path('', views.home, name='home'),  # Assuming this is the form page
    # path('output/', views.output, name='output'),  # Assuming this is the form page

    
]

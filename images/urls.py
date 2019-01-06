# django modules
from django.urls import path

# local modules
from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
]

from django.urls import path
from . import views # Import the views from the current directory  

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL to the index view
]
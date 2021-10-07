from django.urls import path
from .views import send, recieve

urlpatterns = [
    path('', send, name='send'), 
    path('get/', recieve, name='recieve'), 
]
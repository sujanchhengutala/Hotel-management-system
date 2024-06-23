from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegistration),
    path('login/', login),
    
]

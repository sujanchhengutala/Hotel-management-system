from django.urls import path
from .views import *

urlpatterns = [
    path('/register', userRegistration.as_view()),
]

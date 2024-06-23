from django.urls import path
from .views import *

urlpatterns = [
    path('rooms', RoomView.as_view()),
    path('rooms/<int:pk>', RoomView.as_view()),
    
    path('room-type', RoomTypeView.as_view()),
    path('room-type/<int:pk>', RoomTypeViewWithId.as_view())
    
]

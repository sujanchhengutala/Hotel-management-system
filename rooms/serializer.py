from rest_framework import serializers
from .models import *



class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_type
        fields = "__all__"



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'
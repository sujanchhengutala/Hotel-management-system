from django.db import models

# Create your models here.


class Room_type(models.Model):
    name=models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    amenities = models.TextField(null=True, blank=True)

class Rooms(models.Model):
    room_no = models.CharField(max_length=30)
    room_type = models.ForeignKey(Room_type, on_delete=models.SET_NULL, null=True)
    is_availability = models.BooleanField(default=True)
    # price = models.IntegerField()
    
    def tttype(self):
        return self.room_type.name 
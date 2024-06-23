from django.shortcuts import render
from .serializer import *
from rest_framework.generics import GenericAPIView
from .models import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class RoomTypeView(GenericAPIView):
    queryset = Room_type.objects.all()
    serializer_class = RoomTypeSerializer
    
    def post(self, request):
        data = request.data 
        serializer = self.serializer_class(data = data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors}, status=status.HTTP_403_FORBIDDEN)
        
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class RoomTypeViewWithId(GenericAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomTypeSerializer
    
    def get(self, request,pk):
        id = Room_type.objects.get(id = pk)
        serializer = self.serializer_class(id)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, pk):
        new_data = request.data
        id = Room_type.objects.get(id = pk)
        serializer = self.serializer_class(id, data = new_data)
        
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        id = Room_type.objects.get(id = pk)
        id.delete()
        return Response("delete successful")
        
        
        
        
        
        


class RoomView(GenericAPIView):
    serializer_class = RoomSerializer
    queryset = queryset = Rooms.objects.all()
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        # roomtype = Rooms.objects.get(room_type)
        # print(roomtype)
        return Response(serializer.data)
        
    
    def post(self, request):
        data = request.data 
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Info" : serializer.data}, status=status.HTTP_200_OK )
        else:
            return Response({"message" : serializer.errors}, status=status.HTTP_403_FORBIDDEN )
        

            
class RoomViewWithId(GenericAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomTypeSerializer
    
    def get(self, request,pk):
        id = Rooms.objects.get(id = pk)
        serializer = self.serializer_class(id)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, pk):
        new_data = request.data
        id = Rooms.objects.get(id = pk)
        serializer = self.serializer_class(id, data = new_data)
        
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        id = Rooms.objects.get(id = pk)
        id.delete()
        return Response("delete successful")
        
    
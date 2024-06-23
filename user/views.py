from django.shortcuts import render
from .models import *
from rest_framework import status
# from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from .serializer import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token 
# Create your views here.


@api_view(['POST'])
def userRegistration(request):
    user_data = request.data
    serializer = UserSerializer(data = user_data)
    if(serializer.is_valid()):
        a = serializer.save()
        password = request.data.get('password')
        hash_password = make_password(password)
        a.password = hash_password
        a.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(email = email, password = password)
    if user is None:
        return Response({'message':"invalid email and password"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        token,_ = Token.objects.get_or_create(user = user)
        return Response(token.key, status=status.HTTP_200_OK, )
        
    
    
    
        
    


# class userRegistration(GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
#     def post(self, request):
#         user_data = request.data
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(data = user_data)
#         if(serializer.is_valid()):
#             password = request.data.get('password')
#             hash_password = make_password(password)
#             print(hash_password)
#             a=serializer.save()
#             print(a)
#             a.password = hash_password
#             a.save()
            
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            
            
    
    
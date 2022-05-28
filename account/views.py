from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class UserCreate(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class =  UserSerializer

from django.shortcuts import render
from rest_framework import generics 
from .models import Person
from .serializer import PersonSerializer

class UserPost(generics.ListCreateAPIView):
    queryset= Person.objects.all()
    serializer_class =PersonSerializer

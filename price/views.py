from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .serializers import userSerializer
from.models import Price_Calculate
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = Price_Calculate.objects.all()
    serializer_class = userSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price_Calculate.objects.all()
    serializer_class = userSerializer
    lookup_field = 'id'



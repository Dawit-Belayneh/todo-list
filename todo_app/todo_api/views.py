from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoItemSerializer
from list.models import TodoItem

# Create your views here.

class TodoItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
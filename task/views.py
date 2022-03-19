from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer


from rest_framework import generics

# Create your views here.

# class TaskViewSet(viewsets.ModelViewSet):
#     querysets = Task.objects.all()
#     serializer_class = TaskSerializer
#


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

from django.shortcuts import render
from rest_framework import viewsets
from toy.models import Floor
from toy.serializers import FloorSerializer


# Create your views here.
class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

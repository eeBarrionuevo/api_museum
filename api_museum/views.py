from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import ArtistSerializer

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer




from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Departure
from .serializers import DepartureSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class DepartureView(viewsets.ModelViewSet):
    permission_class = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Departure.objects.all()
    serializer_class=DepartureSerializer



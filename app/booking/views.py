from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class BookingView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Booking.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=BookingSerializer



class UserBooking(generics.GenericAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes=[permissions.AllowAny]
    def get(self,request,format=None):
        model = Booking.objects.filter(user_id = self.request.user.id)
        serializer = BookingSerializer(model,many=True)
        return Response(data = serializer.data)
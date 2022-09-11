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
import requests
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

class BuyPaymaya(generics.GenericAPIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request,format=None):
        res = request.data
        url = "https://pg-sandbox.paymaya.com/checkout/v1/checkouts"
        payload = {
            "totalAmount": {
                "value": res.get('price'),
                "currency": "PHP"
            },
            "buyer": {
                "billingAddress": {"countryCode": "GB"},
                "shippingAddress": {"countryCode": "GB"},
                "firstName": "Juan",
                "middleName": "D",
                "lastName": "Delacruz",
                "birthday": "2019-10-19"
            },
            "items": [
                {
                    "amount": {"value": res.get('price')},
                    "totalAmount": {"value": res.get('price')},
                    "name": res.get('product'),
                    "quantity": "1",
                    "code": "uus",
                    "description": "dse"
                }
            ],
            "requestReferenceNumber": "123123"
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic cGstWjBPU3pMdkljT0kyVUl2RGhkVEdWVmZSU1NlaUdTdG5jZXF3VUU3bjBBaDo="
        }

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return Response(data=response.text)
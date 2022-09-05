from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"
    
    def create(self,validated_data):
        validated_data['status']='Pending'
        return Booking.objects.create(**validated_data)
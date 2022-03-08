
from rest_framework import serializers
from .models.hotel import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'description', 'availability', 'phone_number', 'city', 'price']
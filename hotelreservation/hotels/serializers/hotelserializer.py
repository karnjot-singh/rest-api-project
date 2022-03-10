
from rest_framework import serializers
from hotels.models.hotel import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'description', 'availability', 'phone_number', 'city', 'price']
from rest_framework import serializers
from hotels.models.guest import Guest

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'gender']
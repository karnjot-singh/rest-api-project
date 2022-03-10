from rest_framework import serializers
from hotels.models.reservation import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'hotel', 'confirmation_number', 'check_in', 'check_out']
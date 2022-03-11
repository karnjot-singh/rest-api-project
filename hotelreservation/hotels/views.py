from django.core import serializers
from django.shortcuts import get_object_or_404

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

import re
import json
from datetime import datetime

from .models.hotel import Hotel
from .models.reservation import Reservation
from .models.guest import Guest
from .serializers.hotelserializer import HotelSerializer
from .serializers.reservationserializer import ReservationSerializer
from .serializers.guestserializer import GuestSerializer


@api_view(['GET'])
def fetchReservations(request):
    
    reservations = Reservation.objects.all()
    
    lst = []
    for reservation in reservations:
        item = ReservationSerializer(reservation, many=False).data
        guests = Guest.objects.filter(reservation=reservation)
        guests_list = GuestSerializer(guests, many=True).data
        item['guest_list'] = guests_list
        
        lst.append(item)

    return Response(lst)

class hotel_view(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

@api_view(['POST'])
def reservationConfirmation(request):
    data = json.loads(request.body)
    errors = {}
    
    try:
        if "hotel_name" in data:
            hotel = Hotel.objects.get(name=data['hotel_name'])
        else:
            errors["hotel_name"] = [ "This field is required" ]
    except Hotel.DoesNotExist:
        hotel = None
        errors["hotel_name"] = [ "Ensure that hotel with name '"+ data['hotel_name'] +"' exist in database" ]
    
    try:
        if "checkin" in data: 
            datetime.strptime(data['checkin'], '%Y-%m-%d')
        else:
            errors["checkin"] = [ "This field is required" ]
    except:
        errors["checkin"] = [ "Ensure that checkin has valid format YYYY-MM-DD" ]
    
    try:
        if "checkout" in data: 
            datetime.strptime(data['checkout'], '%Y-%m-%d')
        else:
            errors["checkout"] = [ "This field is required" ]
    except:
        errors["checkout"] = [ "Ensure that checkout has valid format YYYY-MM-DD" ]

    if "checkin" not in errors and "checkout" not in errors:

        if not (datetime.strptime(data['checkin'], '%Y-%m-%d') < datetime.strptime(data['checkout'], '%Y-%m-%d')):
            errors["checkin"] = ["Ensure that checkout date is greater than checkin date"]

    guests=None
    if "guests_list" in data: 
        guests = data['guests_list']
    else:
        errors["guests_list"] =  [ "This field is required" ]



    if guests is not None and len(guests)==0:
        errors["guests_list"] =  [ "Ensure that there are guest details" ]
    elif guests is not None:
        guest_flag = True
        gender_flag = True
        for guest in guests:
            if guest_flag:
                if "guest_name" in guest:
                    if re.match(r'^[a-zA-Z ]+$', guest['guest_name']) is None:
                        if "guests_list" in errors: errors["guests_list"].append("Ensure Guest name has only characters")
                        else: errors["guests_list"] = [ "Ensure Guest name has only characters" ]
                        guest_flag = False

                    if len(guest['guest_name']) < 4 or len(guest['guest_name']) > 30:
                        if "guests_list" in errors: errors["guests_list"].append("Ensure Guest name has 4-30 characters")
                        else: errors["guests_list"] = [ "Ensure Guest name has atleast 4 characters" ]
                        guest_flag = False
                else:
                    if "guests_list" in errors: errors["guests_list"].append("guest_name field is required for all guests")
                    else: errors["guests_list"] = [ "guest_name field is required for all guests" ]
                    guest_flag = False
            if gender_flag:
                if "gender" in guest:
                    if guest['gender'].lower() != "m" and guest['gender'].lower() != "f":
                        if "guests_list" in errors: errors["guests_list"].append("Ensure gender has valid value m/f")
                        else: errors["guests_list"] = [ "Ensure gender has valid value m/f" ]
                        gender_flag = False
                else:
                    if "guests_list" in errors: errors["guests_list"].append("gender field is required for all guests")
                    else: errors["guests_list"] = [ "gender field is required for all guests" ]
                    gender_flag = False
            
            if not guest_flag and not gender_flag: break

    if errors == {}:
        reservation = Reservation()
        hotel = Hotel.objects.get(name=data['hotel_name'])
        reservation.hotel = hotel
        
        reservation.check_in = data['checkin']
        reservation.check_out = data['checkout']

        reservation.save()
        reservation.refresh_from_db()
        
        confirmation_number = hotel.name.replace(" ", "")[:3] + str(reservation.id).zfill(6)
        reservation.confirmation_number = confirmation_number
        reservation.save()
        
        for guest in data['guests_list']:
            guest = Guest(name=guest['guest_name'], gender=guest['gender'], reservation=reservation)
            guest.save()

        return Response({"confirmation_number": reservation.confirmation_number})
    else:
        return Response(errors)
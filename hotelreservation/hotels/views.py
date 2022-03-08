from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.hotel import Hotel
from .serializers import HotelSerializer


@api_view(['GET'])
def getListOfHotels(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def reservationConfirmation(request):
    
    return Response({"message": "Done",
                    "data": request.body})

class hotel_view(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
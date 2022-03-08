from django.urls import path
from . import views

urlpatterns = [
   path('hotels', views.getListOfHotels, name="HotelList"),
   path('reserve', views.reservationConfirmation, name="Reservation Confirmation"),
   path('hotel', views.hotel_view.as_view(), name="HotelListAndCreate"),
]
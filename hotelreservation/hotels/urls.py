from django.urls import path
from . import views

urlpatterns = [
   path('makereservation', views.reservationConfirmation, name="Reservation Confirmation"),
   path('hotel', views.hotel_view.as_view(), name="HotelListAndCreate"),
   path('reservations', views.fetchReservations, name="Test"),
]
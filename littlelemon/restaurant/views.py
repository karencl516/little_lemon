from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics,status

from django.contrib.auth.models import User

from .models import Booking , MenuItem
from .serializers import BookingSerializer , MenuItemSerializer,UserSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]     
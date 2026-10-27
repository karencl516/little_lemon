from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework import generics,status
from djoser.serializers import UserCreateSerializer

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseForbidden
from django.core import serializers

from .forms import BookingForm
from .models import Booking , MenuItem
from .serializers import BookingSerializer , MenuItemSerializer,UserSerializer
from .permissions import IsAdminOrReadOnly
from datetime import datetime



class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]

class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]     

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'register.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Log in to reserve a table.')
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu_items.html', {"menu_items": menu_items})


def display_menu_item(request, pk):
    menu_item = get_object_or_404(MenuItem, pk=pk)
    return render(request, 'menu_items.html', {"menu_item": menu_item})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def bookings(request):
    if request.method == 'POST':
        serializer = BookingSerializer(data={
            'name': request.data.get('name'),
            'persons': request.data.get('persons'),
            'booking_date': request.data.get('reservation_date'),
        })
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all().filter(booking_date=date)
    booking_json = serializers.serialize('json', bookings)
    return HttpResponse(
        booking_json, content_type = 'application/json'
    )
    
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuItemView, SingleMenuItemView,home, bookings , book, about,reservations, menu, display_menu_item, RegistrationView

urlpatterns = [
    path('',home, name='home'),
    path('about/', about, name="about"),
    path('book/', book, name="book"),
    path('reservations/', reservations, name="reservations"),
    path('menu/', menu, name="menu"),
    path('menu/<int:pk>/', display_menu_item, name="menu_item"),
    path('api/menu-items/', MenuItemView.as_view()),
    path('api/menu-items/<int:pk>/', SingleMenuItemView.as_view()),
    path('api/api-token-auth/', obtain_auth_token),
    path('api/bookings/', bookings, name='bookings'),
    path('api/registration/', RegistrationView.as_view(), name='registration'),
]

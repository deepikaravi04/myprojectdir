# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # RoomDetails URLs
    path('rooms/', views.room_details_list, name='room_details_list'),
    path('rooms/create/', views.room_details_create, name='room_details_create'),
    path('rooms/update/<int:pk>/', views.room_details_update, name='room_details_update'),
    path('rooms/delete/<int:pk>/', views.room_details_delete, name='room_details_delete'),

    # Hosteller URLs
    path('hostellers/', views.hosteller_list, name='hosteller_list'),
    path('hostellers/create/', views.hosteller_create, name='hosteller_create'),
    path('hostellers/update/<int:pk>/', views.hosteller_update, name='hosteller_update'),
    path('hostellers/delete/<int:pk>/', views.hosteller_delete, name='hosteller_delete'),

    # RentHistory URLs
    path('rent_histories/', views.rent_history_list, name='rent_history_list'),
    path('rent_histories/create/', views.rent_history_create, name='rent_history_create'),
    path('rent_histories/update/<int:pk>/', views.rent_history_update, name='rent_history_update'),
    path('rent_histories/delete/<int:pk>/', views.rent_history_delete, name='rent_history_delete'),
]

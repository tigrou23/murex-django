from django.urls import path
from webanalytics import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('bookings/', views.booking_list),
    path('bookings/<int:pk>/', views.booking_detail),
    path('inactivity/', views.inactivity_list),
    path('inactivity/<int:pk>/', views.inactivity_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
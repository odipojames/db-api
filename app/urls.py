from django.urls import path
from . views import TrackingAPIView

urlpatterns = [
    path('track/<str:reg_number>/', TrackingAPIView.as_view(),name='home'),

]

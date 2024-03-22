# routing.py

from django.urls import path
from .consumers import QRListConsumer

websocket_urlpatterns = [
    path("ws/attendance_updates/", QRListConsumer.as_asgi()),
]

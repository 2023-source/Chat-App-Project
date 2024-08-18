from django.urls import path

from . import consumers

websocket_urlpatterns = [
    # It expects a URL in the format ws/<str:room_name>/,
    #  where <str:room_name> is a string capturing group representing the name of the chat room.
    # .as_asgi() is used to convert it to an ASGI application callable.
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]
"""
ASGI config for chatApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

# Protocol Router is used to route different types of protocols here it used for HTTP and WebSocket.
# URLRouter is used for routing websocket URL.
from channels.routing import ProtocolTypeRouter, URLRouter

#  It retrieves the standard ASGI application instance for the Django project that is responsible for handling 
# HTTP request based on url route in urls.py
from django.core.asgi import get_asgi_application

# It allows stack authentication middleware on top of WebSocket consumers.py  to handle user authentication.
from channels.auth import AuthMiddlewareStack

import room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatApp.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        ),
    )
})

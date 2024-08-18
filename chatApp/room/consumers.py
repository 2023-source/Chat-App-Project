import json

from django.contrib.auth.models import User
# It is a base class provided by channels for handling WebSocket connection asynchronously .

from channels.generic.websocket import AsyncWebsocketConsumer

# The sync_to_async decorator is used in Django Channels with async consumers to allow
#  for the synchronous execution of synchronous code within an asynchronous context.
from asgiref.sync import sync_to_async

from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Retrieves room_name from url route's keyword argument.
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # Groups WebSocket connection that belong to same room.
        self.room_group_name = 'chat_%s' % self.room_name

        # Adds current Websocket Connection to the room_group so that the messages in this room are accessible to it. 
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    # Mainly used to discard or disconnect the current WebSocket connection.
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        # print(data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room, content=message)
from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    # Here it creates relationship between Room and Message. You can use 'messages' on instance of Room to access Message.
    # If a room is deleted then Messages related to it are also deleted.
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Used for maintaining chronological occurence of the message.
        ordering = ('date_added',)
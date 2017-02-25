from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Channel(models.Model):
    users = models.ManyToManyField(
        User, related_name='belonged_channel',
    )
    name = models.TextField()
    def add_user(self, user):
        self.users.add(user)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='has_chats', default=1)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channel, related_name='messages', default=1)
# Create your models here.


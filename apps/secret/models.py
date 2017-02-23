from __future__ import unicode_literals
from ..login.models import User, UserManager
from django.db import models

# Create your models here.
class MessageManager(models.Manager):
    def validate(self, postData, id):
        if len(postData["text"]) < 4:
            return (False, "Message too short!")
        else:
            return (True, Message.objects.create(content=postData["text"], creator=User.objects.get(id=id)))
    def createLike(self, user_id, message_id):
        message = self.get(id=message_id)
        liker = User.objects.get(id=user_id)
        alreadyLiked = User.objects.filter(liked=message, id=user_id)
        if(len(alreadyLiked) == 0):
            message.likes.add(liker)
            return True
        else:
            return False


class Message(models.Model):
    content = models.TextField(max_length=1000)
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked")
    objects = MessageManager()

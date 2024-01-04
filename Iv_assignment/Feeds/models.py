from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    liked_by=models.ForeignKey(User, on_delete=models.CASCADE)
    
    


from django.db import models

# Create your models here.

class Feedback(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    message_subject = models.CharField(max_length=255)
    message_text = models.TextField()

    def __str__(self):
        return self.username

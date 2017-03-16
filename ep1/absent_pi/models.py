from django.db import models

class Entrance(models.Model):
    title = models.CharField(max_length=25)
    text = models.TextField()

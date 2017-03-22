from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=25)
    text = models.TextField()

    def __str__(self):
        return '%s' % (self.title)

from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=120)
    body  = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

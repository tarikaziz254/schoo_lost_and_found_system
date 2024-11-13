from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_lost_or_found = models.DateField()
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='item_photos/')
    is_found = models.BooleanField(default=False)
    collected = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


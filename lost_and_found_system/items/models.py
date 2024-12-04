from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('picked', 'picked')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_lost_or_found = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='item_photos/')
    collected = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lost')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # If the status is 'found', delete the item from the database
        if self.status == 'picked':
            self.delete()  # This will delete the item from the database
            return
        
        # If not marked as found, proceed with normal save
        super().save(*args, **kwargs)

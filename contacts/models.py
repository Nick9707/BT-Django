from django.db import models
from django.utils import timezone


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=timezone.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __set__(self):
        return self.name

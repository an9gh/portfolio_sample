from django.utils import timezone
from django.db import models

# Create your modecl


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    desc = models.TextField()

    def __self__(self):
        return self.name



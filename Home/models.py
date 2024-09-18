from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=12)
    desc = models.TextField(default='Default description')
    date = models.DateField()

    def __str__(self):
        return self.name

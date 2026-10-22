from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}={self.price}'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    persons = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return f'{self.name}={self.price}'
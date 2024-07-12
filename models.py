from django.db import models

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    reservation_time = models.TimeField()

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

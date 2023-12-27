from django.db import models


class Product(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
from django.db import models

# Seller Model
class Seller(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='sellers/', null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)  # rating out of 5

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='products/')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    warranty_period = models.CharField(max_length=100, null=True, blank=True)  # e.g., '1 year', '6 months'

    def __str__(self):
        return self.name

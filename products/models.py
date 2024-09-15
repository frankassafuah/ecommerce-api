from django.db import models
from users.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # a user can create many products and a product can belong to a one user
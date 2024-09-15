from rest_framework import viewsets
from .serializers import ProductSerializer
from products.models import Product
from rest_framework.permissions import IsAuthenticated
import random
from users.models import User

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        depth = 1
        fields = '__all__'

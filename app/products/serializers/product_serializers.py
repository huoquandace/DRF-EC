from products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "cost_price",
            "price",
            "tax_rate",
            "is_available",
            "created_at",
            "updated_at",
        ]
        name = serializers.CharField(max_length=100)
        description = serializers.CharField(max_length=1000)
        cost_price = serializers.DecimalField(max_digits=10, decimal_places=2)
        price = serializers.DecimalField(
            max_digits=10, decimal_places=2, required=False
        )
        tax_rate = serializers.FloatField(required=False)
        is_available = serializers.BooleanField()
        created_at = serializers.DateTimeField()
        updated_at = serializers.DateTimeField()

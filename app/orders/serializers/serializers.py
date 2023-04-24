from django.utils.translation import gettext_lazy as _
from orders.models import Order, OrderItem, OrderStatus
from products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price")


class ItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ("id", "date_added", "quantity", "product")


class OrderDetailSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    date_ordered = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Order
        fields = [
            "id",
            "date_ordered",
            "status",
            "total_price",
            "items",
        ]


class CreateItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        try:
            Product.objects.get(id=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError(_("product_id not exists"))
        return value


class CreateOrderSerializer(serializers.Serializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    items = serializers.ListField(child=CreateItemSerializer())


class UpdateOrderSerializer(serializers.Serializer):
    status = serializers.CharField()

    def validate_status(self, value):
        if value not in OrderStatus.values:
            raise serializers.ValidationError(
                _(f"value must be in {OrderStatus.values}")
            )
        return value

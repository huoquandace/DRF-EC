from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Product
from users.models import UserData


class OrderStatus(models.TextChoices):
    NEW = "NEW", _("Mới tạo")
    DONE = "DONE", _("Hoàn thành")
    CANCER = "CANCER", _("Hủy")
    DELIVERY = "DELIVERY", _("Đang giao")


class Order(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, default=OrderStatus.NEW, choices=OrderStatus.choices, null=True
    )
    total_price = models.DecimalField(
        null=True, default=0, decimal_places=2, max_digits=10
    )

    def __str__(self):
        return self.id


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

from common.models import TimeStampedModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(TimeStampedModel):
    name = models.CharField(_("name"), max_length=100)
    description = models.TextField(_("description"))
    cost_price = models.DecimalField(_("cost price"), max_digits=10, decimal_places=2)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2, null=True)
    tax_rate = models.FloatField(_("tax rate"), null=True)
    is_available = models.BooleanField(_("is available"), default=True)

    class Meta:
        db_table = "product"
        ordering = ["id"]

    def __str__(self):
        return self.name

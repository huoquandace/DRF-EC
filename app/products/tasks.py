import logging
from decimal import Decimal

from products.models import Product


def update_product_prices():
    products = Product.objects.all()
    for product in products:
        if product.tax_rate:
            product.price = product.cost_price * (Decimal(1) + product.tax_rate)
            product.save()


if __name__ == "__main__":
    try:
        update_product_prices()
    except Exception:
        logging.exception("BATCH ERROR")

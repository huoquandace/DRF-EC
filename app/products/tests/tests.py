import json

from django.test import Client
from django.urls import reverse
from products.models import Product
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class ProductListTestCase(APITestCase):
    def setUp(self):
        self.client = Client()

    def test_get_all_products(self):
        url = reverse("all_product")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        url = reverse("all_product")
        data = {
            "name": "Milk",
            "description": "To drink",
            "cost_price": 19.99,
            "is_available": True,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProductRetrieveTestCase(APITestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name="Cream cake",
            description="To eat",
            cost_price=10.0,
            is_available=True,
        )

    def test_get_product(self):
        url = reverse("retrieve-product", args=[self.product.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        url = reverse("retrieve-product", args=[self.product.pk])
        data = {"name": "Cookies", "cost_price": 12.99}
        response = self.client.put(
            url, data=json.dumps(data), content_type="application/json"
        )

    def test_delete_product(self):
        url = reverse("retrieve-product", args=[self.product.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

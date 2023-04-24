from orders.models import Order
from orders.serializers import OrderDetailSerializer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase
from users.models import UserData

factory = APIRequestFactory()


class OrdersTest(APITestCase):
    def login(self):
        user = UserData.objects.create_user(
            name="Mark", email="mark@example.com", password="password1234"
        )
        url_user = reverse("login")
        data_user = {"email": user.email, "password": "password1234"}
        response_user = self.client.post(url_user, data_user, format="json")
        access = response_user.data.get("access")
        headers = {"Authorization": f"Bearer {access}"}
        return headers

    def test_invalid_order_list(self):
        url = reverse("order")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_order_create(self):
        url = reverse("order")
        data = {"total_price": 1000, "items": [{"quantity": 1, "product_id": 1}]}
        response = self.client.post(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_order_detail(self):
        headers = OrdersTest.login(self)

        url = reverse("order_id", kwargs={"pk": 1})
        response = self.client.get(url, format="json", **headers)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_order_update(self):
        url = reverse("order_id", kwargs={"pk": 1})
        data = {
            "status": "DONE",
        }
        response = self.client.put(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

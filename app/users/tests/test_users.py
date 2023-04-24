from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase
from users.models import UserData

factory = APIRequestFactory()


class UsersTest(APITestCase):
    def test_user_create(self):
        url = reverse("register")
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "password": "password1234",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_detail(self):
        user = UserData.objects.create_user(
            name="Jane", email="jane@example.com", password="password1234"
        )
        url = reverse("user-detail", args=(user.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        user = UserData.objects.create_user(
            name="Jenny", email="jenny@example.com", password="password1234"
        )
        url = reverse("user-detail", args=(user.id,))
        data = {"name": "Julia", "email": "julia@example.com"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        user = UserData.objects.create_user(
            name="Jim", email="jim@example.com", password="password1234"
        )
        url = reverse("user-detail", args=(user.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_login(self):
        user = UserData.objects.create_user(
            name="Mark", email="mark@example.com", password="password1234"
        )
        url = reverse("login")
        data = {"email": user.email, "password": "password1234"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        url = reverse("logout")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PasswordResetTestCase(APITestCase):
    def setUp(self):
        self.email = "test@example.com"
        self.user = UserData.objects.create(email=self.email)

    def test_invalid_email_address(self):
        url = reverse("password_reset:reset-password-request")
        data = {"email": "invalid@example.com"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {
                "email": [
                    "We couldn't find an account associated with that email. Please try a different e-mail address."
                ]
            },
        )

    def test_invalid_form_data(self):
        url = reverse("password_reset:reset-password-request")
        data = {"email": "abc"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {"email": ["Enter a valid email address."]},
        )

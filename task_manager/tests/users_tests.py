from django.test import Client, TestCase
from django.urls import reverse


class TestUsers(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = {
            "username": "test_user",
            "first_name": "First_name_3",
            "last_name": "Last_name_3",
            "password1": "test_pass_3",
            "password2": "test_pass_3",
        }

    def test_users_crud(self):
        response = self.client.get(reverse("users"))
        self.assertNotContains(response, "First_name_3 Last_name_3")

        response = self.client.post(
            reverse("user_create"), data=self.test_user
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("login"))

        response = self.client.get(reverse("users"))
        self.assertContains(response, "First_name_3 Last_name_3")

        response = self.client.get(reverse("user_update", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("login"))

        response = self.client.get(reverse("user_delete", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("login"))

        self.client.login(
            username=self.test_user["username"],
            password=self.test_user["password1"]
        )
        self.test_user["last_name"] = "Last_name_changed_3"
        response = self.client.post(
            reverse("user_update", kwargs={"pk": 1}), data=self.test_user
        )
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("users"))
        self.assertContains(response, "First_name_3 Last_name_changed_3")

        response = self.client.post(reverse("user_delete", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("users"))

        response = self.client.get(reverse("users"))
        self.assertNotContains(response, "First_name_3 Last_name_change_3")

from django.test import Client, TestCase
from django.urls import reverse
from django.utils.translation import gettext as _
from task_manager.users.models import User


class TestStatuses(TestCase):
    fixtures = [
        "users.json",
    ]

    def setUp(self):
        self.client = Client()
        self.user = User.objects.first()

    def test_index_page_no_auth(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _("Hello from Hexlet!")
        )
        self.assertContains(
            response,
            _("Login")
        )
        self.assertContains(
            response,
            _("Register user")
        )
        self.assertContains(
            response,
            _("Users")
        )
        self.assertNotContains(
            response,
            _("Statuses")
        )
        self.assertNotContains(
            response,
            _("Labels")
        )
        self.assertNotContains(
            response,
            _("Tasks")
        )
        self.assertNotContains(
            response,
            self.user.username
        )

    def test_index_page_with_auth(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _("Hello from Hexlet!")
        )
        self.assertContains(
            response,
            _("Logout")
        )
        self.assertContains(
            response,
            _("Users")
        )
        self.assertContains(
            response,
            _("Statuses")
        )
        self.assertContains(
            response,
            _("Labels")
        )
        self.assertContains(
            response,
            _("Tasks")
        )
        self.assertContains(
            response,
            self.user.username
        )

    def test_logout(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("statuses"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("labels"))
        self.assertEqual(response.status_code, 302)

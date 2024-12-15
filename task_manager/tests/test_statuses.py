from django.test import Client, TestCase
from django.urls import reverse
from django.utils.translation import gettext as _
from task_manager.users.models import User


class TestStatuses(TestCase):
    fixtures = [
        "statuses.json",
        "labels.json",
        "users.json",
        "tasks.json"
    ]

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())

    def test_statuses_crud(self):
        response = self.client.get(reverse("statuses"))
        self.assertNotContains(response, "Status 3")

        response = self.client.post(
            reverse("status_create"), data={"name": "Status 3"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("statuses"))

        response = self.client.get(reverse("statuses"))
        self.assertContains(response, "Status 3")

        response = self.client.post(
            reverse("status_update", kwargs={"pk": 4}),
            data={"name": "Updated status 1"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("statuses"))

        response = self.client.get(reverse("statuses"))
        self.assertNotContains(response, "Status 3")
        self.assertContains(response, "Updated status 1")

        response = self.client.post(
            reverse("status_delete", kwargs={"pk": 4})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("statuses"))

        response = self.client.get(reverse("statuses"))
        self.assertNotContains(response, "Updated status 1")

        response = self.client.post(
            reverse("status_delete", kwargs={"pk": 1})
        )
        response = self.client.get(reverse("statuses"))
        self.assertContains(
            response,
            _("Cannot delete a status because it is in use")
        )

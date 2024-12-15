from django.test import Client, TestCase
from django.urls import reverse
from django.utils.translation import gettext as _
from task_manager.users.models import User


class TestLabels(TestCase):
    fixtures = [
        "statuses.json",
        "labels.json",
        "users.json",
        "tasks.json"
    ]

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())

    def test_labels_crud(self):
        response = self.client.get(reverse("labels"))
        self.assertNotContains(response, "New label 1")

        response = self.client.post(
            reverse("label_create"), data={"name": "New label 1"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("labels"))

        response = self.client.get(reverse("labels"))
        self.assertContains(response, "New label 1")

        response = self.client.post(
            reverse("label_update", kwargs={"pk": 4}),
            data={"name": "Updated label 1"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("labels"))

        response = self.client.get(reverse("labels"))
        self.assertNotContains(response, "New label 1")
        self.assertContains(response, "Updated label 1")

        response = self.client.post(
            reverse("label_delete", kwargs={"pk": 4})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("labels"))

        response = self.client.get(reverse("labels"))
        self.assertNotContains(response, "Updated label 1")

        response = self.client.post(
            reverse("label_delete", kwargs={"pk": 1})
        )
        response = self.client.get(reverse("labels"))
        self.assertContains(
            response,
            _("Cannot delete a label because it is in use")
        )

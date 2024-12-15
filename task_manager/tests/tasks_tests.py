from django.test import Client, TestCase
from django.urls import reverse
from django.utils.translation import gettext as _
from task_manager.users.models import User


class TestTasks(TestCase):
    fixtures = [
        "statuses.json",
        "labels.json",
        "users.json",
        "tasks.json"
    ]

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.first())

    def test_list_task(self):
        response = self.client.get(reverse("tasks"))
        self.assertContains(response, "Test task 1")
        self.assertContains(response, "Test task 2")
        self.assertNotContains(response, "Test task 3")

    def test_task_detail(self):
        response = self.client.get(reverse("task_show", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Used label 1")
        self.assertContains(response, "Status 1")
        self.assertNotContains(response, "Used label 2")
        self.assertNotContains(response, "Status 2")
        self.assertContains(response, "First_name_1 Last_name_1")
        self.assertContains(response, "First_name_2 Last_name_2")

    def test_create_task(self):
        response = self.client.post(
            reverse("task_create"),
            data={
                "name": "Test task 3",
                "description": "Test case 3",
                "status": 1,
                "creator": 2,
                "executor": 2,
                "labels": [1]
            }
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("tasks"))
        self.assertContains(response, "Test task 3")
        response = self.client.get(reverse("task_show", kwargs={"pk": 3}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test task 3")
        self.assertContains(response, "Test case 3")
        self.assertContains(response, "Used label 1")
        self.assertContains(response, "Status 1")
        self.assertContains(response, "First_name_1 Last_name_1")
        self.assertContains(response, "First_name_2 Last_name_2")
        self.assertNotContains(response, "Status 2")

    def test_update_task(self):
        response = self.client.post(
            reverse("task_update", kwargs={"pk": 1}),
            data={
                "name": "Test task 3",
                "description": "Test case 3",
                "status": 2,
                "creator": 1,
                "executor": 2,
                "labels": [2]
            }
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("task_show", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Test task 1")
        self.assertContains(response, "Test case 3")
        self.assertContains(response, "Used label 2")
        self.assertContains(response, "First_name_1 Last_name_1")
        self.assertContains(response, "First_name_2 Last_name_2")
        self.assertNotContains(response, "Status 1")
        self.assertContains(response, "Status 2")

    def test_delete_task(self):

        response = self.client.post(
            reverse("task_delete", kwargs={"pk": 2}),
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("tasks"))
        self.assertContains(response, "Test task 1")
        self.assertContains(response, "Test task 2")
        self.assertContains(
            response,
            _("A task can only be deleted by its creator")
        )

        response = self.client.post(
            reverse("task_delete", kwargs={"pk": 1}),
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("tasks"))
        self.assertNotContains(response, "Test task 1")
        self.assertContains(response, "Test task 2")

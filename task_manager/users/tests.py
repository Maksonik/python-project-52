from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_user_registration(self):
        response = self.client.post(reverse('user_create'), {'username': 'newuser', 'password': 'pass123'})
        self.assertRedirects(response, reverse('login'))

    def test_user_update(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('user_update', args=[self.user.pk]), {'username': 'updateduser'})
        self.assertRedirects(response, reverse('user_list'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_user_delete(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('user_delete', args=[self.user.pk]))
        self.assertRedirects(response, reverse('user_list'))
        self.assertEqual(User.objects.count(), 0)

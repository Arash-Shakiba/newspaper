from django.contrib.auth import get_user_model
from django.test import TestCase

class UserManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="1234"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@gmail.com",
            password="1234super"
        )
        self.assertEqual(user.username, "testsuperuser")
        self.assertEqual(user.email, "testsuperuser@gmail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

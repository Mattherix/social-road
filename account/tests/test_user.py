from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.test import TestCase, tag


# https://testdriven.io/blog/django-custom-user-model/#tests
class UserTests(TestCase):

    @tag('fast')
    def test_create_user(self):
        User = get_user_model()
        password = User.objects.make_random_password()
        user = User.objects.create_user(
            username='John Doe',
            email='John@doe.com',
            password=password
        )
        self.assertEqual(user.username, 'John Doe')
        self.assertEqual(user.slug, 'john-doe')
        self.assertEqual(user.email, 'John@doe.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', email='', password='foo')

    @tag('fast')
    def test_create_superuser(self):
        User = get_user_model()
        password = User.objects.make_random_password()
        admin_user = User.objects.create_superuser(username='root', email='root@user.com', password=password)
        self.assertEqual(admin_user.username, 'root')
        self.assertEqual(admin_user.slug, 'root')
        self.assertEqual(admin_user.email, 'root@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='root',
                email='super@user.com',
                password='foo',
                is_superuser=False
            )

    @tag('fast')
    def test_unique_slug(self):
        User = get_user_model()
        password1 = User.objects.make_random_password()
        User.objects.create_user(
            username='John',
            email='John@d.com',
            password=password1
        )
        User.objects.make_random_password()
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username='john',
                email='John@doe2.com',
                password=password1
            )

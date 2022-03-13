from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


class TestCustomManager(TestCase):

    def test_create_user(self):
        self.phone = '+79999999999'
        self.name = 'TestUserManager'
        self.password = 'super_password'

        user = User.objects.create_user(
            phone=self.phone, name=self.name, password=self.password
        )

        self.assertEqual(user.phone, '+79999999999')
        self.assertEqual(user.name, 'TestUserManager')
        self.assertEqual(user.slug, 'testusermanager')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_verified)
        self.assertNotEqual(user.phone, '+78888888888')
        self.assertNotEqual(user.name, 'NoTestUserManager')
        self.assertNotEqual(user.slug, 'notestusermanager')

        with self.assertRaises(TypeError):
            User.objects.create_user(

            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                phone='', name='', password=''
            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                phone=self.phone, name='', password=''
            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                phone='', name=self.name, password=''
            )

    def test_create_superuser(self):
        self.phone = '+77777777777'
        self.name = 'TestSuperUserManager'
        self.password = 'super_password'

        super_user = User.objects.create_superuser(
            phone=self.phone, name=self.name, password=self.password
        )

        self.assertEqual(super_user.phone, '+77777777777')
        self.assertEqual(super_user.name, 'TestSuperUserManager')
        self.assertEqual(super_user.slug, 'testsuperusermanager')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        self.assertFalse(super_user.is_verified)
        self.assertNotEqual(super_user.phone, '+78888888888')
        self.assertNotEqual(super_user.name, 'NoSuperTestUserManager')
        self.assertNotEqual(super_user.slug, 'notestsuperusermanager')

        with self.assertRaises(TypeError):
            User.objects.create_superuser(

            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                phone='', name='', password=''
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                phone=self.phone, name='', password=''
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                phone='', name=self.name, password=''
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                phone=self.phone, name=self.name, password=self.password, is_superuser=False
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                phone=self.phone, name=self.name, password=self.password, is_staff=False
            )

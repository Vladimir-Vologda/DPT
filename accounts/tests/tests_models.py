from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


class TestCustomUserModel(TestCase):

    def setUp(self) -> None:
        self.phone = '+76666666666'
        self.name = 'TestUserModel'
        self.password = 'super_password'

        self.user = User.objects.create_user(
            phone=self.phone, name=self.name, password=self.password
        )

    def tearDown(self) -> None:
        self.user.delete()

    def test_verbose_name(self):
        self.field_label = self.user._meta.get_field('phone').verbose_name
        self.assertEqual(self.field_label, 'Номер телефона')
        self.field_label = self.user._meta.get_field('name').verbose_name
        self.assertEqual(self.field_label, 'Имя пользователя')
        self.field_label = self.user._meta.get_field('first_name').verbose_name
        self.assertEqual(self.field_label, 'Name')
        self.field_label = self.user._meta.get_field('last_name').verbose_name
        self.assertEqual(self.field_label, 'Surname')
        self.field_label = self.user._meta.get_field('photo').verbose_name
        self.assertEqual(self.field_label, 'Photo')
        self.field_label = self.user._meta.get_field('is_active').verbose_name
        self.assertEqual(self.field_label, 'Status active')
        self.field_label = self.user._meta.get_field('is_staff').verbose_name
        self.assertEqual(self.field_label, 'Status staff')
        self.field_label = self.user._meta.get_field('is_superuser').verbose_name
        self.assertEqual(self.field_label, 'Status superuser')
        self.field_label = self.user._meta.get_field('is_verified').verbose_name
        self.assertEqual(self.field_label, 'Verified')
        self.field_label = self.user._meta.get_field('otp').verbose_name
        self.assertEqual(self.field_label, 'Verification code')
        self.field_label = self.user._meta.get_field('slug').verbose_name
        self.assertEqual(self.field_label, 'URL-address')

    def test_max_length(self):
        self.max_length = self.user._meta.get_field('name').max_length
        self.assertEqual(self.max_length, 50)
        self.max_length = self.user._meta.get_field('first_name').max_length
        self.assertEqual(self.max_length, 50)
        self.max_length = self.user._meta.get_field('last_name').max_length
        self.assertEqual(self.max_length, 50)
        self.max_length = self.user._meta.get_field('otp').max_length
        self.assertEqual(self.max_length, 6)

    def test__str__(self):
        self.expected_object_name = f'{self.user.name} - {self.user.phone}'
        self.assertEqual(self.expected_object_name, str(self.user))

    def test_slug(self):
        self.expected_object_slug = self.user.slug
        self.assertEqual(self.expected_object_slug, 'testusermodel')

    def test_unique(self):
        self.unique = self.user._meta.get_field('phone').unique
        self.assertTrue(self.unique)
        self.unique = self.user._meta.get_field('name').unique
        self.assertTrue(self.unique)
        self.unique = self.user._meta.get_field('slug').unique
        self.assertTrue(self.unique)

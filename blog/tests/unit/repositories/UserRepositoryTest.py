from unittest.mock import Mock, MagicMock

from django.contrib.auth.models import User
from django.test import TestCase

from blog.IoCContainer import IoCContainer
from blog.models import GradeModel
from blog.models.UserModel import UserModel
from blog.repositories.UserRepository import UserRepository

first_name = "test__first"
last_name = "test__last"
grade = Mock(value=1)


# This class does not test database. Test with db is executed in integration tests.
class UserRepositoryTest(TestCase):
    @classmethod
    def setUpClass(cls):
        auth_user: User = User()
        auth_user.first_name = first_name
        auth_user.last_name = last_name
        auth_user.username = first_name + " " + last_name
        auth_user.save()

        user: UserModel = UserModel()
        user.auth_user = auth_user
        user.grade = GradeModel.objects.get(pk=grade.value)
        user.save()
        cls.user_id = user.id

        factory = Mock(get=MagicMock(return_value=user))
        IoCContainer.user_factory.override(factory)

    @classmethod
    def tearDownClass(cls):
        IoCContainer.user_factory.reset_override()

    def test_get(self):
        actual = UserRepository().get(self.user_id)

        self.assertEqual(first_name, actual.first_name)
        self.assertEqual(last_name, actual.last_name)
        self.assertEqual(grade.value, actual.grade.value)

    def test_save(self):
        actual = UserRepository().save(first_name, last_name, grade)

        self.assertEqual(first_name, actual.first_name)
        self.assertEqual(last_name, actual.last_name)
        self.assertEqual(grade, actual.grade)

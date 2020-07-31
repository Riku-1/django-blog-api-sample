from unittest.mock import Mock, MagicMock

from django.db import IntegrityError
from django.test import TestCase

from blog.IoCContainer import IoCContainer
from blog.models import GradeModel
from blog.models.UserModel import UserModel
from blog.repositories.UserRepository import UserRepository

factory_get_return = "return_value"


# This class does not test database. Test with db is executed in integration tests.
class UserRepositoryTest(TestCase):
    @classmethod
    def setUpClass(cls):
        factory = Mock(get=MagicMock(return_value=factory_get_return))
        IoCContainer.user_factory.override(factory)

    @classmethod
    def tearDownClass(cls):
        IoCContainer.user_factory.reset_override()

    def test_get(self):
        # Save user into DB for avoid missing error when get.
        user: UserModel = UserModel()
        user.first_name = "first"
        user.last_name = "last"
        user.username = "get_test"
        user.grade = GradeModel.objects.get(pk=1)
        user.save()

        actual = UserRepository().get(user.id)
        self.assertEqual(factory_get_return, actual)

    def test_save(self):
        actual = UserRepository().save("first", "last", "test_save", Mock(value=1))

        self.assertEqual(factory_get_return, actual)

    def test_save_duplicate_nickname(self):
        with self.assertRaises(
                IntegrityError
        ):
            UserRepository().save("fist", "last", "duplicate_nickName", Mock(value=1))
            UserRepository().save("fist", "last", "duplicate_nickName", Mock(value=1))

from unittest.mock import Mock

from django.test import TestCase

from blog.core.user.FreeUser import FreeUser
from blog.core.user.GoldUser import GoldUser
from blog.core.user.SilverUser import SilverUser
from blog.models import GradeModel, UserModel
from blog.repositories.UserFactory import UserFactory


def _get_user_model(user_id: int, first_name: str, last_name: str, username: str, grade_id: int) -> UserModel:
    grade_model = GradeModel.objects.get(pk=grade_id)
    return UserModel(pk=user_id, first_name=first_name, last_name=last_name,
                     username=username, grade=grade_model)


class UserFactoryTest(TestCase):
    factory: UserFactory

    def setUp(self) -> None:
        self.factory = UserFactory()

    def test_get_user(self):
        user_id = 111
        first_name = "get_first"
        last_name = "get_last"
        username = "get_nickname"
        grade_id = 1
        user_model = _get_user_model(user_id, first_name, last_name, username, grade_id)

        actual_free = self.factory.get(user_model)
        self.assertEqual(user_id, actual_free.id)
        self.assertEqual(first_name, actual_free.first_name)
        self.assertEqual(last_name, actual_free.last_name)
        self.assertEqual(username, actual_free.username)

    def test_get_free_user(self):
        user_model = _get_user_model(111, "free_first", "free_last", "free_user", 1)

        actual = self.factory.get(user_model)
        self.assertIsInstance(actual, FreeUser)

    def test_get_silver_user(self):
        user_model = _get_user_model(222, "silver_first", "silver_last", "silver_user", 2)

        actual = self.factory.get(user_model)
        self.assertIsInstance(actual, SilverUser)

    def test_get_gold_user(self):
        user_model = _get_user_model(333, "gold_first", "gold_last", "gold_user", 3)

        actual = self.factory.get(user_model)
        self.assertIsInstance(actual, GoldUser)

    def test_invalid_grade_user(self):
        invalid_grade = Mock(pk=999)
        invalid_grade_user = Mock(id=444, first_name="invalid", last_name="invalid",
                                  username="invalid", grade=invalid_grade)
        with self.assertRaises(ValueError):
            self.factory.get(invalid_grade_user)

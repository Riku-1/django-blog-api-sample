from unittest.mock import Mock

from django.test import TestCase

from blog.core.user.FreeUser import FreeUser
from blog.core.user.GoldUser import GoldUser
from blog.core.user.SilverUser import SilverUser
from blog.models import GradeModel, UserModel
from blog.repositories.UserFactory import UserFactory


class UserFactoryTest(TestCase):
    factory: UserFactory

    def setUp(self) -> None:
        self.factory = UserFactory()

    def test_get(self):
        user_id = 111
        first_name = "get_first"
        last_name = "get_last"
        nick_name = "get_nickname"
        free_grade_model = GradeModel.objects.get(pk=1)
        free_user_model = UserModel(pk=user_id, first_name=first_name, last_name=last_name,
                                    username=nick_name, grade=free_grade_model)

        actual_free = self.factory.get(free_user_model)
        self.assertEqual(user_id, actual_free.id)
        self.assertEqual(first_name, actual_free.first_name)
        self.assertEqual(last_name, actual_free.last_name)
        self.assertEqual(nick_name, actual_free.nick_name)
        self.assertIsInstance(actual_free, FreeUser)

        silver_grade_model = GradeModel.objects.get(pk=2)
        silver_user_model = UserModel(pk=user_id, first_name=first_name, last_name=last_name,
                                      username=nick_name, grade=silver_grade_model)
        actual_silver = self.factory.get(silver_user_model)
        self.assertIsInstance(actual_silver, SilverUser)

        gold_grade_model = GradeModel.objects.get(pk=3)
        gold_user_model = UserModel(pk=user_id, first_name=first_name, last_name=last_name,
                                    username=nick_name, grade=gold_grade_model)
        actual_gold = self.factory.get(gold_user_model)
        self.assertIsInstance(actual_gold, GoldUser)

from unittest.mock import Mock

from django.test import TestCase

from blog.core.user.FreeUser import FreeUser
from blog.core.user.GoldUser import GoldUser
from blog.core.user.SilverUser import SilverUser
from blog.core.values.GradeValue import GradeValue
from blog.models import GradeModel
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
        free_grade = GradeModel.objects.get(pk=1)
        free_user = Mock(pk=user_id, first_name=first_name, last_name=last_name, nick_name=nick_name, grade=free_grade)

        actual_free = self.factory.get(free_user)
        self.assertEqual(user_id, actual_free.id)
        self.assertEqual(first_name, actual_free.first_name)
        self.assertEqual(last_name, actual_free.last_name)
        self.assertEqual(nick_name, actual_free.nick_name)
        self.assertIsInstance(actual_free, FreeUser)

        silver_grade = GradeModel.objects.get(pk=2)
        silver_user = Mock(pk=user_id, first_name=first_name, last_name=last_name, grade=silver_grade)
        actual_silver = self.factory.get(silver_user)
        self.assertIsInstance(actual_silver, SilverUser)

        gold_grade = GradeModel.objects.get(pk=3)
        gold_user = Mock(pk=user_id, first_name=first_name, last_name=last_name, grade=gold_grade)
        actual_gold = self.factory.get(gold_user)
        self.assertIsInstance(actual_gold, GoldUser)

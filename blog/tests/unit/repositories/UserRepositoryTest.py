from unittest.mock import Mock, MagicMock

from django.contrib.auth.models import User
from django.test import TestCase

from blog.core.values.GradeValue import GradeValue
from blog.models import GradeModel
from blog.models.UserModel import UserModel
from blog.repositories.UserRepository import UserRepository


def _get_mocked_repository(first_name: str, last_name: str, grade: GradeValue) -> UserRepository:
    factory = Mock()
    user = Mock(first_name=first_name, last_name=last_name, grade=grade)
    factory.get = MagicMock(return_value=user)
    return UserRepository(factory)


class UserRepositoryTest(TestCase):
    # This test does not test database. Test with db is executed in integration tests.
    def test_get(self):
        first_name = "test_get_first"
        last_name = "test_get_last"
        grade = GradeValue.FREE

        auth_user: User = User()
        auth_user.first_name = first_name
        auth_user.last_name = last_name
        auth_user.username = first_name + " " + last_name
        auth_user.save()

        user: UserModel = UserModel()
        user.auth_user = auth_user
        user.grade = GradeModel.objects.get(pk=grade.value)
        user.save()  # Save is required to avoid no records error.

        repository = _get_mocked_repository(first_name, last_name, grade)
        actual = repository.get(auth_user.pk)

        self.assertEqual(first_name, actual.first_name)
        self.assertEqual(last_name, actual.last_name)
        self.assertEqual(grade.value, actual.grade.value)

    def test_save(self):
        first_name = "test_save_first"
        last_name = "test_save_last"
        grade = Mock(value=1)
        repository = _get_mocked_repository(first_name, last_name, grade)

        actual = repository.save(first_name, last_name, grade)

        self.assertEqual(first_name, actual.first_name)
        self.assertEqual(last_name, actual.last_name)
        self.assertEqual(grade, actual.grade)

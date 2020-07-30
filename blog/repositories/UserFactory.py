from abc import ABC, abstractmethod

from blog.core.user.FreeUser import FreeUser
from blog.core.user.GoldUser import GoldUser
from blog.core.user.IUser import IUser
from blog.core.user.SilverUser import SilverUser
from blog.core.values.GradeValue import GradeValue
from blog.models import UserModel


class IUserFactory(ABC):
    @abstractmethod
    def get(self, user: UserModel) -> IUser:
        pass


class UserFactory(IUserFactory):
    def get(self, user: UserModel) -> IUser:
        user_id = user.pk
        first_name = user.first_name
        last_name = user.last_name
        nick_name = user.username
        grade = user.grade

        if grade.pk == GradeValue.FREE.value:
            return FreeUser(user_id, first_name, last_name, nick_name)
        elif grade.pk == GradeValue.SILVER.value:
            return SilverUser(user_id, first_name, last_name, nick_name)
        elif grade.pk == GradeValue.GOLD.value:
            return GoldUser(user_id, first_name, last_name, nick_name)
        else:
            raise Exception(f'grade of user {user_id} is invalid')

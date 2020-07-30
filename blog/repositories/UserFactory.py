from abc import ABC, abstractmethod

from blog.core.user.FreeUser import FreeUser
from blog.core.user.GoldUser import GoldUser
from blog.core.user.IUser import IUser
from blog.core.user.SilverUser import SilverUser
from blog.core.values.GradeValue import GradeValue
from blog.models import UserModel


class IUserFactory(ABC):
    @abstractmethod
    def get(self, user_model: UserModel) -> IUser:
        pass


class UserFactory(IUserFactory):
    def get(self, user_model: UserModel) -> IUser:
        user_id = user_model.pk
        first_name = user_model.first_name
        last_name = user_model.last_name
        username = user_model.username
        grade = user_model.grade

        if grade.pk == GradeValue.FREE.value:
            return FreeUser(user_id, first_name, last_name, username)
        elif grade.pk == GradeValue.SILVER.value:
            return SilverUser(user_id, first_name, last_name, username)
        elif grade.pk == GradeValue.GOLD.value:
            return GoldUser(user_id, first_name, last_name, username)
        else:
            raise ValueError(f'grade of user {user_id} is invalid')

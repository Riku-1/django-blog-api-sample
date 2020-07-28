from abc import ABC, abstractmethod

from django.contrib.auth.models import User

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
        grade = user.grade
        user_id = user.pk
        auth_user: User = user.auth_user
        first_name = auth_user.first_name
        last_name = auth_user.last_name

        if grade == GradeValue.FREE:
            return FreeUser(user_id, first_name, last_name)
        elif grade == GradeValue.SILVER:
            return SilverUser(user_id, first_name, last_name)
        elif grade == GradeValue.GOLD:
            return GoldUser(user_id, first_name, last_name)
        else:
            raise Exception(f"grade of user {user_id} is invalid")

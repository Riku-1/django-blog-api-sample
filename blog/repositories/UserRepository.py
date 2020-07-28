from abc import ABC, abstractmethod
from dataclasses import dataclass

from django.contrib.auth.models import User

from blog.core.values.GradeValue import GradeValue
from blog.core.user.IUser import IUser
from blog.models import GradeModel
from blog.models.UserModel import UserModel
from blog.repositories.UserFactory import IUserFactory


@dataclass
class IUserRepository(ABC):
    factory: IUserFactory

    @abstractmethod
    def get(self, user_id: int) -> IUser:
        pass

    @abstractmethod
    def save(self, first_name: str, last_name: str, grade: GradeValue) -> IUser:
        pass


class UserRepository(IUserRepository):
    def get(self, user_id: int) -> IUser:
        user: UserModel = UserModel.objects.get(pk=user_id)

        return self.factory.get(user)

    def save(self, first_name: str, last_name: str, grade: GradeValue) -> IUser:
        auth_user: User = User()
        auth_user.first_name = first_name
        auth_user.last_name = last_name
        auth_user.username = first_name + " " + last_name
        auth_user.save()

        user = UserModel()
        user.auth_user = auth_user
        user.grade = GradeModel.objects.get(pk=grade.value)

        return self.factory.get(user)

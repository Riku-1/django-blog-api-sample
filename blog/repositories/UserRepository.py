from abc import ABC, abstractmethod
from dataclasses import dataclass

from blog.IoCContainer import IoCContainer
from blog.core.values.GradeValue import GradeValue
from blog.core.user.IUser import IUser
from blog.models import GradeModel
from blog.models.UserModel import UserModel
from blog.repositories.UserFactory import IUserFactory


@dataclass
class IUserRepository(ABC):
    @abstractmethod
    def get(self, user_id: int) -> IUser:
        pass

    @abstractmethod
    def save(self, first_name: str, last_name: str, username: str, grade: GradeValue) -> IUser:
        pass


class UserRepository(IUserRepository):
    factory: IUserFactory = IoCContainer.user_factory()

    def get(self, user_id: int) -> IUser:
        user: UserModel = UserModel.objects.get(pk=user_id)

        return self.factory.get(user)

    def save(self, first_name: str, last_name: str, username: str, grade: GradeValue) -> IUser:
        user = UserModel()
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.grade = GradeModel.objects.get(pk=grade.value)
        user.save()

        return self.factory.get(user)

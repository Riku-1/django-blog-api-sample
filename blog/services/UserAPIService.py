from abc import ABC, abstractmethod

from django.http import JsonResponse

from blog.repositories.UserRepository import IUserRepository
from blog.response_creators.UserResponseCreator import IUserResponseCreator


class IUserAPIService(ABC):
    @abstractmethod
    def get(self, user_id: int) -> JsonResponse:
        pass


class UserAPIService(IUserAPIService):
    repository: IUserRepository
    json_creator: IUserResponseCreator

    def __init__(self):
        from blog.IoCContainer import IoCContainer
        self.repository = IoCContainer.user_repository()
        self.json_creator = IoCContainer.user_api_json_creator()

    def get(self, user_id: int) -> JsonResponse:
        user = self.repository.get(user_id)
        return self.json_creator.get(user)

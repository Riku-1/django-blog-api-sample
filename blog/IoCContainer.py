from dependency_injector import containers, providers

from blog.repositories.UserFactory import UserFactory
from blog.repositories.UserRepository import UserRepository
from blog.response_creators.UserResponseCreator import UserResponseCreator
from blog.services.UserAPIService import UserAPIService


class IoCContainer(containers.DeclarativeContainer):
    user_factory = providers.Singleton(UserFactory)
    user_repository = providers.Singleton(UserRepository)
    user_api_json_creator = providers.Singleton(UserResponseCreator)
    user_api_service = providers.Singleton(UserAPIService)

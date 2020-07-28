from dependency_injector import containers, providers

from blog.repositories.UserFactory import UserFactory


class IoCContainer(containers.DeclarativeContainer):
    user_factory = providers.Singleton(UserFactory)

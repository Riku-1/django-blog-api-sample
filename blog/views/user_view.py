from blog.IoCContainer import IoCContainer
from blog.services.UserAPIService import IUserAPIService

user_api_service: IUserAPIService = IoCContainer.user_api_service()


def base(request):
    pass


def with_id(request, user_id: int):
    if request.method == "GET":
        return user_api_service.get(user_id)

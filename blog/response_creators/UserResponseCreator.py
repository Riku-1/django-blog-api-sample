from abc import ABC, abstractmethod

from django.http import JsonResponse
from rest_framework import serializers

from blog.core.user.IUser import IUser


class IUserResponseCreator(ABC):
    @abstractmethod
    def get(self, user: IUser) -> JsonResponse:
        pass


class UserResponseCreator(IUserResponseCreator):
    def get(self, user: IUser) -> JsonResponse:
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)


class GradeSerializer(serializers.Serializer):
    value = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    username = serializers.CharField(max_length=20)
    grade = GradeSerializer()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass




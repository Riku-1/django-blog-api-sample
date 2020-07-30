from django.contrib.auth.models import User
from django.db import models

from blog.models.GradeModel import GradeModel


class UserModel(User):
    grade = models.ForeignKey(GradeModel, on_delete=models.PROTECT)

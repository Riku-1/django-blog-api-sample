from django.contrib.auth.models import User
from django.db import models

from blog.models.GradeModel import GradeModel


class UserModel(models.Model):
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.ForeignKey(GradeModel, on_delete=models.PROTECT)

    class Meta:
        db_table = "user"

from blog.core.user.IUser import IUser
from blog.core.values.GradeValue import GradeValue


class GoldUser(IUser):
    @property
    def grade(self) -> GradeValue:
        return GradeValue.GOLD

    @property
    def readable_paid_post_num(self) -> int:
        return 20

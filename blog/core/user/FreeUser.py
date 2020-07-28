from blog.core.values.GradeValue import GradeValue
from blog.core.user.IUser import IUser


class FreeUser(IUser):
    @property
    def grade(self) -> GradeValue:
        return GradeValue.FREE

    @property
    def readable_paid_post_num(self) -> int:
        return 0

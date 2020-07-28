from blog.core.user.IUser import IUser
from blog.core.values.GradeValue import GradeValue


class SilverUser(IUser):
    @property
    def grade(self) -> GradeValue:
        return GradeValue.SILVER

    @property
    def readable_paid_post_num(self) -> int:
        return 5

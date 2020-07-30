from abc import ABC, abstractmethod
from dataclasses import dataclass

from blog.core.values.GradeValue import GradeValue


@dataclass
class IUser(ABC):
    id: int
    first_name: str
    last_name: str
    username: str

    @property
    @abstractmethod
    def grade(self) -> GradeValue:
        pass

    @property
    @abstractmethod
    def readable_paid_post_num(self) -> int:
        pass

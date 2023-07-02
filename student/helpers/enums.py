from enum import Enum


class SexOptions(Enum):
    FEMALE: str = "f"
    MALE: str = "m"


class GradeOptions(Enum):
    DIPLOMA: str = "diploma"
    BACHELOR: str = "bachelor"
    MASTER: str = "master"
    DOCTORATE: str = "phd"

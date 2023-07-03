from enum import Enum

class GenderOptions(Enum):
    """
    An enumeration of gender options.

    This enumeration is used to represent the gender of a person. It has two
    possible values: "f" for female and "m" for male.

    Attributes
    ----------
    FEMALE : str
        Represents the female gender.
    MALE : str
        Represents the male gender.

    Examples
    --------
    >>> gender = GenderOptions.FEMALE
    >>> print(gender.value)
    'f'
    """
    FEMALE: str = "f"
    MALE: str = "m"


class GradeOptions(Enum):
    """
    An enumeration of grade options.

    This enumeration is used to represent the academic degree of a person. It
    has four possible values: "diploma", "bachelor", "master", and "phd".

    Attributes
    ----------
    DIPLOMA : str
        Represents a diploma degree.
    BACHELOR : str
        Represents a bachelor's degree.
    MASTER : str
        Represents a master's degree.
    DOCTORATE : str
        Represents a doctoral degree.

    Examples
    --------
    >>> grade = GradeOptions.BACHELOR
    >>> print(grade.value)
    'bachelor'
    """
    DIPLOMA: str = "diploma"
    BACHELOR: str = "bachelor"
    MASTER: str = "master"
    DOCTORATE: str = "phd"

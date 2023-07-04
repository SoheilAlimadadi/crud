from enum import (
    Enum,
    StrEnum
)

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
    'FEMALE'
    """
    FEMALE: str = "FEMALE"
    MALE: str = "MALE"


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
    'BACHELOR'
    """
    DIPLOMA: str = "DIPLOMA"
    BACHELOR: str = "BACHELOR"
    MASTER: str = "MASTER"
    DOCTORATE: str = "DOCTRATE"


class RegexPatternEnum(StrEnum):
    """
    An enumeration class for regex patterns.

    This class represents different regex patterns as an enumeration.
    It currently contains only one member, `IRAN_PHONE_NUMBER`, representing the regex pattern for
    Iranian phone numbers.

    Attributes
    ----------
    IRAN_PHONE_NUMBER : str
        The regex pattern for Iranian phone numbers. It matches a string that starts with '+98' or '0',
        followed by exactly 9 digits.
    """

    IRAN_PHONE_NUMBER = r'^(\+98|0)?9\d{9}$'

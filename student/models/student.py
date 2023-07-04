import re
from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    DateTime,
    Integer,
    Enum,
    CheckConstraint
)
from sqlalchemy.orm import validates

from database import db
from student.helpers.enums import (
    GenderOptions,
    GradeOptions,
    RegexPatternEnum
)
from student.helpers.exceptions import InvalidPhoneNumberError

class Student(db.Base):
    """
    A database model representing a student.

    Attributes
    ----------
    id : int
        The primary key of the student, autoincremented.
    first_name : str
        The first name of the student.
    last_name : str
        The last name of the student.
    phone_number : str
        The unique phone number of the student.
    gender : GenderOptions
        The gender of the student. It is an Enum with constraints and string validation.
    birth_date : DateTime
        The birth date of the student.
    education : GradeOptions
        The education level of the student. It is an Enum with constraints and string validation.
    enrollment_date : DateTime
        The date of enrollment of the student. It defaults to the current date and time.
    graduation_date : DateTime
        The date of graduation of the student.
    address : str
        The address of the student.

    Methods
    -------
    validate_phone_number(key, value)
        Validates the phone number of the student.
    """
    __tablename__ = "students"
    database = db

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    first_name = Column(
        String(50),
    )

    last_name = Column(
        String(50),
    )

    phone_number = Column(
        String(15),
        unique=True,
    )

    gender = Column(
        Enum(
            GenderOptions,
            create_constraint=True,
            validate_strings=True,
        ),
    )

    birth_date = Column(
        DateTime,
    )

    education = Column(
        Enum(
            GradeOptions,
            create_constraint=True,
            validate_strings=True
        ),
    )

    enrollment_date = Column(
        DateTime,
        default=datetime.now()
    )

    graduation_date = Column(
        DateTime,
    )

    address = Column(
        String(255),
    )

    @validates('phone_number')
    def validate_phone_number(self, key, value: str) -> str:
        """
        Validates the phone number of the student.

        Parameters
        ----------
        key : str
            The key to validate.
        value : str
            The value of the key to validate.

        Returns
        -------
        str
            The validated phone number.

        Raises
        ------
        InvalidPhoneNumberError
            If the phone number is not valid.
        """
        if value.isdigit() and re.match(
            RegexPatternEnum.IRAN_PHONE_NUMBER,
            value
        ):
            return value
        else:
            raise InvalidPhoneNumberError

    def __str__(self) -> str:
        """
        Returns a string representation of the student.

        Returns
        -------
        str
            A string representation of the student.
        """
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the student suitable for debugging.

        Returns
        -------
        str
            A string representation of the student suitable for debugging.
        """
        return f"<student: {self.first_name} {self.last_name}, " \
                f"phone number: {self.phone_number}>"

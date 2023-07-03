from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import column_property
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database import Base, db
from student.helpers.enums import (
    GenderOptions,
    GradeOptions
)


class Student(Base):
    """
    A class representing a student in the database.

    This class defines a SQLAlchemy model for a student in the database.
    It includes attributes for the student's first and last name, phone
    number, gender, birth date, grade level, enrollment date, graduation
    date, and address. The `fullname` attribute is a computed column that
    combines the student's first and last name.

    Attributes
    ----------
    id : Mapped[int]
        The primary key for the student record.
    firstname : Mapped[str]
        The first name of the student.
    lastname : Mapped[str]
        The last name of the student.
    fullname : Mapped[str]
        A computed column that combines the first and last name of the student.
    phone_number : Mapped[str]
        The phone number of the student.
    gender : Mapped[GenderOptions]
        The gender of the student.
    birth_date : Mapped[date]
        The birth date of the student.
    grade : Mapped[GradeOptions]
        The grade level of the student.
    enrollment_date : Mapped[date]
        The enrollment date of the student.
    graduation_date : Mapped[date]
        The graduation date of the student.
    address : Mapped[str]
        The address of the student.

    Methods
    -------
    __str__() -> str
        Returns a string representation of the student.
    __repr__() -> str
        Returns a string representation of the student suitable for debugging.

    Examples
    --------
    To create a new student record, simply create a new instance of the `Student`
    class and add it to the session:

    >>> from datetime import date
    >>> from student.helpers.enums import GenderOptions, GradeOptions
    >>> from database import db
    >>> from models import Student
    >>> student = Student(firstname='John', lastname='Doe', phone_number='555-1234',
    ...                    gender=GenderOptions.MALE, birth_date=date(2000, 1, 1),
    ...                    grade=GradeOptions.BACHELOR, enrollment_date=date(2020, 9, 1),
    ...                    graduation_date=date(2024, 5, 1), address='123 Main St')
    >>> db.session.add(student)
    >>> db.session.commit()
    """
    __tablename__ = "student"
    database = db

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[str] = column_property(firstname + " " + lastname)
    phone_number: Mapped[str] = mapped_column(String(15), unique=True)
    gender : Mapped[GenderOptions]
    birth_date: Mapped[date]
    grade: Mapped[GradeOptions]
    enrollment_date: Mapped[date]
    graduation_date: Mapped[date]
    address: Mapped[str] = mapped_column(String(255))

    def __str__(self) -> str:
        """
        Returns a string representation of the student.

        Returns
        -------
        str
            A string representation of the student.
        """
        return f'{self.fullname}'

    def __repr__(self) -> str:
        """
        Returns a string representation of the student suitable for debugging.

        Returns
        -------
        str
            A string representation of the student suitable for debugging.
        """
        return f'<student {self.fullname}>'

from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import column_property
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database import Base
from student.helpers.enums import (
    SexOptions,
    GradeOptions
)


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[str] = column_property(firstname + " " + lastname)
    sex : Mapped[SexOptions]
    birth_date: Mapped[date]
    grade: Mapped[GradeOptions]
    enrollment_date: Mapped[date]
    graduation_date: Mapped[date]
    address: Mapped[str] = mapped_column(String(255))
    phone_number: Mapped[str] = mapped_column(String(15))

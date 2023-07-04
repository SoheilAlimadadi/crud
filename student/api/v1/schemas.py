from pydantic import BaseModel
from datetime import date, datetime
from student.helpers.enums import (
    GenderOptions,
    GradeOptions
)


class StudentBase(BaseModel):
    """
    A Pydantic model representing the base attributes of a student.

    This class defines a Pydantic model for the base attributes of a student.
    It is used as a base class for other Pydantic models that include additional
    attributes.

    Config:
        orm_mode (bool): A configuration option that allows this model to be
        used in SQLAlchemy ORM mode.

    Examples
    --------
    To create a new Pydantic model representing a student with additional
    attributes, simply inherit from the `StudentBase` class and add the
    additional attributes:

    >>> from pydantic import BaseModel
    >>> from datetime import date
    >>> from student.helpers.enums import GenderOptions, GradeOptions
    >>> class StudentResponseSchema(StudentBase):
    ...     first_name: str
    ...     last_name: str
    ...     phone_number: str
    ...     gender: GenderOptions
    ...     birth_date: date
    ...     education: GradeOptions
    ...     enrollment_date: date
    ...     graduation_date: date
    ...     address: str
    """
    class Config:
        orm_mode = True


class StudentResponseSchema(StudentBase):
    """
    A Pydantic model representing the attributes of a student.

    This class defines a Pydantic model for the attributes of a student.
    It includes attributes for the student's first and last name, phone
    number, gender, birth date, education level, enrollment date, graduation
    date, and address.

    Examples
    --------
    To create a new Pydantic model representing a student with the same
    attributes as the `StudentResponseSchema`, simply inherit from the
    `StudentResponseSchema` class:

    >>> from student.schemas import StudentResponseSchema
    >>> class StudentRequestSchema(StudentResponseSchema):
    ...     pass
    """
    id: int
    first_name: str
    last_name: str
    phone_number: str
    gender: GenderOptions
    birth_date: date
    education: GradeOptions
    enrollment_time = datetime
    graduation_date: date
    address: str


class StudentUpdateSchema(StudentBase):
    """
    A Pydantic model representing the attributes of a student.

    This class defines a Pydantic model for the attributes of a student.
    It includes attributes for the student's first and last name, phone
    number, gender, birth date, education level, enrollment date, graduation
    date, and address.

    Examples
    --------
    To create a new Pydantic model representing a student with the same
    attributes as the `StudentResponseSchema`, simply inherit from the
    `StudentResponseSchema` class:

    >>> from student.schemas import StudentResponseSchema
    >>> class StudentRequestSchema(StudentResponseSchema):
    ...     pass
    """
    first_name: str
    last_name: str
    phone_number: str
    gender: GenderOptions
    birth_date: date
    education: GradeOptions
    graduation_date: date
    address: str


class UpdateResponseSchema(BaseModel):
    """
    A Pydantic model representing the result of an update operation.

    This class defines a Pydantic model for the result of an update operation.
    It includes a single attribute `result`, which is a boolean value indicating
    whether the update operation was successful or not.

    Attributes
    ----------
    result : bool
        A boolean value indicating whether the update operation was successful.

    Examples
    --------
    To create a new instance of the `UpdateResponseSchema` class, simply
    provide a value for the `result` attribute:

    >>> from student.schemas import UpdateResponseSchema
    >>> result = UpdateResponseSchema(result=True)
    """
    result: bool


class DeleteResponseSchema(BaseModel):
    """
    A Pydantic model representing the result of a delete operation.

    This class defines a Pydantic model for the result of a delete operation.
    It includes a single attribute `result`, which is a boolean value indicating
    whether the delete operation was successful or not.

    Attributes
    ----------
    result : bool
        A boolean value indicating whether the delete operation was successful.

    Examples
    --------
    To create a new instance of the `DeleteResponseSchema` class, simply
    provide a value for the `result` attribute:

    >>> from student.schemas import DeleteResponseSchema
    >>> result = DeleteResponseSchema(result=True)
    """
    result: bool

from typing import List, Optional

from sqlalchemy import select, update, insert, delete
from sqlalchemy.exc import SQLAlchemyError

from .interface import IDataAccessLayer
from student.models import Student
from kernel.settings.logging import coreLogger
from student.helpers.exceptions import (
    RetrievalError,
    DeletionError,
    CreationError,
    UpdateError,
)


class StudentDataAccessLayer(IDataAccessLayer):
    """
    A class used to interact with the Student model in the database.

    ...

    Attributes
    ----------
    Student : model
        a data model representing a student in the database

    Methods
    -------
    get_all():
        Retrieves all students from the database.
    get_one(phone_number):
        Retrieves a student from the database by their phone number.
    create(**kwargs):
        Creates a new student in the database.
    update(id, **kwargs):
        Updates a student in the database by their id.
    delete(phone_number):
        Deletes a student from the database by their phone number.
    """
    def get_all(self) -> List[Student]:
        """
        Retrieves all students from the database.

        Returns
        -------
        list
            a list of Student objects
        """
        try:
            stmt = select(Student)
            students = Student.database.session.execute(stmt).fetchall()
            coreLogger.info(f"Retrieved all {len(students)} students from the database")
            return students
        except SQLAlchemyError as e:
            coreLogger.error(f"Failed to get all students: {e}")
            raise RetrievalError("Error retrieving all students from database")

    def get_one(self, id: int) -> Optional[Student]:
        """
        Retrieves a student from the database by their id

        Parameters
        ----------
        phone_number : int
            the student's id

        Returns
        -------
        Student
            a Student object
        """
        try:
            stmt = select(Student) \
                    .where(Student.id==id)
            student = Student.database.session.execute(stmt).first()
            if student:
                coreLogger.info(f"Retrieved student with id {id} from the database")
            else:
                coreLogger.info(f"No student found with id {id} in the database")
            return student
        except SQLAlchemyError as e:
            coreLogger.error(f"Failed to get student with id {id}: {e}")
            raise RetrievalError(
                f"Error retrieving student with id {id} from database"
            )

    def create(self, **kwargs) -> Student:
        """
        Creates a new student in the database.

        Parameters
        ----------
        **kwargs : dict
            arbitrary keyword arguments

        Returns
        -------
        Student
            a newly created Student object
        """
        try:
            instance = Student(**kwargs)
            Student.database.session.add(instance)
            Student.database.session.commit()
            coreLogger.info(f"Created new student with id {instance.id}")
            return instance
        except SQLAlchemyError as e:
            Student.database.session.rollback()
            coreLogger.error(f"Failed to create student: {e}")
            raise CreationError("Error creating student in database")

    def update(self, id: int, **kwargs) -> Optional[bool]:
        """
        Updates a student in the database by their id.

        Parameters
        ----------
        id : int
            the student's id
        **kwargs : dict
            arbitrary keyword arguments

        Returns
        -------
        bool
            True if the update operation was successful, False otherwise
        """
        try:
            stmt = update(Student) \
                        .where(Student.id == id) \
                            .values(**kwargs)
            result = Student.database.session.execute(stmt)
            if result:
                Student.database.session.commit()
                coreLogger.info(f"Updated student with id {id}")
            return {'result': f'{result.rowcount > 0}'}
        except SQLAlchemyError as e:
            Student.database.session.rollback()
            coreLogger.error(f"Failed to update student with id {id}: {e}")
            raise UpdateError(
                f"Error updating student with id {id} in database"
            )

    def delete(self, id: int) -> Optional[bool]:
        """
        Deletes a student from the database by their id.

        Parameters
        ----------
        phone_number : str
            the student's id

        Returns
        -------
        bool
            True if the delete operation was successful, False otherwise
        """
        try:
            stmt = delete(Student) \
                        .where(Student.id==id)
            result = Student.database.session.execute(stmt)
            if result:
                Student.database.session.commit()
                coreLogger.info(f"Deleted student with id {id}")
            return {'result': f'{result.rowcount > 0}'}
        except SQLAlchemyError as e:
            Student.database.session.rollback()
            coreLogger.error(f"Failed to delete student with id {id}: {e}")
            raise DeletionError(
                f"Error deleting student with id {id} from database"
            )

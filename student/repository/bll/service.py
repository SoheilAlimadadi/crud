from typing import List, Optional
from student.models import Student
from student.repository.dal import StudentDataAccessLayer

class StudentService:
    """
    A service layer used to interact with the Student model in the database.

    ...

    Methods
    -------
    get_all():
        Retrieves all students from the database.
    get_one(id):
        Retrieves a student from the database by their id.
    create(**kwargs):
        Creates a new student in the database.
    update(id, **kwargs):
        Updates a student in the database by their id.
    delete(id):
        Deletes a student from the database by their id.
    """

    def __init__(self):
        self.dal = StudentDataAccessLayer()

    def get_all(self) -> List[Student]:
        """
        Retrieves all students from the database.

        Returns
        -------
        list
            a list of Student objects
        """
        return self.dal.get_all()

    def get_one(self, id: int) -> Optional[Student]:
        """
        Retrieves a student from the database by their id

        Parameters
        ----------
        id : int
            the student's id

        Returns
        -------
        Student
            a Student object
        """
        return self.dal.get_one(id)

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
        return self.dal.create(**kwargs)

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
        return self.dal.update(id, **kwargs)

    def delete(self, id: int) -> Optional[bool]:
        """
        Deletes a student from the database by their id.

        Parameters
        ----------
        id : int
            the student's id

        Returns
        -------
        bool
            True if the delete operation was successful, False otherwise
        """
        return self.dal.delete(id)

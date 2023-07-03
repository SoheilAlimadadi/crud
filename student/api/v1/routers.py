from fastapi import APIRouter, HTTPException, status
from typing import List

from .schemas import (
    StudentResponseSchema,
    UpdateResponseSchema,
    DeleteResponseSchema,
    StudentUpdateSchema
)
from student.repository.bll import StudentService

router = APIRouter()
service_layer = StudentService()


@router.post("/", response_model=StudentResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentResponseSchema):
    """
    Creates a new student in the database.

    Parameters
    ----------
    student : StudentResponseSchema
        The student data to create.

    Returns
    -------
    StudentResponseSchema
        The newly created student data.

    Raises
    ------
    HTTPException
        If there is an error creating the student.
    """
    new_student = service_layer.create(**student.dict())
    if new_student is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating student")
    return new_student


@router.get("/", response_model=List[StudentResponseSchema])
async def read_students():
    """
    Retrieves all students from the database.

    Returns
    -------
    List[StudentResponseSchema]
        A list of student data.

    Raises
    ------
    HTTPException
        If there are no students found.
    """
    students = service_layer.get_all()
    if not students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No students found")
    return [student[0] for student in students]


@router.get("/{student_id}", response_model=StudentResponseSchema)
async def read_student(student_id: int):
    """
    Retrieves a student from the database by their id.

    Parameters
    ----------
    student_id : int
        The id of the student to retrieve.

    Returns
    -------
    StudentResponseSchema
        The student data.

    Raises
    ------
    HTTPException
        If the student is not found.
    """
    student = service_layer.get_one(student_id)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student[0]


@router.put("/{student_id}", response_model=UpdateResponseSchema)
async def update_student(student_id: int, student: StudentUpdateSchema):
    """
    Updates a student in the database by their id.

    Parameters
    ----------
    student_id : int
        The id of the student to update.
    student : StudentResponseSchema
        The updated student data.

    Returns
    -------
    UpdateResponseSchema
        A response indicating the success or failure of the update operation.

    Raises
    ------
    HTTPException
        If the student is not found.
    """
    updated_student = service_layer.update(student_id, **student.dict())
    if updated_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return updated_student


@router.delete("/{student_id}", response_model=DeleteResponseSchema)
async def delete_student(student_id: int):
    """
    Deletes a student from the database by their id.

    Parameters
    ----------
    student_id : int
        The id of the student to delete.

    Returns
    -------
    DeleteResponseSchema
        A response indicating the success or failure of the delete operation.

    Raises
    ------
    HTTPException
        If the student is not found.
    """
    deleted_student = service_layer.delete(student_id)
    if deleted_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return deleted_student

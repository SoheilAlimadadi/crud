from fastapi import FastAPI
from student.api.v1 import router

app = FastAPI()

app.include_router(router, prefix="/v1/students")

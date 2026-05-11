from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Student(BaseModel):
    name: str
    marks: int


app = FastAPI(title="FastAPI Introduction Demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students: list[Student] = []


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/students")
def get_students() -> list[Student]:
    return students


@app.post("/students")
def create_student(student: Student) -> dict[str, object]:
    students.append(student)
    return {"message": "Student added", "student": student}

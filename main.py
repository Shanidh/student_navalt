from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import get_students, create_student, update_student, delete_student, get_student_teachers
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

app = FastAPI()

# Pydantic models for request validation
class StudentCreate(BaseModel):
    name: str
    email: str

class StudentUpdate(BaseModel):
    name: str
    email: str

@app.get("/students/")
async def read_students(db: AsyncSession = Depends(get_db)):
    return await get_students(db)

@app.post("/students/")
async def add_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    return await create_student(db, student.name, student.email)

@app.put("/students/{student_id}")
async def update_student_info(student_id: int, student: StudentUpdate, db: AsyncSession = Depends(get_db)):
    updated_student = await update_student(db, student_id, student.name, student.email)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@app.delete("/students/{student_id}")
async def remove_student(student_id: int, db: AsyncSession = Depends(get_db)):
    deleted_student =await delete_student(db, student_id)
    if deleted_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"status": "Student deleted successfully"}

@app.get("/students/{student_id}/teachers")
async def list_student_teachers(student_id: int, db: AsyncSession = Depends(get_db)):
    teachers =await get_student_teachers(db, student_id)
    if teachers is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return teachers

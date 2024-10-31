from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Student, Teacher

# Get all students
async def get_students(db: AsyncSession):
    stmt = select(Student)
    result = await db.execute(stmt)
    return result.scalars().all()

# Create a new student
async def create_student(db: AsyncSession, name: str, email: str):
    new_student = Student(name=name, email=email)
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student

# Update a student's details
async def update_student(db: AsyncSession, student_id: int, name: str, email: str):
    stmt = select(Student).filter(Student.id == student_id)
    result = await db.execute(stmt)
    student = result.scalars().first()
    
    if student:
        student.name = name
        student.email = email
        await db.commit()
        await db.refresh(student)
    return student

# Delete a student
async def delete_student(db: AsyncSession, student_id: int):
    stmt = select(Student).filter(Student.id == student_id)
    result = await db.execute(stmt)
    student = result.scalars().first()
    
    if student:
        await db.delete(student)
        await db.commit()
    return student

# Get teachers for a specific student
async def get_student_teachers(db: AsyncSession, student_id: int):
    stmt = select(Student).filter(Student.id == student_id)
    result = await db.execute(stmt)
    student = result.scalars().first()
    
    return student.teachers if student else None

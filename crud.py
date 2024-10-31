from sqlalchemy.orm import Session
from models import Student, Teacher

# Get all students
def get_students(db: Session):
    return db.query(Student).all()

# Create a new student
def create_student(db: Session, name: str, email: str):
    new_student = Student(name=name, email=email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# Update a student's details
def update_student(db: Session, student_id: int, name: str, email: str):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        student.name = name
        student.email = email
        db.commit()
        db.refresh(student)
    return student

# Delete a student
def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student

# Get teachers for a specific student
def get_student_teachers(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    return student.teachers if student else None

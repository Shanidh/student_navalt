from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

association_table = Table(
    "student_teacher",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("teacher_id", Integer, ForeignKey("teachers.id")),
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    teachers = relationship("Teacher", secondary=association_table, back_populates="students")

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    students = relationship("Student", secondary=association_table, back_populates="teachers")

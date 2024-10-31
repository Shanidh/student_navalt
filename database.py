from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/student_management"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get a session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



async def get_db():
    async with SessionLocal() as session:
        yield session

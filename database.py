from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/student_management"

# Use create_async_engine for asynchronous database connections
engine = create_async_engine(DATABASE_URL, echo=True)

# Configure sessionmaker to use AsyncSession
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession  # Use AsyncSession for async support
)

# Base class for models
Base = declarative_base()

# Dependency to get an async database session
async def get_db():
    async with SessionLocal() as session:
        yield session

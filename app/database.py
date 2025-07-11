# db.py
from sqlalchemy import create_engine , text , inspect
from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker
from sqlalchemy.orm import declarative_base


DB_URL = "postgresql+asyncpg://admin:12345678@localhost:5432/secure_female_taxi"

engine = create_async_engine(DB_URL)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
"""
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")

test = inspect(engine)

check_tables = test.get_table_names()

print(check_tables)

"""
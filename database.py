from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from decouple import config


DATABASE_URL = f"postgresql+asyncpg://{config('DB_USER')}:{config('PASSWORD')}@{config('HOST')}:{config('PORT')}/{config('DB_NAME')}"

engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

db_dependency = Annotated[AsyncSession, Depends(get_db)]


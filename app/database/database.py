from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import os 

if find_dotenv():
    load_dotenv()
    
else:
    exit()
DB_PATH = os.getenv('DATABASE_URL') if os.getenv('DATABASE_URL') else os.getenv('DB_PATH')

Base = declarative_base()

engine = create_async_engine(DB_PATH,echo=True)
async_session = sessionmaker(engine, class_= AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session 
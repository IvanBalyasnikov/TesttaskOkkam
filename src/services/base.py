from sqlalchemy import insert
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import async_sessionmaker
from pydantic import BaseModel

class BaseService:
    repository:BaseRepository
    session_maker:async_sessionmaker
    schema:BaseModel
            

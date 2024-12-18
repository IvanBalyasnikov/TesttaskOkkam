
from pydantic import BaseModel
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base

class BaseRepository():
    model:Base = None
    schema:BaseModel

    def __init__(self, session) -> None:
        self.session:AsyncSession = session
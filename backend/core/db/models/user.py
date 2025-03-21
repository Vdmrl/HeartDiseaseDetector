from sqlalchemy.orm import Mapped
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from core.db.engine import Base
from core.db.engine import get_async_session, get_test_async_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession



class User(Base, SQLAlchemyBaseUserTable[int]):
    age: Mapped[int]
    pass

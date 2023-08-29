from database import Base
from sqlalchemy.types import String, Boolean, Integer, DateTime
from sqlalchemy import Column

class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete =Column(Boolean, default=False)
    created = Column(Integer)
    deadline = Column(Integer)
    left_time = Column(Integer, default=0)
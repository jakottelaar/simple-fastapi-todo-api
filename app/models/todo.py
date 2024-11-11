import uuid
from sqlalchemy import Column, UUID, String, Boolean
from ..core.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)
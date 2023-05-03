from database.database import Base


from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class User_Model(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    nickname = Column(String, unique=True)

    task_union = relationship('Task_Model',  back_populates="user_union")

class Task_Model(Base):
    
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    task_title = Column(String)
    task_content = Column(String)
    task_datetime = Column(DateTime)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_union = relationship("User_Model",  back_populates="task_union")
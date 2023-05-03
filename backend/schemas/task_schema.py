# Python imports
from datetime import date


# Pydantic imports
from pydantic import BaseModel, Field



class Task_Schemas(BaseModel):
    task_title: str = Field(min_length=5, max_length=25)
    task_content: str = Field(min_length=5, max_length=3000)
    task_datetime: date
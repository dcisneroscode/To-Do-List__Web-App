# My imports
from models.models import Task_Model, User_Model
from schemas.task_schema import Task_Schemas


# Python imports
import json


# FastAPI imports
from fastapi import HTTPException
from fastapi.responses import JSONResponse



class Task_Services():
    
    def __init__(self, db):
        self.db = db


    def create_tasks(self, id: int, task_schema: Task_Schemas):
        user_data = self.db.query(User_Model).filter(User_Model.id == id).first()   
        new_task = Task_Model(**task_schema.dict())
        if user_data:
            new_task.user_id = user_data.id
            self.db.add(new_task)
            self.db.commit()
        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")
        return
    

    def get_all_tasks(self, id: int):
        task_data = self.db.query(Task_Model).filter(Task_Model.user_id == id).all()
        return task_data
            


    def delete_tasks(self, id: int):
        data = self.db.query(Task_Model).filter(Task_Model.id == id).first()
        if not data:
            raise HTTPException(status_code=404, detail="Task not found")
        self.db.delete(data)
        self.db.commit()
        return
    

    

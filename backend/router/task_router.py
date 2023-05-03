from database.database import Session
from schemas.task_schema import Task_Schemas
from services.task_services import Task_Services
from services.user_services import User_Services
from models.models import User_Model, Task_Model



from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router_task_path = APIRouter()


@router_task_path.post(
    path="/{id}/tasks",
    tags=["Task"],
    status_code=201,
    response_model= dict
)
def create_task(id: int, task_schema: Task_Schemas) -> dict:
    db = Session()
    Task_Services(db).create_tasks(id, task_schema)
    return JSONResponse(status_code=201, content=jsonable_encoder({"message" : "created sucessfully"}))


@router_task_path.get(
        path="/{id}/tasks",
        tags=["Task"],
        status_code=200,
        response_model = dict
)
def get_tasks(id: int):
    db = Session()
    user_data = db.query(User_Model).filter(User_Model.id == id).first()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    data = Task_Services(db).get_all_tasks(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(data))



@router_task_path.delete(
        path="/{id}/tasks",
        tags=["Task"],
        status_code=200,
        response_model = dict
)
def delete_task(id: int):
    db = Session()
    Task_Services(db).delete_tasks(id)
    return JSONResponse(status_code=200, content=jsonable_encoder({"message" : "delete sucessfully"}))

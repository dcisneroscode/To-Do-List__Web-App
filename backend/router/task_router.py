# My imports
from database.database import db
from schemas.task_schema import Task_Schemas
from services.task_services import Task_Services
from models.models import User_Model
from tokens.jwt import JWTBearer


# FastiAPI imports
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router_task_path = APIRouter()


@router_task_path.post(
    path="/tasks/{id}",
    tags=["Task"],
    status_code=201,
    response_model= dict,
    dependencies=[Depends(JWTBearer())]
)
def create_task(id: int, task_schema: Task_Schemas) -> dict:
    """
    create tasks 

    path to create task linked to the user id

    required ->

        title, content and date
 
    returns a json with success or error message
    
    """
    Task_Services(db).create_tasks(id, task_schema)
    return JSONResponse(status_code=201, content=jsonable_encoder({"message" : "created sucessfully"}))




@router_task_path.get(
        path="/tasks/{id}",
        tags=["Task"],
        status_code=200,
        response_model = dict,
        dependencies=[Depends(JWTBearer())]
)
def get_tasks(id: int):
    """
    get tasks 

    path to get all task linked to the user id

    required ->

        user id
 
    returns a json with success or error message
    
    """
    user_data = db.query(User_Model).filter(User_Model.id == id).first()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    data = Task_Services(db).get_all_tasks(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(data))



@router_task_path.delete(
        path="/tasks/{id}",
        tags=["Task"],
        status_code=200,
        response_model = dict,
        dependencies=[Depends(JWTBearer())]
)
def delete_task(id: int):

    """
    delete tasks 

    path to delete a task linked to the user id

    required ->

        user id
 
    returns a json with success or error message
    
    """
    Task_Services(db).delete_tasks(id)
    return JSONResponse(status_code=200, content=jsonable_encoder({"message" : "delete sucessfully"}))

from database.database import Session
from schemas.user_schema import User_Schemas
from services.user_services import User_Services



from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router_user_path = APIRouter()


@router_user_path.post(
    path="/user",
    tags=["User"],
    status_code=201,
    response_model= dict
)
def create_user(user_schema: User_Schemas) -> dict:
    db = Session()
    User_Services(db).create_user(user_schema)
    return JSONResponse(status_code=201, content=jsonable_encoder({"message" : "created sucessfully"}))



@router_user_path.get(
        path="/user",
        tags=["User"],
        status_code=200,
        response_model= dict
)
def get_all_user() -> dict:
    db = Session()
    data = User_Services(db).get_all_user()
    return JSONResponse(status_code=200, content=jsonable_encoder(data))




@router_user_path.delete(
    path="/user",
    tags=["User"],
    status_code=200,
    response_model= dict
)
def delete_user(id: int):
    db = Session()
    User_Services(db).delete_user(id)
    return JSONResponse(status_code=201, content=jsonable_encoder({"message" : "delete sucessfully"}))

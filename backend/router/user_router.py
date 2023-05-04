# My imports
from database.database import db
from schemas.user_schema import User_Schemas
from services.user_services import User_Services
from tokens.jwt import JWTBearer


# FastAPI imports
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router_user_path = APIRouter()


@router_user_path.post(
    path="/user",
    tags=["User"],
    status_code=201,
    response_model= dict,
)
def create_user(user_schema: User_Schemas) -> dict:
   """

    create user

    path to create user in the database

    required ->

        first_name,
        last_name,
        email,
        nickname,
        password,
 
    returns a json with success or error message
    
   
   """
   
   try:
        User_Services(db).create_user(user_schema)
        return JSONResponse(status_code=201, content=jsonable_encoder({"message" : "created sucessfully"}))
   except Exception as error:
       return JSONResponse(status_code=417, content=jsonable_encoder({"message" : error}))



@router_user_path.get(
        path="/user",
        tags=["User"],
        status_code=200,
        response_model= dict,
        dependencies=[Depends(JWTBearer())]
)
def get_all_user() -> dict:

    """
    get user

    path to get all the users in the database

    
    returns a json with success or error message
    
    """
    data = User_Services(db).get_all_user()
    return JSONResponse(status_code=200, content=jsonable_encoder(data))




@router_user_path.put(
        path="/user/{id}",
        tags=["User"],
        status_code=200,
        response_model= dict,
        dependencies=[Depends(JWTBearer())]

)
def update_user(id: int, user: User_Schemas):
    """
    update a user

    path to udpdate a user in the database

    required ->

        id user
    
    returns a json with success or error message
    
    """
    get_user = User_Services(db).update_user(id, user)
    return JSONResponse(status_code=200, content={"message" : "data updated"})




@router_user_path.delete(
    path="/user/{id}",
    tags=["User"],
    status_code=200,
    response_model= dict,
    dependencies=[Depends(JWTBearer())]
)
def delete_user(id: int):
    """
    delete a user

    path to delete a user in the database

    required ->

        id user
    
    returns a json with success or error message
    
    """
    User_Services(db).delete_user(id)
    return JSONResponse(status_code=200, content=jsonable_encoder({"message" : "delete sucessfully"}))

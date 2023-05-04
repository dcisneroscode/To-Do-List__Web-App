# My imports
from database.database import db
from services.login_services import Login_Services
from schemas.user_schema import Login_Schemas
from tokens.jwt import create_toke_jwt


# FastAPI imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse


router_login_path = APIRouter()


@router_login_path.post(
    path="/auth",
    tags=["Auth"],
    status_code=200,
    response_model = dict
)
def login_access(login: Login_Schemas) -> dict:
    """
    Log in path
    
    route to authenticate

    this route performs the authentication of the user and password of the database to access the rest of the routes.

    requires -> 
    
        user and password

    returns a token
    
    """
    data =  Login_Services(db).log_user(login)
    if data:
        token: str = create_toke_jwt(login.dict())
        return JSONResponse(status_code=200, content=token)

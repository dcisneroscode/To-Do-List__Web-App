# My imports
from database.database import db
from services.login_services import Login_Services
from schemas.user_schema import Login_Schemas
from models.models import User_Model


# JSON WEB TOKEN imports
from jwt import encode, decode, PyJWKError


# FastAPI imports
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer


def create_toke_jwt(data: dict) -> str:
    token: str = encode(payload=data, key="my_secret_key_for_the_app", algorithm="HS256")
    return token


def validate_token_jwt(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key_for_the_app", algorithms=["HS256"])
    return data

# data =  Login_Services(db).log_user(login)
#     if data:
#         token: str = create_toke_jwt(login.dict())
#         return JSONResponse(status_code=200, content=token)

class JWTBearer(HTTPBearer):


    def JWT_Auth():
        try:
            auth = validate_token_jwt()
        except PyJWKError:
            raise HTTPException(status_code=403, detail="Credentials invalid")
        

  
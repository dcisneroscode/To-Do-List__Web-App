# My imports
from models.models import User_Model
from schemas.user_schema import Login_Schemas
from tokens.hash_token import hash_token


# FastAPI imports
from fastapi import HTTPException
from fastapi.responses import JSONResponse


class Login_Services():

    def __init__(self, db):
        self.db = db

    
    def log_user(self, login: Login_Schemas):
        get_nickname = self.db.query(User_Model).filter_by(nickname = login.nickname).first()
        if not get_nickname:
            raise HTTPException(status_code=404, detail={"message": "Invalid username or password"})
        password_encode = hash_token(login.password)
        get_password = self.db.query(User_Model).filter(User_Model.password == password_encode).first()
        if not get_password:
            raise HTTPException(status_code=404, detail={"message": "Invalid username or password"})
        return JSONResponse(status_code=200, content={"message" : "Login succesfull"})


        
# My imports
from models.models import User_Model
from schemas.user_schema import User_Schemas


# Python imports
import hashlib
import secrets


# FastAPI imports
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


class User_Services():

    def __init__(self, db):
        self.db = db

    
    def create_user(self, user_schemas: User_Schemas):
        new_user = User_Model(**user_schemas.dict())
        password_hash = new_user.password.encode("utf-8")
        salt = secrets.token_hex(16).encode('utf-8')
        hash_encrypting = hashlib.sha256(password_hash + salt).hexdigest()
        new_user.password = hash_encrypting
        self.db.add(new_user)
        self.db.commit()
        return
    

    def get_nickname(self,nickname: str):
        get_nickname = self.db.query(User_Model).filter(User_Model.nickname == nickname).first()
        return get_nickname

    def get_all_user(self):
        get_a_user = self.db.query(User_Model).all()
        if not get_a_user:
            raise HTTPException(status_code=404, detail="User not found")
        return get_a_user
    

    def update_user(self, id: int, user: User_Schemas):
        get_a_user = self.db.query(User_Model).filter(User_Model.id == id).first()
        if not get_a_user:
            raise HTTPException(status_code=404, detail="User not found")
        get_a_user.first_name = user.first_name
        get_a_user.last_name = user.last_name
        get_a_user.password = user.password
        get_a_user.email = user.email
        get_a_user.nickname = user.nickname
        self.db.commit()
        return
    

    def delete_user(self, id: int):
        get_a_user = self.db.query(User_Model).filter(User_Model.id == id).first()
        if not get_a_user:
            raise HTTPException(status_code=404, detail="User not found")
        self.db.delete(get_a_user)
        self.db.commit()
        return








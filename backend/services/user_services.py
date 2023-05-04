# My imports
from models.models import User_Model
from schemas.user_schema import User_Schemas
from tokens.hash_token import hash_token


# FastAPI imports
from fastapi import HTTPException



class User_Services():

    def __init__(self, db):
        self.db = db

    
    def create_user(self, user_schemas: User_Schemas):
        new_user = User_Model(**user_schemas.dict())
        new_user.password = hash_token(new_user.password)
        self.db.add(new_user)
        self.db.commit()
        return
    

    def get_all_user(self):
        get_a_user = self.db.query(User_Model).all()
        if not get_a_user:
            raise HTTPException(status_code=404, detail="User not found")
        return get_a_user
    

    def update_user(self, id: int, user: User_Schemas):
        get_a_user = self.db.query(User_Model).filter(User_Model.id == id).first()
        if not get_a_user:
            raise HTTPException(status_code=422, detail="Can't update")
        get_a_user.first_name = user.first_name
        get_a_user.last_name = user.last_name
        get_a_user.password = hash_token(user.password)
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








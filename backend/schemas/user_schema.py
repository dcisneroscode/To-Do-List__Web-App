# Pydantic imports
from pydantic import BaseModel, Field



class Login_Schemas(BaseModel):
    password: str
    nickname: str = Field(min_length=5, max_length=20, default="")
    

class User_Schemas(Login_Schemas):
    first_name: str = Field(min_length=5, max_length=15, default="")
    last_name: str = Field(min_length=5, max_length=15, default="")
    email: str = Field(min_length=10, max_length=25, default="")


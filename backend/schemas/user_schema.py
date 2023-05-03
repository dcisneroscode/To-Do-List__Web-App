# Pydantic imports
from pydantic import BaseModel, Field



class User_Schemas(BaseModel):
    first_name: str = Field(min_length=5, max_length=15, default="")
    last_name: str = Field(min_length=5, max_length=15, default="")
    password: str
    email: str = Field(min_length=10, max_length=25, default="")
    nickname: str = Field(min_length=5, max_length=20, default="")


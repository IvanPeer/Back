from pydantic import BaseModel


class UserBase(BaseModel):
    user_name: str
    user_password : str
    user_state: int
    user_rol : str
    user_email : str


class UserCreate(BaseModel):
    user_name: str
    user_password : str
    user_rol : str
    user_email : str


class UserUpdate(BaseModel):
    user_name: str
    user_password : str
    user_rol : str
    user_email : str


class User(UserBase):
    User_id: int

    class Config:
        orm_mode = True
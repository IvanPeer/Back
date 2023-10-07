from pydantic import BaseModel


class ClientBase(BaseModel):
    client_name: str
    client_last_name: str
    client_state: int


class ClientCreate(BaseModel):
    client_name: str
    client_last_name: str


class ClientUpdate(BaseModel):
    client_name: str
    client_last_name: str


class Client(ClientBase):
    client_id: int

    class Config:
        orm_mode = True
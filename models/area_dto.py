from pydantic import BaseModel


class AreaBase(BaseModel):
    area_name: str
    area_description: str
    area_state: int


class AreaCreate(BaseModel):
    area_name: str
    area_description: str


class AreaUpdate(BaseModel):
    area_name: str
    area_description: str


class Area(AreaBase):
    area_id: int

    class Config:
        orm_mode = True


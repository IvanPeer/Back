from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from database.database import SessionLocal

from services import area_service
from models import area_dto

router = APIRouter(
    prefix="/area",
    tags=["Area"],
    responses={404: {"description": "Not found"}},
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def read_areas(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    areas = area_service.get_areas(db, skip=skip, limit=limit)
    return areas


@router.get("/{area_id}")
def get_area_by_id(area_id: int, db: Session = Depends(get_db),):
    db_area = area_service.get_area(db, area_id)
    if db_area is None:
        raise HTTPException(status_code=404, detail="Area not found")
    return db_area


@router.post("/")
def create_area(area: area_dto.AreaCreate, db: Session = Depends(get_db)):

    result = area_service.create_area(db=db, area_create=area)

    if not result:
        return {"result": "Area already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{area_id}")
def update_area(area_id: int, area: area_dto.AreaUpdate, db: Session = Depends(get_db)):

    db_area = area_service.update_area(db, area_id, area)

    if db_area is None:
        raise HTTPException(status_code=404, detail="Area not found")

    return db_area


@router.post("/delete/{area_id}")
def delete_area(area_id: int, db: Session = Depends(get_db)):

    try:

        result = area_service.delete_area(db, area_id)

        if not result:
            return {"result": "error", "message": "El area se encuentra asociada a un puesto"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error al eliminar area"}

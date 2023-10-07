from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from database.database import SessionLocal

from services import user_service
from models import user_dto

router = APIRouter(
    prefix="/user",
    tags=["User"],
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
def read_users(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    users = user_service.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db),):
    db_user = user_service.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/")
def create_user(user: user_dto.UserCreate, db: Session = Depends(get_db)):

    result = user_service.create_user(db=db, user_create=user)

    if not result:
        return {"result": "User already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{user_id}")
def update_user(user_id: int, user: user_dto.UserUpdate, db: Session = Depends(get_db)):

    db_user = user_service.update_user(db, user_id, user)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@router.post("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    try:

        result = user_service.delete_user(db, user_id)

        if not result:
            return {"result": "error", "message": "El Usuario se encuentra asociada"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error al eliminar usuario"}

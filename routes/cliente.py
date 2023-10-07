from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from database.database import SessionLocal

from services import client_service
from models import client_dto

router = APIRouter(
    prefix="/client",
    tags=["Client"],
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
def read_clients(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    clients = client_service.get_clients(db, skip=skip, limit=limit)
    return clients


@router.get("/{client_id}")
def get_client_by_id(client_id: int, db: Session = Depends(get_db),):
    db_client = client_service.get_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@router.post("/")
def create_client(client: client_dto.ClientCreate, db: Session = Depends(get_db)):

    result = client_service.create_client(db=db, client_create=client)

    if not result:
        return {"result": "Client already exist"}
    else:
        return {"result": "success"}


@router.post("/update/{client_id}")
def update_client(client_id: int, client: client_dto.ClientUpdate, db: Session = Depends(get_db)):

    db_client = client_service.update_client(db, client_id, client)

    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")

    return db_client


@router.post("/delete/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):

    try:

        result = client_service.delete_client(db, client_id)

        if not result:
            return {"result": "error", "message": "El cliente se encuentra asociada"}
        else:
            return {"result": "success"}

    except Exception as e:
        print(e)
        return {"result": "error", "detail": "Error al eliminar cliente"}

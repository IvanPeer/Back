from sqlalchemy.orm import Session

import models.client_model as client_model
import models.client_dto as client_dto


def get_clients(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(client_model.Client).filter(client_model.Client.client_state == 1).offset(skip).limit(limit).all()


def get_client(db, client_id):
    return db.query(client_model.Client).filter(client_model.Client.key == client_id,
                                            client_model.Client.client_state == 1).first()


def create_client(db: Session, client_create: client_dto.ClientCreate):
    exist_client = db.query(client_model.Client).filter(client_model.Client.client_name == client_create.client_name,
                                                  client_model.Client.client_state == 1).first()

    if exist_client is not None:
        return False

    db_client = client_model.Client(client_name=client_create.client_name, client_last_name=client_create.client_last_name,
                              client_state=1)

    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client


def update_client(db: Session, client_id: int, client_update: client_dto.ClientUpdate):
    db_client = db.get(client_model.Client, client_id)

    if not db_client:
        return db_client

    client_data = client_update.dict(exclude_unset=True)

    for key, value in client_data.items():
        setattr(db_client, key, value)

    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client


def delete_client(db, client_id):

    db_client = db.get(client_model.Client, client_id)

    setattr(db_client, 'client_state', 0)

    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client

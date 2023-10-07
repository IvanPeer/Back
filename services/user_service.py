from sqlalchemy.orm import Session

import models.user_model as user_model
import models.user_dto as user_dto



def get_users(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(user_model.User).filter(user_model.User.user_state == 1).offset(skip).limit(limit).all()


def get_user(db, user_id):
    return db.query(user_model.User).filter(user_model.User.key == user_id,
                                            user_model.User.user_state == 1).first()


def create_user(db: Session, user_create: user_dto.UserCreate):
    exist_user = db.query(user_model.USer).filter(user_model.User.user_name == user_create.user_name,
                                                  user_model.User.user_state == 1).first()

    if exist_user is not None:
        return False

    db_user = user_model.User(user_name=user_create.user_name, user_rol=user_create.user_rol, user_email=user_create.user_email,
                              user_password=user_create.user_password, user_state=1)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, user_id: int, user_update: user_dto.UserUpdate):
    db_user = db.get(user_model.User, user_id)

    if not db_user:
        return db_user

    user_data = user_update.dict(exclude_unset=True)

    for key, value in user_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db, user_id):

    db_user = db.get(user_model.User, user_id)

    setattr(db_user, 'user_state', 0)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

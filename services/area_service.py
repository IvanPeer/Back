from sqlalchemy.orm import Session

import models.area_model as area_model
import models.area_dto as area_dto


def get_areas(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(area_model.Area).filter(area_model.Area.area_status == 1).offset(skip).limit(limit).all()


def get_area(db, area_id):
    return db.query(area_model.Area).filter(area_model.Area.key == area_id,
                                            area_model.Area.area_status == 1).first()


def create_area(db: Session, area_create: area_dto.AreaCreate):
    exist_area = db.query(area_model.Area).filter(area_model.Area.area_name == area_create.area_name,
                                                  area_model.Area.area_status == 1).first()

    if exist_area is not None:
        return False

    db_area = area_model.Area(area_name=area_create.area_name, area_description=area_create.area_description,
                              area_status=1)

    db.add(db_area)
    db.commit()
    db.refresh(db_area)

    return db_area


def update_area(db: Session, area_id: int, area_update: area_dto.AreaUpdate):
    db_area = db.get(area_model.Area, area_id)

    if not db_area:
        return db_area

    area_data = area_update.dict(exclude_unset=True)

    for key, value in area_data.items():
        setattr(db_area, key, value)

    db.add(db_area)
    db.commit()
    db.refresh(db_area)

    return db_area


def delete_area(db, area_id):
    db_job = db.query(job_model.Job).filter(job_model.Job.area == area_id, job_model.Job.job_status == 1).first()

    if db_job:
        return None

    db_area = db.get(area_model.Area, area_id)

    setattr(db_area, 'area_status', 0)

    db.add(db_area)
    db.commit()
    db.refresh(db_area)

    return db_area

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


class Area(Base):
    __tablename__ = "NOM_AREA"

    key = Column("ARE_IdArea", Integer, primary_key=True, index=True)
    area_name = Column("ARE_Nombre", String)
    area_description = Column("ARE_Descripcion", String)
    area_status = Column("ARE_Estado", Integer)

    job_info = relationship("Job", back_populates="area_info")




from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


class User(Base):
    __tablename__ = "usuario"

    key = Column("id_usuario", Integer, primary_key=True, index=True)
    user_name = Column("nombre", String)
    user_password = Column("contraseña", String)
    user_state = Column("estado", Integer)
    user_rol = Column("rol", String)
    user_email = Column("correo", String)

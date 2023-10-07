from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


class Client(Base):
    __tablename__ = "cliente"

    key = Column("id_cliente", Integer, primary_key=True, index=True)
    client_name = Column("nombre", String)
    client_last_name = Column("apellido", String)
    client_state = Column("estado", Integer)

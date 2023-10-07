from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import get_settings

settings = get_settings()

DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port


engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@localhost/Aseguramiento")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

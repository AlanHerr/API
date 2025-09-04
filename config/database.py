import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from model.products_models import Base
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

# Cargar variables de entorno desde .env
load_dotenv()

DATABASE_URI = os.getenv('MYSQL_URI')  # Usas esta variable en tu .env
SQLITE_URI = 'sqlite:///products_local.db'  # Nombre ajustado para productos

def get_engine():
    """
    Intenta crear una conexión con la base de datos remota. Si falla, usa SQLite local.
    """
    if DATABASE_URI:
        try:
            engine = create_engine(DATABASE_URI, echo=True)
            # Probar conexión
            conn = engine.connect()
            conn.close()
            logging.info('Conexión a la base de datos remota exitosa.')
            return engine
        except OperationalError:
            logging.warning('No se pudo conectar a la base de datos remota. Usando SQLite local.')
    # Fallback a SQLite
    engine = create_engine(SQLITE_URI, echo=True)
    return engine

engine = get_engine()
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def get_db_session():
    """
    Retorna una nueva sesión de base de datos para ser utilizada en los servicios o controladores.
    """
    return Session()

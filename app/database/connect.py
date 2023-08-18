from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings

SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_size=15)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()


# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

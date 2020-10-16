from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from env import settings

database_link = (settings.DB_CONNECTION
                 + "+pymysql://"
                 + settings.DB_USERNAME+":"+settings.DB_PASSWORD
                 + "@"+settings.DB_HOST+"/"+settings.DB_DATABASE)

SQLALCHEMY_DATABASE_URL = database_link

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    # Used Only for SqlLite
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"

# connect_args={'check_same_thread': False}: This argument is specific to SQLite. 
# By default, SQLite connections are not shared between threads. 
# Setting check_same_thread to False allows the same connection to be used across different threads, 
# which can be necessary for multi-threaded applications.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# autocommit=False: To take complete control under our hands, we set autocommit to False.
# autoflush=False: To take complete control under our hands, we set autocommit to False.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: This is the base class for our models.
Base = declarative_base()
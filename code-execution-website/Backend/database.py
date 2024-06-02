from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sqlite URL to database
URL_DATABASE = 'sqlite:///./codesubmission.db'

# creates SQLalchemy engine
engine = create_engine(URL_DATABASE, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# creates base class for ORM class definitions
Base = declarative_base()

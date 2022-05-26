from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///"+os.path.join(BASE_DIR, 'books.db')
Base = declarative_base()

engine = create_engine(connection_string, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
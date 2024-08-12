from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv


ENGINE = create_engine(os.getenv("DATABASE_URL"), connect_args={'check_same_thread': False})
SESSION = sessionmaker(bind=ENGINE)
session = SESSION()
BASE = declarative_base()

def create_db():
    BASE.metadata.create_all(ENGINE)

def drop_db():
    BASE.metadata.dpop_all(ENGINE)
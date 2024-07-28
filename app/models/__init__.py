from .base import BASE, create_db
from sqlalchemy import Column, String, Integer, Text, Boolean
from sqlalchemy.orm import relationship

class User(BASE):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name= Column(String, nullable=False, unique=True)
    email=Column(String(100), nullable=False, unique=True)
    phone=Column(String(30), nullable=False, unique=True)
    password = Column(String(100), nullable=False, unique=True)
    phone = Column(Boolean(100), nullable=False, unique=True)
    admin = Column(Boolean(100), default=False, unique=True)
    email_configured = Column(Boolean(100), default=False, unique=True)
    cart = Column()
    order = relationship("Order", buckref='customer')
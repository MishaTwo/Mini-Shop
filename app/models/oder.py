from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Text, Boolean, ForeignKey
from . import BASE

class Cart(BASE):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    uld = Column(Integer, ForeignKey("users.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
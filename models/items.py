from .base import BASE
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text

class Item(BASE):
    __tablename__ = 'items'

    id  = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(Text, nullable=False)
    image = Column(String, nullable=False)
    details = Column(String, nullable=False)
    price_id = Column(String, nullable=False)
    in_card = relationship("Cart", backref='item')
    orders = relationship("Order_items", backref='item')
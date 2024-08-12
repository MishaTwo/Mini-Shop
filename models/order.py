from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Text, Boolean, ForeignKey, DateTime
from .base import BASE

class Order(BASE):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    vid = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(DateTime, ForeignKey("items.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    items = relationship("Ordered_Item", backref='order')

class Ordered_Item(BASE):
    __tablename__='order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id', nullable=False))
    item_id = Column(Integer, ForeignKey("carts.quantitly"), nullable=False)

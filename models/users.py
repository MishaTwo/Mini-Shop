from .base import BASE, create_db
from sqlalchemy import Column, String, Integer, Text, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from .cart import Cart
from .base import session

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
    cart = relationship("Cart", backref='buyer')
    order = relationship("Order", backref='customer')

    def add_to_card(self,  item_id, quantitly):
        item_to_add = session.query(Cart).filter_by(item_id=item_id, quantitly=quantitly, uid=self.id).first()
        try:
            session.add(item_to_add)
            session.commit()
        except Exception as exc:
            return exc
        finally:
            session.close()

    def remove_from_card(self,  item_id, quantitly):
        item_to_delete = session.query(Cart).filter_by(item_id=item_id, quantitly=quantitly, uid=self.id).first()
        try:
            session.delete(item_to_delete)
            session.commit()
        except Exception as exc:
            return exc
        finally:
            session.close()
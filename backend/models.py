from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from db import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False, index=True)
    author = Column(String(30), nullable=False, index=True)
    release_date = Column(Date(), index=True)

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.author,
            "release_date": self.release_date,
        }

    def __repr__(self):
        return 'BookModel(name=%s, author=%s,release_date=%s)' % (self.name, self.author, self.release_date)


class Shop(Base):
    __tablename__ = "shop"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False, index=True)
    address = Column(String(30), nullable=False, index=True)

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
        }

    def __repr__(self):
        return 'ShopModel(name=%s, address=%s)' % (self.name, self.address)


class OrderItem(Base):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    shop_id = Column(Integer, ForeignKey("shop.id"))
    book_quantity = Column(Integer)

    shop = relationship("Shop")
    order = relationship("Order")
    book = relationship("Book")

    def dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "book_id": self.book_id,
            "shop_id": self.shop_id,
            "book_quantity": self.book_quantity,
        }

    def __repr__(self):
        return 'OrderItemModel(id=%s, order_id=%s, book_id=%s, shop_id=%s, book_quantity=%s\
        )' % (self.id, self.order_id, self.book_id, self.shop_id, self.book_quantity)


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    reg_date = Column(Date(), index=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User")

    def dict(self):
        return {
            "id": self.id,
            "reg_date": self.reg_date,
            "user_id": self.user_id,
        }

    def __repr__(self):
        return 'Order_model(reg_date=%s, user_id=%s)' % (self.reg_date, self.user_id)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, )
    last_name = Column(String(40), nullable=False, index=True)
    first_name = Column(String(40), nullable=False, index=True)
    email = Column(String(80), nullable=False, index=True)

    def dict(self):
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "email": self.email,
        }

    def __repr__(self):
        return 'Order_model(last_name=%s, first_name=%s, email=%s)' % (self.last_name, self.first_name, self.email)

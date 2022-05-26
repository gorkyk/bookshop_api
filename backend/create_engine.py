from db import Base, engine
from models import Book, User, Shop, Order, OrderItem

Base.metadata.create_all(engine)

from db import SessionLocal
from models import User, Shop, Order, Book, OrderItem
from datetime import datetime


def add_users():
    """Adding test objects to user table
    """
    users = [
        {"id": 10, "last_name": "Doe", "first_name": "John", "email": "johndoe@smth.com"},
        {"id": 11, "last_name": "Lutz", "first_name": "Mark", "email": "god@smth.com"},
        {"id": 12, "last_name": "Gates", "first_name": "Bill", "email": "vaccine_king@smth.com"},
        {"id": 13, "last_name": "Korolyov", "first_name": "Sergey", "email": "rocketman@smth.com"},
        {"id": 14, "last_name": "Nemtsow", "first_name": "Boris", "email": "nemtsownn@smth.com"},
    ]
    with SessionLocal.begin() as session:
        session.add_all([User(id=user["id"],
                              last_name=user["last_name"],
                              first_name=user["first_name"],
                              email=user["email"]) for user in users])


def add_orders():
    """Adding test objects to order table
    """
    orders = [
        {"id": 100, "reg_date": datetime(2022,5,10), "user_id": 10},
        {"id": 101, "reg_date": datetime(2022,5,11), "user_id": 10},
        {"id": 102, "reg_date": datetime(2022,5,12), "user_id": 11},
        {"id": 103, "reg_date": datetime(2022,5,13), "user_id": 11},
        {"id": 104, "reg_date": datetime(2022,5,14), "user_id": 11},
    ]
    with SessionLocal.begin() as session:
        session.add_all([Order(id=order["id"],
                              reg_date=order["reg_date"],
                              user_id=order["user_id"]) for order in orders])


def add_books():
    """Adding test objects to book table
    """
    books = [
        {"id": 10, "name": "AAA", "author": "A.B.", "release_date": datetime(1990,5,10)},
        {"id": 11, "name": "BBB", "author": "A.B.", "release_date": datetime(1991,5,10)},
        {"id": 12, "name": "CCC", "author": "A.C.", "release_date": datetime(1992,5,10)},
        {"id": 13, "name": "DDD", "author": "A.C.", "release_date": datetime(1993,5,10)},
        {"id": 14, "name": "EEE", "author": "A.C.", "release_date": datetime(1994,5,10)},
        {"id": 15, "name": "FFF", "author": "A.C.", "release_date": datetime(1995,5,10)},
        {"id": 16, "name": "GGG", "author": "A.C.", "release_date": datetime(1996,5,10)},
        {"id": 17, "name": "HHH", "author": "A.C.", "release_date": datetime(1997,5,10)},
    ]
    with SessionLocal.begin() as session:
        session.add_all([Book(id=book["id"],
                              name=book["name"],
                              author=book["author"],
                              release_date=book["release_date"]) for book in books])


def add_shops():
    """Adding test objects to shop table
    """
    shops = [
        {"id": 10, "name": "Bookshop1", "address": "1.2.3"},
        {"id": 11, "name": "Bookshop2", "address": "1.2.4"},
        {"id": 12, "name": "Bookshop3", "address": "1.2.5"},
        {"id": 13, "name": "Bookshop4", "address": "1.2.6"},
        {"id": 14, "name": "Bookshop5", "address": "1.2.7"},
        {"id": 15, "name": "Bookshop6", "address": "1.2.8"},
        {"id": 16, "name": "Bookshop7", "address": "1.2.9"},
        {"id": 17, "name": "Bookshop8", "address": "1.2.10"},
    ]
    with SessionLocal.begin() as session:
        session.add_all([Shop(id=shop["id"],
                              name=shop["name"],
                              address=shop["address"]) for shop in shops])


def add_order_items():
    """Adding test objects to order_item table
    """
    order_items = [
        {"id": 100, "order_id": 100, "book_id": 10, "shop_id": 10, "book_quantity": 1},
        {"id": 101, "order_id": 100, "book_id": 11, "shop_id": 10, "book_quantity": 2},
        {"id": 102, "order_id": 100, "book_id": 12, "shop_id": 10, "book_quantity": 3},
        {"id": 103, "order_id": 101, "book_id": 10, "shop_id": 11, "book_quantity": 2},
        {"id": 104, "order_id": 101, "book_id": 11, "shop_id": 11, "book_quantity": 3},
        {"id": 105, "order_id": 102, "book_id": 15, "shop_id": 12, "book_quantity": 1},
        {"id": 106, "order_id": 103, "book_id": 16, "shop_id": 13, "book_quantity": 4},
        {"id": 107, "order_id": 104, "book_id": 17, "shop_id": 14, "book_quantity": 5},
        {"id": 108, "order_id": 104, "book_id": 12, "shop_id": 14, "book_quantity": 2},
        {"id": 109, "order_id": 104, "book_id": 11, "shop_id": 14, "book_quantity": 1},
    ]
    with SessionLocal.begin() as session:
        session.add_all([OrderItem(id=order_item["id"],
                                   order_id=order_item["order_id"],
                                   book_id=order_item["book_id"],
                                   shop_id=order_item["shop_id"],
                                   book_quantity=order_item["book_quantity"]) for order_item in order_items])


if __name__ == "__main__":
    add_users()
    add_orders()
    add_books()
    add_shops()
    add_order_items()
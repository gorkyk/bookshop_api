from fastapi import FastAPI
from models import User, Order, OrderItem
from db import SessionLocal
from schema import AddOrderRequest
import datetime
from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc
import logging

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
async def root() -> dict:
    """Test request with "Hello World"
       status code 200 is expected
       """
    logger.info("Logging from the root request")
    return {"message": "Hello World"}


@app.get("/get_user_info/")
def get_user_info(user_id: int) -> dict:
    """Get info about user:
        {id:
        last_name:
        first_name:
        email:
        }
    """
    with SessionLocal.begin() as session:
        query = jsonable_encoder(session.get(User, {"id": user_id}))
    logger.info(f"Request get_user_info/{user_id}")
    return query


@app.post("/add_order/")
def add_order(request: AddOrderRequest):
    """Add order object:
                {"id": 0,
                "user_id": 0,
                "books": [{"id": 0,
                        "quantity": 0
                        }
                        ]
                }
    """
    with SessionLocal.begin() as session:
        session.add_all([Order(id=request.id, user_id=request.user_id, reg_date=datetime.datetime.now())])
        session.add_all([OrderItem(order_id=request.id,
                                   book_id=book.id,
                                   shop_id=0,
                                   book_quantity=book.quantity)
                         for book in request.books])
    logger.info(f"Request add_order")
    return


@app.get("/get_order/")
def get_order_info(order_id: int) -> dict:
    """Get info about order:
            {id:
            reg_date:
            user_id:
            }
    """
    with SessionLocal.begin() as session:
        query = jsonable_encoder(session.query(Order,OrderItem).filter(Order.id == order_id).filter(OrderItem.order_id == order_id).all())
    logger.info("Request get_order")
    return query


@app.get("/get_order_history/")
def get_order_history(user_id: int) -> dict:
    """Get orders related to user by user.id
    """
    with SessionLocal.begin() as session:
        query = jsonable_encoder(session.query(Order).filter(Order.user_id == user_id).order_by(desc(Order.reg_date)).all())
    logger.info("Request get_order_history")
    return query

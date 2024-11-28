from sqlalchemy.orm import Session
from schemas.schemas import BuyCreate, BuyUpdate
from models.buy import BuyModel


def get_all_buys(db: Session):
    return db.query(BuyModel).all()

def get_one_buy(db: Session, buy_id: int):
    return db.query(BuyModel).filter(BuyModel.id == buy_id).first()

def get_last_buy(db:Session):
    return db.query(BuyModel).order_by(BuyModel.id.desc()).first()
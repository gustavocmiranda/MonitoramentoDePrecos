from sqlalchemy.orm import Session
from schemas.schemas import BuyCreate, BuyUpdate
from models.buy import BuyModel


def get_all_buys(db: Session):
    return db.query(BuyModel).all()

def get_one_buy(db: Session, buy_id: int):
    return db.query(BuyModel).filter(BuyModel.id == buy_id).first()

def get_last_buy(db:Session):
    return db.query(BuyModel).order_by(BuyModel.id.desc()).first()

def create_buy(db: Session, buy: BuyCreate):
    db_buy = BuyModel(**buy.model_dump())
    db.add(db_buy)

    db.commit()

    # db.refresh(db_buy)

    return db_buy

def delete_buy(db: Session, buy_id: int):
    db_buy = db.query(BuyModel).filter(BuyModel.id == buy_id).first()
    db.delete(db_buy)

    db.commit()
    return db_buy

def update_buy(db: Session, buy_id: int, buy: BuyUpdate):
    db_buy = db.query(BuyModel).filter(BuyModel.id == buy_id).first()

    if buy is None:
        return None
    
    if buy.produto is not None:
        db_buy.produto = buy.produto

    if buy.preco is not None:
        db_buy.preco = buy.preco

    if buy.local_de_compra is not None:
        db_buy.local_de_compra = buy.local_de_compra
    
    if buy.promocao is not None:
        db_buy.promocao = buy.promocao
    
    if buy.data_de_compra is not None:
        db_buy.data_de_compra = buy.data_de_compra

    db.commit()
    db.refresh(db_buy)

    return db_buy
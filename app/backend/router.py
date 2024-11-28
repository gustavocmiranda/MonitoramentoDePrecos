from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal, get_db
from schemas.schemas import BuyCreate, BuyResponse, BuyUpdate
from typing import List
from crud import (
    create_buy,
    get_all_buys,
    get_last_buy,
    get_one_buy,
    update_buy,
    delete_buy
)

router = APIRouter()


@router.get(path='/buys/', response_model=List[BuyResponse])
def read_all_buys(db: Session = Depends(get_db)):
    buys = get_all_buys(db)
    return buys

@router.get(path='/buys/{buy_id}', response_model=BuyResponse)
def read_buy(buy_id: int, db: Session = Depends(get_db)):
    db_buy = get_one_buy(db, buy_id)

    if db_buy is None:
        raise HTTPException(status_code=404, detail='Compra não encontrada.')
    
    return db_buy

@router.get(path='/last/', response_model=BuyResponse)
def read_last_buy(db: Session = Depends(get_db)):
    db_buy = get_last_buy(db)
    return db_buy

@router.post(path='/buys/', response_model=BuyResponse)
def post_buy(buy: BuyCreate, db: Session = Depends(get_db)):
    return create_buy(db, buy)

@router.delete(path='/buys/{buy_id}', response_model=BuyResponse)
def delete_one_buy(buy_id: int, db: Session = Depends(get_db)):
    db_buy = delete_buy(db, buy_id)

    if db_buy is None:
        raise HTTPException(status_code=404, detail='Compra não encontrada.')

    return db_buy

@router.put('/buys/{buy_id}', response_model=BuyResponse)
def put_buy(buy_id: int, buy: BuyUpdate, db: Session = Depends(get_db)):
    db_buy = update_buy(db, buy_id, buy)

    if db_buy is None:
            raise HTTPException(status_code=404, detail='Compra não encontrada.')

    return db_buy
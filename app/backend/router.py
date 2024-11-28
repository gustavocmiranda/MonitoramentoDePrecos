from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal, get_db
from schemas.schemas import BuyCreate, BuyResponse, BuyUpdate
from typing import List

router = APIRouter()
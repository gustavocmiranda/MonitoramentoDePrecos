from sqlalchemy import Column, Integer, Boolean, String, Float, DateTime
from database.database import Base

class Buy(Base):
    __tablename__ = 'compras'
    id = Column(Integer, primary_key=True)
    produto = Column(String)
    preco = Column(Float)
    local_de_compra = Column(String)
    promocao = Column(Boolean)
    data_de_compra = Column(DateTime)
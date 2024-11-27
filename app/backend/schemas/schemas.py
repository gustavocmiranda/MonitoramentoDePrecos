# REPRESENTACAO DAS INTERACOES COM O USUARIO
from pydantic import BaseModel, PositiveFloat
from datetime import datetime
from typing import Optional

class BuyBase(BaseModel):
    produto: str
    preco: PositiveFloat
    local_de_compra: str
    promocao: bool
    data_de_compra: datetime

class BuyCreate(BuyBase):
    pass

class BuyResponse(BuyBase):
    id: int

class BuyUpdate(BuyBase):
    produto: Optional[str] = None
    preco: Optional[PositiveFloat] = None
    local_de_compra: Optional[str] = None
    promocao: Optional[bool] = None
    data_de_compra: Optional[datetime] = None
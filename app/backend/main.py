from fastapi import FastAPI
from database.database import engine
from router import router
import models.buy

models.buy.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router=router)
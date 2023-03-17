from http.client import HTTPException

from fastapi import Depends, FastAPI, Body
from sqlalchemy.orm import Session

from db import dbMain, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.Users)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return dbMain.create_user(db=db, user=user)


@app.get("/users/{id}", response_model=schemas.Users)
def get_user(id: int, db: Session = Depends(get_db)):
    db_user = dbMain.get_user(db, user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/trades/{user_id}")
def get_user_trades(user_id: int, db: Session = Depends(get_db)):
    trades = dbMain.get_trades(db, user_id)
    if trades is None:
        raise HTTPException(status_code=404, detail="No trades found")
    return trades


@app.get("/trades/{user_id}/{symbol}")
def get_user_trades_symbol(user_id: int, symbol: str, db: Session = Depends(get_db)):
    return dbMain.get_trades_symbol(db, user_id, symbol)


@app.post("/trades/")
def update_trades_list(user_id: int = Body(...), symbol: str = Body(...), db: Session = Depends(get_db)):
    trades = dbMain.update_trades(db, user_id, symbol)
    return trades

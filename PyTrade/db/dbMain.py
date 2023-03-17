from sqlalchemy.orm import Session
from db import models, schemas
from bybit import api


def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.Users(public_key=user.public_key, private_key=user.private_key)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_trades(db: Session, user_id: int):
    return db.query(models.Trades).filter(models.Trades.userId == user_id).all()


def get_last_trades(db: Session, user_id: int):
    return db.query(models.Trades).order_by(models.Trades.id.desc()).filter(models.Trades.userId == user_id).first()


def get_trades_symbol(db: Session, user_id: int, symbol: str):
    return db.query(models.Trades).filter(models.Trades.userId == user_id, models.Trades.symbol == symbol).all()


def update_trades(db: Session, user_id: int, symbol: str):
    trades = set_trades(db, user_id, symbol)
    print(trades)
    db.add_all(trades)
    db.commit()


def set_trades(db: Session, user_id: int, symbol: str):
    user = get_user(db, user_id)
    bybit_api = api.Bybit(user.public_key, user.private_key)
    last = get_last_trades(db, user_id)
    trades = bybit_api.get_trades(symbol)
    conv_trades = []
    print(last.createdTime)
    for trade in trades['result']['data']:
        print(trade['created_at'])
        if int(trade['created_at']) > int(last.createdTime):
            trades = models.Trades(symbol=trade["symbol"], createdTime=trade["created_at"], closedPnl=trade["closed_pnl"],
                                   userId=user_id)
            conv_trades.append(trades)
    return conv_trades

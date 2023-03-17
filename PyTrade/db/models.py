from sqlalchemy import Column, ForeignKey, Integer, String
from db.database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    public_key = Column(String)
    private_key = Column(String)


class Trades(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String)
    createdTime = Column(String)
    closedPnl = Column(String)
    userId = Column(Integer)

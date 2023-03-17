from pydantic import BaseModel


class Users(BaseModel):
    id: int
    public_key: str
    private_key: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    public_key: str
    private_key: str

    class Config:
        orm_mode = True


class Trades(BaseModel):
    id: int
    symbol: str
    createdTime: str
    closedPnl: str

    class Config:
        orm_mode = True


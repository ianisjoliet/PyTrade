from pybit.usdt_perpetual import HTTP


class Bybit:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.conn = HTTP(None, public_key, private_key)

    def get_trades(self, smb):
        trades = self.conn.closed_profit_and_loss(symbol=smb)
        return trades



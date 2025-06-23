class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return f"Player(name={self.name}, symbol={self.symbol})"

    def __repr__(self):
        return f"Player(name={self.name!r}, symbol={self.symbol!r})"

from src.types.card import BlankCard


class Player:
    def __init__(self, name):
        self.name = name
        self.points: int = 0
        self.cards: list[BlankCard] = []

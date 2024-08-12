from src.types.player import Player
from src.types.card import BlankCard, FillCard


class Game:
    def __init__(self, players: list[Player], blanks: list[BlankCard], fills: list[FillCard]):
        self.players: players
        self.blanks: blanks
        self.fills: fills
        self.curr_czar: Player = players[0]
        self.curr_blank: BlankCard | None = None

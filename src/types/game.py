import itertools

from src.types.player import Player
from src.types.card import BlankCard, FillCard


class Game:
    def __init__(self, players: list[Player], blanks: list[BlankCard], fills: list[FillCard]):
        self.players = players
        self.blanks = blanks
        self.fills = fills

        self.player_sequence = itertools.cycle(players)
        self.curr_czar = next(self.player_sequence)
        self.curr_blank = self.blanks.pop()
        self.curr_player_choices: dict[Player, list[FillCard]] = {}

    def have_winners(self) -> list[Player]:
        return [p for p in self.players if p.points >= 10]  # TODO change num

    def setup_new_round(self):
        assert len(self.blanks) >= 1 and len(self.fills) >= len(self.players) - 1  # TODO move check

        for p in self.players:
            while len(p.fills) < 5:  # TODO change num
                p.fills.append(self.fills.pop())

        self.curr_czar = next(self.player_sequence)
        self.curr_blank = self.blanks.pop()
        self.curr_player_choices.clear()

    def play(self):
        print("Blank card is:")
        print(self.curr_blank)

        self.curr_player_choices = {p: p.choose_fills() for p in self.players if p != self.curr_czar}
        player_indexes = list(self.curr_player_choices.keys())

        print(f"{self.curr_czar.name} - choose a winner from:")
        for i, choices in enumerate(self.curr_player_choices.values()):
            print(f"{i}: {self.curr_blank.fill(choices)}")

        winner = player_indexes[int(input())]
        print(f"{winner.name} wins this round")
        winner.points += 1

        for p in self.players:
            print(f"{p.name}: {p.points} point")

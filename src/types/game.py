import itertools

from src.types.player import Player
from src.types.card import BlankCard, FillCard


class Game:
    def __init__(self, players: list[Player], blanks: list[BlankCard], fills: list[FillCard]):
        self.players = players
        self.blanks = blanks
        self.fills = fills
        self.player_sequence = itertools.cycle(players)

    def have_winner(self) -> list[Player]:
        return [p for p in self.players if p.points >= 10]  # TODO change num

    def play(self):
        assert len(self.blanks) >= 1 and len(self.fills) >= len(self.players) - 1  # TODO move check

        curr_czar = next(self.player_sequence)
        curr_blank = self.blanks.pop()

        print("Blank card is:")
        print(curr_blank)

        all_choices = {p: p.choose_fills() for p in self.players if p != curr_czar}
        player_indexes = list(all_choices.keys())

        print(f"{curr_czar.name} - choose a winner from:")
        for i, choices in enumerate(all_choices.values()):
            print(f"{i}: {curr_blank.fill(choices)}")

        winner = player_indexes[int(input())]
        print(f"{winner.name} wins this round")
        winner.points += 1

        for p in self.players:
            print(f"{p.name}: {p.points} point")
            p.fills.append(self.fills.pop())

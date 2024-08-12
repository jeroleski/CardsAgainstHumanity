import itertools

from src.types.player import Player
from src.types.card import BlankCard, FillCard, DisplayBlankCard


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

        all_choices = []
        for p in self.players:
            if p == curr_czar:
                continue
            else:
                all_choices.append(p.choose_fills())

        print(f"{curr_czar.name} - choose a winner from:")
        for i, choices in enumerate(all_choices):
            print(f"{i}: {DisplayBlankCard(curr_blank, choices.fills)}")

        winner = all_choices[int(input())].player
        print(f"{winner.name} wins this round")
        winner.points += 1

        for p in self.players:
            print(f"{p.name}: {p.points} point")
            p.fills.append(self.fills.pop())

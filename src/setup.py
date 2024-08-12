from src.types.card import *
from src.types.game import Game
from src.types.player import Player


def parse_cards(blank_path: str, fill_path: str) -> tuple[list[BlankCard], list[FillCard]]:
    with open(blank_path) as file:
        blanks = [BlankCard(s) for s in file]

    with open(fill_path) as file:
        fills = [FillCard(s) for s in file]

    return blanks, fills


def read_players() -> list[Player]:
    print("Provide list of player names (space seperated)")
    line = input().split(" ")
    assert len(line) >= 2  # TODO move check
    return [Player(name) for name in line]


def init_game() -> Game:
    players = read_players()
    blanks, fills = parse_cards("data/blank_cards.txt", "data/fill_cards.txt")
    return Game(players, blanks, fills)

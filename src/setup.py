from random import shuffle

from src.types.card import *
from src.types.game import Game
from src.types.player import Player


def parse_cards(blank_path: str, fill_path: str) -> tuple[list[BlankCard], list[FillCard]]:
    with open(blank_path) as file:
        blanks = [BlankCard(s.strip()) for s in file]
    shuffle(blanks)

    with open(fill_path) as file:
        fills = [FillCard(s.strip()) for s in file]
    shuffle(fills)

    return blanks, fills


def read_player_names() -> list[str]:
    print("Provide list of player names (space seperated)")
    line = input().split(" ")
    assert len(line) >= 2  # TODO move check
    return line


def setup_game() -> Game:
    blanks, fills = parse_cards("./src/data/blank_cards.txt", "./src/data/fill_cards.txt")
    players = []
    for name in read_player_names():
        cards = [fills.pop() for _ in range(5)]  # TODO change num
        players.append(Player(name, cards))
    return Game(players, blanks, fills)

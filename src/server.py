from flask import Flask

from src.setup import parse_cards
from src.types.card import FillCard, Card, DisplayBlankCard
from src.types.game import Game
from src.types.player import Player


# TODO remove if unused
# class State(Enum):
#     WAITING_FOR_PLAYERS = 0
#     PLAYERS_DECIDING = 1
#     CZAR_VOTING = 2
#     GAME_OVER = 3


# def assert_state(required_state: State):
#     def wrapper(func):
#         def inner(self: Server, *args: list[str]) -> str:
#             if self.state != required_state:
#         return f"Can only call {func.__name__} on state {required_state.name} (current state {self.state.name})"
#             else:
#                 return func(args)
#         return inner
#     return wrapper


def format_cards(cards: list[Card]) -> str:
    return "@".join(f"{c}" for c in cards)  # TODO set global var


def extract_fill_cards(fills_stream: str) -> list[FillCard]:
    return [FillCard(text) for text in fills_stream.split("@")]  # TODO set global var


class Server:
    def __init__(self, app: Flask):  # TODO change all cards to id based system
        self.players: dict[str, Player] = {}
        self.game: Game = None  # TODO find alternative for placeholder

        app.route("/register_player/<name>")(self.register_player)
        app.route("/start_game")(self.start_game)
        app.route("/setup_new_round")(self.setup_new_round)
        app.route("/get_curr_blank")(self.get_curr_blank)
        app.route("/get_curr_czar")(self.get_curr_czar)
        app.route("/get_scores")(self.get_scores)
        app.route("/player_get_fills/<name>")(self.player_get_fills)
        app.route("/player_submit_fill/<name>/<fills_stream>")(self.player_submit_fill)
        app.route("/get_display_blanks")(self.get_display_blanks)
        app.route("/czar_submit_winner/<fills_stream>")(self.czar_submit_winner)

    def register_player(self, name: str) -> str:  # TODO not if game started
        self.players[name] = Player(name)  # TODO unique names
        return f"Added '{name}' to players"

    def start_game(self) -> str:
        # TODO change card fetching
        blanks, fills = parse_cards("./src/data/blank_cards.txt", "./src/data/fill_cards.txt")
        self.game = Game(list(self.players.values()), blanks, fills)
        return f"All players joined ({",".join(self.players.keys())}). Starting game"

    def setup_new_round(self) -> str:
        self.game.setup_new_round()
        return "Started next round"

    def get_curr_blank(self) -> str:
        return f"{self.game.curr_blank}"

    def get_curr_czar(self) -> str:
        return f"{self.game.curr_czar.name}"

    def get_scores(self) -> str:
        return "\n".join(f"{p.name}: {p.points} point" for p in self.game.players)

    def player_get_fills(self, name) -> str:
        player = [p for p in self.game.players if p.name == name][0]
        return format_cards(player.fills)

    # TODO move functionality to games, and make that handle players losing cards
    def player_submit_fill(self, name: str, fills_stream: str) -> str:
        fills = extract_fill_cards(fills_stream)
        player = self.players[name]
        self.game.curr_player_choices[player] = fills
        for card in fills:  # TODO handle by id
            player.fills.remove(card)
        return f"{name} plays {fills}"

    # TODO move functionality to games
    def get_display_blanks(self) -> str:
        choices = self.game.curr_player_choices.values()
        return format_cards([DisplayBlankCard(self.game.curr_blank.text, fills) for fills in choices])

    def czar_submit_winner(self, fills_stream: str) -> str:
        fills = extract_fill_cards(fills_stream)
        player = [p for p, c in self.game.curr_player_choices.items() if c == fills][0]
        player.points += 1
        return f"{player.name} wins this round"

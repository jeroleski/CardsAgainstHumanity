from src.server import Server
from src.setup import setup_game
from flask import Flask

app = Flask(__name__)


def main():
    Server(app)
    app.run()


def run_game_loop():
    game = setup_game()
    winners = []
    while not winners:
        print("--- new round ---")
        game.setup_new_round()
        game.play()
        winners = game.have_winners()

    print(f"--- {winners} wins the game ---")


if __name__ == '__main__':
    main()

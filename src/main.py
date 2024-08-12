from src.setup import setup_game


def main():
    game = setup_game()
    winners = []
    while not winners:  # TODO pint winner
        print("--- new round ---")
        game.play()
        winners = game.have_winner()
    print(f"--- {winners} wins the game ---")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

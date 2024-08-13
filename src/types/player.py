from src.types.card import FillCard


class Player:
    def __init__(self, name: str):
        self.name = name
        self.fills: list[FillCard] = []
        self.points: int = 0

    def __hash__(self):  # TODO what if players have the same name?
        return hash(self.name)

    def choose_fills(self) -> list[FillCard]:
        print(f"{self.name} - choose cards from:")
        print(" - ".join([f"{i}: {c}" for i, c in enumerate(self.fills)]))
        card_indexes = [int(index) - i for i, index in enumerate(input().split(" "))]
        return [self.fills.pop(index) for index in card_indexes]

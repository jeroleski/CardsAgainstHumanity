class Card:
    def __init__(self, text: str):
        self.text = text

    def __eq__(self, other) -> bool:  # TODO use dataclass
        return isinstance(other, Card) and self.text == other.text

    def __repr__(self):
        return self.text


class FillCard(Card):
    pass


class DisplayBlankCard(Card):
    def __init__(self, text: str, fills: list[FillCard]):
        super().__init__(text)
        assert text.count("_") == len(fills)  # TODO move check
        self.fills = fills

    def __repr__(self):
        return self.text.replace("_", "{}").format(*self.fills)


class BlankCard(Card):
    def fill(self, fills: list[FillCard]) -> DisplayBlankCard:
        return DisplayBlankCard(self.text, fills)

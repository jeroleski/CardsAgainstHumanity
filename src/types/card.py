from __future__ import annotations


class Card:
    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return self.text


class FillCard(Card):
    pass


class BlankCard(Card):
    def fill(self, blanks: list[FillCard]) -> DisplayBlankCard:
        return DisplayBlankCard(self, blanks)


class DisplayBlankCard:
    def __init__(self, blank: BlankCard, fills: list[FillCard | None]):
        assert blank.text.count("_") == len(fills)  # TODO move check
        self.blank = blank
        self.fills = fills

    def __repr__(self):
        return self.blank.text.replace("_", "{}").format(*self.fills)

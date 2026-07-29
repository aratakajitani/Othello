from enum import Enum


class Stone(Enum):
    EMPTY = 1
    BLACK = 2
    WHITE = 3

    def __repr__(self):
        if self == Stone.BLACK:
            return "B"
        if self == Stone.WHITE:
            return "W"
        else:
            return "."
    __str__ = __repr__

    @classmethod
    def get_opponent_stone(cls, stone):
        if stone == cls.BLACK:
            return cls.WHITE
        if stone == cls.WHITE:
            return cls.BLACK
        else:
            raise Exception("石を引数にしてくれ")

    def get_currunt_color(cls, stone):
        if stone == cls.BLACK:
            return cls.BLACK
        if stone == cls.WHITE:
            return cls.WHITE
        else:
            raise Exception("石を引数にしてくれ")

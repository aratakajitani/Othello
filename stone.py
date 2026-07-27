class stone:
    empty = "."
    black = "B"
    white = "W"

    def get_opponent_stone(color):
        if color == stone.black:
            return stone.white
        return stone.black

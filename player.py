from board import Board


class Player:
    def __init__(self, stone):
        self.stone = stone

    def select_play_show(self, board, stone):
        placable_places = []
        for y in range(Board.size):
            for x in range(Board.size):
                if board.can_place_stone(x, y, stone):
                    placable_places.append((x, y))
        return placable_places

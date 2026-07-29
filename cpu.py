from board import Board
from game import Game


import random


class Cpu:

    def __init__(self, stone):
        self.stone = stone

    def select_play(self, board):
        can_place_flag = False
        placable_places = []
        for y in range(Board.size):
            for x in range(Board.size):
                if board.can_place_stone(x, y, self.stone):
                    placable_places.append((x, y))
                    can_place_flag = True
        if can_place_flag:
            while True:
                x, y = random.choice(placable_places)
                print(x, y)
                if board.can_place_stone(x, y, self.stone):
                    board.reverse_stone(x, y, self.stone)
                    break
        else:
            print("石を置けないのでパスします")
            return Game.plus_pass_count()
            
        return False

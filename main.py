from board import Board
from game import Game
from player import Player
from cpu import Cpu
from stone import Stone


def main():
    board = Board()
    player_1_stone = Game.select_stone()
    player_2_stone = Stone.get_opponent_stone(player_1_stone)
    player_1 = Player(player_1_stone)
    player_2 = Cpu(player_2_stone)
    othello = Game(board=board, player_1=player_1, player_2=player_2)
    othello.run()


if __name__ == "__main__":
    main()

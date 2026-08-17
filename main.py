from board import Board
from game import Game
from stone import Stone
from standard_io import StandardIO
from othello_ui import OthelloUI
import argparse


def main():
    board = Board()
    parser = argparse.ArgumentParser(description='オセロ')
    parser.add_argument('mode', choices=['tkinter', 'terminal'], help='オセロのモード選択')
    args = parser.parse_args()
    if args.mode == 'terminal':
        ui = StandardIO(board)
    else:
        ui = OthelloUI(board)
    mode = ui.select_game_mode()
    if mode == 1:
        player_1_stone = ui.select_stone()
    else:
        player_1_stone = Stone.BLACK
    player_2_stone = Stone.get_opponent_stone(player_1_stone)
    player_1, player_2 = Game.create_players(mode, player_1_stone, player_2_stone)
    othello = Game(board=board, player_1=player_1, player_2=player_2)
    othello.run_game(ui)


if __name__ == "__main__":
    main()

import tkinter as tk
from board import Board
from game import Game
from stone import Stone
from othello_ui import Othello_ui
from standard_io import StandardIO
import sys


def main():
    board = Board()
    run_mode = None

    if len(sys.argv) > 1:
        if sys.argv[1] == "ui":
            run_mode = 1
        elif sys.argv[1] == "terminal":
            run_mode = 2

    if run_mode is None:
        run_mode = StandardIO.select_running()
    if run_mode == 1:
        root = tk.Tk()
        root.title("オセロ")
        root.geometry("1000x1000")
        ui = Othello_ui(root, board) 
        mode = ui.select_game_mode()
        player_1_stone = ui.select_stone()
    else:
        ui = None
        player_1_stone = StandardIO.select_stone()
        mode = StandardIO.select_game_mode()
        terminal_ui = StandardIO(board) 
    player_2_stone = Stone.get_opponent_stone(player_1_stone)
    player_1, player_2 = Game.create_players(mode, player_1_stone, player_2_stone)
    othello = Game(board=board, player_1=player_1, player_2=player_2)

    if run_mode == 1:
        root.after(100, othello.run_game, ui)
        ui.show()
        root.mainloop()
    else:
        othello.run_game(terminal_ui)


if __name__ == "__main__":
    main()

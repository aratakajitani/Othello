import tkinter as tk
from board import Board
from game import Game
from stone import Stone
from othello_ui import Othello_ui
from standard_io import StandardIO


def main():
    board = Board()
    if StandardIO.select_running() == 1:
        root = tk.Tk()
        root.title("オセロ")
        root.geometry("1000x1000")
        ui = Othello_ui(root, board)
        mode = ui.select_game_mode()
        player_1_stone = ui.select_stone()
        player_2_stone = Stone.get_opponent_stone(player_1_stone)
        player_1, player_2 = Game.create_players(mode, player_1_stone, player_2_stone)
        othello = Game(board=board, player_1=player_1, player_2=player_2)
        root.after(100, othello.run_tkinter, ui)
        ui.show()
        root.mainloop()
    else:
        player_1_stone = StandardIO.select_stone()
        player_2_stone = Stone.get_opponent_stone(player_1_stone)
        mode = StandardIO.select_game_mode()
        player_1, player_2 = Game.create_players(mode, player_1_stone, player_2_stone)
        othello = Game(board=board, player_1=player_1, player_2=player_2)
        othello.run_terminal()


if __name__ == "__main__":
    main()

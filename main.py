import tkinter as tk
from board import Board
from game import Game
from stone import Stone
from othello_ui import Othello_ui


def main():
    root = tk.Tk()
    root.title("オセロ")
    root.geometry("1000x1000")
    board = Board()
    ui = Othello_ui(root, board)
    mode = ui.select_game_mode()
    player_1_stone = ui.select_stone()
    player_2_stone = Stone.get_opponent_stone(player_1_stone)
    player_1, player_2 = Game.create_players(mode, player_1_stone, player_2_stone)
    othello = Game(board=board, player_1=player_1, player_2=player_2)
    ui.show()
    root.after(100, othello.run)
    root.mainloop()


if __name__ == "__main__":
    main()
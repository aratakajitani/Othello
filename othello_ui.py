import tkinter as tk
from stone import Stone


class Othello_ui:
    def __init__(self, master, board):
        self.master = master
        self.board = board

        self.board_label = tk.Label(self.master, text="", font=("Courier", 24), justify="left")
        self.board_label.pack(pady=20)

        self.wait_var = tk.IntVar()
        self.chosen_value = None

    def select_game_mode(self):
        one_btn = tk.Button(self.master, text='一人モード', command=lambda: self.button_clicked(1))
        one_btn.pack()
        two_btn = tk.Button(self.master, text='二人モード', command=lambda: self.button_clicked(2))
        two_btn.pack()
        self.master.wait_variable(self.wait_var)
        one_btn.pack_forget()
        two_btn.pack_forget()
        return self.chosen_value

    def select_stone(self):
        black_btn = tk.Button(self.master, text='黒を選ぶ(先手)', command=lambda: self.button_clicked(Stone.BLACK))
        black_btn.pack()
        white_btn = tk.Button(self.master, text='白を選ぶ(後手)', command=lambda: self.button_clicked(Stone.WHITE))
        white_btn.pack()
        self.master.wait_variable(self.wait_var)
        black_btn.pack_forget()
        white_btn.pack_forget()
        return self.chosen_value

    def button_clicked(self, value):
        self.chosen_value = value
        self.wait_var.set(1)

    def show(self):
        board_string = ""
        for y in range(len(self.board.board)):
            for x in range(len(self.board.board[y])):
                stone = self.board.board[y][x]
                if stone == Stone.BLACK:
                    board_string += "⚫️"
                elif stone == Stone.WHITE:
                    board_string += "⚪️"
                else:
                    board_string += "・"
            board_string += "\n"
        self.board_label.config(text=board_string)

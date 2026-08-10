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

        self.entry_place_x = tk.Entry(self.master, width=20)
        self.entry_place_y = tk.Entry(self.master, width=20)
        self.label_x = tk.Label(self.master, text='')
        self.label_x.pack(pady=5)
        self.label_y = tk.Label(self.master, text='')
        self.label_y.pack(pady=5)

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

    def can_place_show(self, game, current_player):
        places = game.select_play_show(current_player)
        for x, y in places:
            places = tk.Label(self.master, text=f"座標: ({x},{y})")
            places.pack()

    def select_place_stone(self):
        self.entry_place_x.pack()
        self.entry_place_y.pack()
        completion_btn = tk.Button(self.master, text="完了", command=self.get_entry)
        completion_btn.pack()
        self.master.wait_variable(self.wait_var)
        self.entry_place_x.pack_forget()
        self.entry_place_y.pack_forget()
        completion_btn.pack_forget()
        return self.chosen_value

    def get_entry(self):
        self.get_entry_x()
        self.get_entry_y()

    def get_entry_x(self):
        get_text_x = self.entry_place_x.get()
        self.label_x.config(text=f"入力された文字: {get_text_x}")

    def get_entry_y(self):
        get_text_y = self.entry_place_y.get()
        self.label_y.config(text=f"入力された文字: {get_text_y}")

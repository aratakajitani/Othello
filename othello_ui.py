import tkinter as tk
from stone import Stone


class Othelloui:
    def __init__(self, board):
        self.master = tk.Tk()
        self.master.title("オセロ")
        self.master.geometry("1000x1000")
        self.board = board

        self.board_label = tk.Label(self.master, text="", font=("Courier", 24), justify="left")
        self.board_label.pack(pady=20)

        self.wait_var = tk.IntVar()
        self.chosen_value = None

        self.cpu_select_label = tk.Label(self.master, text="")
        self.cpu_select_label.pack()

        self.current_color_label = tk.Label(self.master, text="")
        self.current_color_label.pack()

        self.pass_labels = []

        self.places_btn = []

        self.chosen_places = []

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

    def turn_color_show(self, color_str):
        self.current_color_label.config(text=f"【{color_str}のターンです】")

    def cpu_select(self, current_x_y):
        self.cpu_select_label.config(text=f"【cpuは{current_x_y}に置きました。】")

    def button_clicked(self, value):
        self.chosen_value = value
        self.wait_var.set(1)

    def show(self):
        numbers = ["０", "１", "２", "３", "４", "５", "６", "７", "８"]
        board_string = "　"
        for x in range(len(self.board.board)):
            board_string += numbers[x]
        board_string += "\n"
        for y in range(len(self.board.board)):
            board_string += numbers[y]
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
        self.master.update()

    def select_play(self, game, current_player):
        places = game.select_play_show(current_player)
        if places:
            for x, y in places:
                places_btn = tk.Button(self.master, text=f"座標: ({y},{x})", command=lambda bx=x, by=y: self.places_button_clicked(bx, by))
                places_btn.pack()
                self.places_btn.append(places_btn)
            self.master.wait_variable(self.wait_var)
        else:
            return None
        return self.chosen_places

    def places_button_clicked(self, x, y):
        if self.pass_labels:
            self.pass_labels[-1].pack_forget()
        self.chosen_places = x, y
        for btn in self.places_btn:
            btn.pack_forget()
        self.wait_var.set(1)

    def finish_running(self, winner):
        for pass_label in self.pass_labels:
            pass_label.pack_forget()
        self.pass_labels.clear()
        self.cpu_select_label.pack_forget()
        self.current_color_label.pack_forget()
        self.winner_label = tk.Label(self.master, text=f"【{winner}】")
        self.winner_label.pack()

    def pass_count(self):
        pass_label = tk.Label(self.master, text="おける場所がないのでパスしました。")
        pass_label.pack()
        self.pass_labels.append(pass_label)

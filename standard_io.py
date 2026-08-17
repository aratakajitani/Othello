from stone import Stone


class StandardIO:

    def __init__(self, board):
        self.board = board

    def turn_color_show(self, color_str):
        print(f"【{color_str}のターンです】")

    def show(self):
        self.board.show()

    def pass_count(self):
        print("置ける場所がないためパスしました。")

    def finish_running(self, winner):
        print("--- ゲーム終了 ---")
        print(winner)

    def cpu_select(self, current_x_y):
        print(f"【cpuは{current_x_y}に置きました。】")

    @classmethod
    def select_stone(cls):
        while True:
            try:
                c = int(input("黒を選ぶ(先手)なら1 白を選ぶ(後手)なら2を入力してください:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 1:
                    print("--- ゲーム開始 ---")
                    return Stone.BLACK
                else:
                    print("--- ゲーム開始 ---")
                    return Stone.WHITE
            except ValueError:
                print("入力エラーです")
                continue

    def select_game_mode(self):
        while True:
            try:
                c = int(input("1人モードなら1 2人モードならなら2を入力してください:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 1:
                    return 1
                else:
                    print("--- ゲーム開始 ---")
                    return 2 
            except ValueError:
                print("入力エラーです")
                continue

    def select_running():
        while True:
            try:
                c = int(input("TKinterで遊ぶなら1 ターミナルで遊ぶなら2を入力してください。:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 1:
                    return 1
                else:
                    return 2
            except ValueError:
                print("入力エラーです")
                continue

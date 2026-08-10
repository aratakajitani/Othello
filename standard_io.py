class StandardIO:
    def __init__(self):
        pass

    def show_board(self, board):
        print(board)

    def can_select_place(self, x, y):
        print(f"座標: ({x},{y})")

    def input_place(self, board, board_size: int):
        can_place_flag = True
        if can_place_flag:
            while True:
                try:
                    x = int(input("x座標を入力してください:"))
                    if not 0 <= x <= board_size:
                        print("入力エラーです")
                        continue
                    y = int(input("y座標を入力してください:"))
                    if not 0 <= y <= board_size:
                        print("入力エラーです")
                        continue
                except ValueError:
                    print("入力エラーです")
                    continue
                if board.can_place_stone(x, y, self.stone):
                    board.reverse_stone(x, y, self.stone)
                    break
                else:
                    print("そこには置けません")
        else:
            print("石を置けないのでパスします")
            return None
        return x, y

    def select_stone(self, stone):
        while True:
            try:
                c = int(input("最初の色を白なら1 黒なら2を入力してください:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 2:
                    return stone.BLACK
                else:
                    return stone.WHITE
            except ValueError:
                print("入力エラーです")
                continue

    def player_1_color(self, stone):
        if self.player_1.stone == stone.BLACK:
            print("黒のターンです")
        if self.player_1.stone == stone.WHITE:
            print("白のターンです")

    def player_2_color(self, stone):
        if self.player_2.stone == stone.BLACK:
            print("黒のターンです")
        if self.player_2.stone == stone.WHITE:
            print("白のターンです")

    def start_running(self):
        print("--- ゲーム開始 ---")

    def turn_color_view(self, color_str):
        print(f"【{color_str}のターンです】")

    def finish_running(self):
        print("--- ゲーム終了 ---")

    def view_pass(self):
        print("置ける場所がないためパスしました。")

    def select_game_mode():
        while True:
            try:
                c = int(input("1人モードなら1 2人モードならなら2を入力してください:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 2:
                    return 2
                else:
                    return 1
            except ValueError:
                print("入力エラーです")
                continue

    def viwe_winner(self, black_count, white_count):
        if black_count > white_count:
            print("黒の勝ちです")
        elif black_count == white_count:
            print("引き分けです")
        else:
            print("白の勝ちです")

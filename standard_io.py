class StandardIO:
    def __init__(self):
        pass

    def show_board(self, board):
        print(board)

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


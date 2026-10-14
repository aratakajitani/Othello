class Player:
    def __init__(self, stone):
        self.stone = stone

    def select_place(self, board):
        can_place_flag = False
        for y in range(board.size):
            for x in range(board.size):
                if board.can_place_stone(x, y, self.stone):
                    print(f"座標: ({x},{y})")
                    can_place_flag = True
        if can_place_flag:
            while True:
                try:
                    x = int(input("x座標を入力してください:"))
                    if not 0 <= x <= board.size:
                        print("入力エラーです")
                        continue
                    y = int(input("y座標を入力してください:"))
                    if not 0 <= y <= board.size:
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
            return None
        return x, y

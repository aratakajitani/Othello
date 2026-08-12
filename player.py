from board import Board


class Player:
    def __init__(self, stone):
        self.stone = stone

    def select_play_show(self, board, stone):
        can_place_flag = False
        placable_places = []
        for y in range(Board.size):
            for x in range(Board.size):
                if board.can_place_stone(x, y, stone):
                    placable_places.append((x, y))
                    can_place_flag = True
        if can_place_flag:
            while True:
                return placable_places
        else:
            return None

    def select_play(self, board):
        can_place_flag = False
        for y in range(Board.size):
            for x in range(Board.size):
                if board.can_place_stone(x, y, self.stone):
                    print(f"座標: ({x},{y})")
                    can_place_flag = True
        if can_place_flag:
            while True:
                try:
                    x = int(input("x座標を入力してください:"))
                    if not 0 <= x <= Board.size:
                        print("入力エラーです")
                        continue
                    y = int(input("y座標を入力してください:"))
                    if not 0 <= y <= Board.size:
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
    
    

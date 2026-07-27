from board import board
from stone import stone


class game:

    def __init__(self):
        self.board = board()
        self.game = []
        self.pass_check()

    def pass_check(self):
        self.pass_count = 0

    def select_color(self):
        while True:
            try:
                c = int(input("最初の色を白なら1 黒なら2を入力してください:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 2:
                    return stone.black
                else:
                    return stone.white
            except ValueError:
                print("入力エラーです")
                continue

    def currunt_color(self, color):
        if color == stone.black:
            print("黒のターンです")
        if color == stone.white:
            print("白のターンです")

    def turn_change(self, color):
        color = stone.get_opponent_stone(color)

    def turn(self):
        board.show()
        color = self.select_color()
        self.pass_check()
        while self.pass_count < 2:
            self.currunt_color(color)
            board.show()
            can_place_flag = False
            for y in range(board.size):
                for x in range(board.size):
                    if board.can_place_stone(x, y, color):
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
                    self.pass_count = 0
                    if board.can_place_stone(x, y, color):
                        board.reverse_stone(x, y, color)
                        break
                    else:
                        print("そこには置けません")
            else:
                print("石を置けないのでパスします")
                self.pass_count += 1
            color = stone.get_opponent_stone(color)

        self.count_stone(x, y)
        return False

    def count_stone(self, x, y):
        black_count = 0
        white_count = 0
        for y in range(board.size):
            for x in range(board.size):
                if board.board[y][x] == stone.black:
                    black_count += 1
                if board.board[y][x] == stone.white:
                    white_count += 1
            if black_count > white_count:
                print("黒の勝ちです")
            elif black_count == white_count:
                print("引き分けです")
            else:
                print("白の勝ちです")
            return False


if __name__ == "__main__":
    game.turn()

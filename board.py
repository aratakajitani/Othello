class Board:
    size = 8
    empty = "."
    black = "B"
    white = "W"
    direction = [
        (0, 1),   # 下
        (1, 0),   # 右
        (0, -1),  # 上
        (-1, 0),  # 左
        (1, 1),   # 右下
        (-1, -1),  # 左上
        (1, -1),  # 右上
        (-1, 1)   # 左下
    ]

    def __init__(self):
        self.board = []
        self.prepare()
        self.setup()
        self.count_empty()
        self.pass_check()

    def prepare(self):
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(self.empty)
            self.board.append(row)

    def setup(self):
        self.board[3][3] = self.white
        self.board[3][4] = self.black
        self.board[4][3] = self.black
        self.board[4][4] = self.white

    def count_empty(self):
        self.empty_count = 60

    def get_opponent_stone(self, color):
        if color == self.black:
            return self.white
        return self.black

    def can_place_stone(self, x, y, color):
        if self.board[y][x] != self.empty:
            return False
        for dx, dy in self. direction:
            next_x = x + dx
            next_y = y + dy
            opposite = False

            while 0 <= next_x < self.size and 0 <= next_y < self.size:
                if self.board[next_y][next_x] == self.empty:
                    break
                elif self.board[next_y][next_x] == self.get_opponent_stone(color):
                    opposite = True
                elif self.board[next_y][next_x] == color:
                    if opposite:
                        return True
                    break
                next_x += dx
                next_y += dy

        return False

    def can_reverse_stone(self, x, y, color):

        if not self.can_place_stone(x, y, color):
            print("そこには置けません")
            return False

        can_reverse_stone = []

        if self.board[y][x] != self.empty:
            return False

        for dx, dy in self. direction:
            next_x = x + dx
            next_y = y + dy
            opposite = False

            while 0 <= next_x < self.size and 0 <= next_y < self.size:
                if self.board[next_y][next_x] == self.empty:
                    break
                elif self.board[next_y][next_x] == self.get_opponent_stone(color):
                    opposite = True
                elif self.board[next_y][next_x] == color:
                    if opposite:
                        while (next_y, next_x) != (y, x):
                            next_x = next_x - dx
                            next_y = next_y - dy
                            if (next_y, next_x) == (y, x):
                                break
                            can_reverse_stone.append((next_y, next_x, color))
                    break

                next_x += dx
                next_y += dy

        return can_reverse_stone

    def reverse_stone(self, x, y, color):
        can_reverse_stone = self.can_reverse_stone(x, y, color)
        if can_reverse_stone:
            self.board[y][x] = color
            for y, x, color in can_reverse_stone:
                self.board[y][x] = color

    def show(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.board[y][x], end=" ")
            print()

    def count_stone(self, x, y):
        black_count = 0
        white_count = 0
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x] == self.black:
                    black_count += 1
                if self.board[y][x] == self.white:
                    white_count += 1
        if black_count > white_count:
            print("黒の勝ちです")
        elif black_count == white_count:
            print("引き分けです")
        else:
            print("白の勝ちです")
        return False

    def pass_check(self):
        self.pass_count = 0

    def turn_change(self, color):
        color = self.get_opponent_stone(color)

    def select_color(self):
        while True:
            try:
                c = int(input("最初の色を白なら1 黒なら2を入力してください:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 1:
                    self.black
                return self.white
            except ValueError:
                print("入力エラーです")
                continue

    def currunt_color(self, color):
        if color == self.black:
            print("黒のターンです")
        if color == self.white:
            print("白のターンです")

    def game(self, color):
        self.pass_check()
        while self.pass_count < 2 and self.empty_count > 0:
            self.show()
            self.currunt_color(color)
            can_place_flag = False
            for y in range(self.size):
                for x in range(self.size):
                    if self.can_place_stone(x, y, color):
                        print(f"座標: ({x},{y})")
                        can_place_flag = True
            if can_place_flag:
                while True:
                    try:
                        x = int(input("x座標を入力してください:"))
                        if not 0 <= x <= 8:
                            print("入力エラーです")
                            continue
                        y = int(input("y座標を入力してください:"))
                        if not 0 <= y <= 8:
                            print("入力エラーです")
                            continue
                    except ValueError:
                        print("入力エラーです")
                        continue
                    self.pass_count = 0
                    if self.can_place_stone(x, y, color):
                        self.reverse_stone(x, y, color)
                        self.empty_count -= 1
                        print(self.empty_count)
                        break
                    else:
                        print("そこには置けません")
            else:
                print("石を置けないのでパスします")
                self.pass_count += 1
            color = self.get_opponent_stone(color)

        self.count_stone(x, y)
        return False


if __name__ == "__main__":
    board = Board()
    board.show()
    board.can_place_black()

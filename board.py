from stone import Stone


class Board:
    size = 8
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

    def prepare(self):
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(Stone.EMPTY)
            self.board.append(row)

    def setup(self):
        self.board[3][3] = Stone.WHITE
        self.board[3][4] = Stone.BLACK
        self.board[4][3] = Stone.BLACK
        self.board[4][4] = Stone.WHITE

    def can_place_stone(self, x, y, stone):
        if self.board[y][x] != Stone.EMPTY:
            return False
        for dx, dy in self.direction:
            next_x = x + dx
            next_y = y + dy
            opposite = False

            while 0 <= next_x < self.size and 0 <= next_y < self.size:
                if self.board[next_y][next_x] == Stone.EMPTY:
                    break
                elif self.board[next_y][next_x] == Stone.get_opponent_stone(stone):
                    opposite = True
                elif self.board[next_y][next_x] != Stone.get_opponent_stone(stone):
                    if opposite:
                        return True
                    break
                next_x += dx
                next_y += dy

        return False

    def can_reverse_stone(self, x, y, stone):

        if not self.can_place_stone(x, y, stone):
            return False

        can_reverse_stone = []

        if self.board[y][x] != Stone.EMPTY:
            return False

        for dx, dy in self.direction:
            next_x = x + dx
            next_y = y + dy
            opposite = False

            while 0 <= next_x < self.size and 0 <= next_y < self.size:
                if self.board[next_y][next_x] == Stone.EMPTY:
                    break
                elif self.board[next_y][next_x] == Stone.get_opponent_stone(stone):
                    opposite = True
                elif self.board[next_y][next_x] == stone:
                    if opposite:
                        while (next_y, next_x) != (y, x):
                            next_x = next_x - dx
                            next_y = next_y - dy
                            if (next_y, next_x) == (y, x):
                                break
                            can_reverse_stone.append((next_y, next_x, stone))
                    break

                next_x += dx
                next_y += dy

        return can_reverse_stone

    def reverse_stone(self, x, y, stone):
        can_reverse_stone = self.can_reverse_stone(x, y, stone)
        if can_reverse_stone:
            self.board[y][x] = stone
            for y, x, stone in can_reverse_stone:
                self.board[y][x] = stone

    def show(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.board[y][x], end=" ")
            print()

    def count_stone(self):
        black_count = 0
        white_count = 0
        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x] == Stone.BLACK:
                    black_count += 1
                if self.board[y][x] == Stone.WHITE:
                    white_count += 1
        if black_count > white_count:
            print("黒の勝ちです")
        elif black_count == white_count:
            print("引き分けです")
        else:
            print("白の勝ちです")


if __name__ == "__main__":
    Board.show()

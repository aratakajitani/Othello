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
        self.field = []
        self.prepare()
        self.setup()

    def prepare(self):
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(self.empty)
            self.field.append(row)

    def setup(self):
        self.field[3][3] = self.white
        self.field[3][4] = self.black
        self.field[4][3] = self.black
        self.field[4][4] = self.white
        self.field[5][4] = self.white

    def can_place_black(self, x, y):
        if self.field[y][x] != self.empty:
            return False
        for dx, dy in self. direction:
            next_x = x + dx
            next_y = y + dy
            opposite = False

            while 0 <= next_x < self.size and 0 <= next_y < self.size:
                if self.field[next_y][next_x] == self.empty:
                    break
                elif self.field[next_y][next_x] == self.white:
                    opposite = True
                elif self.field[next_y][next_x] == self.black:
                    if opposite:
                        return True
                    break

                next_x += dx
                next_y += dy

        return False

    def can_place_white(self, x, y):
        if self.field[y][x] != self.empty:
            return False

        for dx, dy in self. direction:
            next_x = x + dx
            next_y = y + dy
            opposite = False

            while 0 <= next_x < self.size and 0 <= next_y < self.size:
                if self.field[next_y][next_x] == self.empty:
                    break
                elif self.field[next_y][next_x] == self.black:
                    opposite = True
                elif self.field[next_y][next_x] == self.white:
                    if opposite:
                        return True
                    break

                next_x += dx
                next_y += dy

        return False

    def place_black(self, x, y):
        self.field[y][x] = self.black

    def place_white(self, x, y):
        self.field[y][x] = self.white

    def can_reverse_black(self, x, y):

        if self.field[y][x] != self.empty:
            return []

        self.place_black(x, y)

        all_reversible_stones = []

        for dx, dy in self. direction:
            next_x = x + dx
            next_y = y + dy
            opposite = False

            while 0 <= next_x < self.size and 0 <= next_y < self.size:
                if self.field[next_y][next_x] == self.empty:
                    break
                elif self.field[next_y][next_x] == self.white:
                    opposite = True
                elif self.field[next_y][next_x] == self.black:
                    if opposite:
                        can_reverse_stone = []
                        while (next_y, next_x) != (y, x):
                            next_x = next_x - dx
                            next_y = next_y - dy
                            if (next_y, next_x) == (y, x):
                                break
                            can_reverse_stone.append((next_y, next_x))
                            print(can_reverse_stone)
                            all_reversible_stones.extend(can_reverse_stone)
                    break

                next_x += dx
                next_y += dy

        return all_reversible_stones

    def can_reverse_white(self, x, y):

        if self.field[y][x] != self.empty:
            return []

        self.place_white(x, y)

        all_reversible_stones = []

        for dx, dy in self. direction:
            next_x = x + dx
            next_y = y + dy
            opposite = False

            while 0 <= next_x < self.size and 0 <= next_y < self.size:
                if self.field[next_y][next_x] == self.empty:
                    break
                elif self.field[next_y][next_x] == self.black:
                    opposite = True
                elif self.field[next_y][next_x] == self.white:
                    if opposite:
                        can_reverse_stone = []
                        while (next_y, next_x) != (y, x):
                            next_x = next_x - dx
                            next_y = next_y - dy
                            if (next_y, next_x) == (y, x):
                                break
                            can_reverse_stone.append((next_y, next_x))
                            print(can_reverse_stone)
                            all_reversible_stones.extend(can_reverse_stone)
                    break

                next_x += dx
                next_y += dy

        return all_reversible_stones

    def reverese_black(self, x, y):
        can_reverse_stone = self.can_reverse_black(x, y)
        for y, x in can_reverse_stone:
            self.field[y][x] = self.black

    def reverese_white(self, x, y):
        can_reverse_stone = self.can_reverse_white(x, y)
        for y, x in can_reverse_stone:
            self.field[y][x] = self.white

    def show(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.field[y][x], end=" ")
            print()


if __name__ == "__main__":
    board = Board()
    board.show()
    board.can_place_black()
    board.place_black[2][3]

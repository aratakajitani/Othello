from stone import stone


class board:
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
        board.board = []
        self.prepare()
        self.setup()

    def prepare(self):
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(stone.empty)
            self.board.append(row)

    def setup(self):
        self.board[3][3] = stone.white
        self.board[3][4] = stone.black
        self.board[4][3] = stone.black
        self.board[4][4] = stone.white

    def can_place_stone(x, y, color):
        if board.board[y][x] != stone.empty:
            return False
        for dx, dy in board.direction:
            next_x = x + dx
            next_y = y + dy
            opposite = False

            while 0 <= next_x < board.size and 0 <= next_y < board.size:
                if board.board[next_y][next_x] == stone.empty:
                    break
                elif board.board[next_y][next_x] == stone.get_opponent_stone(color):
                    opposite = True
                elif board.board[next_y][next_x] == color:
                    if opposite:
                        return True
                    break
                next_x += dx
                next_y += dy

        return False

    def can_reverse_stone(x, y, color):

        if not board.can_place_stone(x, y, color):
            print("そこには置けません")
            return False

        can_reverse_stone = []

        if board.board[y][x] != stone.empty:
            return False

        for dx, dy in board.direction:
            next_x = x + dx
            next_y = y + dy
            opposite = False

            while 0 <= next_x < board.size and 0 <= next_y < board.size:
                if board.board[next_y][next_x] == stone.empty:
                    break
                elif board.board[next_y][next_x] == stone.get_opponent_stone(color):
                    opposite = True
                elif board.board[next_y][next_x] == color:
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

    def reverse_stone(x, y, color):
        can_reverse_stone = board.can_reverse_stone(x, y, color)
        if can_reverse_stone:
            board.board[y][x] = color
            for y, x, color in can_reverse_stone:
                board.board[y][x] = color

    def show():
        for y in range(board.size):
            for x in range(board.size):
                print(board.board[y][x], end=" ")
            print()


if __name__ == "__main__":
    board.show()

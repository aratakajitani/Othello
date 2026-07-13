class Board:
    SIZE = 8
    EMPTY = "."
    BLACK = "B"
    WHITE = "W"
    DIRECTIONS = [
        (0, 1),   # 下
        (1, 0),   # 右
        (0, -1),  # 上
        (-1, 0),  # 左
        (1, 1),   # 右下
        (-1, -1), # 左上
        (1, -1),  # 右上
        (-1, 1)   # 左下
    ]

    def __init__(self):
        self.field = []
        self.prepare()
        self.setup()

    def prepare(self):
        for _ in range(self.SIZE):
            row = []
            for _ in range(self.SIZE):
                row.append(self.EMPTY)
            self.field.append(row)

    def setup(self):
        self.field[3][3] = self.WHITE
        self.field[3][4] = self.BLACK
        self.field[4][3] = self.BLACK
        self.field[4][4] = self.WHITE
        self.field[5][4] = self.WHITE
        

    def BLACK_turn_select(self,x,y):
        if self.field[y][x] != self.EMPTY:
            return False
        
        
        for dx,dy in self. DIRECTIONS:
            next_x = x + dx
            next_y = y + dy
            opposite = False
            
            while 0 <= next_x < self.SIZE and 0 <= next_y < self.SIZE:
                if self.field[next_y][next_x] == self.EMPTY:
                    break
                elif self.field[next_y][next_x] == self.WHITE:
                    opposite = True
                elif self.field[next_y][next_x] == self.BLACK:
                    if opposite:
                        return True
                    break    

                next_x += dx
                next_y += dy

        return False

    
    def show(self):
        for y in range(self.SIZE):
            for x in range(self.SIZE):
                print(self.field[y][x], end=" ")
            print()


if __name__ == "__main__":
    board = Board()
    board.show()
    board.select()
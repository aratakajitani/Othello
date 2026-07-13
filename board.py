class Board:
    SIZE = 8
    EMPTY = "."
    BLACK = "B"
    WHITE = "W"

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

    def select(self,x,y):
        if self.field[y][x] != self.EMPTY:
            return False
        if self.field[y][x+1] == self.WHITE:
            if self.field[y][x+2] == self.BLACK:
                return True
        
    def show(self):
        for y in range(self.SIZE):
            for x in range(self.SIZE):
                print(self.field[y][x], end=" ")
            print()


if __name__ == "__main__":
    board = Board()
    board.show()
    board.select()
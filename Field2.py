class Field:
    SIZE=8
    EMPTY="."
    BLACK="B"
    WHITE="W"


    def __init__(self):
        self.field=[]
        self.prepare()
        self.setup()


    def prepare(self):
        
        for y in range(self.SIZE):
            row = []
            for x in range(self.SIZE):
                row.append(self.EMPTY)
            self.field.append(row)  

    def setup(self):
        self.field[3][3]=self.WHITE
        self.field[3][4]=self.BLACK
        self.field[4][3]=self.BLACK
        self.field[4][4]=self.WHITE

    def show(self):
        for y in range(self.SIZE):
            for x in range(self.SIZE):
                print(self.field[y][x],end=" ")
            print()

field=Field()
field.show()
from stone import Stone


class Game:

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.pass_check()
        self.player_1 = player_1
        self.player_2 = player_2

    @classmethod
    def pass_check(cls):
        cls.pass_count = 0

    @classmethod
    def plus_pass_count(cls):
        cls.pass_count += 1

    @classmethod
    def select_stone(cls):
        while True:
            try:
                c = int(input("最初の色を白なら1 黒なら2を入力してください:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 2:
                    return Stone.BLACK
                else:
                    return Stone.WHITE
            except ValueError:
                print("入力エラーです")
                continue

    def player_1_color(self):
        if self.player_1.stone == Stone.BLACK:
            print("黒のターンです")
        if self.player_1.stone == Stone.WHITE:
            print("白のターンです")

    def player_2_color(self):
        if self.player_2.stone == Stone.BLACK:
            print("黒のターンです")
        if self.player_2.stone == Stone.WHITE:
            print("白のターンです")

    def turn_change(self, stone):
        stone = Stone.get_opponent_stone(stone)

    def run(self):
        self.board.show()
        while self.pass_count < 2:
            self.player_1_color()
            self.player_1.select_play(self.board)
            self.board.show()
            self.player_2_color()
            self.player_2.select_play(self.board)
            self.board.show()
        self.board.count_stone()
        return False


if __name__ == "__main__":
    Game.turn()

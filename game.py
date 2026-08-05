from stone import Stone
from cpu import Cpu
from player import Player


class Game:

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.pass_check()
        self.player_1 = player_1
        self.player_2 = player_2

    def pass_check(cls):
        cls.pass_count = 0

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

    @classmethod
    def create_players(cls, mode, player_1_stone, player_2_stone):
        player_1 = Player(player_1_stone)
        player_2 = Cpu(player_2_stone) if mode == 1 else Player(player_2_stone)
        return player_1, player_2

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
        print("--- ゲーム開始 ---")
        self.board.show()
        if self.player_1.stone == Stone.BLACK:
            current_player = self.player_1
            next_player = self.player_2
        else:
            current_player = self.player_2
            next_player = self.player_1
        while self.pass_count < 2:
            if current_player.stone == Stone.BLACK:
                color_str = "黒"
            else:
                color_str = "白"
            print(f"【{color_str}のターンです】")
            current_x_y = current_player.select_play(self.board)
            if current_x_y is None:
                self.pass_count += 1
                print("置ける場所がないためパスしました。")
            else:
                x, y = current_x_y
                self.board.reverse_stone(x, y, current_player.stone)
                self.pass_count = 0
                self.board.show()
            current_player, next_player = next_player, current_player
        print("--- ゲーム終了 ---")
        self.board.count_stone()
        return False

    def select_game_mode():
        while True:
            try:
                c = int(input("1人モードなら1 2人モードならなら2を入力してください:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 2:
                    return 2
                else:
                    return 1
            except ValueError:
                print("入力エラーです")
                continue


if __name__ == "__main__":
    Game.turn()

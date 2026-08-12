from stone import Stone
from cpu import Cpu
from player import Player
from standard_io import StandardIO


class Game:

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.pass_check()
        self.player_1 = player_1
        self.player_2 = player_2

    def pass_check(self):
        self.pass_count = 0

    @classmethod
    def create_players(cls, mode, player_1_stone, player_2_stone):
        player_1 = Player(player_1_stone)
        if mode == 1:
            player_2 = Cpu(player_2_stone)
        else:
            player_2 = Player(player_2_stone)
        return player_1, player_2

    def turn_change(self, stone):
        stone = Stone.get_opponent_stone(stone)

    def run_tkinter(self, ui):
        if self.player_1.stone == Stone.BLACK:
            current_player = self.player_1
            next_player = self.player_2
        else:
            current_player = self.player_2
            next_player = self.player_1
        while self.pass_count < 2:
            ui.show()
            ui.master.update()
            if isinstance(current_player, Cpu):
                current_x_y = current_player.select_play(self.board)
            else:
                ui.can_place_show(self, current_player)
                current_x_y = ui.select_place_stone()
            if current_x_y is None:
                self.pass_count += 1
            else:
                x, y = current_x_y
                x = int(x)
                y = int(y)
                self.board.reverse_stone(x, y, current_player.stone)
                self.pass_count = 0
            current_player, next_player = next_player, current_player
        print("--- ゲーム終了 ---")
        self.board.count_stone()
        return False

    def run_terminal(self):
        StandardIO.start_running()
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
                StandardIO.turn_color_view(color_str)
            current_x_y = current_player.select_play(self.board)
            if current_x_y is None:
                self.pass_count += 1
                StandardIO.view_pass()
            else:
                x, y = current_x_y
                self.board.reverse_stone(x, y, current_player.stone)
                self.pass_count = 0
                self.board.show()
            current_player, next_player = next_player, current_player
        StandardIO.finish_running()
        self.board.count_stone()

        return False

    def select_play_show(self, player):
        placable_places = []
        for y in range(self.board.size):
            for x in range(self.board.size):
                if self.board.can_place_stone(x, y, player.stone):
                    placable_places.append((x, y))
        return placable_places


if __name__ == "__main__":
    Game.turn()

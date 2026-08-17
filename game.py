from stone import Stone
from cpu import Cpu
from player import Player
from othello_ui import OthelloUI


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
        if mode == 2:
            player_2 = Player(player_2_stone)
        else:
            player_2 = Cpu(player_2_stone)
        return player_1, player_2

    def run_game(self, ui):
        if self.player_1.stone == Stone.BLACK:
            current_player = self.player_1
            next_player = self.player_2
        else:
            current_player = self.player_2
            next_player = self.player_1
        while self.pass_count < 2:
            color_str = "黒" if current_player.stone == Stone.BLACK else "白"
            ui.turn_color_show(color_str)
            ui.show()
            if isinstance(current_player, Cpu):
                current_x_y = current_player.select_play(self.board)
                ui.cpu_select(current_x_y)
            elif isinstance(ui, OthelloUI):
                current_x_y = ui.select_play(self, current_player)
            else:
                current_x_y = current_player.select_play(self.board)
            if current_x_y is None:
                self.pass_count += 1
                ui.pass_count()
            else:
                x, y = current_x_y
                self.board.reverse_stone(int(x), int(y), current_player.stone)
                self.pass_count = 0
            current_player, next_player = next_player, current_player
        winner = self.board.count_stone()
        ui.finish_running(winner)
        return False

    def select_play_show(self, player):
        placable_places = []
        for y in range(self.board.size):
            for x in range(self.board.size):
                if self.board.can_place_stone(x, y, player.stone):
                    placable_places.append((x, y))
        return placable_places

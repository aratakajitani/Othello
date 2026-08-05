from board import Board
from game import Game
from stone import Stone


def main():
    board = Board()
    player_1_stone = Game.select_stone()
    player_2_stone = Stone.get_opponent_stone(player_1_stone)
    mode = Game.select_game_mode()
    player_1, player_2 = Game.create_players(mode, player_1_stone, player_2_stone)
    othello = Game(board=board, player_1=player_1, player_2=player_2)
    othello.run()


if __name__ == "__main__":
    main()

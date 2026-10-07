from game import Game
from stone import Stone
from cpu import Cpu
from player import Player


def test_create_players_mode_1():
    player_1, player_2 = Game.create_players(1, Stone.BLACK, Stone.WHITE)
    assert isinstance(player_1, Player)
    assert isinstance(player_2, Cpu)
    assert player_1.stone == Stone.BLACK
    assert player_2.stone == Stone.WHITE


def test_create_players_mode_2():
    player_1, player_2 = Game.create_players(2, Stone.BLACK, Stone.WHITE)
    assert isinstance(player_1, Player)
    assert isinstance(player_2, Player)
    assert player_1.stone == Stone.BLACK
    assert player_2.stone == Stone.WHITE

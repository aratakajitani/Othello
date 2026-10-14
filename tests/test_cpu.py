from board import Board
from stone import Stone
from cpu import Cpu


def test_cpu_select_place():
    cpu = Cpu(Stone.BLACK)
    initial_board = Board()
    placeable = [(2, 3), (3, 2), (4, 5), (5, 4)]
    assert cpu.select_place(initial_board) in placeable


def test_cannot_place():
    cpu = Cpu(Stone.BLACK)
    finished_board = Board()
    W = Stone.WHITE
    B = Stone.BLACK
    finished_board.board = [
        [B, B, B, B, W, W, B, B],
        [B, B, W, W, W, B, W, B],
        [B, W, W, B, W, W, W, W],
        [B, W, B, B, B, B, B, B],
        [B, B, B, B, W, B, W, W],
        [B, W, W, W, W, W, W, W],
        [B, B, B, B, B, B, B, B],
        [W, B, W, W, B, B, W, W],
            ]
    assert cpu.select_place(finished_board) is None

from board import Board
from stone import Stone


def test_board_setup():
    board = Board()
    assert board.board[3][3] == Stone.WHITE
    assert board.board[3][4] == Stone.BLACK
    assert board.board[4][3] == Stone.BLACK
    assert board.board[4][4] == Stone.WHITE
    for x in range(8):
        for y in range(8):
            center_x = (x == 3 or x == 4)
            center_y = (y == 3 or y == 4)
            if center_x and center_y:
                continue
            assert board.board[x][y] == Stone.EMPTY

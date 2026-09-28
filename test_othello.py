from board import Board
from stone import Stone


def test_board_setup():
    board = Board()
    W = Stone.WHITE
    B = Stone.BLACK
    E = Stone.EMPTY

    expected_board = [
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, W, B, E, E, E],
        [E, E, E, B, W, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
    ]
    assert board.board == expected_board


def test_place_stone():
    board = Board()
    assert board.can_place_stone(3, 3, Stone.BLACK) is False
    assert board.can_place_stone(8, 0, Stone.BLACK) is False
    assert board.can_place_stone(-1, 4, Stone.BLACK) is False
    assert board.can_place_stone(0, 0, Stone.BLACK) is False
    assert board.can_place_stone(2, 3, Stone.BLACK) is True


def test_reverse_one_stone():
    board = Board()
    board.reverse_stone(3, 2, Stone.BLACK)
    assert board.board[3][3] == Stone.BLACK


def test_reverse_two_stone():
    board = Board()
    board.board[3][2] = Stone.WHITE
    board.reverse_stone(3, 1, Stone.WHITE)
    assert board.board[3][2] == Stone.WHITE
    assert board.board[3][3] == Stone.WHITE


def test_reverse_two_directions_stone():
    board = Board()

    W = Stone.WHITE
    B = Stone.BLACK
    E = Stone.EMPTY
    board.board = [
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, B, W, E, E, E],
        [E, E, E, B, E, E, E, E],
        [E, E, E, E, W, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
    ]
    board.reverse_stone(2, 2, Stone.WHITE)
    assert board.board[2][3] == Stone.WHITE
    assert board.board[3][3] == Stone.WHITE


def test_stop_revercing_stone():
    board = Board()

    W = Stone.WHITE
    B = Stone.BLACK
    E = Stone.EMPTY
    board.board = [
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, W, B, W, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
    ]
    board.reverse_stone(2, 3, Stone.BLACK)
    assert board.board[3][3] == Stone.BLACK
    assert board.board[3][5] == Stone.WHITE


def test_pass_check():
    initial_board = Board()
    assert initial_board.has_valid_move(Stone.BLACK) is True
    assert initial_board.has_valid_move(Stone.WHITE) is True
    pass_board = Board()
    W = Stone.WHITE
    B = Stone.BLACK
    E = Stone.EMPTY
    pass_board.board = [
        [E, B, B, B, W, W, B, B],
        [B, B, W, W, W, B, W, B],
        [B, W, W, B, W, W, W, W],
        [B, W, B, B, B, B, B, B],
        [B, B, B, B, W, B, W, W],
        [B, W, W, W, W, W, W, W],
        [B, B, B, B, B, B, B, B],
        [W, B, W, W, B, B, W, W],
    ]
    assert pass_board.has_valid_move(Stone.BLACK) is False


def test_finish_game():
    initial_board = Board()
    assert initial_board.finish_game() is False
    assert initial_board.finish_game() is False
    finish_board = Board()
    W = Stone.WHITE
    B = Stone.BLACK
    finish_board.board = [
        [B, B, B, B, W, W, B, B],
        [B, B, W, W, W, B, W, B],
        [B, W, W, B, W, W, W, W],
        [B, W, B, B, B, B, B, B],
        [B, B, B, B, W, B, W, W],
        [B, W, W, W, W, W, W, W],
        [B, B, B, B, B, B, B, B],
        [W, B, W, W, B, B, W, W],
    ]
    assert finish_board.finish_game() is True

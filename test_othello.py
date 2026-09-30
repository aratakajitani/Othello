from board import Board
from stone import Stone


def test_board_setup():
    initial_board = Board()
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
    assert initial_board.board == expected_board


def test_place_stone():
    initial_board = Board()
    assert initial_board.can_place_stone(3, 3, Stone.BLACK) is False
    assert initial_board.can_place_stone(8, 0, Stone.BLACK) is False
    assert initial_board.can_place_stone(-1, 4, Stone.BLACK) is False
    assert initial_board.can_place_stone(0, 0, Stone.BLACK) is False
    assert initial_board.can_place_stone(2, 3, Stone.BLACK) is True


def test_reverse_one_stone():
    initial_board = Board()
    initial_board.reverse_stone(3, 2, Stone.BLACK)
    assert initial_board.board[3][3] == Stone.BLACK


def test_reverse_two_stone():
    test_board = Board()
    test_board.board[3][2] = Stone.WHITE
    test_board.reverse_stone(3, 1, Stone.WHITE)
    assert test_board.board[3][2] == Stone.WHITE
    assert test_board.board[3][3] == Stone.WHITE


def test_reverse_two_directions():
    test_board = Board()

    W = Stone.WHITE
    B = Stone.BLACK
    E = Stone.EMPTY
    test_board.board = [
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, B, W, E, E, E],
        [E, E, E, B, E, E, E, E],
        [E, E, E, E, W, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
    ]
    test_board.reverse_stone(2, 2, Stone.WHITE)
    assert test_board.board[2][3] == Stone.WHITE
    assert test_board.board[3][3] == Stone.WHITE


def test_reverse_stone_limit():
    test_board = Board()

    W = Stone.WHITE
    B = Stone.BLACK
    E = Stone.EMPTY
    test_board.board = [
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, W, B, W, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
        [E, E, E, E, E, E, E, E],
    ]
    test_board.reverse_stone(2, 3, Stone.BLACK)
    assert test_board.board[3][3] == Stone.BLACK
    assert test_board.board[3][5] == Stone.WHITE


def test_initial_pass():
    initial_board = Board()
    assert initial_board.has_places(Stone.BLACK) is True
    assert initial_board.has_places(Stone.WHITE) is True


def test_pass_check():

    passed_board = Board()
    W = Stone.WHITE
    B = Stone.BLACK
    E = Stone.EMPTY
    passed_board.board = [
        [E, B, B, B, W, W, B, B],
        [B, B, W, W, W, B, W, B],
        [B, W, W, B, W, W, W, W],
        [B, W, B, B, B, B, B, B],
        [B, B, B, B, W, B, W, W],
        [B, W, W, W, W, W, W, W],
        [B, B, B, B, B, B, B, B],
        [W, B, W, W, B, B, W, W],
    ]
    assert passed_board.has_places(Stone.BLACK) is False


def test_initial_finish():
    initial_board = Board()
    assert initial_board.finish_game() is False
    assert initial_board.finish_game() is False


def test_finish_game():
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
    assert finished_board.finish_game() is True

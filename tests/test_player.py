from player import Player
from board import Board
from stone import Stone


class MockBoard:
    def __init__(self, size=8):
        self.size = size
        self.reverse_called = False

    def can_place_stone(self, x, y, stone):
        if x == 0 and y == 0:
            return False
        if x == 3 and y == 4:
            return True
        return False

    def reverse_stone(self, x, y, stone):
        self.reverse_called = True


def test_select_place(monkeypatch, capsys):
    player = Player(stone=1)
    board = MockBoard(size=8)
    inputs = iter([
        "0", "0",
        "9",
        "abc",
        "3", "4"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = player.select_place(board)
    assert result == (3, 4)
    assert board.reverse_called is True
    captured = capsys.readouterr()
    output = captured.out
    assert "座標: (3,4)" in output
    assert "入力エラーです" in output
    assert "そこには置けません" in output
    assert output.count("そこには置けません") == 1
    assert output.count("入力エラーです") == 2


def test_cannot_place():
    player = Player(Stone.BLACK)
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
    assert player.select_place(finished_board) is None

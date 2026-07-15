from board import Board


def main():
    board = Board()
    board.show()
    board.get_opponent_stone(board.black)
    board.reverese_stone(4, 6, board.black)
    board.show()


if __name__ == "__main__":
    main()

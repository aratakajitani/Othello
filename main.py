from board import Board


def main():
    board = Board()
    color = board.select_color()
    board.game(color)


if __name__ == "__main__":
    main()

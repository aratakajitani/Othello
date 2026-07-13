from board import Board

def main():
    board = Board()
    board.show()
    print(board.BLACK_turn_select(4,6))


if __name__ == "__main__":
    main()

from board import Board


def main():
    board = Board()
    board.show()
    for y in range(board.size):
        for x in range(board.size):
            if board.can_place_black(x, y):
                print(f"座標: ({x},{y})")


if __name__ == "__main__":
    main()

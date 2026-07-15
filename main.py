from board import Board


def main():
    board = Board()
    board.show()
    board.get_opponent_stone(board.black)
    for y in range(board.size):
        for x in range(board.size):
            if board.can_place_stone(x, y, board.black):
                print(f"座標: ({x},{y})")
    x = int(input("x座標を入力してください:"))
    y = int(input("y座標を入力してください:"))
    board.reverse_stone(x, y, board.black)
    board.show()


if __name__ == "__main__":
    main()

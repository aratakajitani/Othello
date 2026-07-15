from board import Board


def main():
    board = Board()
    while board.empty_count > 0:
        print("黒のターンです")
        board.show()
        print(board.empty_count)
        board.get_opponent_stone(board.black)
        for y in range(board.size):
            for x in range(board.size):
                if board.can_place_stone(x, y, board.black):
                    print(f"座標: ({x},{y})")
        x = int(input("x座標を入力してください:"))
        y = int(input("y座標を入力してください:"))
        if not board.can_place_stone(x, y, board.black):
            continue
        board.reverse_stone(x, y, board.black)
        print("白のターンです")
        board.show()
        print(board.empty_count)
        board.get_opponent_stone(board.white)
        for y in range(board.size):
            for x in range(board.size):
                if board.can_place_stone(x, y, board.white):
                    print(f"座標: ({x},{y})")
        x = int(input("x座標を入力してください:"))
        y = int(input("y座標を入力してください:"))
        if not board.can_place_stone(x, y, board.white):
            continue
        board.reverse_stone(x, y, board.white)
    return False


if __name__ == "__main__":
    main()

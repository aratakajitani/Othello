from board import Board


def main():
    board = Board()
    color = board.black
    while board.empty_count > 0:
        if color == board.black:
                print("黒のターンです")
        if color == board.white:
                print("白のターンです")

        board.show()
        print(board.empty_count)
        board.get_opponent_stone(color)
        for y in range(board.size):
            for x in range(board.size):
                if board.can_place_stone(x, y, color): 
                    print(f"座標: ({x},{y})")
        x = int(input("x座標を入力してください:"))
        y = int(input("y座標を入力してください:"))
        if not board.can_place_stone(x, y, color):
            continue
        board.reverse_stone(x, y, color)
        color = board.get_opponent_stone(color)
    return False


if __name__ == "__main__":
    main()

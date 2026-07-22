from board import Board


def main():
    board = Board()
    color = board.black
    pass_count = 0
    while pass_count < 2 and board.empty_count > 0:
        if color == board.black:
            print("黒のターンです")
        if color == board.white:
            print("白のターンです")
        board.show()
        board.get_opponent_stone(color)
        can_place_flag = False
        for y in range(board.size):
            for x in range(board.size):
                if board.can_place_stone(x, y, color):
                    print(f"座標: ({x},{y})")
                    can_place_flag = True
        if can_place_flag:
            while True:
                try:
                    x = int(input("x座標を入力してください:"))
                    if not 0 <= x <= 8:
                        print("入力エラーです")
                        continue
                    y = int(input("y座標を入力してください:"))
                    if not 0 <= y <= 8:
                        print("入力エラーです")
                        continue
                except ValueError:
                    print("入力エラーです")
                    continue
                pass_count = 0
                if board.can_place_stone(x, y, color):
                    board.reverse_stone(x, y, color)
                    board.empty_count -= 1
                    break
                else:
                    print("そこには置けません")
        else:
            print("石を置けないのでパスします")
            pass_count += 1
        color = board.get_opponent_stone(color)

    board.count_stone(x, y)
    return False


if __name__ == "__main__":
    main()

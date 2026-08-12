from stone import Stone


class StandardIO:

    @classmethod
    def select_stone(cls):
        while True:
            try:
                c = int(input("最初の色を白なら1 黒なら2を入力してください:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 2:
                    return Stone.BLACK
                else:
                    return Stone.WHITE
            except ValueError:
                print("入力エラーです")
                continue

    def select_game_mode():
        while True:
            try:
                c = int(input("1人モードなら1 2人モードならなら2を入力してください:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 2:
                    return 2
                else:
                    return 1
            except ValueError:
                print("入力エラーです")
                continue

    def select_running():
        while True:
            try:
                c = int(input("TKinterで遊ぶなら1 ターミナルで遊ぶなら2を入力してください。:"))
                if c != 1 and c != 2:
                    print("入力エラーです")
                    continue
                if c == 2:
                    return 2
                else:
                    return 1
            except ValueError:
                print("入力エラーです")
                continue

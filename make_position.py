import sys

class game():
    def __init__(self) -> None:
        player = [None, None]
        match_length = 0
        board = [
            0,
            -2, 0, 0, 0, 0, 5,
            0, 3, 0, 0, 0, -5,
            5, 0, 0, 0, -3, 0,
            -5, 0, 0, 0, 0, 2,
            0
        ]
        score = [0, 0]
        crawford = False
        cube = 1

    def reset(self) -> None:
        # from bottom player view
        # first line is number of checkers of the top player
        # last line is number of checkers of the bottom player
        self.board = [
            0,
            -2, 0, 0, 0, 0, 5,
            0, 3, 0, 0, 0, -5,
            5, 0, 0, 0, -3, 0,
            -5, 0, 0, 0, 0, 2,
            0
        ]
        self.cube = 1


    # setter
    def set_player(self, name, pos):
        self.player[pos] = name


class notation():
    def __init__(self) -> None:
        notation = []

    def reading_file(self, f_name: str):
        with open(f_name, "r") as f:
            data = f.readline()
            while True:
                if not data:
                    break
                # skip comment lines
                if data.startswith(";"):
                    continue


class search():
    def __init__(self) -> None:
        player = ""
        game = 0
        cube = None
        dice = None

    def set_player(self, players: list) -> None:
        while True:
            print("手番プレーヤーを指定してください")
            player = input()
            if player not in players:
                print("そのプレーヤーは存在しません")
                continue
            self.player = player
            return

    def set_game(self, game: int) -> None:
        while True:
            print("ゲーム番号を指定してください。\n全検索時は0を入力してください")
            try:
                input_game = int(input())
            except ValueError:
                print("入力値が不正です")
            else:
                if not 0 < input_game <= input_game:
                    print("指定されたゲームは存在しません")
                else:
                    self.game = input_game
                    return
            continue


    def set_cube(self, score: list) -> None:
        while True:
            print("キューブ判定時の倍率を指定してください。")
            try:
                input_cube = int(input())
            except ValueError:
                print("入力値が不正です")
            else:
                if input_cube not in score:
                    print("指定されたキューブアクションは存在しません")
                else:
                    self.cube = input_cube
                    return
            continue

    def set_dice(self) -> None:
        all_dices = [
            "11", "12", "13", "14", "15", "16",
            "21", "22", "23", "24", "25", "26",
            "31", "32", "33", "34", "35", "36",
            "41", "42", "43", "44", "45", "46",
            "51", "52", "53", "54", "55", "56",
            "61", "62", "63", "64", "65", "66"
            ]
        while True:
            print("検索するダイスの目を2桁の数字で入力してください")
            try:
                input_dice = int(input())
            except ValueError:
                print("入力値が不正です")
            else:
                if input_dice not in all_dices:
                    print("そのような出目は存在しません")
                else:
                    self.dice = input_dice
                    return
            continue


def main():
    args = sys.argv

if __name__ == "__main__":
    main()
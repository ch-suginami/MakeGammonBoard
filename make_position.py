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

    def reading_file(self, f_name):
        with open(f_name, "r") as f:
            pass



def main():
    args = sys.argv

if __name__ == "__main__":
    main()
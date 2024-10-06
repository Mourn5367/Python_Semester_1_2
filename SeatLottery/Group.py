import sys


class Group:
    def __init__(self):
        self.rows = 0
        self.cols = 0

    @property
    def totalSeat(self):
        return self.rows * self.cols

    def rows_count(self):
        self.rows = int(input("가로행의 갯수를 적으시오.:"))
        if self.rows <= 0:
            print("0 이하로 입력하여 프로그램을 종료합니다.")
            sys.exit()

    def cols_count(self):
        self.cols = int(input("세로행의 갯수를 적으시오.:"))
        if self.cols <= 0:
            print("0 이하로 입력하여 프로그램을 종료합니다.")
            sys.exit()


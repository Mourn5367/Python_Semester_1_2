class Group:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.totalSeat = self.rows  * self.cols

    def rows_count(self):
        self.rows = int(input("가로행의 갯수를 적으시오.:"))

    def cols_count(self):
        self.cols = int(input("세로행의 갯수를 적으시오.:"))


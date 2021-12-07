import os

BOARD_SIZE = 5
INVALID_CHARACTER = 'X'

class Board:
    def __init__(self):
        self.nums = []
        self.points = 0
        self.is_complete = False
    
    def print_board(self):
        count = 0
        row = ""
        for num in self.nums:
            row += str(num) + " "
            count += 1
            if count % BOARD_SIZE == 0:
                count = 0
                print(row)
                row = ""
            

    def score(self, value):
        row = 0
        col = -1
        count = 0
        for entry in self.nums:
            if count != 0 and count % BOARD_SIZE == 0:
                col = 0
                row += 1
            else:
                col += 1

            if entry != INVALID_CHARACTER and value == int(entry):
                self.nums[count] = INVALID_CHARACTER
                self.points += 1
                break
            count += 1



        if self.is_board_complete(row, col):
            print("BOARD COMPLETE!")
            self.score_board(value)
            self.is_complete = True
            return True
        return False

    def score_board(self, value):
        sum = 0
        for entry in self.nums:
            if entry != INVALID_CHARACTER:
                sum += int(entry)
        print(value * sum)

    def col_score(self, col):
        for i in range(BOARD_SIZE):
            if self.nums[col + i * BOARD_SIZE] != INVALID_CHARACTER:
                return False
        return True

    def row_score(self, row):
        row = row*BOARD_SIZE
        for i in range(BOARD_SIZE):
            if self.nums[row + i] != INVALID_CHARACTER:
                return False
        return True


    def is_board_complete(self, row, col):
        if self.points < BOARD_SIZE:
            return False
        
        if self.row_score(row):
            print("ROW WIN: row: " + str(row))
            return True
        if self.col_score(col):
            print("COL WIN: col: " + str(col))
            return True
        return False

def load_boards():
    game_input = []
    boards = []
    with open(os.getcwd() + "/data/squid_bingo.txt",'r') as data:
        drawn = False
        new_board = Board()
        for line in data:
            if not drawn:
                line = line.strip("\n")
                game_input = line.split(",")
                drawn = True
            else:
                if line == "\n":
                    if len(new_board.nums) > 0:
                        boards.append(new_board)
                    new_board = Board()
                    continue
                else:
                    line = line.strip("\n")
                    entries = line.split(" ")
                    for entry in entries:
                        if entry != "":
                            new_board.nums.append(entry)
        boards.append(new_board)
    return game_input, boards

def simple_bingo():
    game_input, boards = load_boards()
    for point in game_input:
        for board in boards:
            if board.score(int(point)):
                return
 
def advanced_bingo():
    game_input, boards = load_boards()
    count = 0

    while (len(boards) > 0):
        point = int(game_input[count])

        for board in boards:
            board.score(point)
        board_copy = boards
        for board in board_copy:
            if board.is_complete:
                boards.remove(board)
                if len(boards) == 0:
                    board.score_board(point)

        count += 1

advanced_bingo()

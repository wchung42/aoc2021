# Figure out which board wins last

from copy import deepcopy

with open('input.txt', 'r') as f:
    nums = f.readline().strip().split(',')
    rows = [list(filter(None, line.strip().split(' '))) for line in f.readlines()]

rows = [row for row in rows if len(row) > 0] # remove empty rows
boards = [rows[i:i+5] for i in range(0, len(rows), 5)]
boards_after = deepcopy(boards)
bingo_boards_copy = deepcopy(boards)

def bingo(board):
    # check rows for bingo
    for row in board:
        row_string = ''.join(row)
        if row_string == 'xxxxx':
            return board
        
    # check cols for bingo
    n = len(board)
    for col in range(n):
        col_string = ''
        for row in range(n):
            col_string += board[row][col]
        if col_string == 'xxxxx':
            return board


def mark(bingo_boards):
    completed_boards_marked = []
    completed_boards = []
    nums_used = []
    for num in nums:
        target = None
        for i in range(len(bingo_boards)):
            for row in bingo_boards[i]:
                for col in range(len(row)):
                    if row[col] == num:
                        row[col] = 'x'

                        target = bingo(bingo_boards[i]) # check bingo
                        
                        if target is not None:
                            if bingo_boards_copy[i] not in completed_boards:
                                completed_boards_marked.append(deepcopy(bingo_boards[i]))
                                completed_boards.append(bingo_boards_copy[i])
                                nums_used.append(num)
                            
    return completed_boards_marked, completed_boards, nums_used


def compare(board1, board2):
    n = len(board1)
    unmarked = 0
    for row in range(n):
        for col in range(n):
            if board1[row][col] == board2[row][col]:
                unmarked += int(board1[row][col])
    return unmarked


completed_boards_marked, completed_boards, nums_used = mark(boards_after)
# print(completed_boards_marked[-1])
# print(completed_boards[-1])
# print(nums_used[-1])

unmarked = compare(completed_boards_marked[-1], completed_boards[-1])
print(int(unmarked)*int(nums_used[-1]))
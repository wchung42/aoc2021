from copy import deepcopy

with open('input.txt', 'r') as f:
    nums = f.readline().strip().split(',')
    rows = [list(filter(None, line.strip().split(' '))) for line in f.readlines()]

rows = [row for row in rows if len(row) > 0] # remove empty rows
boards = [rows[i:i+5] for i in range(0, len(rows), 5)]
boards_after = deepcopy(boards)

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
    for num in nums:
        target = None
        for i in range(len(bingo_boards)):
            for row in bingo_boards[i]:
                for col in range(len(row)):
                    if row[col] == num:
                        row[col] = 'x'
    
                        target = bingo(bingo_boards[i])

                    if target is not None:
                        return i, target, num

def compare(index, board):
    n = len(board)
    og_board = boards[index]
    # marked = 0
    unmarked = 0
    for row in range(n):
        for col in range(n):
            if board[row][col] == og_board[row][col]:
                unmarked += int(og_board[row][col])
            # else:
            #     marked += int(og_board[row][col])

    return unmarked


index, target, last_num_called = mark(boards_after)
unmarked = compare(index, target)

print(unmarked, last_num_called)
print(int(unmarked)*int(last_num_called))
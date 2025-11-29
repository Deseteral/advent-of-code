#!/usr/local/bin/python3

def process_board_line(line):
    return list(
        map(
            lambda x: int(x),
            filter(lambda x: len(x) > 0, line.split(' '))
        )
    )

def mark_number(num, board):
    for y in range(0, 5):
        for x in range(0, 5):
            if board[y][x] == num: board[y][x] = -1

def check_winning_board(board):
    for y in range(0, 5):
        row_check = 0
        for x in range(0, 5):
            if board[y][x] == -1: row_check += 1
        if row_check == 5: return True

    for x in range(0, 5):
        column_check = 0
        for y in range(0, 5):
            if board[y][x] == -1: column_check += 1
        if column_check == 5: return True

    return False

def calculate_board_sum(board):
    board_sum = 0
    for y in range(0, 5):
        for x in range(0, 5):
            if board[y][x] != -1: board_sum += board[y][x]
    return board_sum

with open('input') as f:
    lines = f.read().splitlines()
    board_lines = lines[2:]

    marked = list(map(lambda x: int(x), lines[0].split(',')))
    boards = []

    for i in range(0, len(board_lines), 6):
        boards.append([
            process_board_line(board_lines[i + 0]),
            process_board_line(board_lines[i + 1]),
            process_board_line(board_lines[i + 2]),
            process_board_line(board_lines[i + 3]),
            process_board_line(board_lines[i + 4])
        ])

    # processing
    win_count = 0

    for marked_num in marked:
        for board_idx in range(0, len(boards)):
            board = boards[board_idx]
            if (board == None): continue

            mark_number(marked_num, board)

            if check_winning_board(board):
                winning_sum = calculate_board_sum(board)

                win_count += 1
                boards[board_idx] = None

                if  (win_count == 1): print(f"first_win {winning_sum * marked_num}")
                if  (win_count == len(boards)): print(f"last_win {winning_sum * marked_num}")

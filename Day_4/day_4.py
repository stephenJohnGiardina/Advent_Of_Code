from datetime import datetime


def challenge_1():
    moves, boards = load_moves_and_boards()

    found = False
    for move in moves:
        mark_boards(move, boards)
        for board in boards:
            if check_board(board):
                found = True
                score = get_score(board, move)
                break
        if found:
            break

    print(score)

def load_moves_and_boards():
    with open("Day_4/input.txt", "r+") as input:
        first = True
        boards = []
        previous = []
        for line in input.readlines():
            if first:
                first = False
                moves = list(map(lambda x: int(x), line.strip().split(",")))
                continue
            if line.strip() == "" and previous != []:
                boards.append(previous)
                previous = []
            else:
                if line.strip() != "":
                    previous.append(list(map(lambda x: int(x), line.strip().split())))

    return moves, boards

def mark_boards(move, boards):
    for board_index in range(len(boards)):
        for row_index in range(len(boards[board_index])):
            for number_index in range(len(boards[board_index][row_index])):
                if boards[board_index][row_index][number_index] == move:
                    boards[board_index][row_index][number_index] = True

def check_board(board):
    if check_rows(board) or check_cols(board):
        return True

def check_rows(board):
    for row in board:
        number_found = False
        for number in row:
            if number is not True:
                number_found = True
        if not number_found:
            return True
    return False

def check_cols(board):
    for col_index in range(len(board)):
        number_found = False
        for row_index in range(len(board)):
            if board[row_index][col_index] is not True:
                number_found = True
        if not number_found:
            return True
    return False

def get_score(board, move):
    sum_of_unmarked = 0
    for row in board:
        for number in row:
            if number is not True:
                sum_of_unmarked += number
    return sum_of_unmarked * move

def challenge_2():
    moves, boards = load_moves_and_boards()

    winning_boards = []
    for move in moves:
        mark_boards(move, boards)
        for board in range(len(boards)):
            if check_board(boards[board]) and board not in winning_boards:
                    winning_boards.append(board)
        if len(winning_boards) == len(boards):
            last_move = move
            break

    score = get_score(boards[winning_boards[-1]], last_move)
    print(score)

if __name__ == "__main__":
    print("Starting Challenges for Day 4")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
